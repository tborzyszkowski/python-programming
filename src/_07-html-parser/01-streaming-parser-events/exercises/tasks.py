"""Zadania: analizator strumieniowy i model zdarzen."""
from html.parser import HTMLParser


def policz_zdarzenia(html: str) -> dict[str, int]:
    """Zlicza zdarzenia wygenerowane przez HTMLParser.

    Zwraca slownik z kluczami:
        "starttag", "endtag", "data", "comment", "startendtag"
    i wartosciami bedacymi liczbami odpowiednich zdarzen.

    Przyklad:
        policz_zdarzenia("<p>Hello</p>")
        -> {"starttag": 1, "endtag": 1, "data": 1, "comment": 0, "startendtag": 0}

        policz_zdarzenia("<!-- x --><br/>")
        -> {"starttag": 0, "endtag": 0, "data": 0, "comment": 1, "startendtag": 1}
    """
    raise NotImplementedError("Zaimplementuj policz_zdarzenia")


def wyciagnij_tekst(html: str) -> str:
    """Zwraca polaczony tekst (handle_data) z dokumentu HTML.

    Biale znaki na poczatku i koncu wyniku sa uciete (strip).

    Przyklad:
        wyciagnij_tekst("<p>Hello <b>World</b></p>")
        -> "Hello World"

        wyciagnij_tekst("<div>  A  <span>B</span>  </div>")
        -> "A  B"
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_tekst")


def czy_tagi_zamkniete(html: str) -> bool:
    """Sprawdza, czy kazdy tag otwierajacy ma odpowiadajacy tag zamykajacy.

    UWAGA: Pomija void elements (br, hr, img, input, meta, link, area, base,
    col, embed, source, track, wbr). Nie sprawdza kolejnosci zagniezdzenia.

    Przyklad:
        czy_tagi_zamkniete("<p>Hello</p>")          -> True
        czy_tagi_zamkniete("<p>Hello")               -> False
        czy_tagi_zamkniete("<br><p>Ok</p>")          -> True  (br to void element)
        czy_tagi_zamkniete("<p><b>Bold</p>")         -> False (brak </b>)
    """
    raise NotImplementedError("Zaimplementuj czy_tagi_zamkniete")

