from django.test import TestCase
from django.urls import reverse
from .forms import RegistrationForm

class RegistrationFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,  # Replace with the correct location value
            'address': '123 Main St',
            'vat': '123456789',  # Optional
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = RegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'fname': 'John',
            'lname': '',  # Missing last name
            'email': 'invalid_email',  # Invalid email format
            'location': 1,  # Replace with the correct location value
            'address': '123 Main St',
            'vat': '123456789',  # Optional
            'number': '12345',  # Too short
            'id_number': '12345678901',  # Too long
            'password1': 'password123',
            'password2': 'password456',  # Passwords don't match
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_submission(self):
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,  # Replace with the correct location value
            'address': '123 Main St',
            'vat': '123456789',  # Optional
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('register_client'), data=data)
        self.assertEqual(response.status_code, 200)  # Adjust the expected status code as needed
        # Add additional assertions to check for successful form submission
