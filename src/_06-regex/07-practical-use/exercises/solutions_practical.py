"""Przykladowe rozwiazania: praktyczne zastosowania."""
import re

_EMAIL_RE = re.compile(
    r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
)

# Wersja bez kotwic – do wyszukiwania emaili wewnątrz dłuższego tekstu
_EMAIL_INLINE_RE = re.compile(
    r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
)

# Domena: dowolne etykiety (w tym jednoliterowe, np. a.b.c), TLD 1+ liter
_URL_RE = re.compile(
    r'^https?://'
    r'[a-zA-Z0-9][a-zA-Z0-9.\-]*\.[a-zA-Z]+'
    r'(/[^\s]*)?$'
)

_LOG_RE = re.compile(
    r'^(\S+)\s+\S+\s+(\S+)\s+\[([^\]]+)\]\s+"(\S+)\s+(\S+)\s+(\S+)"\s+(\d{3})\s+(\d+|-)$'
)

_TELEFON_RE = re.compile(
    r'\b\d{3}[\s\-]?\d{3}[\s\-]?\d{3}\b'
)

_PESEL_WAGI = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]


def waliduj_email(s: str) -> bool:
    return bool(_EMAIL_RE.fullmatch(s))


def waliduj_pesel(s: str) -> bool:
    if not re.fullmatch(r'\d{11}', s):
        return False
    return sum(int(c) * w for c, w in zip(s, _PESEL_WAGI)) % 10 == 0


def waliduj_url(s: str) -> bool:
    return bool(_URL_RE.fullmatch(s))


def parsuj_linie_logu(linia: str) -> dict | None:
    m = _LOG_RE.match(linia.strip())
    if not m:
        return None
    return {
        'ip':         m.group(1),
        'uzytkownik': m.group(2),
        'czas':       m.group(3),
        'metoda':     m.group(4),
        'sciezka':    m.group(5),
        'protokol':   m.group(6),
        'status':     int(m.group(7)),
        'rozmiar':    int(m.group(8)) if m.group(8) != '-' else 0,
    }


def maskuj_dane_osobowe(tekst: str) -> str:
    tekst = _EMAIL_INLINE_RE.sub('[REDACTED_EMAIL]', tekst)
    tekst = _TELEFON_RE.sub('[REDACTED_PHONE]', tekst)
    return tekst



