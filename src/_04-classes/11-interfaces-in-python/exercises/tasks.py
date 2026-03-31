"""Zadanie 11 – Interfejsy w Pythonie (ABC i Protocol).

Napisz klasę BlikProcessor zgodną z interfejsem płatności (metoda pay).
Wymaganie: pay(amount) zwraca napis w formacie "blik:<kwota:.2f>"
"""


class BlikProcessor:
    def pay(self, amount: float) -> str:
        """Zwróć potwierdzenie płatności BLIK."""
        raise NotImplementedError
