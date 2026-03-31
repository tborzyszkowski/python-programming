"""Przykłady metod specjalnych (dunder methods) – rozszerzony."""
from __future__ import annotations

import math


class Vector2D:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # --- reprezentacja ---
    def __str__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x!r}, y={self.y!r})"

    # --- długość i porównanie ---
    def __len__(self) -> int:
        return 2

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # --- operacje arytmetyczne ---
    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> Vector2D:
        return Vector2D(self.x * scalar, self.y * scalar)

    # --- właściwości ---
    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def magnitude_hint(self) -> float:
        return abs(self.x) + abs(self.y)


def main() -> None:
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, -1)
    print(str(v1))          # __str__
    print(repr(v1))         # __repr__
    print(len(v1))          # __len__
    print(v1 == Vector2D(3, 4))  # __eq__
    print(v1 + v2)          # __add__
    print(v1 * 2)           # __mul__
    print(f"magnitude={v1.magnitude:.2f}")


if __name__ == "__main__":
    main()

