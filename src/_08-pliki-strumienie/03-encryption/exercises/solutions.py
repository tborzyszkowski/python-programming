"""Przykładowe rozwiązania zadań do tematu 03 – szyfrowanie."""
from __future__ import annotations

import hashlib
from pathlib import Path


def xor_encrypt(dane: bytes, klucz: bytes) -> bytes:
    """Szyfruje bajty operacją XOR z cyklicznym kluczem."""
    if not klucz:
        raise ValueError("Klucz nie może być pusty")
    n = len(klucz)
    return bytes(b ^ klucz[i % n] for i, b in enumerate(dane))


def xor_decrypt(dane: bytes, klucz: bytes) -> bytes:
    """Deszyfruje bajty operacją XOR (identyczna jak szyfrowanie)."""
    return xor_encrypt(dane, klucz)


def sha256_bytes(dane: bytes) -> str:
    """Zwraca SHA-256 danych jako hex string (64 znaki)."""
    return hashlib.sha256(dane).hexdigest()


def sha256_plik(sciezka: Path, chunk: int = 65_536) -> str:
    """Oblicza SHA-256 pliku blok po bloku (działa dla dużych plików)."""
    h = hashlib.sha256()
    with sciezka.open("rb") as f:
        for blok in iter(lambda: f.read(chunk), b""):
            h.update(blok)
    return h.hexdigest()


def weryfikuj_plik(sciezka: Path, oczekiwany_hash: str) -> bool:
    """Porównuje SHA-256 pliku z oczekiwanym hashem.

    Zwraca True jeśli plik jest nienaruszony, False w przeciwnym razie.
    Porównanie jest odporne na timing attack (hmac.compare_digest).
    """
    import hmac
    aktualny = sha256_plik(sciezka)
    return hmac.compare_digest(aktualny, oczekiwany_hash)


def rot13(tekst: str) -> str:
    """Implementuje szyfr ROT-13 (obrót o 13 liter w alfabecie łacińskim).

    Znaki niebędące literami ASCII pozostają bez zmian.
    """
    wynik = []
    for znak in tekst:
        if "a" <= znak <= "z":
            wynik.append(chr((ord(znak) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= znak <= "Z":
            wynik.append(chr((ord(znak) - ord("A") + 13) % 26 + ord("A")))
        else:
            wynik.append(znak)
    return "".join(wynik)

