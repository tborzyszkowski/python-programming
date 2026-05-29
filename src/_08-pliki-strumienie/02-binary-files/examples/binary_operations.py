"""Operacje na plikach binarnych: struct, bytes, mmap.

Uruchomienie:
    python src/_08-pliki-strumienie/02-binary-files/examples/binary_operations.py
"""
from __future__ import annotations

import mmap
import shutil
import struct
import tempfile
from dataclasses import dataclass
from pathlib import Path


TMP = Path(tempfile.mkdtemp(prefix="py_binarne_"))


def sekcja(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# 1. bytes i bytearray
# ---------------------------------------------------------------------------
sekcja("1. bytes i bytearray")

b = b"\x89PNG\r\n\x1a\n"
print(f"  Literał bytes: {b}")
print(f"  hex:           {b.hex()}")
print(f"  len:           {len(b)}")
print(f"  b[0]:          {b[0]}  (int, nie char!)")

ba = bytearray(b"hello")
ba[0] = ord("H")
print(f"  bytearray zmieniony: {ba}")
print(f"  bytes(ba):           {bytes(ba)}")


# ---------------------------------------------------------------------------
# 2. struct — pakowanie i rozpakowywanie
# ---------------------------------------------------------------------------
sekcja("2. struct — pakowanie danych")

# Format: uint32 LE + float32 LE = 8 bajtów
fmt = "<If"
spakowane = struct.pack(fmt, 42, 3.14)
print(f"  Spakowane ({struct.calcsize(fmt)} B): {spakowane.hex()}")

liczba, pi = struct.unpack(fmt, spakowane)
print(f"  Rozpakowane: liczba={liczba}, pi={pi:.4f}")

# Format mieszany
fmt2 = "<4sHH"
spak2 = struct.pack(fmt2, b"ABCD", 1920, 1080)
sig, szerokosc, wysokosc = struct.unpack(fmt2, spak2)
print(f"  sig={sig}, {szerokosc}x{wysokosc}")


# ---------------------------------------------------------------------------
# 3. Własny format binarny — pomiary temperatury
# ---------------------------------------------------------------------------
sekcja("3. Własny format binarny")

SYGNATURA = b"TEMP"
FMT_HDR = "<4sI"
FMT_REC = "<If"

@dataclass
class Pomiar:
    timestamp: int
    temperatura: float

pomiary = [
    Pomiar(1700000000, 36.6),
    Pomiar(1700000060, 37.1),
    Pomiar(1700000120, 36.8),
]

plik = TMP / "pomiary.bin"

# Zapis
with plik.open("wb") as f:
    f.write(struct.pack(FMT_HDR, SYGNATURA, len(pomiary)))
    for p in pomiary:
        f.write(struct.pack(FMT_REC, p.timestamp, p.temperatura))

print(f"  Zapisano {plik.stat().st_size} bajtów")

# Odczyt
with plik.open("rb") as f:
    syg, n = struct.unpack(FMT_HDR, f.read(struct.calcsize(FMT_HDR)))
    print(f"  Sygnatura: {syg!r}, rekordów: {n}")
    for _ in range(n):
        ts, temp = struct.unpack(FMT_REC, f.read(struct.calcsize(FMT_REC)))
        print(f"    ts={ts}  temp={temp:.1f}°C")


# ---------------------------------------------------------------------------
# 4. mmap — mapowanie pliku w pamięci
# ---------------------------------------------------------------------------
sekcja("4. mmap — mapowanie pliku w pamięci")

# Tworzymy plik testowy
mmap_plik = TMP / "dane.bin"
mmap_plik.write_bytes(b"Hello, World!\n" * 100)
print(f"  Plik mmap: {mmap_plik.stat().st_size} bajtów")

with mmap_plik.open("r+b") as f:
    with mmap.mmap(f.fileno(), 0) as mm:
        print(f"  Pierwsze 13 B: {mm[0:13]}")

        # Szukanie wzorca
        pos = mm.find(b"World")
        print(f"  'World' na pozycji: {pos}")

        # Modyfikacja in-place
        mm[7:12] = b"Pytho"
        mm.flush()

print(f"  Po modyfikacji: {mmap_plik.read_bytes()[0:13]}")


# ---------------------------------------------------------------------------
# 5. Analiza nagłówka — format WAV (prosty)
# ---------------------------------------------------------------------------
sekcja("5. Tworzenie i analiza prostego pliku WAV")

WAV_HDR = struct.Struct("<4sI4s4sIHHIIHH4sI")
# Pola: RIFF, rozmiar_chunka, WAVE, fmt_, rozmiar_fmt, audio_format,
#       kanaly, sample_rate, byte_rate, block_align, bits_per_sample,
#       data, rozmiar_danych

def stworz_mini_wav(sciezka: Path, dane_pcm: bytes, sample_rate: int = 8000) -> None:
    kanaly       = 1
    bits         = 16
    block_align  = kanaly * bits // 8
    byte_rate    = sample_rate * block_align
    rozmiar_fmt  = 16
    rozmiar_danych = len(dane_pcm)
    rozmiar_riff = 36 + rozmiar_danych

    hdr = WAV_HDR.pack(
        b"RIFF", rozmiar_riff, b"WAVE",
        b"fmt ", rozmiar_fmt, 1,       # PCM=1
        kanaly, sample_rate, byte_rate,
        block_align, bits,
        b"data", rozmiar_danych,
    )
    sciezka.write_bytes(hdr + dane_pcm)

# 100 ms ciszy (8000 próbek/s, 16-bit, 800 próbek)
pcm = bytes(1600)   # 800 próbek × 2 bajty = 1600 bajtów
wav_plik = TMP / "cisza.wav"
stworz_mini_wav(wav_plik, pcm)
print(f"  WAV: {wav_plik.stat().st_size} bajtów")

# Analiza
with wav_plik.open("rb") as f:
    dane = f.read(WAV_HDR.size)
    pola = WAV_HDR.unpack(dane)
    print(f"  RIFF sig: {pola[0]!r}")
    print(f"  Kanały:   {pola[6]}")
    print(f"  Sample rate: {pola[7]} Hz")
    print(f"  Bits/sample: {pola[10]}")


# ---------------------------------------------------------------------------
# Porządki
# ---------------------------------------------------------------------------
shutil.rmtree(TMP)
print(f"\n[OK] Katalog tymczasowy usunięty: {TMP}")

