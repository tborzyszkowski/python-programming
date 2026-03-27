from dataclasses import dataclass


@dataclass
class Student:
    name: str
    year: int


def count_first_year(students: list[Student]) -> int:
    return sum(1 for student in students if student.year == 1)
