"""Zadania: ograniczenia HTMLParser i alternatywy."""
from html.parser import HTMLParser


def wyciagnij_tekst_z_klasy(html: str, class_name: str) -> list[str]:
    """Zwraca liste tekstow z tagow <div> o podanej klasie CSS.

    Zbiera tekst bezposrednio wewnatrz div (nie z zagniezdzonych div-ow).
    Wynik strip()-owany.

    Przyklad:
        html = '<div class="info">Hello</div><div class="ad">Reklama</div>'
        wyciagnij_tekst_z_klasy(html, "info")
        -> ["Hello"]
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_tekst_z_klasy")


def napraw_niezamkniete_tagi(html: str) -> str:
    """Dodaje brakujace tagi zamykajace na koncu dokumentu.

    Analizuje tagi otwierajace i zamykajace (pomijajac void elements).
    Dla kazdego niezamknietego tagu dodaje odpowiedni </tag>
    na koncu wyniku, w odwrotnej kolejnosci otwarcia (LIFO).

    Void elements: br, hr, img, input, meta, link, area, base,
    col, embed, source, track, wbr.

    Przyklad:
        napraw_niezamkniete_tagi("<div><p>Tekst")
        -> "<div><p>Tekst</p></div>"

        napraw_niezamkniete_tagi("<p>OK</p>")
        -> "<p>OK</p>"
    """
    raise NotImplementedError("Zaimplementuj napraw_niezamkniete_tagi")


def html_do_markdown(html: str) -> str:
    """Konwertuje prosty HTML na Markdown.

    Obslugiwane tagi:
    - <h1>...<h6> -> # ... ###### (z nowa linia przed i po)
    - <b> lub <strong> -> **...**
    - <i> lub <em> -> *...*
    - <a href="url">tekst</a> -> [tekst](url)
    - <p> -> nowa linia przed i po tekscie
    - <br> lub <br/> -> nowa linia
    - Pozostale tagi sa pomijane (tekst zachowany).

    Wynik jest strip()-owany.

    Przyklad:
        html_do_markdown("<h1>Tytul</h1><p>Tekst z <b>bold</b>.</p>")
        -> "# Tytul\\n\\nTekst z **bold**."
    """
    raise NotImplementedError("Zaimplementuj html_do_markdown")

