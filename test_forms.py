from django.test import TestCase
from forms import CustomerRegistrationForm
from forms import BusinessRegistrationForm

# Start Test Customer form


class CustomerRegistrationFormTest(TestCase):

    def test_fname_required(self):
        form = CustomerRegistrationForm(data={
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('fname', code='required'))

    def test_lname_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'email': 'john@example.com',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('lname', code='required'))

    def test_email_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('email', code='required'))

    def test_email_valid_format(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'invalid_email',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('email', code='invalid'))

    def test_location_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('location', code='required'))

    def test_address_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('address', code='required'))

    def test_vat_not_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertTrue(form.is_valid())

    def test_number_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,
            'address': '123 Main St',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('number', code='required'))

    def test_id_number_required(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('id_number', code='required'))

    def test_passwords_match(self):
        form = CustomerRegistrationForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': 1,
            'address': '123 Main St',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password456'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'], ['Passwords do not match.'])

# End Test Customer form

# Start Test Business form


class BusinessRegistrationFormTest(TestCase):
    def test_required_fields(self):
        form_data = {
            'fname': '',
            'lname': '',
            'email': '',
            'location': '',
            'address': '',
            'vat': '',
            'businessname': '',
            'number': '',
            'id_number': '',
            'password1': '',
            'password2': '',
        }

        form = BusinessRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 11)

    def test_invalid_email_format(self):
        form_data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'invalid_email',
            'location': '1',
            'address': '123 Main St',
            'vat': 'MT1245-1245',
            'businessname': 'Example Business',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123',
        }

        form = BusinessRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_vat_number_format(self):
        form_data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': '1',
            'address': '123 Main St',
            'vat': 'invalid_vat',
            'businessname': 'Example Business',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123',
        }

        form = BusinessRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('vat', form.errors)

    def test_valid_vat_number_format(self):
        form_data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': '1',
            'address': '123 Main St',
            'vat': 'MT1245-1245',
            'businessname': 'Example Business',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123',
        }

        form = BusinessRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_matching(self):
        form_data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': '1',
            'address': '123 Main St',
            'vat': 'MT1245-1245',
            'businessname': 'Example Business',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password456',
         }

        form = BusinessRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'], ['Passwords do not match.'])

    def test_valid_form(self):
        form_data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'location': '1',
            'address': '123 Main St',
            'vat': 'MT1245-1245',
            'businessname': 'Example Business',
            'number': '12345678',
            'id_number': '1234567890',
            'password1': 'password123',
            'password2': 'password123',
        }

        form = BusinessRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

# End Test Business form
