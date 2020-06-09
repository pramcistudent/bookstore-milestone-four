from django.urls import path
from . import views
from reviews.views import add_review

urlpatterns = [
    path("", views.books, name="books"),
    path("book/<int:book_id>", views.book, name="book"),
    path("search", views.search, name="search"),
    path("book/<int:pk>/reviews/", add_review, name="add_review"),
]
