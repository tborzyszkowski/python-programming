"""Zadanie 09 – Polimorfizm: jedna operacja, wiele implementacji.

Napisz klasę Triangle dziedziczącą po Shape z metodą area().
Wzór: pole = 0.5 * podstawa * wysokość
"""


class Shape:
    def area(self) -> float:
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        """Oblicz pole trójkąta: 0.5 * base * height."""
        raise NotImplementedError
