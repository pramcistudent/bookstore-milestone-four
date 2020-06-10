from django.test import TestCase
from .forms import LoginForm, RegisterForm

# Create your tests here.
class TestLoginForm(TestCase):
    def test_user_can_log_in(self):
        """
        Tests that the user can login with a username and password
        """
        form = LoginForm({"username": "TestUser", "password": "Password"})
        self.assertTrue(form.is_valid())

    def test_blank_field_error_message(self):
        """
        Tests that the fields are required for the form to be valid
        """
        form = LoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], [u"This field is required."])


class TestRegisterForm(TestCase):
    def test_user_can_register(self):
        """
        Tests that the user can register by entering the relevant details
        """
        form = RegisterForm(
            {
                "username": "TestUser",
                "email": "user@test.com",
                "first_name": "FirstName",
                "last_name": "LastName",
                "password": "Password",
                "password_confirm": "Password",
            }
        )
        self.assertTrue(form.is_valid())

    def test_blank_field_error_message(self):
        """
        Tests that the fields are required for the form to be valid
        """
        form = RegisterForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], [u"This field is required."])
