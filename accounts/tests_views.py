from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client


# Create your tests here.
class TestAccountsViews(TestCase):
    def test_get_register_page(self):
        """
        Tests that the register view renders the register template
        """
        response = self.client.get("/accounts/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_get_login_page(self):
        """
        Tests that the login view renders the login template
        """
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def setUp(self):
        """
        Create test user
        """
        self.client = Client()
        self.user = User.objects.create_user("joe", "joe@bloggs.com", "joepassword")

    def testLogin_get_profile_page(self):
        """
        Tests that the profile view redirects to the profile template
        """
        self.client.login(username="joe", password="joepassword")
        response = self.client.get(reverse("index"))
        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")
        self.assertEqual(response.status_code, 200)
