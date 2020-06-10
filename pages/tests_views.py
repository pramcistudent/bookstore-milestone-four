from django.test import TestCase

# Create your tests here.
class TestAccountsViews(TestCase):
    def test_get_home_page(self):
        """
        Tests that user view redirects to the index template
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/index.html")
