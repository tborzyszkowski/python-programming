import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_callbacks import (
    wyciagnij_komentarze,
    zbierz_atrybuty,
    tekst_bez_tagow,
    mapa_zdarzen,
)


# ── wyciagnij_komentarze ──────────────────────────────────────────

def test_wyciagnij_komentarze_dwa():
    assert wyciagnij_komentarze("<!-- TODO --><p>X</p><!-- v2 -->") == ["TODO", "v2"]


def test_wyciagnij_komentarze_brak():
    assert wyciagnij_komentarze("<p>Brak</p>") == []


def test_wyciagnij_komentarze_wieloliniowy():
    html = "<!--\n  linia1\n  linia2\n-->"
    wynik = wyciagnij_komentarze(html)
    assert len(wynik) == 1
    assert "linia1" in wynik[0]


# ── zbierz_atrybuty ───────────────────────────────────────────────

def test_zbierz_atrybuty_a():
    html = '<a href="x" class="c">A</a><a href="y">B</a>'
    wynik = zbierz_atrybuty(html, "a")
    assert wynik == [{"href": "x", "class": "c"}, {"href": "y"}]


def test_zbierz_atrybuty_img():
    html = '<img src="a.png"><img src="b.png" alt="B">'
    wynik = zbierz_atrybuty(html, "img")
    assert wynik == [{"src": "a.png"}, {"src": "b.png", "alt": "B"}]


def test_zbierz_atrybuty_brak():
    assert zbierz_atrybuty("<p>Tekst</p>", "a") == []


# ── tekst_bez_tagow ───────────────────────────────────────────────

def test_tekst_bez_tagow_encje():
    assert tekst_bez_tagow("<p>Hello &amp; World</p>") == "Hello & World"


def test_tekst_bez_tagow_zagniezdzony():
    assert tekst_bez_tagow("<!-- c --><div>  A  <b>B</b>  </div>") == "A  B"


def test_tekst_bez_tagow_pusty():
    assert tekst_bez_tagow("<div></div>") == ""


# ── mapa_zdarzen ──────────────────────────────────────────────────

def test_mapa_zdarzen_prosty():
    wynik = mapa_zdarzen("<p>Hi</p><!-- x -->")
    assert ("starttag", "<p>") in wynik
    assert ("data", "Hi") in wynik
    assert ("endtag", "</p>") in wynik
    assert ("comment", "x") in wynik


def test_mapa_zdarzen_pomija_puste_data():
    wynik = mapa_zdarzen("<div>  </div>")
    typy = [e[0] for e in wynik]
    assert "data" not in typy


def test_mapa_zdarzen_startendtag():
    wynik = mapa_zdarzen("<br/>")
    assert ("startendtag", "<br/>") in wynik

