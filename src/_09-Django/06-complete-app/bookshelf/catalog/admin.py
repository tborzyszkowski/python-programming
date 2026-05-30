"""Rejestracja modeli w panelu admina."""
from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ['last_name', 'first_name', 'birth_year', 'book_count']
    search_fields = ['last_name', 'first_name']
    list_filter   = ['birth_year']

    @admin.display(description='Liczba książek')
    def book_count(self, obj):
        return obj.books.count()


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ['title', 'author', 'year', 'isbn']
    search_fields = ['title', 'author__last_name']
    list_filter   = ['year', 'author']
    raw_id_fields = ['author']

