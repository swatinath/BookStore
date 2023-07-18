from django.shortcuts import render, get_object_or_404
from book.models import Book, Category
# Create your views here.

def all_books(request):
    books = Book.objects.all()
    categories = Category.objects.all().order_by('category')
    #print(books.query)
    context = {
        "books" : books,
        "categories" : categories,
    }
    return render(request, "book/books.html", context)

def book_details(request, id):
    #book = Book.objects.get(id=id)
    book = get_object_or_404(Book, id=id)
    context = {
        "book" : book
    }
    return render(request, "book/book.html", context)

def category_books(request, cid):
    books = Book.objects.filter(category=cid)
    categories = Category.objects.all().order_by('category')
    #print(books.query)
    context = {
        "books" : books,
        "categories" : categories,
    }
    return render(request, "book/books.html", context)

