from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        """ Creates about content for testing """
        self.about_content = About(
            title='About Us',
            content='This is a test about us content.')
        self.about_content.save()

    def test_render_about_page_with_contact_form(self):
        """ Test about page renders with contact form """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Us", response.content)
        self.assertIn(b"This is a test about us content.", response.content)
        self.assertIsInstance(response.context['contact'], ContactForm)

    def test_successful_contact_form_submission(self):
        """ Test successful contact form submission """
        contact_data = {
            'name': 'Test User',
            'email': 'test@test.com',
            'message': 'This is a test message.',
        }
        response = self.client.post(reverse('about'), contact_data)
        print(response.content)  # Add this line to inspect the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Message sent successfully.", response.content)
