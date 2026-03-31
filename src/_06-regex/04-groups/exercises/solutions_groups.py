"""Przykladowe rozwiazania: grupy i przechwytywanie."""
import re

_DATA_RE = re.compile(r'(?P<rok>\d{4})-(?P<miesiac>\d{2})-(?P<dzien>\d{2})')
_WERSJA_RE = re.compile(r'(\d+)\.(\d+)\.(\d+)')
_KV_RE = re.compile(r'(\w+)=(\w+)')


def wyciagnij_date(s: str) -> dict | None:
    m = _DATA_RE.search(s)
    if not m:
        return None
    return {'rok': m.group('rok'), 'miesiac': m.group('miesiac'), 'dzien': m.group('dzien')}


def zamien_format_daty(s: str) -> str:
    return _DATA_RE.sub(r'\g<dzien>.\g<miesiac>.\g<rok>', s)


def znajdz_powtorzenia(s: str) -> list[str]:
    return re.findall(r'\b(\w+)\s+\1\b', s, re.IGNORECASE)


def parsuj_wersje(s: str) -> tuple[int, int, int] | None:
    m = _WERSJA_RE.search(s)
    if not m:
        return None
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))


def wyciagnij_pary_klucz_wartosc(s: str) -> dict[str, str]:
    return dict(_KV_RE.findall(s))

