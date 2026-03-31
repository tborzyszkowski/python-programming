"""Przykladowe rozwiazania: zaawansowane wzorce."""
import re

_HASLO_RE = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}')


def znajdz_tagi_html(s: str) -> list[str]:
    return re.findall(r'<.*?>', s)


def liczby_przed_jednostka(s: str, jednostka: str) -> list[str]:
    pattern = r'\d+(?=\s?' + re.escape(jednostka) + r'\b)'
    return re.findall(pattern, s)


def waliduj_haslo(s: str) -> bool:
    return bool(_HASLO_RE.fullmatch(s))


def slowa_nie_poprzedzone_liczba(s: str) -> list[str]:
    return re.findall(r'(?<!\d)\b[a-z]+\b', s)


def bezpieczne_wyszukaj(wzorzec_uzytkownika: str, tekst: str) -> list[str]:
    return re.findall(re.escape(wzorzec_uzytkownika), tekst)

