from django.contrib import admin

# Register your models here.
from .models import Category, Writer, Book

class AddCategory(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Category, AddCategory)

class AddWriter(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Writer, AddWriter)

class AddBook(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock']
	list_filter = ['name', 'stock',]
	list_editable = ['price', 'stock']
admin.site.register(Book, AddBook)
