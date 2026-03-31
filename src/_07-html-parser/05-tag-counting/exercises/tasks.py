"""Zadania: zliczanie tagow HTML."""
from collections import Counter
from html.parser import HTMLParser


def policz_tagi(html: str) -> Counter:
    """Zwraca Counter z liczba wystapien kazdego tagu (otwierajacego i samozamykajacego).

    Przyklad:
        policz_tagi("<div><p>A</p><p>B</p><br></div>")
        -> Counter({"p": 2, "div": 1, "br": 1})
    """
    raise NotImplementedError("Zaimplementuj policz_tagi")


def najczestszy_tag(html: str) -> str | None:
    """Zwraca nazwe tagu, ktory wystepuje najczesciej.

    Jesli jest remis, zwraca dowolny z najczestszych.
    Jesli html nie zawiera tagow, zwraca None.

    Przyklad:
        najczestszy_tag("<p>A</p><p>B</p><div>C</div>")
        -> "p"
    """
    raise NotImplementedError("Zaimplementuj najczestszy_tag")


def glebokosc_zagniezdzenia(html: str) -> int:
    """Zwraca maksymalna glebokosc zagniezdzenia tagow w dokumencie.

    Void elements (br, hr, img, input, meta, link, area, base, col,
    embed, source, track, wbr) nie zwiekszaja glebokosci.

    Przyklad:
        glebokosc_zagniezdzenia("<div><p><b>X</b></p></div>")
        -> 3

        glebokosc_zagniezdzenia("<br><p>A</p>")
        -> 1

        glebokosc_zagniezdzenia("tekst bez tagow")
        -> 0
    """
    raise NotImplementedError("Zaimplementuj glebokosc_zagniezdzenia")


def statystyki_dokumentu(html: str) -> dict:
    """Zwraca slownik ze statystykami dokumentu HTML.

    Klucze:
        "total_tags"  (int) – laczna liczba tagow
        "unique_tags" (int) – liczba unikalnych tagow
        "max_depth"   (int) – maks. glebokosc zagniezdzenia
        "text_length" (int) – laczna dlugosc tekstu (strip, suma)

    Przyklad:
        statystyki_dokumentu("<p>Hello</p>")
        -> {"total_tags": 1, "unique_tags": 1, "max_depth": 1, "text_length": 5}
    """
    raise NotImplementedError("Zaimplementuj statystyki_dokumentu")

