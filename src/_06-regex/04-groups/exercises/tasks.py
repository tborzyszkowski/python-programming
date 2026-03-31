"""Zadania: grupy i przechwytywanie."""
import re


def wyciagnij_date(s: str) -> dict | None:
    """Parsuje date w formacie YYYY-MM-DD i zwraca slownik lub None.

    Klucze slownika: 'rok', 'miesiac', 'dzien' (wartosci str).

    Przyklad:
        wyciagnij_date("Data: 2024-03-15")
        -> {'rok': '2024', 'miesiac': '03', 'dzien': '15'}
        wyciagnij_date("brak daty") -> None
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_date")


def zamien_format_daty(s: str) -> str:
    """Zamienia wszystkie daty YYYY-MM-DD na format DD.MM.YYYY w napisie.

    Przyklad:
        zamien_format_daty("Urodziny: 1990-05-20")
        -> "Urodziny: 20.05.1990"
    """
    raise NotImplementedError("Zaimplementuj zamien_format_daty")


def znajdz_powtorzenia(s: str) -> list[str]:
    """Zwraca liste slow powtorzonych bezposrednio po sobie (case-insensitive).

    Przyklad:
        znajdz_powtorzenia("to to jest jest test")  -> ['to', 'jest']
        znajdz_powtorzenia("brak powtorzen")        -> []
    """
    raise NotImplementedError("Zaimplementuj znajdz_powtorzenia")


def parsuj_wersje(s: str) -> tuple[int, int, int] | None:
    """Wyciaga wersje w formacie MAJOR.MINOR.PATCH i zwraca krotke intow lub None.

    Przyklad:
        parsuj_wersje("Python 3.12.0")  -> (3, 12, 0)
        parsuj_wersje("brak wersji")    -> None
    """
    raise NotImplementedError("Zaimplementuj parsuj_wersje")


def wyciagnij_pary_klucz_wartosc(s: str) -> dict[str, str]:
    """Wyciaga wszystkie pary klucz=wartosc z napisu i zwraca je jako slownik.

    Klucz i wartosc to ciagi znakow slowa (\\w+).

    Przyklad:
        wyciagnij_pary_klucz_wartosc("host=localhost port=5432 db=test")
        -> {'host': 'localhost', 'port': '5432', 'db': 'test'}
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_pary_klucz_wartosc")

