"""Przykladowe rozwiazania: modul re."""
import re

_EMAIL_RE = re.compile(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}')


def pierwsza_liczba(s: str) -> int | None:
    m = re.search(r'\d+', s)
    return int(m.group()) if m else None


def wszystkie_emaile(s: str) -> list[str]:
    return _EMAIL_RE.findall(s)


def normalizuj_spacje(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip()


def podziel_na_tokeny(s: str) -> list[str]:
    return [t for t in re.split(r'[;,\s]+', s) if t]


def pozycje_slowa(s: str, slowo: str) -> list[tuple[int, int]]:
    pattern = r'\b' + re.escape(slowo) + r'\b'
    return [m.span() for m in re.finditer(pattern, s)]

