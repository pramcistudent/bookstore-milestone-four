from django.shortcuts import render
from books.models import Books
from authors.models import Author

# Create homepage


def index(request):
    books = Books.objects.filter(is_published=True).order_by("-list_date")
    context = {"books": books}
    return render(request, "pages/index.html", context)

