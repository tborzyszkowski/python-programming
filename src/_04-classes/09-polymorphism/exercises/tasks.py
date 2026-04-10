"""Zadanie 09 – Polimorfizm: jedna operacja, wiele implementacji.

Napisz klasy figur geometrycznych i funkcje operujące polimorficznie.
"""
import math


class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}"


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        """Oblicz pole trójkąta: 0.5 * base * height."""
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Oblicz pole koła: π * r²."""
        raise NotImplementedError


def total_area(shapes: list[Shape]) -> float:
    """Oblicz łączne pole wszystkich figur (polimorficznie).

    Przykład:
        total_area([Triangle(4, 3), Circle(1)])  ->  6.0 + π ≈ 9.14
    """
    raise NotImplementedError


def largest_shape(shapes: list[Shape]) -> Shape:
    """Zwróć figurę o największym polu. Zakładamy, że lista jest niepusta."""
    raise NotImplementedError

