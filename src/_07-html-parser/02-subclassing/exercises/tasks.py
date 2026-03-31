"""Zadania: rozszerzanie parsera (subclassing)."""
from html.parser import HTMLParser


def zbierz_naglowki(html: str) -> list[tuple[int, str]]:
    """Zwraca liste krotek (poziom, tekst) dla naglowkow h1-h6.

    Przyklad:
        zbierz_naglowki("<h1>Tytul</h1><h2>Podtytul</h2>")
        -> [(1, "Tytul"), (2, "Podtytul")]

        zbierz_naglowki("<p>Tekst</p>")
        -> []
    """
    raise NotImplementedError("Zaimplementuj zbierz_naglowki")


def wyciagnij_src_obrazkow(html: str) -> list[str]:
    """Zwraca liste wartosci atrybutu src ze wszystkich tagow <img>.

    Przyklad:
        wyciagnij_src_obrazkow('<img src="a.png"><p>x</p><img src="b.jpg">')
        -> ["a.png", "b.jpg"]

        wyciagnij_src_obrazkow('<p>Brak obrazkow</p>')
        -> []
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_src_obrazkow")


def zbierz_tekst_z_tagu(html: str, target_tag: str) -> list[str]:
    """Zwraca liste tekstow znajdujacych sie bezposrednio wewnatrz podanego tagu.

    Zbiera TYLKO tekst bedacy bezposrednim dzieckiem target_tag
    (nie zbiera tekstu z tagow zagniezdzonych glebiej).

    Przyklad:
        zbierz_tekst_z_tagu("<p>AAA</p><div>BBB</div><p>CCC</p>", "p")
        -> ["AAA", "CCC"]

        zbierz_tekst_z_tagu("<ul><li>X</li><li>Y</li></ul>", "li")
        -> ["X", "Y"]
    """
    raise NotImplementedError("Zaimplementuj zbierz_tekst_z_tagu")

