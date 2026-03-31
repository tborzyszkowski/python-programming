"""Demonstracja tworzenia wlasnych podklas HTMLParser.

Uruchomienie:
    python src/_07-html-parser/02-subclassing/examples/custom_parser.py
"""
from html.parser import HTMLParser


# ── TextCollector ─────────────────────────────────────────────────

class TextCollector(HTMLParser):
    """Zbiera caly tekst z dokumentu HTML, pomijajac tagi."""

    def __init__(self) -> None:
        super().__init__()
        self.texts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.texts.append(data)

    def get_text(self) -> str:
        return " ".join(self.texts).strip()


# ── HeadingCollector ──────────────────────────────────────────────

class HeadingCollector(HTMLParser):
    """Zbiera tresc naglowkow h1-h6 jako liste krotek (poziom, tekst)."""

    HEADING_TAGS = frozenset({"h1", "h2", "h3", "h4", "h5", "h6"})

    def __init__(self) -> None:
        super().__init__()
        self.headings: list[tuple[int, str]] = []
        self._current_tag: str | None = None
        self._current_text: str = ""

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in self.HEADING_TAGS:
            self._current_tag = tag
            self._current_text = ""

    def handle_data(self, data: str) -> None:
        if self._current_tag is not None:
            self._current_text += data

    def handle_endtag(self, tag: str) -> None:
        if tag in self.HEADING_TAGS and self._current_tag == tag:
            level = int(tag[1])
            self.headings.append((level, self._current_text.strip()))
            self._current_tag = None
            self._current_text = ""


# ── ImageExtractor ────────────────────────────────────────────────

class ImageExtractor(HTMLParser):
    """Wyciaga atrybuty src ze wszystkich tagow <img>."""

    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            attrs_dict = dict(attrs)
            src = attrs_dict.get("src")
            if src:
                self.sources.append(src)


# ── Demo ──────────────────────────────────────────────────────────

SAMPLE_HTML = """\
<html>
<head><title>Przykladowa strona</title></head>
<body>
    <h1>Glowny tytul</h1>
    <p>Tekst wprowadzajacy do tematu.</p>
    <h2>Podtytul A</h2>
    <p>Opis sekcji A z <b>pogrubieniem</b>.</p>
    <img src="diagram1.png" alt="Diagram 1">
    <h2>Podtytul B</h2>
    <p>Opis sekcji B.</p>
    <img src="diagram2.png" alt="Diagram 2">
    <img src="foto.jpg" alt="Zdjecie">
</body>
</html>
"""

if __name__ == "__main__":
    # 1. TextCollector
    tc = TextCollector()
    tc.feed(SAMPLE_HTML)
    print("=== TextCollector ===")
    print(f"Tekst: {tc.get_text()[:80]}...")

    # 2. HeadingCollector
    hc = HeadingCollector()
    hc.feed(SAMPLE_HTML)
    print("\n=== HeadingCollector ===")
    for level, text in hc.headings:
        print(f"  h{level}: {text}")

    # 3. ImageExtractor
    ie = ImageExtractor()
    ie.feed(SAMPLE_HTML)
    print("\n=== ImageExtractor ===")
    for src in ie.sources:
        print(f"  src={src}")

