"""Przykladowe rozwiazania: ekstrakcja linkow z HTML."""
from __future__ import annotations

from html.parser import HTMLParser
from urllib.parse import urlparse


# ── wyciagnij_linki ───────────────────────────────────────────────

class _SimpleLinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value is not None:
                    self.links.append(value)
                    break


def wyciagnij_linki(html: str) -> list[str]:
    p = _SimpleLinkExtractor()
    p.feed(html)
    p.close()
    return p.links


# ── wyciagnij_linki_z_tekstem ─────────────────────────────────────

class _LinkTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: str = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value is not None:
                    self._href = value
                    self._text = ""
                    break

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._href is not None:
            self.links.append((self._href, self._text.strip()))
            self._href = None
            self._text = ""


def wyciagnij_linki_z_tekstem(html: str) -> list[tuple[str, str]]:
    p = _LinkTextExtractor()
    p.feed(html)
    p.close()
    return p.links


# ── filtruj_linki_zewnetrzne ──────────────────────────────────────

def filtruj_linki_zewnetrzne(html: str, base_domain: str) -> list[str]:
    all_links = wyciagnij_linki(html)
    base_lower = base_domain.lower()
    result: list[str] = []
    for href in all_links:
        if href.startswith(("http://", "https://")):
            parsed = urlparse(href)
            if parsed.netloc.lower() != base_lower:
                result.append(href)
    return result


# ── wyciagnij_obrazki ─────────────────────────────────────────────

class _ImageExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            d = dict(attrs)
            src = d.get("src")
            if src is not None:
                self.images.append({
                    "src": src,
                    "alt": d.get("alt") or "",
                })


def wyciagnij_obrazki(html: str) -> list[dict[str, str]]:
    p = _ImageExtractor()
    p.feed(html)
    p.close()
    return p.images

