"""Zadanie 01 – Klasa a obiekt: intuicja i historia.

Napisz funkcje operujące na obiektach klasy Student.
"""
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    year: int


def count_first_year(students: list[Student]) -> int:
    """Zwróć liczbę studentów z year == 1."""
    raise NotImplementedError


def students_by_year(students: list[Student], year: int) -> list[str]:
    """Zwróć listę imion studentów z podanego roku, posortowaną alfabetycznie.

    Przykład:
        students_by_year([Student("Ewa", 1), Student("Adam", 1), Student("Ola", 2)], 1)
        ->  ["Adam", "Ewa"]
    """
    raise NotImplementedError


def most_common_year(students: list[Student]) -> int:
    """Zwróć numer roku, na którym jest najwięcej studentów.

    Jeśli jest remis, zwróć najniższy numer roku.

    Przykład:
        most_common_year([Student("A", 1), Student("B", 2), Student("C", 1)])
        ->  1
    """
    raise NotImplementedError
