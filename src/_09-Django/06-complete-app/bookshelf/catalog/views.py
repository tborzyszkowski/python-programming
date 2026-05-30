"""Widoki aplikacji catalog – pełny CRUD dla Author i Book."""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Author, Book
from .forms import AuthorForm, BookForm


# ─── Strona główna ───────────────────────────────────────────────────────────

def home(request):
    return render(request, 'catalog/home.html', {
        'authors_count': Author.objects.count(),
        'books_count':   Book.objects.count(),
        'recent_books':  Book.objects.order_by('-created_at')[:5],
    })


# ─── AUTHOR: READ ────────────────────────────────────────────────────────────

def author_list(request):
    query   = request.GET.get('q', '').strip()
    authors = Author.objects.all()
    if query:
        authors = authors.filter(last_name__icontains=query) | \
                  authors.filter(first_name__icontains=query)
    return render(request, 'catalog/author_list.html', {
        'authors': authors,
        'query':   query,
    })


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books  = author.books.order_by('-year', 'title')
    return render(request, 'catalog/author_detail.html', {
        'author': author,
        'books':  books,
    })


# ─── AUTHOR: CREATE ──────────────────────────────────────────────────────────

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.success(request, f'Autor „{author}" został dodany.')
            return redirect('catalog:author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'catalog/author_form.html', {
        'form':  form,
        'title': 'Nowy autor',
    })


# ─── AUTHOR: UPDATE ──────────────────────────────────────────────────────────

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dane autora „{author}" zostały zaktualizowane.')
            return redirect('catalog:author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'catalog/author_form.html', {
        'form':   form,
        'title':  f'Edycja: {author}',
        'author': author,
    })


# ─── AUTHOR: DELETE ──────────────────────────────────────────────────────────

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        name = str(author)
        author.delete()
        messages.warning(request, f'Autor „{name}" i jego książki zostały usunięte.')
        return redirect('catalog:author_list')
    return render(request, 'catalog/author_confirm_delete.html', {
        'author': author,
        'books':  author.books.all(),
    })


# ─── BOOK: READ ──────────────────────────────────────────────────────────────

def book_list(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.select_related('author').all()
    if query:
        books = books.filter(title__icontains=query) | \
                books.filter(author__last_name__icontains=query)
    return render(request, 'catalog/book_list.html', {
        'books': books,
        'query': query,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book.objects.select_related('author'), pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})


# ─── BOOK: CREATE ────────────────────────────────────────────────────────────

def book_create(request):
    initial    = {}
    author_pk  = request.GET.get('author')
    if author_pk:
        initial['author'] = author_pk

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Książka „{book.title}" została dodana.')
            return redirect('catalog:book_detail', pk=book.pk)
    else:
        form = BookForm(initial=initial)
    return render(request, 'catalog/book_form.html', {
        'form':  form,
        'title': 'Nowa książka',
    })


# ─── BOOK: UPDATE ────────────────────────────────────────────────────────────

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'Książka „{book.title}" została zaktualizowana.')
            return redirect('catalog:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/book_form.html', {
        'form':  form,
        'title': f'Edycja: {book.title}',
        'book':  book,
    })


# ─── BOOK: DELETE ────────────────────────────────────────────────────────────

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title  = book.title
        author = book.author
        book.delete()
        messages.warning(request, f'Książka „{title}" została usunięta.')
        return redirect('catalog:author_detail', pk=author.pk)
    return render(request, 'catalog/book_confirm_delete.html', {'book': book})

