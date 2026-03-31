"""Zadanie 10 – Większy przykład: system ocen.

Napisz klasę WeightedPolicy realizującą ważoną średnią wyników.
Konstruktor przyjmuje w1 i w2 (wagi dla punktów[0] i punktów[1]).
"""


class WeightedPolicy:
    def __init__(self, w1: float, w2: float) -> None:
        self.w1 = w1
        self.w2 = w2

    def final_score(self, points: list[float]) -> float:
        """Zwróć: points[0]*w1 + points[1]*w2."""
        raise NotImplementedError
