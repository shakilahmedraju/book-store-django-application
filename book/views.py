from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def book_list(request):
    categories = Category.objects.all()
    writers = Writer.objects.all()
    books = Book.objects.all()

    category_id = request.GET.get('category')
    writer_id = request.GET.get('writer')

    if category_id:
        books = books.filter(category_id=category_id)

    if writer_id:
        books = books.filter(writer_id=writer_id)
    context = {
        'books': books,
        'categories': categories,
        'writers': writers,
    }
    return render(request, 'index.html', context)


def add_book(request):
    if request.method == 'POST':
        writer_id = request.POST.get('writer')
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        coverpage = request.FILES.get('coverpage')
        description = request.POST.get('description')
        
        writer = Writer.objects.get(id=writer_id)
        category = Category.objects.get(id=category_id)
        
        book = Book(writer=writer, category=category, name=name, price=price, stock=stock,
                    coverpage=coverpage, description=description)
        book.save()
        
        return redirect('book_list')  
    
    writers = Writer.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'writers': writers,
    }
    return render(request, 'add_book.html', context)