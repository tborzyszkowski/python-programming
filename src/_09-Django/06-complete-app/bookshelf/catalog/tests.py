"""Testy jednostkowe dla aplikacji catalog.

Uruchamianie:
    cd src/_09-Django/06-complete-app/bookshelf
    pip install pytest pytest-django
    pytest

Lub przez manage.py:
    python manage.py test catalog
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Author, Book
from catalog.forms import AuthorForm, BookForm


# ─── Testy modeli ────────────────────────────────────────────────────────────

class AuthorModelTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="Adam",
            last_name="Mickiewicz",
            birth_year=1798,
            bio="Poeta romantyczny.",
        )

    def test_str_representation(self):
        self.assertEqual(str(self.author), "Adam Mickiewicz")

    def test_full_name(self):
        self.assertEqual(self.author.full_name(), "Adam Mickiewicz")

    def test_default_ordering_by_last_name(self):
        Author.objects.create(first_name="Bolesław", last_name="Prus")
        authors = list(Author.objects.all())
        self.assertEqual(authors[0].last_name, "Mickiewicz")
        self.assertEqual(authors[1].last_name, "Prus")

    def test_birth_year_optional(self):
        author = Author.objects.create(first_name="Jan", last_name="Kowalski")
        self.assertIsNone(author.birth_year)

    def test_bio_optional(self):
        author = Author.objects.create(first_name="Anna", last_name="Nowak")
        self.assertEqual(author.bio, "")


class BookModelTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="Stanisław", last_name="Lem"
        )
        self.book = Book.objects.create(
            title="Solaris",
            author=self.author,
            year=1961,
            isbn="9788308017791",
        )

    def test_str_representation(self):
        self.assertEqual(str(self.book), "Solaris (Stanisław Lem)")

    def test_foreign_key_author(self):
        self.assertEqual(self.book.author, self.author)

    def test_related_name_books(self):
        books = list(self.author.books.all())
        self.assertIn(self.book, books)

    def test_cascade_delete(self):
        """Usunięcie autora usuwa jego książki (CASCADE)."""
        author_pk = self.author.pk
        self.author.delete()
        self.assertEqual(Book.objects.filter(author_id=author_pk).count(), 0)

    def test_year_optional(self):
        book = Book.objects.create(title="Nieznana", author=self.author)
        self.assertIsNone(book.year)


# ─── Testy formularzy ────────────────────────────────────────────────────────

class AuthorFormTests(TestCase):

    def test_valid_form(self):
        form = AuthorForm(data={
            'first_name': 'Adam',
            'last_name':  'Mickiewicz',
            'birth_year': 1798,
            'bio':        'Poeta.',
        })
        self.assertTrue(form.is_valid())

    def test_required_fields(self):
        form = AuthorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name',  form.errors)

    def test_birth_year_validation_too_early(self):
        form = AuthorForm(data={
            'first_name': 'Jan',
            'last_name':  'Test',
            'birth_year': 500,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('birth_year', form.errors)

    def test_birth_year_optional(self):
        form = AuthorForm(data={'first_name': 'Jan', 'last_name': 'Test'})
        self.assertTrue(form.is_valid())


class BookFormTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="Test", last_name="Author"
        )

    def test_valid_form(self):
        form = BookForm(data={
            'title':  'Test Book',
            'author': self.author.pk,
            'year':   2020,
            'isbn':   '',
            'description': '',
        })
        self.assertTrue(form.is_valid())

    def test_year_too_early(self):
        form = BookForm(data={
            'title':  'Old Book',
            'author': self.author.pk,
            'year':   1000,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors)

    def test_isbn_wrong_length(self):
        form = BookForm(data={
            'title':  'Book',
            'author': self.author.pk,
            'isbn':   '12345',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('isbn', form.errors)

    def test_isbn_13_valid(self):
        form = BookForm(data={
            'title':  'Book',
            'author': self.author.pk,
            'isbn':   '9788308017791',
        })
        self.assertTrue(form.is_valid())

    def test_isbn_optional(self):
        form = BookForm(data={'title': 'No ISBN', 'author': self.author.pk})
        self.assertTrue(form.is_valid())


# ─── Testy widoków ───────────────────────────────────────────────────────────

class AuthorViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(
            first_name="Adam", last_name="Mickiewicz", birth_year=1798
        )
        self.book = Book.objects.create(
            title="Pan Tadeusz", author=self.author, year=1834
        )

    # READ
    def test_author_list_status(self):
        response = self.client.get(reverse('catalog:author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mickiewicz")

    def test_author_list_search(self):
        response = self.client.get(reverse('catalog:author_list') + '?q=mick')
        self.assertContains(response, "Mickiewicz")

    def test_author_detail_status(self):
        url = reverse('catalog:author_detail', kwargs={'pk': self.author.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pan Tadeusz")

    def test_author_detail_404(self):
        url = reverse('catalog:author_detail', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # CREATE
    def test_author_create_get(self):
        response = self.client.get(reverse('catalog:author_create'))
        self.assertEqual(response.status_code, 200)

    def test_author_create_post_valid(self):
        response = self.client.post(reverse('catalog:author_create'), {
            'first_name': 'Bolesław',
            'last_name':  'Prus',
            'birth_year': 1847,
            'bio':        '',
        })
        self.assertEqual(Author.objects.filter(last_name='Prus').count(), 1)
        self.assertEqual(response.status_code, 302)  # redirect

    def test_author_create_post_invalid(self):
        response = self.client.post(reverse('catalog:author_create'), {
            'first_name': '',
            'last_name':  '',
        })
        self.assertEqual(response.status_code, 200)  # brak redirect = błędy
        form = response.context['form']
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name',  form.errors)

    # UPDATE
    def test_author_update_get(self):
        url = reverse('catalog:author_update', kwargs={'pk': self.author.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mickiewicz')

    def test_author_update_post(self):
        url = reverse('catalog:author_update', kwargs={'pk': self.author.pk})
        self.client.post(url, {
            'first_name': 'Adam',
            'last_name':  'Mickiewicz',
            'birth_year': 1798,
            'bio':        'Zaktualizowany biogram.',
        })
        self.author.refresh_from_db()
        self.assertEqual(self.author.bio, 'Zaktualizowany biogram.')

    # DELETE
    def test_author_delete_get(self):
        url = reverse('catalog:author_delete', kwargs={'pk': self.author.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_author_delete_post_cascade(self):
        author_pk = self.author.pk
        url = reverse('catalog:author_delete', kwargs={'pk': author_pk})
        self.client.post(url)
        self.assertEqual(Author.objects.filter(pk=author_pk).count(), 0)
        self.assertEqual(Book.objects.filter(author_id=author_pk).count(), 0)


class BookViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(
            first_name="Stanisław", last_name="Lem"
        )
        self.book = Book.objects.create(
            title="Solaris", author=self.author, year=1961,
            isbn="9788308017791"
        )

    def test_book_list_status(self):
        response = self.client.get(reverse('catalog:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Solaris")

    def test_book_detail_status(self):
        url = reverse('catalog:book_detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Solaris")
        self.assertContains(response, "Stanisław Lem")

    def test_book_create_post(self):
        response = self.client.post(reverse('catalog:book_create'), {
            'title':       'Cyberiada',
            'author':      self.author.pk,
            'year':        1965,
            'isbn':        '',
            'description': '',
        })
        self.assertEqual(Book.objects.filter(title='Cyberiada').count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_book_update_post(self):
        url = reverse('catalog:book_update', kwargs={'pk': self.book.pk})
        self.client.post(url, {
            'title':       'Solaris (wydanie jubileuszowe)',
            'author':      self.author.pk,
            'year':        1961,
            'isbn':        '9788308017791',
            'description': 'Nowy opis.',
        })
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Solaris (wydanie jubileuszowe)')

    def test_book_delete_post(self):
        book_pk = self.book.pk
        url = reverse('catalog:book_delete', kwargs={'pk': book_pk})
        self.client.post(url)
        self.assertEqual(Book.objects.filter(pk=book_pk).count(), 0)

    def test_book_list_search(self):
        response = self.client.get(reverse('catalog:book_list') + '?q=solar')
        self.assertContains(response, "Solaris")


# ─── Test strony głównej ─────────────────────────────────────────────────────

class HomeViewTests(TestCase):

    def test_home_status(self):
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_shows_counts(self):
        Author.objects.create(first_name="Jan", last_name="Test")
        response = self.client.get(reverse('catalog:home'))
        self.assertContains(response, '1')  # liczba autorów


