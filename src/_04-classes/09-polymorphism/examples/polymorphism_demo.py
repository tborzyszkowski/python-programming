"""Przykłady polimorfizmu – rozszerzony."""
from __future__ import annotations

import math


class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)


class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return math.pi * self.r ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.r


class Triangle(Shape):
    def __init__(self, base: float, height: float, a: float, b: float, c: float) -> None:
        self.base = base
        self.height = height
        self._sides = (a, b, c)

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        return sum(self._sides)


def total_area(shapes: list[Shape]) -> float:
    return sum(s.area() for s in shapes)


def main() -> None:
    shapes: list[Shape] = [
        Rectangle(3, 4),
        Circle(2),
        Triangle(6, 4, 6, 5, 5),
    ]
    for shape in shapes:
        print(shape.describe())
    print(f"Łączna powierzchnia: {total_area(shapes):.2f}")


if __name__ == "__main__":
    main()
