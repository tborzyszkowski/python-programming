"""Przykładowe rozwiązania zadań do tematu 05 – filtrowanie strumieni."""
from __future__ import annotations

import gzip
import heapq
import itertools
from collections import Counter
from io import BytesIO
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")


def filtruj_linie_gen(linie: Iterable[str], fraza: str) -> Iterator[str]:
    """Generator filtrujący linie zawierające frazę.

    Zużycie pamięci: O(1) — przetwarza jedną linię naraz.
    """
    return (l for l in linie if fraza in l)


def porcjuj(iterable: Iterable[T], n: int) -> Iterator[list[T]]:
    """Dzieli strumień na porcje (chunks) po n elementów.

    Ostatnia porcja może być krótsza.
    """
    it = iter(iterable)
    while True:
        porcja = list(itertools.islice(it, n))
        if not porcja:
            return
        yield porcja


def policz_wystapienia(
    iterable: Iterable[T],
    klucz: Callable[[T], str],
) -> Counter:
    """Zlicza wystąpienia według wartości funkcji klucz.

    Strumieniowe — nie gromadzi wszystkich elementów w pamięci,
    tylko Counter (słownik kluczy i ich liczb).
    """
    return Counter(klucz(el) for el in iterable)


def transformuj_linie(
    linie: Iterable[str],
    func: Callable[[str], str],
) -> Iterator[str]:
    """Stosuje funkcję transformującą do każdej linii strumienia."""
    return (func(l) for l in linie)


def scalaj_posortowane(strumienie: list[Iterator[T]]) -> Iterator[T]:
    """Scala wiele posortowanych strumieni w jeden posortowany strumień.

    Używa heapq.merge — O(k log k) gdzie k = liczba strumieni.
    Nie wczytuje całych strumieni do pamięci.
    """
    return heapq.merge(*strumienie)


def kompresuj_do_bytes(dane: bytes) -> bytes:
    """Kompresuje dane (bytes) algorytmem gzip i zwraca skompresowane bytes.

    Używa BytesIO — działa w pamięci bez pliku tymczasowego.
    """
    buf = BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb") as gz:
        gz.write(dane)
    return buf.getvalue()

