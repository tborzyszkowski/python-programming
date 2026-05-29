"""Podstawowe operacje na plikach tekstowych.

Uruchomienie:
    python src/_08-pliki-strumienie/01-text-files/examples/text_operations.py
"""
from __future__ import annotations

import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Pomocnik: tymczasowy katalog roboczy
# ---------------------------------------------------------------------------
TMP = Path(tempfile.mkdtemp(prefix="py_teksty_"))


def sekcja(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# 1. Zapis i odczyt całości
# ---------------------------------------------------------------------------
sekcja("1. Zapis i odczyt (całość)")

plik = TMP / "notatka.txt"
plik.write_text("Pierwsza linia\nDruga linia\nTrzecia linia\n", encoding="utf-8")

tekst = plik.read_text(encoding="utf-8")
print(repr(tekst))


# ---------------------------------------------------------------------------
# 2. Odczyt linia po linii (wydajny dla dużych plików)
# ---------------------------------------------------------------------------
sekcja("2. Iteracja po liniach")

with plik.open(encoding="utf-8") as f:
    for nr, linia in enumerate(f, 1):
        print(f"  {nr}: {linia.rstrip()}")


# ---------------------------------------------------------------------------
# 3. Dołączanie
# ---------------------------------------------------------------------------
sekcja("3. Tryb 'a' — dołączanie")

with plik.open("a", encoding="utf-8") as f:
    f.write("Czwarta linia\n")

print(plik.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# 4. Tryb ekskluzywny 'x'
# ---------------------------------------------------------------------------
sekcja("4. Tryb 'x' — tworzenie (błąd gdy istnieje)")

nowy = TMP / "nowy.txt"
with nowy.open("x", encoding="utf-8") as f:
    f.write("Nowy plik\n")

try:
    with nowy.open("x", encoding="utf-8") as f:
        f.write("To nie zadziała\n")
except FileExistsError as e:
    print(f"  Oczekiwany błąd: {e}")


# ---------------------------------------------------------------------------
# 5. Seek / tell
# ---------------------------------------------------------------------------
sekcja("5. Pozycja w pliku: tell() i seek()")

with plik.open("r", encoding="utf-8") as f:
    print(f"  Pozycja startowa: {f.tell()}")
    linia1 = f.readline()
    print(f"  Po readline: {f.tell()}, przeczytano: {linia1!r}")
    f.seek(0)
    print(f"  Po seek(0): {f.tell()}")
    poczatek = f.read(5)
    print(f"  Pierwsze 5 znaków: {poczatek!r}")


# ---------------------------------------------------------------------------
# 6. Kodowania
# ---------------------------------------------------------------------------
sekcja("6. Kodowania: UTF-8 vs Latin-2")

tekst_pl = "Zażółć gęślą jaźń"

utf8_plik   = TMP / "utf8.txt"
latin2_plik = TMP / "latin2.txt"

utf8_plik.write_text(tekst_pl, encoding="utf-8")
latin2_plik.write_text(tekst_pl, encoding="iso-8859-2")

print(f"  UTF-8  rozmiar:  {utf8_plik.stat().st_size} bajtów")
print(f"  Latin-2 rozmiar: {latin2_plik.stat().st_size} bajtów")

# Błędne kodowanie z obsługą
with utf8_plik.open(encoding="ascii", errors="replace") as f:
    odczytany = f.read()
    # ascii() zamienia non-ASCII na \uXXXX — bezpieczne na każdej konsoli
    print(f"  Odczyt UTF-8 przez ASCII (replace): {ascii(odczytany)}")


# ---------------------------------------------------------------------------
# 7. Filtrowanie linii
# ---------------------------------------------------------------------------
sekcja("7. Filtrowanie linii zawierających frazę")

log = TMP / "app.log"
log.write_text(
    "2024-01-01 INFO  Start\n"
    "2024-01-01 ERROR Połączenie nieudane\n"
    "2024-01-01 INFO  Ponów próbę\n"
    "2024-01-01 ERROR Timeout\n"
    "2024-01-01 INFO  Stop\n",
    encoding="utf-8",
)

bledy = [l.rstrip() for l in log.open(encoding="utf-8") if "ERROR" in l]
print(f"  Błędy ({len(bledy)}):")
for b in bledy:
    print(f"    {b}")


# ---------------------------------------------------------------------------
# 8. Statystyki pliku
# ---------------------------------------------------------------------------
sekcja("8. Statystyki pliku")

def statystyki(sciezka: Path) -> dict:
    tekst = sciezka.read_text(encoding="utf-8")
    slowa = tekst.split()
    return {
        "znaki":    len(tekst),
        "slowa":    len(slowa),
        "linie":    tekst.count("\n"),
        "unikalne": len({w.lower() for w in slowa}),
    }

stat = statystyki(log)
for klucz, wartosc in stat.items():
    print(f"  {klucz:12s}: {wartosc}")


# ---------------------------------------------------------------------------
# Porządki
# ---------------------------------------------------------------------------
import shutil
shutil.rmtree(TMP)
print(f"\n[OK] Pliki tymczasowe usunięte z {TMP}")

