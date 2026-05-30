"""Modele aplikacji catalog – Author i Book."""
from django.db import models


class Author(models.Model):
    """Autor książki."""
    first_name = models.CharField(max_length=100, verbose_name="Imię")
    last_name  = models.CharField(max_length=100, verbose_name="Nazwisko")
    birth_year = models.IntegerField(null=True, blank=True,
                                     verbose_name="Rok urodzenia")
    bio        = models.TextField(blank=True, verbose_name="Biogram")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    """Książka powiązana z autorem (relacja N:1)."""
    title       = models.CharField(max_length=200, verbose_name="Tytuł")
    author      = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name="Autor",
    )
    year        = models.IntegerField(null=True, blank=True,
                                      verbose_name="Rok wydania")
    isbn        = models.CharField(max_length=20, blank=True,
                                   verbose_name="ISBN")
    description = models.TextField(blank=True, verbose_name="Opis")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __str__(self) -> str:
        return f"{self.title} ({self.author})"

