from django.test import TestCase
from .forms import ContactForm

# Create your tests here.


class TestContactForm(TestCase):

    def test_contact_form_is_valid(self):
        """ Test for all fields in the contact form """
        form = ContactForm({
            'name': 'Test User',
            'email': 'test@test.com',
            'message': 'This is a test message',
        })

        self.assertTrue(form.is_valid(), msg='Form is not valid')

    def test_contact_form_missing_name_field(self):
        """ Test for missing name field in the contact form """
        form = ContactForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'This is a test message',
        })

        self.assertFalse(form.is_valid(), msg='Form submits '
                                              'with missing name value')

    def test_contact_form_missing_email_field(self):
        """ Test for missing email field in the contact form """
        form = ContactForm({
            'name': 'Test User',
            'email': '',
            'message': 'This is a test message',
        })

        self.assertFalse(form.is_valid(), msg='Form submits '
                                              'with missing email value')

    def test_contact_form_missing_message_field(self):
        """ Test for missing message field in the contact form """
        form = ContactForm({
            'name': 'Test User',
            'email': 'test@test.com',
            'message': '',
        })

        self.assertFalse(form.is_valid(), msg='Form submits '
                                              'with missing message value')
