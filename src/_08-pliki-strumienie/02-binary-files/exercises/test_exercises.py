"""Zadania do tematu 02 – pliki binarne."""
from __future__ import annotations

import struct
from pathlib import Path

import pytest

from solutions import (
    zapisz_macierz,
    czytaj_macierz,
    znajdz_wzorzec_binarny,
    xor_bytes,
    hex_dump,
)


@pytest.fixture()
def tmp_dir(tmp_path: Path) -> Path:
    return tmp_path


# ---------------------------------------------------------------------------
def test_macierz_roundtrip(tmp_dir: Path) -> None:
    """Zapis i odczyt macierzy int powinny dać ten sam wynik."""
    macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    p = tmp_dir / "macierz.bin"
    zapisz_macierz(p, macierz)
    wynik = czytaj_macierz(p)
    assert wynik == macierz


def test_macierz_pusta(tmp_dir: Path) -> None:
    p = tmp_dir / "pusta.bin"
    zapisz_macierz(p, [])
    assert czytaj_macierz(p) == []


def test_macierz_jeden_element(tmp_dir: Path) -> None:
    p = tmp_dir / "jeden.bin"
    zapisz_macierz(p, [[42]])
    assert czytaj_macierz(p) == [[42]]


# ---------------------------------------------------------------------------
def test_znajdz_wzorzec_binarny(tmp_dir: Path) -> None:
    p = tmp_dir / "dane.bin"
    p.write_bytes(b"ABCDEABCFGABC")
    pozycje = znajdz_wzorzec_binarny(p, b"ABC")
    assert pozycje == [0, 5, 10]


def test_znajdz_wzorzec_binarny_brak(tmp_dir: Path) -> None:
    p = tmp_dir / "brak.bin"
    p.write_bytes(b"XYZXYZ")
    assert znajdz_wzorzec_binarny(p, b"ABC") == []


# ---------------------------------------------------------------------------
def test_xor_bytes() -> None:
    dane = b"\x00\xFF\xAA"
    klucz = 0x55
    zaszyfrowane = xor_bytes(dane, klucz)
    assert zaszyfrowane == bytes(b ^ klucz for b in dane)
    # Symetryczność: dwa razy XOR daje oryginał
    assert xor_bytes(zaszyfrowane, klucz) == dane


def test_xor_bytes_pusty() -> None:
    assert xor_bytes(b"", 0x42) == b""


# ---------------------------------------------------------------------------
def test_hex_dump() -> None:
    wynik = hex_dump(b"\x00\x01\x02\x03", width=4)
    linie = wynik.strip().splitlines()
    assert len(linie) == 1
    assert "00 01 02 03" in linie[0]


def test_hex_dump_wieloliniowy() -> None:
    dane = bytes(range(16))
    wynik = hex_dump(dane, width=8)
    linie = wynik.strip().splitlines()
    assert len(linie) == 2

