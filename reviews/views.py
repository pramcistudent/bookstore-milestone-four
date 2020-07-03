from django.shortcuts import render, get_object_or_404
from books.models import Books
from .forms import ReviewForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def add_review(request, book_id):
    '''
    Allows the user to create a book review
    '''
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return render(request, {'form': form})
    else:
        form = ReviewForm()
    return render(request, {'form': form})
