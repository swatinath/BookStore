from django.urls import path

from book.views import all_books, book_details, category_books

urlpatterns = [
    path("", all_books, name="all_books"),
    path("<int:id>/", book_details, name="book_details"),
    path("category/<int:cid>/", category_books, name="book_category"),    
]