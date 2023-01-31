"""Test for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        email = 'teste@example.com'
        password = 'pass1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'samplepass123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Creating users without an email should raise a ValueError."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'samplepass123')

    def test_create_superuser(self):
        """Test creating superusers."""

        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'testpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)