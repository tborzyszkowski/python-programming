"""Przykladowe rozwiazania: ograniczenia HTMLParser i alternatywy."""
from __future__ import annotations

from html.parser import HTMLParser

_VOID = frozenset({
    "br", "hr", "img", "input", "meta", "link",
    "area", "base", "col", "embed", "source", "track", "wbr",
})


# ── wyciagnij_tekst_z_klasy ──────────────────────────────────────

class _ClassTextExtractor(HTMLParser):
    def __init__(self, class_name: str) -> None:
        super().__init__()
        self.target_class = class_name
        self.results: list[str] = []
        self._inside: bool = False
        self._depth: int = 0
        self._text: str = ""

    def handle_starttag(self, tag: str, attrs: list) -> None:
        attrs_dict = dict(attrs)
        if tag == "div" and attrs_dict.get("class") == self.target_class and not self._inside:
            self._inside = True
            self._depth = 1
            self._text = ""
        elif self._inside and tag == "div":
            self._depth += 1

    def handle_data(self, data: str) -> None:
        if self._inside and self._depth == 1:
            self._text += data

    def handle_endtag(self, tag: str) -> None:
        if self._inside and tag == "div":
            self._depth -= 1
            if self._depth <= 0:
                self.results.append(self._text.strip())
                self._inside = False
                self._text = ""


def wyciagnij_tekst_z_klasy(html: str, class_name: str) -> list[str]:
    p = _ClassTextExtractor(class_name)
    p.feed(html)
    p.close()
    return p.results


# ── napraw_niezamkniete_tagi ──────────────────────────────────────

class _TagTracker(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag not in _VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag not in _VOID and self.stack and self.stack[-1] == tag:
            self.stack.pop()


def napraw_niezamkniete_tagi(html: str) -> str:
    p = _TagTracker()
    p.feed(html)
    p.close()
    closing = "".join(f"</{tag}>" for tag in reversed(p.stack))
    return html + closing


# ── html_do_markdown ──────────────────────────────────────────────

class _MarkdownConverter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.output: list[str] = []
        self._heading_level: int = 0
        self._in_bold: bool = False
        self._in_italic: bool = False
        self._href: str | None = None
        self._link_text: str = ""

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading_level = int(tag[1])
            self.output.append("\n" + "#" * self._heading_level + " ")
        elif tag in ("b", "strong"):
            self._in_bold = True
            self.output.append("**")
        elif tag in ("i", "em"):
            self._in_italic = True
            self.output.append("*")
        elif tag == "a":
            attrs_dict = dict(attrs)
            self._href = attrs_dict.get("href", "")
            self._link_text = ""
        elif tag == "p":
            self.output.append("\n\n")
        elif tag in ("br",):
            self.output.append("\n")

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        if tag in ("br",):
            self.output.append("\n")

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._link_text += data
        else:
            self.output.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading_level = 0
        elif tag in ("b", "strong"):
            self._in_bold = False
            self.output.append("**")
        elif tag in ("i", "em"):
            self._in_italic = False
            self.output.append("*")
        elif tag == "a" and self._href is not None:
            self.output.append(f"[{self._link_text}]({self._href})")
            self._href = None
            self._link_text = ""


def html_do_markdown(html: str) -> str:
    p = _MarkdownConverter()
    p.feed(html)
    p.close()
    return "".join(p.output).strip()

