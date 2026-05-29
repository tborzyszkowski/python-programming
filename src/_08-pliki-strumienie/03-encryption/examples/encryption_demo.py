"""Szyfrowanie plików: XOR, SHA-256, Fernet/AES.

Uruchomienie:
    python src/_08-pliki-strumienie/03-encryption/examples/encryption_demo.py

Wymagania:
    pip install cryptography
"""
from __future__ import annotations

import base64
import hashlib
import os
import shutil
import tempfile
from pathlib import Path

TMP = Path(tempfile.mkdtemp(prefix="py_crypto_"))


def sekcja(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# 1. Szyfr XOR — ilustracja idei
# ---------------------------------------------------------------------------
sekcja("1. Szyfr XOR")


def xor_cipher(dane: bytes, klucz: bytes) -> bytes:
    """Szyfruje/deszyfruje bajty XOR-em z cyklicznym kluczem."""
    n = len(klucz)
    return bytes(b ^ klucz[i % n] for i, b in enumerate(dane))


plaintext  = b"Tajna wiadomosc - Python 3!"
klucz      = b"SECRETKEY"
ciphertext = xor_cipher(plaintext, klucz)
recovered  = xor_cipher(ciphertext, klucz)

print(f"  Plaintext:  {plaintext}")
print(f"  Key:        {klucz}")
print(f"  Ciphertext: {ciphertext.hex()}")
print(f"  Recovered:  {recovered}")
assert recovered == plaintext, "XOR roundtrip failed!"


# ---------------------------------------------------------------------------
# 2. Hashowanie SHA-256
# ---------------------------------------------------------------------------
sekcja("2. Hashowanie SHA-256")

tekst = b"Ala ma kota"
h = hashlib.sha256(tekst).hexdigest()
print(f"  SHA-256('{tekst.decode()}'): {h}")

# Efekt lawinowy — zmiana jednego znaku
tekst2 = b"Ala ma Kota"
h2 = hashlib.sha256(tekst2).hexdigest()
print(f"  SHA-256('{tekst2.decode()}'): {h2}")
print(f"  Różne: {h != h2}")

# Hash pliku blok po bloku
plik = TMP / "dane.txt"
plik.write_bytes(b"Zawartosc pliku\n" * 1000)


def sha256_pliku(sciezka: Path) -> str:
    h = hashlib.sha256()
    with sciezka.open("rb") as f:
        for blok in iter(lambda: f.read(65_536), b""):
            h.update(blok)
    return h.hexdigest()


print(f"  SHA-256 pliku: {sha256_pliku(plik)}")


# ---------------------------------------------------------------------------
# 3. Fernet (AES-128-CBC + HMAC-SHA256)
# ---------------------------------------------------------------------------
sekcja("3. Fernet — szyfrowanie symetryczne")

try:
    from cryptography.fernet import Fernet

    klucz_f = Fernet.generate_key()
    f = Fernet(klucz_f)

    wiadomosc  = b"Dane pacjenta: Jan Kowalski, PESEL 80010112345"
    token      = f.encrypt(wiadomosc)
    odszyfrowane = f.decrypt(token)

    print(f"  Klucz (base64): {klucz_f[:30]}...")
    print(f"  Token (pierwsze 40 B): {token[:40]}...")
    print(f"  Odszyfrowane: {odszyfrowane}")
    assert odszyfrowane == wiadomosc

    # Zły klucz → wyjątek
    zly_klucz = Fernet.generate_key()
    try:
        Fernet(zly_klucz).decrypt(token)
    except Exception as e:
        print(f"  Zły klucz → {type(e).__name__}: {e}")

except ImportError:
    print("  [POMINIĘTO] pip install cryptography")


# ---------------------------------------------------------------------------
# 4. Szyfrowanie pliku Fernetem
# ---------------------------------------------------------------------------
sekcja("4. Szyfrowanie i deszyfrowanie pliku")

try:
    from cryptography.fernet import Fernet  # noqa: F811

    klucz_plik = TMP / "sekret.key"
    klucz_b    = Fernet.generate_key()
    klucz_plik.write_bytes(klucz_b)

    oryginal   = TMP / "tajny_raport.txt"
    zaszyfrowany = TMP / "tajny_raport.enc"
    odtworzony   = TMP / "tajny_raport_dec.txt"

    oryginal.write_text(
        "TAJNE — tylko do użytku wewnętrznego\n"
        "Wyniki egzaminu: wszyscy zdali!\n",
        encoding="utf-8",
    )

    fern = Fernet(klucz_b)
    zaszyfrowany.write_bytes(fern.encrypt(oryginal.read_bytes()))
    odtworzony.write_bytes(fern.decrypt(zaszyfrowany.read_bytes()))

    print(f"  Oryginal:     {oryginal.stat().st_size} B")
    print(f"  Zaszyfrowany: {zaszyfrowany.stat().st_size} B")
    print(f"  Odtworzony:   {odtworzony.read_text(encoding='utf-8')!r}")
    assert odtworzony.read_bytes() == oryginal.read_bytes()
    print("  [OK] Roundtrip pliku poprawny")

except ImportError:
    print("  [POMINIĘTO] pip install cryptography")


# ---------------------------------------------------------------------------
# 5. Klucz z hasła (PBKDF2)
# ---------------------------------------------------------------------------
sekcja("5. Klucz Fernet wyprowadzony z hasła (PBKDF2)")

try:
    from cryptography.fernet import Fernet  # noqa: F811
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    def klucz_z_hasla(haslo: str, sol: bytes | None = None) -> tuple[bytes, bytes]:
        if sol is None:
            sol = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=sol,
            iterations=480_000,
        )
        return base64.urlsafe_b64encode(kdf.derive(haslo.encode("utf-8"))), sol

    haslo = "moje_super_haslo_2024!"
    klucz_p, sol_p = klucz_z_hasla(haslo)
    f2 = Fernet(klucz_p)

    token2 = f2.encrypt(b"Dane chronione haslem")
    # Odszyfrowanie: wyprowadź klucz z tego samego hasła i soli
    klucz_p2, _ = klucz_z_hasla(haslo, sol_p)
    print(f"  Odszyfrowane: {Fernet(klucz_p2).decrypt(token2)}")

except ImportError:
    print("  [POMINIĘTO] pip install cryptography")


# ---------------------------------------------------------------------------
# Porządki
# ---------------------------------------------------------------------------
shutil.rmtree(TMP)
print(f"\n[OK] Katalog tymczasowy usunięty: {TMP}")

