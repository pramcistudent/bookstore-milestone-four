from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404
from accounts.views import register, login, logout, profile


# Create your tests here.
class TestView(TestCase):

    def test_get_login_page(self):
        """
        Tests that the login page view renders the login template
        """
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_can_login(self):
        """
        Tests that the user can login using username and passwords
        """
        user1 = User.objects.create_user(
            username='testUser',
            email='testUser@example.com',
            password='password')

        response = self.client.get('/books/')
        self.assertEqual(response.context['user'], AnonymousUser())

        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'password'
        })

        response = self.client.get('/accounts/login')

    def test_logout_view(self):
        """
        Tests that the user can logout
        """
        response = self.client.get("/accounts/logout")
        self.assertRedirects(response, '/')

    def test_get_register_page(self):
        """
        Tests that the register view renders the register template
        """
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_get_profile_page(self):
        """
        Tests that the user can view the profile page when user is logged in
        """
        self.client.login(username='profileName', password='profilePassword')
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 302)
        