"""Przykladowe rozwiazania: analizator strumieniowy i model zdarzen."""
from html.parser import HTMLParser


# ── policz_zdarzenia ──────────────────────────────────────────────

class _EventCounter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.counts: dict[str, int] = {
            "starttag": 0,
            "endtag": 0,
            "data": 0,
            "comment": 0,
            "startendtag": 0,
        }

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self.counts["starttag"] += 1

    def handle_endtag(self, tag: str) -> None:
        self.counts["endtag"] += 1

    def handle_data(self, data: str) -> None:
        self.counts["data"] += 1

    def handle_comment(self, data: str) -> None:
        self.counts["comment"] += 1

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self.counts["startendtag"] += 1


def policz_zdarzenia(html: str) -> dict[str, int]:
    parser = _EventCounter()
    parser.feed(html)
    parser.close()
    return parser.counts


# ── wyciagnij_tekst ───────────────────────────────────────────────

class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def wyciagnij_tekst(html: str) -> str:
    parser = _TextExtractor()
    parser.feed(html)
    parser.close()
    return "".join(parser.parts).strip()


# ── czy_tagi_zamkniete ────────────────────────────────────────────

_VOID_ELEMENTS = frozenset({
    "br", "hr", "img", "input", "meta", "link",
    "area", "base", "col", "embed", "source", "track", "wbr",
})


class _TagBalanceChecker(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.open_counts: dict[str, int] = {}
        self.close_counts: dict[str, int] = {}

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag not in _VOID_ELEMENTS:
            self.open_counts[tag] = self.open_counts.get(tag, 0) + 1

    def handle_endtag(self, tag: str) -> None:
        if tag not in _VOID_ELEMENTS:
            self.close_counts[tag] = self.close_counts.get(tag, 0) + 1


def czy_tagi_zamkniete(html: str) -> bool:
    parser = _TagBalanceChecker()
    parser.feed(html)
    parser.close()
    all_tags = set(parser.open_counts) | set(parser.close_counts)
    return all(
        parser.open_counts.get(t, 0) == parser.close_counts.get(t, 0)
        for t in all_tags
    )

