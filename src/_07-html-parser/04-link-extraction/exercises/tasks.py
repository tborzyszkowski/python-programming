"""Zadania: ekstrakcja linkow z HTML."""
from html.parser import HTMLParser


def wyciagnij_linki(html: str) -> list[str]:
    """Zwraca liste URL-i (href) ze wszystkich tagow <a> w html.

    Pomija tagi <a> bez atrybutu href. Zachowuje kolejnosc wystapienia.

    Przyklad:
        wyciagnij_linki('<a href="https://x.com">X</a><a href="/y">Y</a>')
        -> ["https://x.com", "/y"]

        wyciagnij_linki('<a name="anchor">Bez href</a>')
        -> []
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_linki")


def wyciagnij_linki_z_tekstem(html: str) -> list[tuple[str, str]]:
    """Zwraca liste krotek (href, anchor_text) ze wszystkich <a>.

    anchor_text to tekst widoczny pomiedzy <a> a </a>, strip()-owany.

    Przyklad:
        wyciagnij_linki_z_tekstem('<a href="/home">  Strona glowna  </a>')
        -> [("/home", "Strona glowna")]
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_linki_z_tekstem")


def filtruj_linki_zewnetrzne(html: str, base_domain: str) -> list[str]:
    """Zwraca liste href prowadzacych do INNEJ domeny niz base_domain.

    Bierze pod uwage tylko linki zaczynajace sie od http:// lub https://.
    Porownanie domen jest case-insensitive.

    Przyklad:
        html = '<a href="https://other.com/x">X</a><a href="https://my.com/y">Y</a>'
        filtruj_linki_zewnetrzne(html, "my.com")
        -> ["https://other.com/x"]
    """
    raise NotImplementedError("Zaimplementuj filtruj_linki_zewnetrzne")


def wyciagnij_obrazki(html: str) -> list[dict[str, str]]:
    """Zwraca liste slownikow z atrybutami 'src' i 'alt' tagow <img>.

    Jesli atrybut alt nie istnieje, wartosc to pusty string "".
    Jesli atrybut src nie istnieje, pomija tag.

    Przyklad:
        wyciagnij_obrazki('<img src="a.png" alt="Logo"><img src="b.jpg">')
        -> [{"src": "a.png", "alt": "Logo"}, {"src": "b.jpg", "alt": ""}]
    """
    raise NotImplementedError("Zaimplementuj wyciagnij_obrazki")

