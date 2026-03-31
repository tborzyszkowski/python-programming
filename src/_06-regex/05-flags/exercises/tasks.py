"""Zadania: flagi i tryby modulu re."""
import re


def szukaj_bez_wielkosci(tekst: str, wzorzec: str) -> list[str]:
    """Zwraca liste wszystkich dopasowań wzorca niezaleznie od wielkosci liter.

    Przyklad:
        szukaj_bez_wielkosci("Python PYTHON python", "python")
        -> ['Python', 'PYTHON', 'python']
    """
    raise NotImplementedError("Zaimplementuj szukaj_bez_wielkosci")


def znajdz_naglowki_markdown(tekst: str) -> list[str]:
    """Zwraca liste wszystkich naglowkow Markdown (linie zaczynajace sie od #).

    Zwraca sam tekst naglowka (bez znakow # i wiodacej spacji).

    Przyklad:
        tekst = "# Tytul\\n## Sekcja\\nnormalny tekst\\n### Podsekcja"
        znajdz_naglowki_markdown(tekst)
        -> ['Tytul', 'Sekcja', 'Podsekcja']
    """
    raise NotImplementedError("Zaimplementuj znajdz_naglowki_markdown")


def wyciagnij_bloki_html(tekst: str, tag: str) -> list[str]:
    """Zwraca liste zawartosci wszystkich blokow <tag>...</tag> (moze byc wieloliniowa).

    Przyklad:
        wyciagnij_bloki_html("<p>Ala\\nma kota</p><p>kot</p>", "p")
        -> ['Ala\\nma kota', 'kot']
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_bloki_html")


def waliduj_numer_verbose(s: str) -> bool:
    """Zwraca True, jesli napis jest polskim numerem telefonu.

    Akceptowane formaty: 600100200, 600 100 200, 600-100-200, +48600100200.
    Napisz wzorzec z uzyciem re.VERBOSE i komentarzami.

    Przyklad:
        waliduj_numer_verbose("600 100 200")   -> True
        waliduj_numer_verbose("+48600100200")  -> True
        waliduj_numer_verbose("123")           -> False
    """
    raise NotImplementedError("Zaimplementuj waliduj_numer_verbose")

