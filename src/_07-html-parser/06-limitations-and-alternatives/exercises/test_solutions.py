import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_alternatives import (
    wyciagnij_tekst_z_klasy,
    napraw_niezamkniete_tagi,
    html_do_markdown,
)


# ── wyciagnij_tekst_z_klasy ──────────────────────────────────────

def test_wyciagnij_tekst_z_klasy_info():
    html = '<div class="info">Hello</div><div class="ad">Reklama</div>'
    assert wyciagnij_tekst_z_klasy(html, "info") == ["Hello"]


def test_wyciagnij_tekst_z_klasy_brak():
    html = '<div class="other">X</div>'
    assert wyciagnij_tekst_z_klasy(html, "info") == []


def test_wyciagnij_tekst_z_klasy_wiele():
    html = '<div class="item">A</div><p>X</p><div class="item">B</div>'
    assert wyciagnij_tekst_z_klasy(html, "item") == ["A", "B"]


# ── napraw_niezamkniete_tagi ──────────────────────────────────────

def test_napraw_niezamkniete_div_p():
    assert napraw_niezamkniete_tagi("<div><p>Tekst") == "<div><p>Tekst</p></div>"


def test_napraw_zamkniete():
    assert napraw_niezamkniete_tagi("<p>OK</p>") == "<p>OK</p>"


def test_napraw_void():
    assert napraw_niezamkniete_tagi("<p>A<br>B") == "<p>A<br>B</p>"


def test_napraw_wiele():
    result = napraw_niezamkniete_tagi("<div><span><b>X")
    assert result.endswith("</b></span></div>")


# ── html_do_markdown ──────────────────────────────────────────────

def test_markdown_naglowek():
    assert html_do_markdown("<h1>Tytul</h1>") == "# Tytul"


def test_markdown_bold():
    assert "**bold**" in html_do_markdown("<p>Tekst z <b>bold</b>.</p>")


def test_markdown_italic():
    assert "*kursywa*" in html_do_markdown("<p>Tekst <i>kursywa</i> koniec.</p>")


def test_markdown_link():
    wynik = html_do_markdown('<a href="https://x.com">Link</a>')
    assert "[Link](https://x.com)" in wynik


def test_markdown_zlozony():
    html = "<h1>Tytul</h1><p>Tekst z <b>bold</b>.</p>"
    wynik = html_do_markdown(html)
    assert "# Tytul" in wynik
    assert "**bold**" in wynik

