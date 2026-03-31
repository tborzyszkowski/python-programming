"""Zadanie 03 – Rola `self` w Pythonie.

Uzupełnij klasę Counter o metodę add_many(n), która zwiększa wartość licznika o n.
"""


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> int:
        self.value += 1
        return self.value

    def add_many(self, n: int) -> int:
        """Zwiększ wartość licznika o n i zwróć nową wartość."""
        raise NotImplementedError
