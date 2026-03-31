import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_counting import (
    policz_tagi,
    najczestszy_tag,
    glebokosc_zagniezdzenia,
    statystyki_dokumentu,
)


# ── policz_tagi ───────────────────────────────────────────────────

def test_policz_tagi_prosty():
    c = policz_tagi("<div><p>A</p><p>B</p><br></div>")
    assert c["p"] == 2
    assert c["div"] == 1
    assert c["br"] == 1


def test_policz_tagi_pusty():
    c = policz_tagi("zwykly tekst")
    assert len(c) == 0


def test_policz_tagi_startendtag():
    c = policz_tagi("<br/><hr/>")
    assert c["br"] == 1
    assert c["hr"] == 1


# ── najczestszy_tag ───────────────────────────────────────────────

def test_najczestszy_tag_p():
    assert najczestszy_tag("<p>A</p><p>B</p><div>C</div>") == "p"


def test_najczestszy_tag_none():
    assert najczestszy_tag("brak tagow") is None


def test_najczestszy_tag_jeden():
    assert najczestszy_tag("<span>X</span>") == "span"


# ── glebokosc_zagniezdzenia ───────────────────────────────────────

def test_glebokosc_zagniezdzenia_3():
    assert glebokosc_zagniezdzenia("<div><p><b>X</b></p></div>") == 3


def test_glebokosc_zagniezdzenia_void():
    assert glebokosc_zagniezdzenia("<br><p>A</p>") == 1


def test_glebokosc_zagniezdzenia_zero():
    assert glebokosc_zagniezdzenia("tekst bez tagow") == 0


def test_glebokosc_zagniezdzenia_zlozone():
    html = "<html><body><div><ul><li>X</li></ul></div></body></html>"
    assert glebokosc_zagniezdzenia(html) == 5


# ── statystyki_dokumentu ──────────────────────────────────────────

def test_statystyki_dokumentu_prosty():
    s = statystyki_dokumentu("<p>Hello</p>")
    assert s["total_tags"] == 1
    assert s["unique_tags"] == 1
    assert s["max_depth"] == 1
    assert s["text_length"] == 5


def test_statystyki_dokumentu_zlozone():
    html = "<div><p>AB</p><p>CD</p><br></div>"
    s = statystyki_dokumentu(html)
    assert s["total_tags"] == 4  # div, p, p, br
    assert s["unique_tags"] == 3  # div, p, br
    assert s["max_depth"] == 2
    assert s["text_length"] == 4  # AB + CD

