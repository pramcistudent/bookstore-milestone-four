from django.test import TestCase
from .models import Books
from authors.models import Author

# Create your tests here.
class TestAccountsViews(TestCase):
    def test_get_books_page(self):
        """
        Tests to return a book
        """
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/books.html")

    def test_get_book_page_for_book_that_does_not_exist(self):
        """
        Tests to return a book that doesn't exist
        """
        response = self.client.get("/books/book/0")
        self.assertEqual(response.status_code, 404)

    def test_get_search_page(self):
        """
        Tests that returns the search page
        """
        response = self.client.get("/books/search")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/search.html")
