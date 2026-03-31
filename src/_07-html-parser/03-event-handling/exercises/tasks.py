"""Zadania: obsluga zdarzen i wywolania zwrotne (callbacks)."""
from html.parser import HTMLParser


def wyciagnij_komentarze(html: str) -> list[str]:
    """Zwraca liste komentarzy HTML (tresc miedzy <!-- a -->), z obcietymi bialymi znakami.

    Przyklad:
        wyciagnij_komentarze("<!-- TODO --><p>X</p><!-- v2 -->")
        -> ["TODO", "v2"]

        wyciagnij_komentarze("<p>Brak komentarzy</p>")
        -> []
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_komentarze")


def zbierz_atrybuty(html: str, tag: str) -> list[dict[str, str | None]]:
    """Zwraca liste slownikow atrybutow dla kazdego wystapienia podanego tagu.

    Przyklad:
        zbierz_atrybuty('<a href="x" class="c">A</a><a href="y">B</a>', "a")
        -> [{"href": "x", "class": "c"}, {"href": "y"}]

        zbierz_atrybuty('<img src="a.png"><img src="b.png" alt="B">', "img")
        -> [{"src": "a.png"}, {"src": "b.png", "alt": "B"}]
    """
    raise NotImplementedError("Zaimplementuj zbierz_atrybuty")


def tekst_bez_tagow(html: str) -> str:
    """Zwraca caly tekst z dokumentu HTML z zachowaniem spacji,
    ale bez tagow, komentarzy i deklaracji. Wynik jest strip()-owany.

    Encje sa automatycznie konwertowane (convert_charrefs=True).

    Przyklad:
        tekst_bez_tagow("<p>Hello &amp; World</p>")
        -> "Hello & World"

        tekst_bez_tagow("<!-- c --><div>  A  <b>B</b>  </div>")
        -> "A  B"
    """
    raise NotImplementedError("Zaimplementuj tekst_bez_tagow")


def mapa_zdarzen(html: str) -> list[tuple[str, str]]:
    """Zwraca liste krotek (typ_zdarzenia, opis) w kolejnosci wystapienia.

    Typy zdarzen i format opisu:
        ("starttag",    "<tag>")
        ("endtag",      "</tag>")
        ("data",        tekst – tylko niepuste po strip)
        ("comment",     tresc komentarza strip)
        ("startendtag", "<tag/>")

    Pomija zdarzenia data, ktorych strip() jest pusty.

    Przyklad:
        mapa_zdarzen("<p>Hi</p><!-- x -->")
        -> [("starttag", "<p>"), ("data", "Hi"), ("endtag", "</p>"), ("comment", "x")]
    """
    raise NotImplementedError("Zaimplementuj mapa_zdarzen")

