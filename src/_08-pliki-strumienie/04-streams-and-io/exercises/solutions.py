"""Przykładowe rozwiązania zadań do tematu 04 – strumienie io."""
from __future__ import annotations

import csv
import io
import zipfile


def csv_do_stringa(wiersze: list[dict], pola: list[str]) -> str:
    """Serializuje listę słowników do stringa w formacie CSV z nagłówkiem."""
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=pola)
    writer.writeheader()
    writer.writerows(wiersze)
    return buf.getvalue()


def string_do_csv(tekst: str) -> list[dict]:
    """Parsuje string w formacie CSV (z nagłówkiem) do listy słowników."""
    reader = csv.DictReader(io.StringIO(tekst))
    return list(reader)


def dlugosc_strumienia(strumien: io.RawIOBase | io.BufferedIOBase) -> int:
    """Zwraca długość (w bajtach) strumienia binarnego bez zmiany pozycji."""
    pos = strumien.tell()
    strumien.seek(0, 2)   # seek do końca
    rozmiar = strumien.tell()
    strumien.seek(pos)    # wróć na oryginalne miejsce
    return rozmiar


def sklej_strumienie(strumienie: list[io.BytesIO]) -> bytes:
    """Scala zawartość wielu strumieni binarnych w jeden obiekt bytes."""
    wynik = io.BytesIO()
    for s in strumienie:
        s.seek(0)
        wynik.write(s.read())
    return wynik.getvalue()


def stworz_zip_w_pamieci(pliki: dict[str, bytes]) -> bytes:
    """Tworzy archiwum ZIP w pamięci i zwraca je jako bytes."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for nazwa, dane in pliki.items():
            zf.writestr(nazwa, dane)
    return buf.getvalue()


def wypakuj_zip_z_pamieci(dane_zip: bytes) -> dict[str, bytes]:
    """Rozpakowuje archiwum ZIP z bytes i zwraca słownik nazwa→zawartość."""
    wynik = {}
    with zipfile.ZipFile(io.BytesIO(dane_zip)) as zf:
        for nazwa in zf.namelist():
            wynik[nazwa] = zf.read(nazwa)
    return wynik


class CountingStream:
    """Wrapper strumienia zliczający odczytane i zapisane bajty."""

    def __init__(self, strumien: io.IOBase) -> None:
        self._s = strumien
        self.bytes_written = 0
        self.bytes_read    = 0

    def write(self, dane: bytes) -> int:
        n = self._s.write(dane)
        self.bytes_written += n
        return n

    def read(self, size: int = -1) -> bytes:
        if size == -1:
            wynik = self._s.read()
        else:
            wynik = self._s.read(size)
        self.bytes_read += len(wynik)
        return wynik

    def seek(self, pos: int, whence: int = 0) -> int:
        return self._s.seek(pos, whence)

    def tell(self) -> int:
        return self._s.tell()

    def flush(self) -> None:
        self._s.flush()

