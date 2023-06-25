from django.shortcuts import render, redirect
from book.models import *

# Create your views here.

from django.contrib import messages

def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    cart = request.session.get('cart', {})
    cart[book_id] = cart.get(book_id, 0) + 1
    request.session['cart'] = cart
    messages.success(request, f"{book.name} added to cart.")
    return redirect('cart')

def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    if str(book_id) in cart:
        del cart[str(book_id)]
        request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    book_ids = cart.keys()
    books = Book.objects.filter(id__in=book_ids)
    cart_items = []
    total_price = 0

    for book in books:
        quantity = cart[str(book.id)]
        total = quantity * book.price
        cart_items.append({
            'book': book,
            'quantity': quantity,
            'total': total
        })
        total_price += total

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

