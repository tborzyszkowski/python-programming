"""Demonstracja biblioteki pathlib.

Uruchomienie:
    python src/_08-pliki-strumienie/01-text-files/examples/pathlib_demo.py
"""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path


TMP = Path(tempfile.mkdtemp(prefix="py_pathlib_"))


def sekcja(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# 1. Tworzenie ścieżek
# ---------------------------------------------------------------------------
sekcja("1. Tworzenie ścieżek")

p = Path("dane") / "rok2024" / "wyniki.csv"
print(f"  Ścieżka:  {p}")
print(f"  parent:   {p.parent}")
print(f"  name:     {p.name}")
print(f"  stem:     {p.stem}")
print(f"  suffix:   {p.suffix}")
print(f"  suffixes: {p.suffixes}")
print(f"  parts:    {p.parts}")
print(f"  absolutna: {p.is_absolute()}")

abs_p = Path.cwd() / p
print(f"  CWD/... : {abs_p}")


# ---------------------------------------------------------------------------
# 2. Operacje na plikach przez Path
# ---------------------------------------------------------------------------
sekcja("2. Operacje na plikach")

katalog = TMP / "projekt" / "dane"
katalog.mkdir(parents=True, exist_ok=True)
print(f"  Utworzono: {katalog}")

plik = katalog / "dane.txt"
plik.write_text("linia1\nlinia2\nlinia3\n", encoding="utf-8")
print(f"  Zapisano:  {plik}")
print(f"  Rozmiar:   {plik.stat().st_size} bajtów")
print(f"  Istnieje:  {plik.exists()}")
print(f"  Jest plik: {plik.is_file()}")

tekst = plik.read_text(encoding="utf-8")
print(f"  Odczytano: {tekst!r}")


# ---------------------------------------------------------------------------
# 3. Glob — wyszukiwanie plików
# ---------------------------------------------------------------------------
sekcja("3. Glob – wyszukiwanie plików")

(TMP / "a.txt").write_text("a", encoding="utf-8")
(TMP / "b.txt").write_text("b", encoding="utf-8")
(TMP / "c.csv").write_text("c", encoding="utf-8")
(TMP / "projekt" / "main.py").write_text("# kod", encoding="utf-8")

print("  Wszystkie .txt (rekurencyjnie):")
for p in sorted(TMP.rglob("*.txt")):
    print(f"    {p.relative_to(TMP)}")

print("  Pliki w katalogu głównym TMP:")
for p in sorted(TMP.iterdir()):
    typ = "DIR " if p.is_dir() else "FILE"
    print(f"    [{typ}] {p.name}")


# ---------------------------------------------------------------------------
# 4. Zmiana nazwy i kopiowanie
# ---------------------------------------------------------------------------
sekcja("4. Zmiana nazwy i suffixu")

oryginal = TMP / "a.txt"
zmieniony = oryginal.with_suffix(".bak")
oryginal.rename(zmieniony)
print(f"  Zmieniono: {oryginal.name} → {zmieniony.name}")
print(f"  Istnieje oryginal: {oryginal.exists()}")
print(f"  Istnieje nowy:     {zmieniony.exists()}")


# ---------------------------------------------------------------------------
# 5. Ścieżki względne i bezwzględne
# ---------------------------------------------------------------------------
sekcja("5. Ścieżki względne vs bezwzględne")

wzgledna = Path("foo/bar/baz.txt")
bezwzgledna = wzgledna.resolve()
print(f"  Względna:     {wzgledna}")
print(f"  Bezwzględna:  {bezwzgledna}")

# relative_to — wyciąganie ścieżki względem bazy
baza = TMP
plik2 = TMP / "projekt" / "dane" / "dane.txt"
wzgledna2 = plik2.relative_to(baza)
print(f"  relative_to TMP: {wzgledna2}")


# ---------------------------------------------------------------------------
# 6. Praca z Path.home() i Path.cwd()
# ---------------------------------------------------------------------------
sekcja("6. Katalog domowy i roboczy")

print(f"  Katalog domowy:  {Path.home()}")
print(f"  Katalog roboczy: {Path.cwd()}")


# ---------------------------------------------------------------------------
# Porządki
# ---------------------------------------------------------------------------
shutil.rmtree(TMP)
print(f"\n[OK] Katalog tymczasowy usunięty: {TMP}")

