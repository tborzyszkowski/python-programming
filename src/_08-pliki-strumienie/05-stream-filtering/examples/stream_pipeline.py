"""Potoki generatorów i przetwarzanie strumieniowe plików.

Uruchomienie:
    python src/_08-pliki-strumienie/05-stream-filtering/examples/stream_pipeline.py
"""
from __future__ import annotations

import gzip
import itertools
import random
import shutil
import tempfile
from collections import Counter
from pathlib import Path


TMP = Path(tempfile.mkdtemp(prefix="py_pipeline_"))


def sekcja(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# Pomocnicze filtry generatorowe
# ---------------------------------------------------------------------------

def czytaj_linie(sciezka: Path):
    """Źródło: generator linii pliku tekstowego."""
    with sciezka.open(encoding="utf-8") as f:
        yield from f


def odfiltruj(linie, fraza: str):
    """Filtr: przepuszcza tylko linie zawierające frazę."""
    return (l for l in linie if fraza in l)


def usun_biale(linie):
    """Transformacja: usuwa białe znaki z końca każdej linii."""
    return (l.rstrip() for l in linie)


def dodaj_numer(linie, start: int = 1):
    """Transformacja: dodaje numer linii."""
    return ((i, l) for i, l in enumerate(linie, start))


def porcjuj(iterable, n: int):
    """Filtr: grupuje elementy w porcje po n."""
    it = iter(iterable)
    while True:
        porcja = list(itertools.islice(it, n))
        if not porcja:
            return
        yield porcja


# ---------------------------------------------------------------------------
# 1. Prosty potok filtrowania logów
# ---------------------------------------------------------------------------
sekcja("1. Potok filtrowania logów")

# Generowanie pliku logów
log = TMP / "app.log"
poziomy = ["INFO", "WARNING", "ERROR", "DEBUG"]
wagi    = [0.7, 0.15, 0.1, 0.05]

with log.open("w", encoding="utf-8") as f:
    random.seed(42)
    for i in range(10_000):
        poz = random.choices(poziomy, wagi)[0]
        f.write(f"2024-01-{i%28+1:02d} {poz} Zdarzenie nr {i}\n")

print(f"  Wygenerowano log: {log.stat().st_size // 1024} KB, 10 000 linii")

# Potok: plik → filtry ERROR → usuń białe → pierwsze 5
# Uwaga: otwieramy plik bezpośrednio w bloku with, żeby plik zamknął się
# po wyjściu z bloku (nawet przy niepełnym przetworzeniu przez islice).
with log.open(encoding="utf-8") as f:
    potok = usun_biale(odfiltruj(f, "ERROR"))
    print("  Pierwsze 5 błędów:")
    for linia in itertools.islice(potok, 5):
        print(f"    {linia}")


# ---------------------------------------------------------------------------
# 2. Statystyki strumieniowo (Counter)
# ---------------------------------------------------------------------------
sekcja("2. Statystyki logów — strumieniowo")

def statystyki_logów(sciezka: Path) -> Counter:
    with sciezka.open(encoding="utf-8") as f:
        return Counter(
            linia.split()[1]
            for linia in f
            if linia.strip()
        )

stats = statystyki_logów(log)
print(f"  Łącznie linii: {sum(stats.values())}")
for poz, n in sorted(stats.items()):
    print(f"    {poz:8s}: {n:5d}")


# ---------------------------------------------------------------------------
# 3. Przetwarzanie porcjami (batch processing)
# ---------------------------------------------------------------------------
sekcja("3. Przetwarzanie porcjami (batch)")

with log.open(encoding="utf-8") as f:
    bledy = odfiltruj(f, "ERROR")
    porcje = list(porcjuj(bledy, 10))

print(f"  Porcji po 10 linii: {len(porcje)}")
print(f"  Pierwsza porcja (3 pierwsze linie):")
for linia in porcje[0][:3]:
    print(f"    {linia.rstrip()}")


# ---------------------------------------------------------------------------
# 4. Kompozycja funkcyjna potoku
# ---------------------------------------------------------------------------
sekcja("4. Kompozycja potoku — wyodrębnij i ponumeruj błędy")

# Używamy bezpośrednio pliku w bloku with, nie generatora otwierającego plik
with log.open(encoding="utf-8") as f:
    numerowane = list(
        itertools.islice(
            dodaj_numer(usun_biale(odfiltruj(f, "ERROR"))),
            5,
        )
    )
for nr, linia in numerowane:
    print(f"  #{nr:3d}  {linia}")


# ---------------------------------------------------------------------------
# 5. Kompresja strumieniowa gzip
# ---------------------------------------------------------------------------
sekcja("5. Kompresja strumieniowa (gzip)")

gz_plik = TMP / "app.log.gz"

with log.open("rb") as src, gzip.open(gz_plik, "wb") as dst:
    for blok in iter(lambda: src.read(65_536), b""):
        dst.write(blok)
    # dst jest zamknięty po wyjściu z bloku with — niezbędne na Windows

przed = log.stat().st_size
po    = gz_plik.stat().st_size
print(f"  Oryginal:    {przed:>8d} B")
print(f"  Skompresowany: {po:>6d} B")
print(f"  Kompresja:   {100 * (1 - po / przed):.1f}%")

# Odczyt z gzip strumieniowo
print("  Pierwsze 2 linie z gz:")
with gzip.open(gz_plik, "rt", encoding="utf-8") as f:
    for linia in itertools.islice(f, 2):
        print(f"    {linia.rstrip()}")


# ---------------------------------------------------------------------------
# 6. Wyszukiwanie wzorca binarnego na granicy buforów
# ---------------------------------------------------------------------------
sekcja("6. Wyszukiwanie binarne w strumieniu")

bin_plik = TMP / "dane.bin"
# Plik z kilkoma wystąpieniami wzorca przy granicach buforów
wzorzec = b"MARKER"
dane = b"A" * 60 + wzorzec + b"B" * 60 + wzorzec + b"C" * 10
bin_plik.write_bytes(dane)

def szukaj_binarnie(sciezka: Path, wzorzec: bytes, buf: int = 64) -> list[int]:
    overlap = len(wzorzec) - 1
    pozycje = []
    offset  = 0
    poprzedni = b""
    with sciezka.open("rb") as f:
        while True:
            blok = f.read(buf)
            if not blok:
                break
            okno = poprzedni + blok
            pos = 0
            while True:
                idx = okno.find(wzorzec, pos)
                if idx == -1:
                    break
                pozycje.append(offset - len(poprzedni) + idx)
                pos = idx + 1
            poprzedni = okno[-overlap:] if overlap else b""
            offset += len(blok)
    return pozycje

znalezione = szukaj_binarnie(bin_plik, wzorzec)
print(f"  Wzorzec {wzorzec!r} znaleziony na pozycjach: {znalezione}")
assert znalezione == [60, 126]


# ---------------------------------------------------------------------------
# Porządki
# ---------------------------------------------------------------------------
import gc
gc.collect()   # Wymuś zamknięcie generatorów trzymających uchwyty plików
shutil.rmtree(TMP)
print(f"\n[OK] Katalog tymczasowy usunięty: {TMP}")

