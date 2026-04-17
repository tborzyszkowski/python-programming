"""Komponenty prywatne – rozszerzone przykłady: Point, Segment, TemperatureSensor."""
from __future__ import annotations
from math import sqrt


class Point:
    """Punkt w układzie współrzędnych (tylko nieujemne)."""

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x   # przechodzi przez setter
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.__x}, {self.__y})"

    def __repr__(self) -> str:
        return f"Point(x={self.__x!r}, y={self.__y!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.__x == other.__x and self.__y == other.__y  # type: ignore[attr-defined]

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, value: float) -> None:
        self.__x = abs(value)   # name-mangling: _Point__x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, value: float) -> None:
        self.__y = abs(value)

    def distance(self, other: Point) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def translate(self, dx: float, dy: float) -> Point:
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor: float) -> Point:
        return Point(self.x * factor, self.y * factor)


class Segment:
    """Odcinek wyznaczony przez dwa punkty."""

    def __init__(self, first: Point = Point(0, 0), second: Point = Point(1, 1)) -> None:
        self.first_point = first    # przechodzi przez setter
        self.second_point = second

    def __str__(self) -> str:
        return f"Segment({self.__first_point}, {self.__second_point})"

    @property
    def first_point(self) -> Point:
        return self.__first_point

    @first_point.setter
    def first_point(self, p: Point) -> None:
        if not isinstance(p, Point):
            raise TypeError("Oczekiwano obiektu Point")
        self.__first_point = p

    @property
    def second_point(self) -> Point:
        return self.__second_point

    @second_point.setter
    def second_point(self, p: Point) -> None:
        if not isinstance(p, Point):
            raise TypeError("Oczekiwano obiektu Point")
        self.__second_point = p

    def length(self) -> float:
        return self.__first_point.distance(self.__second_point)

    def midpoint(self) -> Point:
        return Point(
            (self.__first_point.x + self.__second_point.x) / 2,
            (self.__first_point.y + self.__second_point.y) / 2,
        )

    def is_horizontal(self) -> bool:
        return self.__first_point.y == self.__second_point.y

    def is_vertical(self) -> bool:
        return self.__first_point.x == self.__second_point.x


class TemperatureSensor:
    """Czujnik temperatury – ilustracja różnych poziomów dostępu."""

    def __init__(self, celsius: float) -> None:
        self._celsius = celsius           # chroniony (konwencja)
        self.__calibration_offset = 0.0   # prywatny (name-mangling)

    @property
    def celsius(self) -> float:
        return self._celsius

    def calibrate(self, offset: float) -> None:
        self.__calibration_offset = offset

    def read(self) -> float:
        return self._celsius + self.__calibration_offset


def main() -> None:
    # Point
    p1, p2 = Point(0, 0), Point(3, 4)
    print(f"p1={p1}, p2={p2}")
    print(f"Odległość: {p1.distance(p2):.2f}")     # 5.0
    print(f"Przesunięcie: {p1.translate(1, 2)}")

    # Segment
    seg = Segment(p1, p2)
    print(f"\n{seg}")
    print(f"Długość: {seg.length():.2f}")           # 5.0
    print(f"Środek: {seg.midpoint()}")
    print(f"Poziomy: {seg.is_horizontal()}")

    # Name-mangling – demonstracja
    print(f"\nAtrybut prywatny (mangled): {seg._Segment__first_point}")

    # TemperatureSensor
    sensor = TemperatureSensor(20.0)
    sensor.calibrate(0.5)
    print(f"\nOdczyt czujnika: {sensor.read()}")    # 20.5


if __name__ == "__main__":
    main()
