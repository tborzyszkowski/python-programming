"""Zadanie 06 – Metody specjalne (dunder methods).

Uzupełnij klasę Vector2D o metodę __repr__ zwracającą jednoznaczny zapis obiektu.
Wymaganie: eval(repr(v)) == v (dla odpowiedniej definicji __eq__).
"""


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

