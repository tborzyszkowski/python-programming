"""Zadania: biblioteka standardowa."""

from datetime import datetime


def histogram(values: list[str]) -> dict[str, int]:
    """Zlicz wystąpienia elementów bez użycia bibliotek zewnętrznych."""
    raise NotImplementedError


def all_pairs(values: list[int]) -> list[tuple[int, int]]:
    """Zwróć wszystkie pary i<j."""
    raise NotImplementedError


def days_between(date1: str, date2: str) -> int:
    """Oblicz liczbę dni między dwiema datami w formacie 'YYYY-MM-DD'.

    Zwraca wartość bezwzględną (zawsze >= 0).

    Przykład:
        days_between("2026-01-01", "2026-01-10")  ->  9
        days_between("2026-03-15", "2026-03-10")  ->  5
    """
    raise NotImplementedError


def file_extension(path: str) -> str:
    """Zwróć rozszerzenie pliku (z kropką) używając pathlib.

    Przykład:
        file_extension("/home/user/raport.txt")  ->  ".txt"
        file_extension("dane.csv")  ->  ".csv"
        file_extension("README")  ->  ""
    """
    raise NotImplementedError
