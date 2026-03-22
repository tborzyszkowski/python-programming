"""Funkcje matematyczne dla basic_pkg."""


def add(a: float, b: float) -> float:
    return a + b


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

