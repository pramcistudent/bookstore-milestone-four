from django.shortcuts import render
from books.models import Books
from authors.models import Author
# Create homepage


def index(request):
    books = Books.objects.filter(is_published=True).order_by("-list_date")[:3]
    context = {"books": books}
    return render(request, "pages/index.html", context)


def view_404(request, exception):
    return render(request, 'pages/404.html')


def view_500(request):
    return render(request, 'pages/500.html')
