"""Zadania: modul re – wyszukiwanie, zamiana, podzial."""
import re


def pierwsza_liczba(s: str) -> int | None:
    """Zwraca pierwsza liczbe calkowita znaleziona w napisie lub None.

    Przyklad:
        pierwsza_liczba("abc 42 xyz 7")  -> 42
        pierwsza_liczba("brak")          -> None
    """
    raise NotImplementedError("Zaimplementuj pierwsza_liczba")


def wszystkie_emaile(s: str) -> list[str]:
    """Zwraca liste wszystkich adresow e-mail znalezionych w napisie.

    Uproszczony wzorzec: lokalny@domena.tld (bez RFC-pelnej walidacji).

    Przyklad:
        wszystkie_emaile("Kontakt: a@b.com i x@y.pl")  -> ['a@b.com', 'x@y.pl']
        wszystkie_emaile("brak emaili")                 -> []
    """
    raise NotImplementedError("Zaimplementuj wszystkie_emaile")


def normalizuj_spacje(s: str) -> str:
    """Zastepuje kazdy ciag bialych znakow pojedyncza spacją i przycina krawedzie.

    Przyklad:
        normalizuj_spacje("za   duzo    spacji")  -> "za duzo spacji"
        normalizuj_spacje("  hello  world  ")     -> "hello world"
    """
    raise NotImplementedError("Zaimplementuj normalizuj_spacje")


def podziel_na_tokeny(s: str) -> list[str]:
    """Dzieli napis po przecinkach, srednikach lub bialych znakach (jeden lub wiecej).

    Pomija puste tokeny.

    Przyklad:
        podziel_na_tokeny("a,b; c  d")  -> ['a', 'b', 'c', 'd']
        podziel_na_tokeny("x")          -> ['x']
    """
    raise NotImplementedError("Zaimplementuj podziel_na_tokeny")


def pozycje_slowa(s: str, slowo: str) -> list[tuple[int, int]]:
    """Zwraca liste spanow (start, end) wszystkich pelnych wystapien slowa w napisie.

    Uzyj granic slowa (\\b), zeby 'an' nie dopasowalo 'band'.

    Przyklad:
        pozycje_slowa("Ala ma kota i Ala ma psa", "Ala")
        -> [(0, 3), (14, 17)]
    """
    raise NotImplementedError("Zaimplementuj pozycje_slowa")

