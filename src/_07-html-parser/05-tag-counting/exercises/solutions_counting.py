"""Przykladowe rozwiazania: zliczanie tagow HTML."""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser

_VOID = frozenset({
    "br", "hr", "img", "input", "meta", "link",
    "area", "base", "col", "embed", "source", "track", "wbr",
})


# ── policz_tagi ───────────────────────────────────────────────────

class _TagCounter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.counter: Counter[str] = Counter()

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self.counter[tag] += 1

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self.counter[tag] += 1


def policz_tagi(html: str) -> Counter:
    p = _TagCounter()
    p.feed(html)
    p.close()
    return p.counter


# ── najczestszy_tag ───────────────────────────────────────────────

def najczestszy_tag(html: str) -> str | None:
    c = policz_tagi(html)
    if not c:
        return None
    return c.most_common(1)[0][0]


# ── glebokosc_zagniezdzenia ───────────────────────────────────────

class _DepthMeter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.depth: int = 0
        self.max_depth: int = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag not in _VOID:
            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)

    def handle_endtag(self, tag: str) -> None:
        if tag not in _VOID:
            self.depth = max(0, self.depth - 1)


def glebokosc_zagniezdzenia(html: str) -> int:
    p = _DepthMeter()
    p.feed(html)
    p.close()
    return p.max_depth


# ── statystyki_dokumentu ──────────────────────────────────────────

class _StatsCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tag_counts: Counter[str] = Counter()
        self.total: int = 0
        self.depth: int = 0
        self.max_depth: int = 0
        self.text_len: int = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self.tag_counts[tag] += 1
        self.total += 1
        if tag not in _VOID:
            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)

    def handle_endtag(self, tag: str) -> None:
        if tag not in _VOID:
            self.depth = max(0, self.depth - 1)

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self.tag_counts[tag] += 1
        self.total += 1

    def handle_data(self, data: str) -> None:
        self.text_len += len(data.strip())


def statystyki_dokumentu(html: str) -> dict:
    p = _StatsCollector()
    p.feed(html)
    p.close()
    return {
        "total_tags": p.total,
        "unique_tags": len(p.tag_counts),
        "max_depth": p.max_depth,
        "text_length": p.text_len,
    }

