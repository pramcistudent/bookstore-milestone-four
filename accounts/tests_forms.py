from django.test import TestCase
from .forms import LoginForm, RegisterForm


# Create your tests here.
class TestLoginForm(TestCase):

    def test_login_with_username_only(self):
        """
        Tests that the user cannot login with only a username
        """
        form = LoginForm({'username': 'bookStore'})
        self.assertFalse(form.is_valid())

    def test_login_with_password_only(self):
        """
        Tests that the user cannot login with only a password
        """
        form = LoginForm({'password': 'password'})
        self.assertFalse(form.is_valid())


class TestRegisterForm(TestCase):

    def test_message_for_missing_firstname(self):
        """
        Tests that the correct message is shown when firstname
        is missing from register form
        """
        form = RegisterForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], [u'This field is required.'])
  
    def test_message_for_missing_lastname(self):
        """
        Tests that the correct message is shown when lastname
        is missing from register form
        """
        form = RegisterForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['last_name'], [u'This field is required.'])

    def test_message_for_missing_username(self):
        """
        Tests that the correct message is shown when username
        is missing from register form
        """
        form = RegisterForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_message_for_missing_email(self):
        """
        Tests that the correct message is shown when email
        is missing from register form
        """
        form = RegisterForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])

    def test_message_for_missing_password(self):
        """
        Tests that the correct message is shown when password
        is missing from register form
        """
        form = RegisterForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])

    def test_message_for_missing_password_confirm(self):
        """
        Tests that the correct message is shown when password reconfirm 
        is missing from register form
        """
        form = RegisterForm({'password_confirm': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password_confirm'], [u'This field is required.'])