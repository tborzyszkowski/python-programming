import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_re_module import (
    normalizuj_spacje,
    pierwsza_liczba,
    podziel_na_tokeny,
    pozycje_slowa,
    wszystkie_emaile,
)


def test_pierwsza_liczba():
    assert pierwsza_liczba("abc 42 xyz 7") == 42
    assert pierwsza_liczba("100abc") == 100
    assert pierwsza_liczba("brak") is None


def test_wszystkie_emaile():
    assert wszystkie_emaile("Kontakt: a@b.com i x@y.pl") == ["a@b.com", "x@y.pl"]
    assert wszystkie_emaile("brak emaili") == []
    assert wszystkie_emaile("Jan jan@example.com") == ["jan@example.com"]


def test_normalizuj_spacje():
    assert normalizuj_spacje("za   duzo    spacji") == "za duzo spacji"
    assert normalizuj_spacje("  hello  world  ") == "hello world"
    assert normalizuj_spacje("jeden") == "jeden"


def test_podziel_na_tokeny():
    assert podziel_na_tokeny("a,b; c  d") == ["a", "b", "c", "d"]
    assert podziel_na_tokeny("x") == ["x"]
    assert podziel_na_tokeny("a,b,c") == ["a", "b", "c"]


def test_pozycje_slowa():
    wynik = pozycje_slowa("Ala ma kota i Ala ma psa", "Ala")
    assert wynik == [(0, 3), (14, 17)]


def test_pozycje_slowa_brak():
    assert pozycje_slowa("nic tu nie ma", "Ala") == []


def test_pozycje_slowa_granica():
    # 'an' nie powinno pasowac do 'band'
    wynik = pozycje_slowa("an band an", "an")
    assert wynik == [(0, 2), (8, 10)]

