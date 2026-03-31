"""Kompletny analizator HTML – zliczanie tagow, histogram, glebokosc.

Uruchomienie:
    python src/_07-html-parser/05-tag-counting/examples/tag_counter.py
"""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser


VOID_ELEMENTS = frozenset({
    "br", "hr", "img", "input", "meta", "link",
    "area", "base", "col", "embed", "source", "track", "wbr",
})


class HTMLAnalyzer(HTMLParser):
    """Zbiera statystyki struktury dokumentu HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.tag_counts: Counter[str] = Counter()
        self.depth: int = 0
        self.max_depth: int = 0
        self.text_length: int = 0
        self.total_tags: int = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self.tag_counts[tag] += 1
        self.total_tags += 1
        if tag not in VOID_ELEMENTS:
            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)

    def handle_endtag(self, tag: str) -> None:
        if tag not in VOID_ELEMENTS:
            self.depth = max(0, self.depth - 1)

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self.tag_counts[tag] += 1
        self.total_tags += 1

    def handle_data(self, data: str) -> None:
        stripped = data.strip()
        self.text_length += len(stripped)


def drukuj_histogram(counter: Counter, top_n: int = 10) -> None:
    """Drukuje histogram czestosci tagow jako slupki ASCII."""
    najczestsze = counter.most_common(top_n)
    if not najczestsze:
        print("  (brak tagow)")
        return
    max_count = najczestsze[0][1]
    max_bar = 40

    for tag, count in najczestsze:
        bar_len = int(count / max_count * max_bar) if max_count > 0 else 0
        bar = "\u2588" * bar_len
        print(f"  {tag:12s} | {bar} ({count})")


def analizuj(html: str) -> HTMLAnalyzer:
    """Analizuje dokument HTML i zwraca obiekt ze statystykami."""
    analyzer = HTMLAnalyzer()
    analyzer.feed(html)
    analyzer.close()
    return analyzer


# ── Demo ──────────────────────────────────────────────────────────

SAMPLE_HTML = """\
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Przykladowa strona</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <main>
        <h1>Tytul strony</h1>
        <p>Pierwszy akapit z <b>pogrubieniem</b> i <i>kursywa</i>.</p>
        <p>Drugi akapit z <a href="/link">linkiem</a>.</p>
        <div class="gallery">
            <img src="img1.jpg" alt="Obraz 1">
            <img src="img2.jpg" alt="Obraz 2">
            <img src="img3.jpg" alt="Obraz 3">
        </div>
        <h2>Podsekcja</h2>
        <ul>
            <li>Element 1</li>
            <li>Element 2</li>
            <li>Element 3</li>
        </ul>
    </main>
    <footer>
        <p>Stopka &copy; 2025</p>
    </footer>
</body>
</html>
"""

if __name__ == "__main__":
    a = analizuj(SAMPLE_HTML)

    print("=" * 55)
    print("  Analiza struktury HTML")
    print("=" * 55)
    print(f"\n  Laczna liczba tagow:    {a.total_tags}")
    print(f"  Unikalne tagi:          {len(a.tag_counts)}")
    print(f"  Maks. glebokosc:        {a.max_depth}")
    print(f"  Dlugosc tekstu:         {a.text_length} znakow")

    print(f"\n  Top 10 tagow:")
    drukuj_histogram(a.tag_counts, 10)

    print(f"\n  Wszystkie tagi:")
    for tag, count in sorted(a.tag_counts.items()):
        print(f"    <{tag}>: {count}")

