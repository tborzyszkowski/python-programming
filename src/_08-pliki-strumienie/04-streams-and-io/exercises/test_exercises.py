"""Zadania do tematu 04 – strumienie io."""
from __future__ import annotations

import csv
import io
import zipfile

import pytest

from solutions import (
    csv_do_stringa,
    string_do_csv,
    dlugosc_strumienia,
    sklej_strumienie,
    stworz_zip_w_pamieci,
    wypakuj_zip_z_pamieci,
    CountingStream,
)


# ---------------------------------------------------------------------------
# csv_do_stringa / string_do_csv
# ---------------------------------------------------------------------------
def test_csv_do_stringa_naglowek() -> None:
    wiersze = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    wynik = csv_do_stringa(wiersze, ["a", "b"])
    linie = wynik.splitlines()
    assert linie[0] == "a,b"
    assert linie[1] == "1,2"
    assert linie[2] == "3,4"


def test_csv_do_stringa_pusty() -> None:
    assert csv_do_stringa([], ["x"]) == "x\r\n"


def test_string_do_csv() -> None:
    tekst = "imie,wiek\nAnna,20\nPiotr,21\n"
    wiersze = string_do_csv(tekst)
    assert len(wiersze) == 2
    assert wiersze[0]["imie"] == "Anna"
    assert wiersze[1]["wiek"] == "21"


# ---------------------------------------------------------------------------
# dlugosc_strumienia
# ---------------------------------------------------------------------------
def test_dlugosc_strumienia_bytes() -> None:
    buf = io.BytesIO(b"\x00" * 100)
    assert dlugosc_strumienia(buf) == 100


def test_dlugosc_strumienia_pusty() -> None:
    assert dlugosc_strumienia(io.BytesIO(b"")) == 0


def test_dlugosc_strumienia_nie_przesuwa_pozycji() -> None:
    """Po wywołaniu strumień powinien być z powrotem na pozycji 0."""
    buf = io.BytesIO(b"abcde")
    _ = dlugosc_strumienia(buf)
    assert buf.tell() == 0


# ---------------------------------------------------------------------------
# sklej_strumienie
# ---------------------------------------------------------------------------
def test_sklej_strumienie() -> None:
    s1 = io.BytesIO(b"aaa")
    s2 = io.BytesIO(b"bbb")
    s3 = io.BytesIO(b"ccc")
    wynik = sklej_strumienie([s1, s2, s3])
    assert wynik == b"aaabbbccc"


def test_sklej_strumienie_pusty() -> None:
    assert sklej_strumienie([]) == b""


# ---------------------------------------------------------------------------
# ZIP in-memory
# ---------------------------------------------------------------------------
def test_stworz_zip_w_pamieci() -> None:
    pliki = {"a.txt": b"hello", "b.bin": b"\x00\x01\x02"}
    dane = stworz_zip_w_pamieci(pliki)
    with zipfile.ZipFile(io.BytesIO(dane)) as zf:
        assert set(zf.namelist()) == {"a.txt", "b.bin"}
        assert zf.read("a.txt") == b"hello"


def test_wypakuj_zip_z_pamieci() -> None:
    pliki = {"x.txt": b"test", "y.txt": b"data"}
    dane = stworz_zip_w_pamieci(pliki)
    wypakowne = wypakuj_zip_z_pamieci(dane)
    assert wypakowne == pliki


# ---------------------------------------------------------------------------
# CountingStream
# ---------------------------------------------------------------------------
def test_counting_stream_write() -> None:
    cs = CountingStream(io.BytesIO())
    cs.write(b"hello")
    cs.write(b"world")
    assert cs.bytes_written == 10


def test_counting_stream_read() -> None:
    cs = CountingStream(io.BytesIO(b"abcde"))
    cs.read(3)
    assert cs.bytes_read == 3
    cs.read()
    assert cs.bytes_read == 5

