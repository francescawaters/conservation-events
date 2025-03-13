from django.test import TestCase
from .forms import CommentForm

# Create your tests here.


class TestCommentForm(TestCase):

    def test_comment_form_is_valid(self):
        form = CommentForm({
            'body': 'This is a test comment',
        })

        self.assertTrue(form.is_valid(), msg='Form is not valid')

    def test_comment_form_missing_required_fields(self):
        form = CommentForm({
            'body': '',
        })

        self.assertFalse(form.is_valid(), msg='Form submits with missing '
                                              'required fields')
