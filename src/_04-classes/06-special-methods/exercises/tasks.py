"""Zadanie 06 – Metody specjalne (dunder methods).

Uzupełnij klasę Vector2D o brakujące metody specjalne.
"""
import math


class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __len__(self) -> int:
        return 2

    def __str__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __repr__(self) -> str:
        """Zwróć jednoznaczny zapis: Vector2D(x=..., y=...)."""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """Porównanie dwóch wektorów po współrzędnych."""
        raise NotImplementedError

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """Dodawanie wektorów: Vector2D(1,2) + Vector2D(3,4) == Vector2D(4,6)."""
        raise NotImplementedError

    def __neg__(self) -> "Vector2D":
        """Negacja wektora: -Vector2D(1,2) == Vector2D(-1,-2)."""
        raise NotImplementedError

    @property
    def magnitude(self) -> float:
        """Długość wektora (norma euklidesowa)."""
        raise NotImplementedError
