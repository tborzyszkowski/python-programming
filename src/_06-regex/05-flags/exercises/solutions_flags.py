"""Przykladowe rozwiazania: flagi i tryby modulu re."""
import re

_TELEFON_RE = re.compile(r"""
    ^                   # poczatek napisu
    (?:\+48)?           # opcjonalny prefix +48
    \s?                 # opcjonalna spacja po prefixie
    \d{3}               # pierwsze 3 cyfry
    [\s\-]?             # opcjonalny separator
    \d{3}               # srodkowe 3 cyfry
    [\s\-]?             # opcjonalny separator
    \d{3}               # ostatnie 3 cyfry
    $                   # koniec napisu
""", re.VERBOSE)


def szukaj_bez_wielkosci(tekst: str, wzorzec: str) -> list[str]:
    return re.findall(wzorzec, tekst, re.IGNORECASE)


def znajdz_naglowki_markdown(tekst: str) -> list[str]:
    return re.findall(r'^#+\s+(.+)', tekst, re.MULTILINE)


def wyciagnij_bloki_html(tekst: str, tag: str) -> list[str]:
    pattern = rf'<{re.escape(tag)}>(.*?)</{re.escape(tag)}>'
    return re.findall(pattern, tekst, re.DOTALL)


def waliduj_numer_verbose(s: str) -> bool:
    return bool(_TELEFON_RE.match(s))

