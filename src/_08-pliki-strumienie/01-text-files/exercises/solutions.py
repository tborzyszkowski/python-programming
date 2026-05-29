"""Przykładowe rozwiązania zadań do tematu 01 – pliki tekstowe."""
from __future__ import annotations

from pathlib import Path


def licz_linie(sciezka: Path) -> int:
    """Zwraca liczbę linii w pliku tekstowym.

    Pusta linia '\n' jest liczona jako jedna linia.
    Plik bez znaków nowej linii ma 0 linii.
    """
    with sciezka.open(encoding="utf-8") as f:
        return sum(1 for _ in f)


def filtruj_linie(sciezka: Path, fraza: str) -> list[str]:
    """Zwraca listę linii (bez znaku nowej linii) zawierających frazę."""
    with sciezka.open(encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if fraza in l]


def zamien_slowo(zrodlo: Path, cel: Path, stare: str, nowe: str) -> int:
    """Kopiuje plik zastępując wszystkie wystąpienia 'stare' przez 'nowe'.

    Zwraca łączną liczbę wykonanych zamian.
    """
    licznik = 0
    with zrodlo.open(encoding="utf-8") as src, cel.open("w", encoding="utf-8") as dst:
        for linia in src:
            licznik += linia.count(stare)
            dst.write(linia.replace(stare, nowe))
    return licznik


def statystyki_pliku(sciezka: Path) -> dict:
    """Zwraca słownik ze statystykami pliku tekstowego.

    Klucze: 'znaki', 'slowa', 'linie', 'unikalne_slowa'.
    """
    tekst = sciezka.read_text(encoding="utf-8")
    slowa = tekst.split()
    return {
        "znaki":         len(tekst),
        "slowa":         len(slowa),
        "linie":         tekst.count("\n"),
        "unikalne_slowa": len({w.lower() for w in slowa}),
    }


def znajdz_pliki(katalog: Path, wzorzec: str) -> list[Path]:
    """Zwraca posortowaną listę plików pasujących do wzorca glob (rekurencyjnie)."""
    return sorted(katalog.rglob(wzorzec))


def csv_do_slownikow(sciezka: Path, separator: str = ",") -> list[dict]:
    """Wczytuje prosty plik CSV i zwraca listę słowników.

    Pierwsza linia to nagłówek.
    """
    with sciezka.open(encoding="utf-8") as f:
        naglowek = f.readline().rstrip().split(separator)
        return [
            dict(zip(naglowek, linia.rstrip().split(separator)))
            for linia in f
            if linia.strip()
        ]

