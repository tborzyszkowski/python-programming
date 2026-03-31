"""Porownanie HTMLParser z BeautifulSoup na tym samym dokumencie.

Uruchomienie:
    python src/_07-html-parser/06-limitations-and-alternatives/examples/alternatives_demo.py

BeautifulSoup jest opcjonalny – jesli nie jest zainstalowany,
skrypt pokaze tylko wynik HTMLParser.
"""
from __future__ import annotations

from html.parser import HTMLParser

# ── Wspolny dokument testowy ──────────────────────────────────────

SAMPLE_HTML = """\
<!DOCTYPE html>
<html>
<body>
    <div class="content">
        <h1>Tytul artykulu</h1>
        <p>Pierwszy akapit z <b>pogrubieniem</b>.</p>
        <p>Drugi akapit z <a href="/link">linkiem</a>.</p>
    </div>
    <div class="sidebar">
        <p>Reklama</p>
    </div>
    <!-- Malformed: brak zamkniecia p -->
    <p>Akapit bez zamkniecia
    <div>Kolejny blok</div>
</body>
</html>
"""

# ── 1. Rozwiazanie HTMLParser ─────────────────────────────────────

class ContentParagraphExtractor(HTMLParser):
    """Wyciaga tekst z <p> wewnatrz <div class='content'>."""

    def __init__(self) -> None:
        super().__init__()
        self._in_content_div: bool = False
        self._div_depth: int = 0
        self._in_p: bool = False
        self._text: str = ""
        self.paragraphs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        attrs_dict = dict(attrs)
        if tag == "div":
            if attrs_dict.get("class") == "content":
                self._in_content_div = True
                self._div_depth = 1
            elif self._in_content_div:
                self._div_depth += 1
        elif tag == "p" and self._in_content_div:
            self._in_p = True
            self._text = ""

    def handle_data(self, data: str) -> None:
        if self._in_p:
            self._text += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "p" and self._in_p:
            self.paragraphs.append(self._text.strip())
            self._in_p = False
        elif tag == "div" and self._in_content_div:
            self._div_depth -= 1
            if self._div_depth <= 0:
                self._in_content_div = False


def demo_htmlparser() -> list[str]:
    """Wyciaga akapity z div.content uzywajac HTMLParser."""
    parser = ContentParagraphExtractor()
    parser.feed(SAMPLE_HTML)
    parser.close()
    return parser.paragraphs


# ── 2. Rozwiazanie BeautifulSoup (opcjonalne) ────────────────────

def demo_beautifulsoup() -> list[str] | None:
    """Wyciaga akapity z div.content uzywajac BeautifulSoup (jesli dostepny)."""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        return None

    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    return [p.get_text() for p in soup.select("div.content > p")]


# ── Demo ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  Porownanie: HTMLParser vs BeautifulSoup")
    print("=" * 60)

    # HTMLParser
    wynik_hp = demo_htmlparser()
    print(f"\n1. HTMLParser ({len(wynik_hp)} akapitow):")
    for i, p in enumerate(wynik_hp, 1):
        print(f"   {i}. {p}")
    print(f"   Liczba linii kodu klasy: ~30")

    # BeautifulSoup
    wynik_bs = demo_beautifulsoup()
    if wynik_bs is not None:
        print(f"\n2. BeautifulSoup ({len(wynik_bs)} akapitow):")
        for i, p in enumerate(wynik_bs, 1):
            print(f"   {i}. {p}")
        print(f"   Liczba linii kodu: 3")
    else:
        print("\n2. BeautifulSoup: nie zainstalowany (pip install beautifulsoup4)")

    # Porownanie
    print("\n" + "-" * 60)
    print("  Wnioski:")
    print("  - HTMLParser wymaga wiecej kodu, ale nie ma zaleznosci.")
    print("  - BeautifulSoup: 3 linie zamiast 30, ale wymaga instalacji.")
    print("  - Dla malformed HTML, BS4 radzi sobie lepiej.")
    print("  - Dla duzych plikow, HTMLParser zuzywa mniej pamieci.")

