from django.shortcuts import render
from .models import Books

# Create your views here.
def books(request):
    return render(request, "books/books.html")
