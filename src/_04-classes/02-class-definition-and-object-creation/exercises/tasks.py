"""Zadanie 02 – Definicja klasy i tworzenie obiektu.

Uzupełnij klasę BankAccount o metodę withdraw oraz napisz funkcję safe_transfer.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Pobierz amount z konta. Zgłoś ValueError gdy brak środków."""
        raise NotImplementedError


def safe_transfer(src: "BankAccount", dst: "BankAccount", amount: float) -> None:
    """Przenieś amount z konta src na dst w sposób bezpieczny."""
    raise NotImplementedError


def total_balance(accounts: list["BankAccount"]) -> float:
    """Zwróć sumę sald wszystkich kont.

    Przykład:
        total_balance([BankAccount("A", 100), BankAccount("B", 200)])  ->  300.0
    """
    raise NotImplementedError
