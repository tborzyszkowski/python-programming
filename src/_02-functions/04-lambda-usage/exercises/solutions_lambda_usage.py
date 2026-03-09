"""Przykładowe rozwiązania: lambda usage."""

from functools import reduce


def sortuj_produkty(produkty: list[dict], klucz: str) -> list[dict]:
    return sorted(produkty, key=lambda p: p[klucz])


def filtruj_transakcje(transakcje: list[dict], prog: float) -> list[dict]:
    return list(filter(lambda t: t["kwota"] >= prog, transakcje))


def mapuj_kwoty_brutto(transakcje: list[dict], vat: float = 0.23) -> list[float]:
    return list(map(lambda t: round(t["kwota"] * (1 + vat), 2), transakcje))


def agreguj_kwoty(transakcje: list[dict]) -> float:
    return reduce(lambda acc, t: acc + t["kwota"], transakcje, 0.0)


def ranking_studentow(studenci: list[dict]) -> list[str]:
    posortowani = sorted(studenci, key=lambda s: s["srednia"], reverse=True)
    return [s["imie"] for s in posortowani]

