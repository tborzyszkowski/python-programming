"""Większy przykład: System oceniania kursów z polimorfizmem."""
from __future__ import annotations
from abc import ABC, abstractmethod


class GradePolicy(ABC):
    """Abstrakcyjna polityka oceniania."""

    @abstractmethod
    def final_score(self, points: list[float]) -> float:
        ...

    def letter_grade(self, points: list[float]) -> str:
        score = self.final_score(points)
        if score >= 90: return "A"
        if score >= 80: return "B"
        if score >= 70: return "C"
        if score >= 60: return "D"
        return "F"

    def __str__(self) -> str:
        return type(self).__name__


class MeanPolicy(GradePolicy):
    """Średnia arytmetyczna wszystkich punktów."""

    def final_score(self, points: list[float]) -> float:
        if not points:
            raise ValueError("Brak punktów")
        return sum(points) / len(points)


class BestOfTwoPolicy(GradePolicy):
    """Średnia z dwóch najlepszych wyników."""

    def final_score(self, points: list[float]) -> float:
        if len(points) < 2:
            raise ValueError("Potrzeba co najmniej 2 punktów")
        top2 = sorted(points, reverse=True)[:2]
        return sum(top2) / len(top2)


class WeightedPolicy(GradePolicy):
    """Średnia ważona."""

    def __init__(self, weights: list[float]) -> None:
        if abs(sum(weights) - 1.0) > 1e-9:
            raise ValueError("Suma wag musi wynosić 1.0")
        self._weights = weights

    def final_score(self, points: list[float]) -> float:
        if len(points) != len(self._weights):
            raise ValueError("Liczba punktów musi równać się liczbie wag")
        return sum(p * w for p, w in zip(points, self._weights))


class Student:
    """Student z historią ocen."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._scores: dict[str, list[float]] = {}

    def __str__(self) -> str:
        return self._name

    def add_scores(self, course: str, points: list[float]) -> None:
        self._scores[course] = points

    def average(self) -> float:
        all_scores = [s for scores in self._scores.values() for s in scores]
        return sum(all_scores) / len(all_scores) if all_scores else 0.0


class Course:
    """Kurs z przypisaną polityką oceniania."""

    def __init__(self, name: str, policy: GradePolicy) -> None:
        self._name = name
        self._policy = policy
        self._students: list[Student] = []

    def __str__(self) -> str:
        return f"Course({self._name!r}, policy={self._policy})"

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def evaluate(self, points: list[float]) -> float:
        return self._policy.final_score(points)

    def class_report(self, results: dict[str, list[float]]) -> str:
        lines = [f"=== {self._name} (polityka: {self._policy}) ==="]
        for name, pts in results.items():
            score = self._policy.final_score(pts)
            grade = self._policy.letter_grade(pts)
            lines.append(f"  {name:20s}: {score:6.2f} ({grade})")
        return "\n".join(lines)


def main() -> None:
    results = {
        "Jan Kowalski":  [70, 80, 65],
        "Anna Nowak":    [90, 88, 92],
        "Piotr Wiśnicki": [55, 60, 58],
    }

    policies: list[GradePolicy] = [
        MeanPolicy(),
        BestOfTwoPolicy(),
        WeightedPolicy([0.2, 0.3, 0.5]),
    ]

    for policy in policies:
        course = Course("Python 101", policy)
        print(course.class_report(results))
        print()


if __name__ == "__main__":
    main()
