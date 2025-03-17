from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .forms import CommentForm
from .models import Event


class TestEventViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@test.com',
        )
        self.event = Event.objects.create(
            title='Event Title',
            slug='event-title',
            author=self.user,
            featured_image='placeholder',
            description='This is a test event',
            location='Test Location',
            date='2022-12-12',
            time='12:00:00',
            tags='Test, Event',
            status=1,
            created_on='2022-12-12 12:00:00',
            excerpt='This is a test excerpt',
            updated_on='2022-12-12 12:00:00',
        )
        self.event.save()

    def test_render_event_detail_page_with_comment_form(self):
        """
        Test that the event detail page renders with a comment form.
        """
        response = self.client.get(reverse(
            'event_detail', args=['event-title']
            ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Event Title", response.content)
        self.assertIn(b"This is a test event", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """
        Test that a comment can be successfully submitted.
        """
        self.client.login(username='testuser', password='testpassword')
        event_data = {
            'body': 'This is a test comment',
        }
        response = self.client.post(reverse(
            'event_detail', args=['event-title']
            ), event_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)
