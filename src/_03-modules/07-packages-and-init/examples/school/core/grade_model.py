"""Warstwa modelu obliczen."""


def final_grade(points: list[int]) -> float:
    if not points:
        raise ValueError("points cannot be empty")
    return round(sum(points) / len(points), 2)

