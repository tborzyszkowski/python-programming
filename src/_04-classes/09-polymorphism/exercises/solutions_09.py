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
        return 0.5 * self.base * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


def total_area(shapes: list[Shape]) -> float:
    return sum(s.area() for s in shapes)


def largest_shape(shapes: list[Shape]) -> Shape:
    return max(shapes, key=lambda s: s.area())

