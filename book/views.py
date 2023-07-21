from django.shortcuts import render, get_object_or_404, redirect
from book.models import Book, Category, Order
from user.models import Address
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
    quantity = 1
    if request.session.get('cart_items'):
        if request.session.get('cart_items').get(str(id)):
            quantity = request.session.get('cart_items')[str(id)]
    context = {
        "book" : book,
        "quantity" : quantity
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

def add_to_cart(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        quantity = request.POST.get("quantity")
        cart_items = {}
        if request.session.get("cart_items"):
            cart_items = request.session.get("cart_items")
        cart_items[book_id] = quantity
        request.session["cart_items"] = cart_items 
        print(request.session.get("cart_items"))
    return redirect("cart")

def cart(request):
    cart_details, total_price = get_cart_details(request)
    context = {
        "books" : cart_details,
        "total_price" : total_price
    }
    return render(request, 'book/cart.html', context)


def remove_from_cart(request, id):
    cart_items = request.session.get('cart_items')
    del cart_items[str(id)]
    request.session['cart_items'] = cart_items
    return redirect("cart")

def check_out(request):
    addresses = Address.objects.filter(user=request.user)
    cart_details, total_price = get_cart_details(request)
    context = {
        "addresses" : addresses,
        "books" : cart_details,
        "total_price" : total_price
    }
    return render(request, 'book/check_out.html', context)

def place_order(request):
    if request.method == "POST":
        user = request.user
        address = request.POST.get("address")
        address = Address.objects.get(id=address)
        payment_mode = request.POST.get("payment_mode")
        cart_details, total_price = get_cart_details(request)
        orders = []
        for book in cart_details:
            order = Order(
                book = Book.objects.get(id=book['id']),
                user = user,
                address = address,
                quantity = book['quantity'], #custom dictionary 
                price = book['price'],
                payment_method = payment_mode
            )
            orders.append(order)
        Order.objects.bulk_create(orders)
        request.session['cart_items'] = {}
        return redirect('all_books')
        
        

def get_cart_details(request):
    total_price = 0
    cart_details = []
    if not request.session.get("cart_items"):
        return cart_details, total_price
    cart_items = request.session.get("cart_items")
    books = Book.objects.filter(id__in=list(cart_items.keys()))
    for book in books:
        quantity = int(cart_items[str(book.id)])
        price = quantity * book.price
        total_price += price
        cart_details.append({
            "id" : book.id,
            "title" : book.title,
            "quantity" : quantity,
            "price" : price,
            "image" : book.image
        })
    return cart_details, total_price
