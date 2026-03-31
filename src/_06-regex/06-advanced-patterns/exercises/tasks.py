"""Zadania: zaawansowane wzorce – leniwe kwantyfikatory, lookahead, lookbehind."""
import re


def znajdz_tagi_html(s: str) -> list[str]:
    """Zwraca liste wszystkich tagow HTML (razem z nawiasami < >).

    Uzyj leniwego kwantyfikatora, zeby nie lacyc kilku tagow w jedno dopasowanie.

    Przyklad:
        znajdz_tagi_html("<b>tekst</b>")      -> ['<b>', '</b>']
        znajdz_tagi_html("<p><em>x</em></p>") -> ['<p>', '<em>', '</em>', '</p>']
    """
    raise NotImplementedError("Zaimplementuj znajdz_tagi_html")


def liczby_przed_jednostka(s: str, jednostka: str) -> list[str]:
    """Zwraca liste liczb (ciagi cyfr) wystepujacych bezposrednio przed podana jednostka.

    Miedzy liczba a jednostka moze byc jedna spacja lub jej brak.

    Przyklad:
        liczby_przed_jednostka("42 zl i 100 zl", "zl")  -> ['42', '100']
        liczby_przed_jednostka("10 EUR 20 USD", "EUR")   -> ['10']
    """
    raise NotImplementedError("Zaimplementuj liczby_przed_jednostka")


def waliduj_haslo(s: str) -> bool:
    """Zwraca True, jesli haslo spelnia wszystkie wymagania:
    - Co najmniej 8 znakow
    - Co najmniej jedna wielka litera (A-Z)
    - Co najmniej jedna mala litera (a-z)
    - Co najmniej jedna cyfra (0-9)

    Uzyj lookahead dla kazdego wymagania.

    Przyklad:
        waliduj_haslo("Abc12def")  -> True
        waliduj_haslo("abc12def")  -> False  (brak wielkiej)
        waliduj_haslo("Abc1def")   -> False  (za krotkie – 7 znakow)
    """
    raise NotImplementedError("Zaimplementuj waliduj_haslo")


def slowa_nie_poprzedzone_liczba(s: str) -> list[str]:
    """Zwraca liste slow (ciagow liter a-z) NIE poprzedzonych bezposrednio cyfra.

    Przyklad:
        slowa_nie_poprzedzone_liczba("abc 3xyz def")  -> ['abc', 'def']
    """
    raise NotImplementedError("Zaimplementuj slowa_nie_poprzedzone_liczba")


def bezpieczne_wyszukaj(wzorzec_uzytkownika: str, tekst: str) -> list[str]:
    """Wyszukuje dokladnie wzorzec podany przez uzytkownika (traktowany dosłownie).

    Uzyj re.escape, zeby znaki specjalne nie byly interpretowane jako metaznaki.

    Przyklad:
        bezpieczne_wyszukaj("3.14", "wynik: 3.14 przybl: 3x14")  -> ['3.14']
        bezpieczne_wyszukaj("(ok)", "status: (ok) i (ok)")        -> ['(ok)', '(ok)']
    """
    raise NotImplementedError("Zaimplementuj bezpieczne_wyszukaj")

