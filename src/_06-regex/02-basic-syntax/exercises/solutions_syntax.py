"""Przykladowe rozwiazania: podstawowa skladnia wyrazen regularnych."""
import re


def czy_tylko_litery(s: str) -> bool:
    if not s:
        return False
    return bool(re.fullmatch(r'[a-zA-Z]+', s))


def znajdz_liczby_calkowite(s: str) -> list[str]:
    return re.findall(r'\d+', s)


def czy_data_iso(s: str) -> bool:
    return bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', s))


def znajdz_slowa_na_wielka(s: str) -> list[str]:
    return re.findall(r'[A-Z][a-zA-Z]*', s)


def czy_poprawny_identyfikator(s: str) -> bool:
    if not s:
        return False
    return bool(re.fullmatch(r'[a-zA-Z_]\w*', s))

