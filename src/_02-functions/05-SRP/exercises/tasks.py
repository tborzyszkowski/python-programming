"""Zadania do samodzielnego rozwiazania - SRP dla funkcji."""


def parse_student_line(line: str) -> tuple[str, list[float]]:
    """Parsuje linie 'Imie;80;90;70' -> ('Imie', [80.0, 90.0, 70.0])."""
    raise NotImplementedError("Zaimplementuj parse_student_line")


def validate_score(score: float) -> None:
    """Waliduje pojedynczy wynik (0-100). Dla zlego wyniku rzuca ValueError."""
    raise NotImplementedError("Zaimplementuj validate_score")


def compute_average(scores: list[float]) -> float:
    """Oblicza srednia z listy wynikow. Dla pustej listy rzuca ValueError."""
    raise NotImplementedError("Zaimplementuj compute_average")


def classify_result(avg: float) -> str:
    """Klasyfikuje srednia: >=90 A, >=75 B, >=60 C, >=50 D, inaczej F."""
    raise NotImplementedError("Zaimplementuj classify_result")


def build_summary(name: str, avg: float, cls: str) -> str:
    """Buduje napis: '<name>: srednia=<avg>, ocena=<cls>' z avg do 2 miejsc."""
    raise NotImplementedError("Zaimplementuj build_summary")


def process_student_record(line: str) -> str:
    """Orkiestruje caly proces poprzez wywolanie mniejszych funkcji SRP."""
    raise NotImplementedError("Zaimplementuj process_student_record")

