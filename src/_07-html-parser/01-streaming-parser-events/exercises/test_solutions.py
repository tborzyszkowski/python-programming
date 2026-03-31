import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_streaming import (
    policz_zdarzenia,
    wyciagnij_tekst,
    czy_tagi_zamkniete,
)


# ── policz_zdarzenia ──────────────────────────────────────────────

def test_policz_zdarzenia_prosty():
    wynik = policz_zdarzenia("<p>Hello</p>")
    assert wynik["starttag"] == 1
    assert wynik["endtag"] == 1
    assert wynik["data"] == 1


def test_policz_zdarzenia_komentarz_i_startend():
    wynik = policz_zdarzenia("<!-- x --><br/>")
    assert wynik["comment"] == 1
    assert wynik["startendtag"] == 1
    assert wynik["starttag"] == 0


def test_policz_zdarzenia_zlozone():
    html = "<div><p>A</p><p>B</p></div>"
    wynik = policz_zdarzenia(html)
    assert wynik["starttag"] == 3   # div, p, p
    assert wynik["endtag"] == 3     # p, p, div
    assert wynik["data"] == 2       # A, B


# ── wyciagnij_tekst ───────────────────────────────────────────────

def test_wyciagnij_tekst_prosty():
    assert wyciagnij_tekst("<p>Hello <b>World</b></p>") == "Hello World"


def test_wyciagnij_tekst_zagniezdzony():
    assert wyciagnij_tekst("<div>  A  <span>B</span>  </div>") == "A  B"


def test_wyciagnij_tekst_pusty():
    assert wyciagnij_tekst("<div></div>") == ""


# ── czy_tagi_zamkniete ────────────────────────────────────────────

def test_czy_tagi_zamkniete_true():
    assert czy_tagi_zamkniete("<p>Hello</p>") is True


def test_czy_tagi_zamkniete_false():
    assert czy_tagi_zamkniete("<p>Hello") is False


def test_czy_tagi_zamkniete_void():
    assert czy_tagi_zamkniete("<br><p>Ok</p>") is True


def test_czy_tagi_zamkniete_brak_zamkniecia():
    assert czy_tagi_zamkniete("<p><b>Bold</p>") is False

