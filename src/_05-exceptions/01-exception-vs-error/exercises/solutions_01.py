"""Rozwiązania: wyjątek vs błąd."""


def parse_positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise ValueError("Wartość musi być dodatnia")
    return number

