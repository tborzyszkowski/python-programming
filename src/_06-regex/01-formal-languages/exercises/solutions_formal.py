"""Przykladowe rozwiazania: jezyki formalne i automaty skonczone."""
import re


def czy_zawiera_cyfre(s: str) -> bool:
    return bool(re.search(r'\d', s))


def czy_ciag_binarny(s: str) -> bool:
    if not s:
        return False
    return bool(re.fullmatch(r'[01]+', s))


def symuluj_dfa(przejscia: dict, start: str, akceptujace: set, slowo: str) -> bool:
    stan = start
    for symbol in slowo:
        klucz = (stan, symbol)
        if klucz not in przejscia:
            return False
        stan = przejscia[klucz]
    return stan in akceptujace


def licz_dopasowania(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text))

