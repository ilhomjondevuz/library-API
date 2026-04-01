from django.contrib import admin

from books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'author', 'price')
    list_filter = ('author',)
    search_fields = ('title', 'author', 'isbn')
    ordering = ('-price',)

admin.site.register(Book, BookAdmin)