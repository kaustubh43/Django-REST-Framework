"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_creat_user_with_email_succesfull(self):
        """Test creating a user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.checkpassword(password))
