"""Demonstracja StringIO, BytesIO i wrapperów strumieni.

Uruchomienie:
    python src/_08-pliki-strumienie/04-streams-and-io/examples/streams_demo.py
"""
from __future__ import annotations

import csv
import io
import sys
import zipfile


def sekcja(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# 1. StringIO — bufor tekstowy in-memory
# ---------------------------------------------------------------------------
sekcja("1. StringIO — bufor tekstowy")

buf = io.StringIO()
buf.write("Pierwsza linia\n")
buf.write("Druga linia\n")
buf.write("Trzecia linia\n")

print(f"  Pozycja po write: {buf.tell()}")
print(f"  getvalue(): {buf.getvalue()!r}")

buf.seek(0)
print("  readline() x2:")
print(f"    {buf.readline()!r}")
print(f"    {buf.readline()!r}")

# Inicjalizacja z gotowym tekstem
src = io.StringIO("abc\ndef\nghi\n")
linie = list(src)
print(f"  Linie z inicjalizacji: {linie}")


# ---------------------------------------------------------------------------
# 2. StringIO jako plik — CSV
# ---------------------------------------------------------------------------
sekcja("2. StringIO + csv.DictReader")

csv_data = "imie,ocena,miasto\nAnna,5,Kraków\nPiotr,4,Warszawa\nMaria,5,Gdańsk\n"
reader = csv.DictReader(io.StringIO(csv_data))
for row in reader:
    print(f"  {row['imie']:8s} ocena={row['ocena']} {row['miasto']}")

# Zapis CSV do bufora
out = io.StringIO()
writer = csv.writer(out)
writer.writerows([["x", "y", "z"], [1, 2, 3], [4, 5, 6]])
csv_wynik = out.getvalue()
print(f"  CSV string:\n{csv_wynik}")


# ---------------------------------------------------------------------------
# 3. BytesIO — bufor binarny in-memory
# ---------------------------------------------------------------------------
sekcja("3. BytesIO — bufor binarny")

import struct  # noqa: E402

bbuf = io.BytesIO()
bbuf.write(b"MAGIC")
bbuf.write(struct.pack("<I", 42))
bbuf.write(b"\xDE\xAD\xBE\xEF")

print(f"  Rozmiar bufora: {bbuf.tell()} bajtów")
print(f"  getvalue() hex: {bbuf.getvalue().hex()}")

bbuf.seek(0)
print(f"  magic: {bbuf.read(5)}")
(n,) = struct.unpack("<I", bbuf.read(4))
print(f"  liczba: {n}")
print(f"  reszta: {bbuf.read().hex()}")


# ---------------------------------------------------------------------------
# 4. TextIOWrapper — opakowanie strumienia binarnego
# ---------------------------------------------------------------------------
sekcja("4. TextIOWrapper — kodowanie UTF-8 nad BytesIO")

raw = io.BytesIO()
txt = io.TextIOWrapper(raw, encoding="utf-8", newline="\n")

txt.write("Zażółć gęślą jaźń\n")
txt.write("Hello, World!\n")
txt.flush()   # ważne: opróżnij bufor TextIOWrapper

raw.seek(0)
bajty = raw.read()
print(f"  Bajty UTF-8 ({len(bajty)} B): {bajty[:30].hex()}...")

# Odczyt przez TextIOWrapper
raw.seek(0)
txt2 = io.TextIOWrapper(raw, encoding="utf-8")
for linia in txt2:
    print(f"  > {linia.rstrip()}")


# ---------------------------------------------------------------------------
# 5. Przechwytywanie stdout
# ---------------------------------------------------------------------------
sekcja("5. Przechwytywanie stdout")

def przechwyc(func, *args, **kwargs) -> str:
    """Uruchamia funkcję i zwraca jej stdout jako str."""
    stary_stdout = sys.stdout
    sys.stdout = bufor = io.StringIO()
    try:
        func(*args, **kwargs)
        return bufor.getvalue()
    finally:
        sys.stdout = stary_stdout

wydruk = przechwyc(print, "Witaj, Świecie!", "–", 42)
print(f"  Przechwycono: {wydruk!r}")


# ---------------------------------------------------------------------------
# 6. ZIP w pamięci
# ---------------------------------------------------------------------------
sekcja("6. ZIP w pamięci z BytesIO")

def stworz_zip(pliki: dict[str, bytes]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for nazwa, dane in pliki.items():
            zf.writestr(nazwa, dane)
    return buf.getvalue()

archiwum = stworz_zip({
    "README.txt":  b"Dokumentacja projektu\n",
    "data.csv":    b"x,y\n1,2\n3,4\n",
    "config.json": b'{"debug": false, "version": "1.0"}\n',
})
print(f"  Rozmiar ZIP: {len(archiwum)} bajtów")

with zipfile.ZipFile(io.BytesIO(archiwum)) as zf:
    print(f"  Zawartość: {zf.namelist()}")
    print(f"  README: {zf.read('README.txt')!r}")


# ---------------------------------------------------------------------------
# 7. Własny strumień (duck typing)
# ---------------------------------------------------------------------------
sekcja("7. Własny strumień (protokół duck typing)")

class CountingWriter:
    """Strumień zliczający zapisane bajty/znaki."""

    def __init__(self, underlying: io.IOBase) -> None:
        self._stream    = underlying
        self.bytes_written = 0

    def write(self, dane) -> int:
        n = self._stream.write(dane)
        self.bytes_written += n
        return n

    def getvalue(self):
        return self._stream.getvalue()

    def flush(self) -> None:
        self._stream.flush()

cw = CountingWriter(io.StringIO())
cw.write("Hello ")
cw.write("World")
print(f"  Zapisano: {cw.bytes_written} znaków")
print(f"  Zawartość: {cw.getvalue()!r}")

