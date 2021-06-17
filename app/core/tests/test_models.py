from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gve.com'
        password = 'Aa12345678*'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Test email for new user is normalized"""
        email = 'test@GVE.COM'
        user = get_user_model().objects.create_user(email, 'Test123')
        
        self.assertEqual(user.email, email.lower())
