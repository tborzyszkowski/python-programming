"""Przykladowe rozwiazania: obsluga zdarzen i wywolania zwrotne."""
from html.parser import HTMLParser


# ── wyciagnij_komentarze ──────────────────────────────────────────

class _CommentCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.comments: list[str] = []

    def handle_comment(self, data: str) -> None:
        self.comments.append(data.strip())


def wyciagnij_komentarze(html: str) -> list[str]:
    p = _CommentCollector()
    p.feed(html)
    p.close()
    return p.comments


# ── zbierz_atrybuty ───────────────────────────────────────────────

class _AttrCollector(HTMLParser):
    def __init__(self, target_tag: str) -> None:
        super().__init__()
        self.target = target_tag
        self.results: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == self.target:
            self.results.append(dict(attrs))


def zbierz_atrybuty(html: str, tag: str) -> list[dict[str, str | None]]:
    p = _AttrCollector(tag)
    p.feed(html)
    p.close()
    return p.results


# ── tekst_bez_tagow ───────────────────────────────────────────────

class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def tekst_bez_tagow(html: str) -> str:
    p = _TextExtractor()
    p.feed(html)
    p.close()
    return "".join(p.parts).strip()


# ── mapa_zdarzen ──────────────────────────────────────────────────

class _EventMapper(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.events: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self.events.append(("starttag", f"<{tag}>"))

    def handle_endtag(self, tag: str) -> None:
        self.events.append(("endtag", f"</{tag}>"))

    def handle_data(self, data: str) -> None:
        stripped = data.strip()
        if stripped:
            self.events.append(("data", stripped))

    def handle_comment(self, data: str) -> None:
        self.events.append(("comment", data.strip()))

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self.events.append(("startendtag", f"<{tag}/>"))


def mapa_zdarzen(html: str) -> list[tuple[str, str]]:
    p = _EventMapper()
    p.feed(html)
    p.close()
    return p.events

