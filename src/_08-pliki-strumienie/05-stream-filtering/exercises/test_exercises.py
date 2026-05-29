"""Zadania do tematu 05 – filtrowanie strumieni i generatory."""
from __future__ import annotations

import gzip
import itertools
from io import StringIO
from pathlib import Path

import pytest

from solutions import (
    filtruj_linie_gen,
    porcjuj,
    policz_wystapienia,
    transformuj_linie,
    scalaj_posortowane,
    kompresuj_do_bytes,
)


# ---------------------------------------------------------------------------
# filtruj_linie_gen
# ---------------------------------------------------------------------------
def test_filtruj_linie_gen_podstawowy() -> None:
    linie = ["INFO ok", "ERROR crash", "INFO end", "ERROR timeout"]
    wynik = list(filtruj_linie_gen(iter(linie), "ERROR"))
    assert wynik == ["ERROR crash", "ERROR timeout"]


def test_filtruj_linie_gen_brak_dopasowania() -> None:
    linie = ["INFO a", "DEBUG b"]
    assert list(filtruj_linie_gen(iter(linie), "ERROR")) == []


def test_filtruj_linie_gen_pusty() -> None:
    assert list(filtruj_linie_gen(iter([]), "x")) == []


# ---------------------------------------------------------------------------
# porcjuj
# ---------------------------------------------------------------------------
def test_porcjuj_podstawowy() -> None:
    wynik = list(porcjuj(range(7), 3))
    assert wynik == [[0, 1, 2], [3, 4, 5], [6]]


def test_porcjuj_rowny_podzial() -> None:
    wynik = list(porcjuj(range(6), 2))
    assert wynik == [[0, 1], [2, 3], [4, 5]]


def test_porcjuj_pusty() -> None:
    assert list(porcjuj([], 5)) == []


def test_porcjuj_wiekszy_niz_strumien() -> None:
    wynik = list(porcjuj(range(3), 10))
    assert wynik == [[0, 1, 2]]


# ---------------------------------------------------------------------------
# policz_wystapienia
# ---------------------------------------------------------------------------
def test_policz_wystapienia() -> None:
    linie = ["INFO a", "ERROR b", "INFO c", "ERROR d", "WARNING e"]
    wynik = policz_wystapienia(iter(linie), klucz=lambda l: l.split()[0])
    assert wynik["INFO"] == 2
    assert wynik["ERROR"] == 2
    assert wynik["WARNING"] == 1


def test_policz_wystapienia_pusty() -> None:
    wynik = policz_wystapienia(iter([]), klucz=lambda x: x)
    assert len(wynik) == 0


# ---------------------------------------------------------------------------
# transformuj_linie
# ---------------------------------------------------------------------------
def test_transformuj_linie() -> None:
    linie = [" abc ", "  def  ", "ghi"]
    wynik = list(transformuj_linie(iter(linie), str.strip))
    assert wynik == ["abc", "def", "ghi"]


def test_transformuj_linie_upper() -> None:
    linie = ["hello", "world"]
    wynik = list(transformuj_linie(iter(linie), str.upper))
    assert wynik == ["HELLO", "WORLD"]


# ---------------------------------------------------------------------------
# scalaj_posortowane
# ---------------------------------------------------------------------------
def test_scalaj_posortowane() -> None:
    s1 = iter([1, 3, 5])
    s2 = iter([2, 4, 6])
    wynik = list(scalaj_posortowane([s1, s2]))
    assert wynik == [1, 2, 3, 4, 5, 6]


def test_scalaj_posortowane_jeden() -> None:
    wynik = list(scalaj_posortowane([iter([1, 2, 3])]))
    assert wynik == [1, 2, 3]


def test_scalaj_posortowane_pusty() -> None:
    assert list(scalaj_posortowane([])) == []


# ---------------------------------------------------------------------------
# kompresuj_do_bytes
# ---------------------------------------------------------------------------
def test_kompresuj_do_bytes_roundtrip() -> None:
    dane = b"Hello, World!\n" * 100
    skompresowane = kompresuj_do_bytes(dane)
    assert len(skompresowane) < len(dane)
    # Weryfikacja przez dekompresję
    import gzip
    assert gzip.decompress(skompresowane) == dane


def test_kompresuj_do_bytes_pusty() -> None:
    skompresowane = kompresuj_do_bytes(b"")
    assert gzip.decompress(skompresowane) == b""

