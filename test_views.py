from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from accounts.models import Car, Customer
from client.forms import CarCreateForm, CustomerForm
from client.views import car_crud, customer_profile_update
from accounts.models import Customer, User


class ViewsTestCase(TestCase):
    def test_get_home_page(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_about_page(self):
        response = self.client.get('/about/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html', 'base.html')

    def test_contact_page(self):
        response = self.client.get('/contact/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html', 'base.html')

    def test_customer_register_page(self):
        response = self.client.get('/register_client/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html', 'base.html')

    def test_service_garage_register_page(self):
        response = self.client.get('/register_business/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'register_business.html',
                                'base.html')

    def test_login_page(self):
        response = self.client.get('/login/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html', 'base.html')

    def test_login_register_page(self):
        response = self.client.get('/signinpage/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signinpage.html', 'base.html')
