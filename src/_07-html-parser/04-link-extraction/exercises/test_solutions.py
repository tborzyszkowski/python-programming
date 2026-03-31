import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_links import (
    wyciagnij_linki,
    wyciagnij_linki_z_tekstem,
    filtruj_linki_zewnetrzne,
    wyciagnij_obrazki,
)


# ── wyciagnij_linki ───────────────────────────────────────────────

def test_wyciagnij_linki_dwa():
    html = '<a href="https://x.com">X</a><a href="/y">Y</a>'
    assert wyciagnij_linki(html) == ["https://x.com", "/y"]


def test_wyciagnij_linki_brak_href():
    assert wyciagnij_linki('<a name="anchor">Bez href</a>') == []


def test_wyciagnij_linki_pusty_html():
    assert wyciagnij_linki("<p>Tekst</p>") == []


def test_wyciagnij_linki_wiele():
    html = """
    <nav>
        <a href="/a">A</a>
        <a href="/b">B</a>
        <a href="/c">C</a>
    </nav>
    """
    assert wyciagnij_linki(html) == ["/a", "/b", "/c"]


# ── wyciagnij_linki_z_tekstem ─────────────────────────────────────

def test_wyciagnij_linki_z_tekstem_prosty():
    html = '<a href="/home">  Strona glowna  </a>'
    assert wyciagnij_linki_z_tekstem(html) == [("/home", "Strona glowna")]


def test_wyciagnij_linki_z_tekstem_wiele():
    html = '<a href="/a">AAA</a><a href="/b">BBB</a>'
    wynik = wyciagnij_linki_z_tekstem(html)
    assert wynik == [("/a", "AAA"), ("/b", "BBB")]


# ── filtruj_linki_zewnetrzne ──────────────────────────────────────

def test_filtruj_linki_zewnetrzne():
    html = '<a href="https://other.com/x">X</a><a href="https://my.com/y">Y</a>'
    assert filtruj_linki_zewnetrzne(html, "my.com") == ["https://other.com/x"]


def test_filtruj_linki_zewnetrzne_brak():
    html = '<a href="https://my.com/a">A</a><a href="/local">L</a>'
    assert filtruj_linki_zewnetrzne(html, "my.com") == []


def test_filtruj_linki_zewnetrzne_case_insensitive():
    html = '<a href="https://My.COM/x">X</a><a href="https://Other.COM/y">Y</a>'
    # My.COM case-insensitive == my.com → NIE jest zewnetrzny
    # Other.COM != my.com → jest zewnetrzny
    assert filtruj_linki_zewnetrzne(html, "my.com") == ["https://Other.COM/y"]


# ── wyciagnij_obrazki ─────────────────────────────────────────────

def test_wyciagnij_obrazki_dwa():
    html = '<img src="a.png" alt="Logo"><img src="b.jpg">'
    assert wyciagnij_obrazki(html) == [
        {"src": "a.png", "alt": "Logo"},
        {"src": "b.jpg", "alt": ""},
    ]


def test_wyciagnij_obrazki_brak_src():
    assert wyciagnij_obrazki('<img alt="x">') == []


def test_wyciagnij_obrazki_brak():
    assert wyciagnij_obrazki("<p>Tekst</p>") == []


