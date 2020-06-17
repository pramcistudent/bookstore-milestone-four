from django.test import TestCase
from .models import Books
from authors.models import Author

# Create your tests here.
class TestBooksViews(TestCase):
    
    def test_get_books_page(self):
        """
        Tests that the browse books page view renders the books template
        """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_get_book_page(self):
        """
        Tests that the book page view renders the book template
        """
        author = Author(name="Test Author Name", photo="test.jpg")
        author.save()
        book = Books(title="Test Book Title", price=10.00,
                     author_id=author.id, book_image="test.jpg")
        book.save()

        response = self.client.get("/books/book/1")
        self.assertEqual(response.status_code, 200)

    def test_get_search_page(self):
        """
        Tests that the search page view renders the search template
        """
        response = self.client.get('/books/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/search.html')