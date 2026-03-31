import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_advanced import (
    bezpieczne_wyszukaj,
    liczby_przed_jednostka,
    slowa_nie_poprzedzone_liczba,
    waliduj_haslo,
    znajdz_tagi_html,
)


def test_znajdz_tagi_html_podstawowe():
    assert znajdz_tagi_html("<b>tekst</b>") == ["<b>", "</b>"]


def test_znajdz_tagi_html_zagniezdzne():
    wynik = znajdz_tagi_html("<p><em>x</em></p>")
    assert wynik == ["<p>", "<em>", "</em>", "</p>"]


def test_znajdz_tagi_html_brak():
    assert znajdz_tagi_html("zwykly tekst") == []


def test_liczby_przed_jednostka():
    assert liczby_przed_jednostka("42 zl i 100 zl", "zl") == ["42", "100"]
    assert liczby_przed_jednostka("10 EUR 20 USD", "EUR") == ["10"]


def test_liczby_przed_jednostka_brak():
    assert liczby_przed_jednostka("brak", "zl") == []


def test_waliduj_haslo_true():
    assert waliduj_haslo("Abc12def") is True
    assert waliduj_haslo("SuperPass1") is True
    assert waliduj_haslo("Aa1bbbbb") is True


def test_waliduj_haslo_false_brak_wielkiej():
    assert waliduj_haslo("abc12def") is False


def test_waliduj_haslo_false_brak_cyfry():
    assert waliduj_haslo("AbcDefgh") is False


def test_waliduj_haslo_false_za_krotkie():
    assert waliduj_haslo("Abc1def") is False  # 7 znakow


def test_slowa_nie_poprzedzone_liczba():
    wynik = slowa_nie_poprzedzone_liczba("abc 3xyz def")
    assert wynik == ["abc", "def"]


def test_bezpieczne_wyszukaj():
    assert bezpieczne_wyszukaj("3.14", "wynik: 3.14 przybl: 3x14") == ["3.14"]
    assert bezpieczne_wyszukaj("(ok)", "status: (ok) i (ok)") == ["(ok)", "(ok)"]


def test_bezpieczne_wyszukaj_brak():
    assert bezpieczne_wyszukaj("xyz", "abc def") == []

