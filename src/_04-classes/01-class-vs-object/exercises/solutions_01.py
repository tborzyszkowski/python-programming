from dataclasses import dataclass


@dataclass
class Student:
    name: str
    year: int


def count_first_year(students: list[Student]) -> int:
    return sum(1 for student in students if student.year == 1)


def students_by_year(students: list[Student], year: int) -> list[str]:
    return sorted(s.name for s in students if s.year == year)


def most_common_year(students: list[Student]) -> int:
    counts: dict[int, int] = {}
    for s in students:
        counts[s.year] = counts.get(s.year, 0) + 1
    return min(counts, key=lambda y: (-counts[y], y))
