"""Zadanie 07 – Dziedziczenie w OOP i w Pythonie.

Napisz klasę Train dziedziczącą po Vehicle z nadpisaną metodą move().
"""


class Vehicle:
    def move(self) -> str:
        return "Pojazd przemieszcza się"


class Train(Vehicle):
    def move(self) -> str:
        """Zwróć opis ruchu pociągu."""
        raise NotImplementedError
