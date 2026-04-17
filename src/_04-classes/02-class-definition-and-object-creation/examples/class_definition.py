"""Definicja klasy i tworzenie obiektów – rozszerzony przykład."""
from __future__ import annotations


class BankAccount:
    """Konto bankowe z walidacją operacji."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if not owner.strip():
            raise ValueError("Właściciel konta nie może być pusty")
        self._owner = owner
        self._balance = float(balance)
        self._history: list[str] = []

    # ── reprezentacja ──────────────────────────────────────
    def __str__(self) -> str:
        return f"BankAccount({self._owner!r}, balance={self._balance:.2f})"

    def __repr__(self) -> str:
        return f"BankAccount(owner={self._owner!r}, balance={self._balance!r})"

    # ── właściwości ────────────────────────────────────────
    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return self._balance

    # ── operacje ───────────────────────────────────────────
    def deposit(self, amount: float) -> None:
        """Wpłata środków."""
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia")
        self._balance += amount
        self._history.append(f"+{amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """Wypłata środków."""
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być dodatnia")
        if amount > self._balance:
            raise ValueError(f"Niewystarczające środki (saldo: {self._balance:.2f})")
        self._balance -= amount
        self._history.append(f"-{amount:.2f}")

    def transfer(self, target: BankAccount, amount: float) -> None:
        """Przelew na inne konto."""
        self.withdraw(amount)
        target.deposit(amount)
        self._history.append(f"→ {target.owner}")

    def get_history(self) -> list[str]:
        return list(self._history)


def main() -> None:
    jan = BankAccount("Jan", 500.0)
    anna = BankAccount("Anna", 200.0)

    jan.deposit(100.0)
    jan.withdraw(50.0)
    jan.transfer(anna, 200.0)

    print(jan)
    print(anna)
    print("Historia Jana:", jan.get_history())

    # Próba wypłaty powyżej salda
    try:
        jan.withdraw(10_000.0)
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    main()
