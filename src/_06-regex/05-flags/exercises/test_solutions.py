import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_flags import (
    szukaj_bez_wielkosci,
    znajdz_naglowki_markdown,
    wyciagnij_bloki_html,
    waliduj_numer_verbose,
)


def test_szukaj_bez_wielkosci():
    wynik = szukaj_bez_wielkosci("Python PYTHON python", "python")
    assert wynik == ["Python", "PYTHON", "python"]


def test_szukaj_bez_wielkosci_brak():
    assert szukaj_bez_wielkosci("hello world", "xyz") == []


def test_znajdz_naglowki_markdown():
    tekst = "# Tytul\n## Sekcja\nnormalny tekst\n### Podsekcja"
    assert znajdz_naglowki_markdown(tekst) == ["Tytul", "Sekcja", "Podsekcja"]


def test_znajdz_naglowki_markdown_brak():
    assert znajdz_naglowki_markdown("brak naglowkow") == []


def test_wyciagnij_bloki_html_jednoliniowe():
    wynik = wyciagnij_bloki_html("<p>kot</p><p>pies</p>", "p")
    assert wynik == ["kot", "pies"]


def test_wyciagnij_bloki_html_wieloliniowe():
    tekst = "<p>Ala\nma kota</p>"
    wynik = wyciagnij_bloki_html(tekst, "p")
    assert wynik == ["Ala\nma kota"]


def test_wyciagnij_bloki_html_brak():
    assert wyciagnij_bloki_html("<div>cos</div>", "p") == []


def test_waliduj_numer_verbose_true():
    assert waliduj_numer_verbose("600100200") is True
    assert waliduj_numer_verbose("600 100 200") is True
    assert waliduj_numer_verbose("600-100-200") is True
    assert waliduj_numer_verbose("+48600100200") is True


def test_waliduj_numer_verbose_false():
    assert waliduj_numer_verbose("123") is False
    assert waliduj_numer_verbose("abc def ghi") is False
    assert waliduj_numer_verbose("") is False

