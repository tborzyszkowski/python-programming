"""Kompletny ekstraktor linkow z HTML z normalizacja i filtrowaniem.

Uruchomienie:
    python src/_07-html-parser/04-link-extraction/examples/link_extractor.py
"""
from __future__ import annotations

from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse


# ── Ekstraktor linkow ─────────────────────────────────────────────

_SKIP_SCHEMES = ("javascript:", "mailto:", "tel:")


class LinkExtractor(HTMLParser):
    """Wyciaga linki <a href="..."> wraz z tekstem (anchor text).

    Opcjonalnie normalizuje URL-e wzgledem podanego base_url
    i pomija schematy javascript:, mailto:, tel:.
    """

    def __init__(self, base_url: str = "") -> None:
        super().__init__()
        self.base_url = base_url
        self.links: list[tuple[str, str]] = []   # (href, anchor_text)
        self._href: str | None = None
        self._text: str = ""

    # ── Callbacki ─────────────────────────────────────────────────

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            # Szukamy atrybutu href
            for name, value in attrs:
                if name == "href" and value is not None:
                    self._href = value.strip()
                    self._text = ""
                    break

    def handle_data(self, data: str) -> None:
        # Zbieramy tekst wewnatrz <a>...</a>
        if self._href is not None:
            self._text += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._href is not None:
            href = self._normalize(self._href)
            if href and not href.startswith(_SKIP_SCHEMES):
                self.links.append((href, self._text.strip()))
            self._href = None
            self._text = ""

    # ── Normalizacja ──────────────────────────────────────────────

    def _normalize(self, href: str) -> str:
        """Zamienia sciezki relatywne na absolutne (jesli podano base_url)."""
        if self.base_url:
            return urljoin(self.base_url, href)
        return href


# ── Funkcje pomocnicze ────────────────────────────────────────────

def wyciagnij_linki(html: str, base_url: str = "") -> list[tuple[str, str]]:
    """Zwraca liste (href, anchor_text) ze wszystkich <a> w html."""
    parser = LinkExtractor(base_url)
    parser.feed(html)
    parser.close()
    return parser.links


def filtruj_zewnetrzne(
    links: list[tuple[str, str]], base_domain: str
) -> list[tuple[str, str]]:
    """Zwraca tylko linki prowadzace do innej domeny niz base_domain."""
    wynik = []
    for href, text in links:
        parsed = urlparse(href)
        if parsed.netloc and parsed.netloc != base_domain:
            wynik.append((href, text))
    return wynik


def deduplikuj(links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Usuwa duplikaty zachowujac kolejnosc (po href)."""
    seen: set[str] = set()
    wynik = []
    for href, text in links:
        if href not in seen:
            seen.add(href)
            wynik.append((href, text))
    return wynik


# ── Demo ──────────────────────────────────────────────────────────

SAMPLE_HTML = """\
<!DOCTYPE html>
<html>
<head>
    <title>Strona z linkami</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <nav>
        <a href="/">Strona glowna</a>
        <a href="/about">O nas</a>
        <a href="https://github.com/python">Python na GitHub</a>
    </nav>

    <main>
        <h1>Artykul</h1>
        <p>
            Odwiedz <a href="https://docs.python.org/3/">dokumentacje Pythona</a>
            lub <a href="/tutorials/intro">nasz poradnik</a>.
        </p>
        <p>
            Kontakt: <a href="mailto:info@example.com">info@example.com</a>
        </p>
        <p>
            <a href="javascript:void(0)">Kliknij (JS)</a>
        </p>
        <p>
            <a href="https://docs.python.org/3/">dokumentacja (duplikat)</a>
        </p>
    </main>

    <footer>
        <a href="https://example.com/privacy">Polityka prywatnosci</a>
    </footer>
</body>
</html>
"""

BASE_URL = "https://example.com/blog/post.html"

if __name__ == "__main__":
    print("=" * 60)
    print("  Ekstrakcja linkow z HTML")
    print("=" * 60)

    # 1. Wyciagniecie wszystkich linkow
    linki = wyciagnij_linki(SAMPLE_HTML, base_url=BASE_URL)
    print(f"\n1. Wszystkie linki ({len(linki)}):")
    for href, text in linki:
        print(f"   {text:30s} -> {href}")

    # 2. Filtrowanie zewnetrznych
    zewnetrzne = filtruj_zewnetrzne(linki, "example.com")
    print(f"\n2. Linki zewnetrzne ({len(zewnetrzne)}):")
    for href, text in zewnetrzne:
        print(f"   {text:30s} -> {href}")

    # 3. Deduplikacja
    unikalne = deduplikuj(linki)
    print(f"\n3. Po deduplikacji ({len(unikalne)}):")
    for href, text in unikalne:
        print(f"   {text:30s} -> {href}")

