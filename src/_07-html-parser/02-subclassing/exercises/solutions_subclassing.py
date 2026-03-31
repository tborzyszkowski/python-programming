"""Przykladowe rozwiazania: rozszerzanie parsera (subclassing)."""
from html.parser import HTMLParser


# ── zbierz_naglowki ──────────────────────────────────────────────

_HEADING_TAGS = frozenset({"h1", "h2", "h3", "h4", "h5", "h6"})


class _HeadingCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings: list[tuple[int, str]] = []
        self._tag: str | None = None
        self._text: str = ""

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in _HEADING_TAGS:
            self._tag = tag
            self._text = ""

    def handle_data(self, data: str) -> None:
        if self._tag is not None:
            self._text += data

    def handle_endtag(self, tag: str) -> None:
        if tag in _HEADING_TAGS and self._tag == tag:
            self.headings.append((int(tag[1]), self._text.strip()))
            self._tag = None


def zbierz_naglowki(html: str) -> list[tuple[int, str]]:
    p = _HeadingCollector()
    p.feed(html)
    p.close()
    return p.headings


# ── wyciagnij_src_obrazkow ────────────────────────────────────────

class _ImageSrcExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            for name, value in attrs:
                if name == "src" and value:
                    self.sources.append(value)


def wyciagnij_src_obrazkow(html: str) -> list[str]:
    p = _ImageSrcExtractor()
    p.feed(html)
    p.close()
    return p.sources


# ── zbierz_tekst_z_tagu ──────────────────────────────────────────

class _TagTextCollector(HTMLParser):
    def __init__(self, target: str) -> None:
        super().__init__()
        self.target = target
        self.results: list[str] = []
        self._inside: bool = False
        self._depth: int = 0
        self._text: str = ""

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == self.target and not self._inside:
            self._inside = True
            self._depth = 1
            self._text = ""
        elif self._inside:
            self._depth += 1

    def handle_data(self, data: str) -> None:
        if self._inside and self._depth == 1:
            self._text += data

    def handle_endtag(self, tag: str) -> None:
        if self._inside:
            if tag == self.target:
                self._depth -= 1
            if self._depth == 0:
                self.results.append(self._text.strip())
                self._inside = False


def zbierz_tekst_z_tagu(html: str, target_tag: str) -> list[str]:
    p = _TagTextCollector(target_tag)
    p.feed(html)
    p.close()
    return p.results

