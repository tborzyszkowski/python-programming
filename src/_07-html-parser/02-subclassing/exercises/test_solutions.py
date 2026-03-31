import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_subclassing import (
    zbierz_naglowki,
    wyciagnij_src_obrazkow,
    zbierz_tekst_z_tagu,
)


# ── zbierz_naglowki ──────────────────────────────────────────────

def test_zbierz_naglowki_podstawowy():
    html = "<h1>Tytul</h1><h2>Podtytul</h2>"
    assert zbierz_naglowki(html) == [(1, "Tytul"), (2, "Podtytul")]


def test_zbierz_naglowki_brak():
    assert zbierz_naglowki("<p>Tekst</p>") == []


def test_zbierz_naglowki_zagniezdzony_tekst():
    html = "<h3>Naglowek z <b>pogrubieniem</b></h3>"
    wynik = zbierz_naglowki(html)
    assert len(wynik) == 1
    assert wynik[0][0] == 3
    assert "Naglowek" in wynik[0][1]


# ── wyciagnij_src_obrazkow ────────────────────────────────────────

def test_wyciagnij_src_obrazkow_dwa():
    html = '<img src="a.png"><p>x</p><img src="b.jpg">'
    assert wyciagnij_src_obrazkow(html) == ["a.png", "b.jpg"]


def test_wyciagnij_src_obrazkow_brak():
    assert wyciagnij_src_obrazkow("<p>Brak</p>") == []


def test_wyciagnij_src_obrazkow_bez_src():
    assert wyciagnij_src_obrazkow('<img alt="x">') == []


# ── zbierz_tekst_z_tagu ──────────────────────────────────────────

def test_zbierz_tekst_z_tagu_p():
    html = "<p>AAA</p><div>BBB</div><p>CCC</p>"
    assert zbierz_tekst_z_tagu(html, "p") == ["AAA", "CCC"]


def test_zbierz_tekst_z_tagu_li():
    html = "<ul><li>X</li><li>Y</li></ul>"
    assert zbierz_tekst_z_tagu(html, "li") == ["X", "Y"]


def test_zbierz_tekst_z_tagu_brak():
    assert zbierz_tekst_z_tagu("<p>Hello</p>", "span") == []

