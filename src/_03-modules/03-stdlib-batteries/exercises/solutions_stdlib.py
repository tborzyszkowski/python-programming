"""Rozwiązania: biblioteka standardowa."""

from datetime import datetime
from itertools import combinations
from pathlib import Path


def histogram(values: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return out


def all_pairs(values: list[int]) -> list[tuple[int, int]]:
    return list(combinations(values, 2))


def days_between(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def file_extension(path: str) -> str:
    return Path(path).suffix
