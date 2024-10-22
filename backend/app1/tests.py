from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .validators import validate_illinois_email
from django.core.exceptions import ValidationError



class CustomEmailValidatorTests(TestCase):
    def test_valid_illinois_email(self):
        """
        Test that an email with @illinois.edu passes the validation.
        """
        try:
            validate_illinois_email('test@illinois.edu')
        except ValidationError:
            self.fail("validate_illinois_email() raised ValidationError unexpectedly!")

    def test_invalid_email(self):
        """
        Test that an email without @illinois.edu raises ValidationError.
        """
        with self.assertRaises(ValidationError):
            validate_illinois_email('test@example.com')

class LoginTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@illinois.edu',
            password='testpassword'
        )

    def test_login_success(self):
        """
        Test a successful login using the correct credentials.
        """
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('account_login'), login_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect on successful login
        self.assertRedirects(response, '/')  # Should redirect to the homepage after login

    def test_login_failure(self):
        """
        Test login failure with incorrect credentials.
        """
        login_data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('account_login'), login_data)
        self.assertEqual(response.status_code, 200)  # Should return the login page again

