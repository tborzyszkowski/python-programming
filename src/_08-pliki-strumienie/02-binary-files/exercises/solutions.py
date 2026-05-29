"""Przykładowe rozwiązania zadań do tematu 02 – pliki binarne."""
from __future__ import annotations

import struct
from pathlib import Path


# Format nagłówka: sygnatura(4B) + wiersze(I) + kolumny(I)
_HDR = struct.Struct("<4sII")
# Format elementu: int32 (I)
_EL  = struct.Struct("<i")


def zapisz_macierz(sciezka: Path, macierz: list[list[int]]) -> None:
    """Zapisuje macierz liczb całkowitych w binarnym formacie własnym.

    Nagłówek: b'MTRX' + uint32 wiersze + uint32 kolumny
    Dane:     wiersz po wierszu, każdy element jako int32 LE.
    """
    wiersze  = len(macierz)
    kolumny  = len(macierz[0]) if macierz else 0

    with sciezka.open("wb") as f:
        f.write(_HDR.pack(b"MTRX", wiersze, kolumny))
        for wiersz in macierz:
            for elem in wiersz:
                f.write(_EL.pack(elem))


def czytaj_macierz(sciezka: Path) -> list[list[int]]:
    """Odczytuje macierz zapisaną przez :func:`zapisz_macierz`."""
    with sciezka.open("rb") as f:
        syg, wiersze, kolumny = _HDR.unpack(f.read(_HDR.size))
        if syg != b"MTRX":
            raise ValueError(f"Zła sygnatura: {syg!r}")
        wynik = []
        for _ in range(wiersze):
            wiersz = [_EL.unpack(f.read(_EL.size))[0] for _ in range(kolumny)]
            wynik.append(wiersz)
        return wynik


def znajdz_wzorzec_binarny(sciezka: Path, wzorzec: bytes) -> list[int]:
    """Zwraca listę wszystkich pozycji (offset) wzorca w pliku binarnym."""
    dane = sciezka.read_bytes()
    pozycje = []
    start = 0
    while True:
        pos = dane.find(wzorzec, start)
        if pos == -1:
            break
        pozycje.append(pos)
        start = pos + 1
    return pozycje


def xor_bytes(dane: bytes, klucz: int) -> bytes:
    """Wykonuje operację XOR każdego bajtu z kluczem (0–255)."""
    return bytes(b ^ klucz for b in dane)


def hex_dump(dane: bytes, width: int = 16) -> str:
    """Zwraca czytelny zrzut hex podobny do hexdump -C.

    Każda linia zawiera offset (hex), bajty w hex i ich reprezentację ASCII.
    """
    linie = []
    for i in range(0, len(dane), width):
        kawałek = dane[i : i + width]
        hex_czesc = " ".join(f"{b:02x}" for b in kawałek)
        ascii_czesc = "".join(chr(b) if 32 <= b < 127 else "." for b in kawałek)
        linie.append(f"{i:08x}  {hex_czesc:<{width * 3}}  |{ascii_czesc}|")
    return "\n".join(linie)

