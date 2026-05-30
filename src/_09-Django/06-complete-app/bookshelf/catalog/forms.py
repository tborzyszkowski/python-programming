"""Formularze ModelForm dla Author i Book."""
from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model  = Author
        fields = ['first_name', 'last_name', 'birth_year', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'birth_year': forms.NumberInput(attrs={'min': 1000, 'max': 2100,
                                                   'placeholder': 'np. 1798'}),
        }

    def clean_birth_year(self):
        year = self.cleaned_data.get('birth_year')
        if year is not None and (year < 1000 or year > 2100):
            raise forms.ValidationError("Rok urodzenia musi być między 1000 a 2100.")
        return year


class BookForm(forms.ModelForm):
    class Meta:
        model  = Book
        fields = ['title', 'author', 'year', 'isbn', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.order_by('last_name', 'first_name')
        self.fields['author'].empty_label = "-- Wybierz autora --"

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year is not None and (year < 1450 or year > 2100):
            raise forms.ValidationError("Rok wydania musi być między 1450 a 2100.")
        return year

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '').replace('-', '').replace(' ', '')
        if isbn and len(isbn) not in (10, 13):
            raise forms.ValidationError("ISBN musi zawierać 10 lub 13 cyfr.")
        return isbn

