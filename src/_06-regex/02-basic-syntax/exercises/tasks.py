"""Zadania: podstawowa skladnia wyrazen regularnych."""
import re


def czy_tylko_litery(s: str) -> bool:
    """Zwraca True, jesli niepusty napis sklada sie wylacznie z liter (a-z, A-Z).

    Przyklad:
        czy_tylko_litery("Hello")   -> True
        czy_tylko_litery("Hello2")  -> False
        czy_tylko_litery("")        -> False
    """
    raise NotImplementedError("Zaimplementuj czy_tylko_litery")


def znajdz_liczby_calkowite(s: str) -> list[str]:
    """Zwraca liste wszystkich liczb calkowitych (ciagi cyfr) znalezionych w napisie.

    Przyklad:
        znajdz_liczby_calkowite("cena 42 zl, ilosc: 3")  -> ['42', '3']
        znajdz_liczby_calkowite("brak")                   -> []
    """
    raise NotImplementedError("Zaimplementuj znajdz_liczby_calkowite")


def czy_data_iso(s: str) -> bool:
    """Zwraca True, jesli napis ma format YYYY-MM-DD (4-2-2 cyfry z kreskami).

    Przyklad:
        czy_data_iso("2024-01-15")  -> True
        czy_data_iso("24-1-5")      -> False
        czy_data_iso("2024/01/15")  -> False
    """
    raise NotImplementedError("Zaimplementuj czy_data_iso")


def znajdz_slowa_na_wielka(s: str) -> list[str]:
    """Zwraca liste slow zaczynajacych sie wielka litera (A-Z).

    Slowo to ciag liter (a-zA-Z) zaczynajacy sie od wielkiej litery.

    Przyklad:
        znajdz_slowa_na_wielka("Pan Jan jedzie do Krakowa")
        -> ['Pan', 'Jan', 'Krakowa']
    """
    raise NotImplementedError("Zaimplementuj znajdz_slowa_na_wielka")


def czy_poprawny_identyfikator(s: str) -> bool:
    """Zwraca True, jesli napis jest poprawnym identyfikatorem Pythona
    (zaczyna sie od litery lub _, potem litery, cyfry lub _).

    Nie sprawdzamy slow kluczowych.

    Przyklad:
        czy_poprawny_identyfikator("my_var")   -> True
        czy_poprawny_identyfikator("_priv")    -> True
        czy_poprawny_identyfikator("2bad")     -> False
        czy_poprawny_identyfikator("good-name") -> False
    """
    raise NotImplementedError("Zaimplementuj czy_poprawny_identyfikator")

