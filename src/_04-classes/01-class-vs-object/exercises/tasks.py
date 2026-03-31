"""Zadanie 01 – Klasa a obiekt: intuicja i historia.

Napisz funkcję count_first_year, która policzy studentów z pierwszego roku.
"""
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    year: int


def count_first_year(students: list[Student]) -> int:
    """Zwróć liczbę studentów z year == 1."""
    raise NotImplementedError
