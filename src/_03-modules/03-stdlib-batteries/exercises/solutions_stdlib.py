"""Rozwiazania: stdlib."""

from itertools import combinations


def histogram(values: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return out


def all_pairs(values: list[int]) -> list[tuple[int, int]]:
    return list(combinations(values, 2))

