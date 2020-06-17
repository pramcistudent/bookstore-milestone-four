from django.test import TestCase
from books.models import Books

# Create your tests here.
class TestBookModel(TestCase):

    def test_create_book(self):
        book = Books(title='Book', description='Some test content description.')
        self.assertEqual(book.title, 'Book')
        self.assertEqual(book.description, "Some test content description.")
        self.assertFalse(book.book_image)
        self.assertFalse(book.price)
        self.assertTrue(book.available)