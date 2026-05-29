"""Zadania do tematu 03 – szyfrowanie plików."""
from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from solutions import (
    xor_encrypt,
    xor_decrypt,
    sha256_bytes,
    sha256_plik,
    weryfikuj_plik,
    rot13,
)


# ---------------------------------------------------------------------------
# XOR
# ---------------------------------------------------------------------------
def test_xor_roundtrip() -> None:
    dane  = b"Hello, World!"
    klucz = b"KEY"
    assert xor_decrypt(xor_encrypt(dane, klucz), klucz) == dane


def test_xor_pusty() -> None:
    assert xor_encrypt(b"", b"k") == b""


def test_xor_symetria() -> None:
    """Szyfrowanie i deszyfrowanie to ta sama operacja."""
    d, k = b"Python 3", b"XYZ"
    enc = xor_encrypt(d, k)
    assert xor_encrypt(enc, k) == d


def test_xor_klucz_jednobajtowy() -> None:
    dane  = bytes(range(10))
    klucz = b"\xFF"
    zaszyfrowane = xor_encrypt(dane, klucz)
    assert all(b == (i ^ 0xFF) for i, b in zip(range(10), zaszyfrowane))


# ---------------------------------------------------------------------------
# SHA-256
# ---------------------------------------------------------------------------
def test_sha256_bytes_znany() -> None:
    # echo -n "" | sha256sum
    pusty_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert sha256_bytes(b"") == pusty_hash


def test_sha256_bytes_hello() -> None:
    h = sha256_bytes(b"hello")
    assert len(h) == 64
    assert h == hashlib.sha256(b"hello").hexdigest()


def test_sha256_plik(tmp_path: Path) -> None:
    p = tmp_path / "test.bin"
    dane = b"dane testowe 12345"
    p.write_bytes(dane)
    oczekiwany = hashlib.sha256(dane).hexdigest()
    assert sha256_plik(p) == oczekiwany


def test_weryfikuj_plik_ok(tmp_path: Path) -> None:
    p = tmp_path / "ok.txt"
    dane = b"prawidlowe dane"
    p.write_bytes(dane)
    poprawny_hash = hashlib.sha256(dane).hexdigest()
    assert weryfikuj_plik(p, poprawny_hash) is True


def test_weryfikuj_plik_uszkodzony(tmp_path: Path) -> None:
    p = tmp_path / "uszkodzony.txt"
    p.write_bytes(b"zmienione dane")
    zly_hash = hashlib.sha256(b"oryginalne dane").hexdigest()
    assert weryfikuj_plik(p, zly_hash) is False


# ---------------------------------------------------------------------------
# ROT-13 (odmiana szyfru Cezara)
# ---------------------------------------------------------------------------
def test_rot13_roundtrip() -> None:
    tekst = "Ala ma kota"
    assert rot13(rot13(tekst)) == tekst


def test_rot13_tylko_litery() -> None:
    assert rot13("abc") == "nop"
    assert rot13("xyz") == "klm"
    assert rot13("ABC") == "NOP"


def test_rot13_niezmienne_cyfry() -> None:
    assert rot13("abc123") == "nop123"

