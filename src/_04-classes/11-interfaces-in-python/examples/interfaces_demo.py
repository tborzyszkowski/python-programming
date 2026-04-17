"""Interfejsy w Pythonie: ABC i Protocol – rozszerzony przykład."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# ─────────────────────────────────────────────────────────
#  ABC – nominalne (jawne dziedziczenie)
# ─────────────────────────────────────────────────────────

class PaymentProcessor(ABC):
    """Abstrakcyjny interfejs procesora płatności."""

    @abstractmethod
    def pay(self, amount: float) -> str:
        ...

    @abstractmethod
    def refund(self, amount: float) -> str:
        ...

    def receipt(self, amount: float) -> str:
        return f"Paragon: {self.pay(amount)}"


class CardProcessor(PaymentProcessor):
    def __init__(self, card_number: str) -> None:
        self._card = card_number[-4:]   # tylko ostatnie 4 cyfry

    def pay(self, amount: float) -> str:
        return f"Karta *{self._card}: zapłacono {amount:.2f} PLN"

    def refund(self, amount: float) -> str:
        return f"Karta *{self._card}: zwrot {amount:.2f} PLN"


class BLIKProcessor(PaymentProcessor):
    def __init__(self, phone: str) -> None:
        self._phone = phone

    def pay(self, amount: float) -> str:
        return f"BLIK ({self._phone}): zapłacono {amount:.2f} PLN"

    def refund(self, amount: float) -> str:
        return f"BLIK ({self._phone}): zwrot {amount:.2f} PLN"


class CashProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Gotówka: zapłacono {amount:.2f} PLN"

    def refund(self, amount: float) -> str:
        return f"Gotówka: zwrot {amount:.2f} PLN"


# ─────────────────────────────────────────────────────────
#  Protocol – strukturalne (duck typing ze wsparciem mypy)
# ─────────────────────────────────────────────────────────

@runtime_checkable
class SupportsPay(Protocol):
    """Protokół: każdy obiekt z metodą pay() spełnia ten interfejs."""
    def pay(self, amount: float) -> str:
        ...


class CryptoWallet:
    """Klasa NIE dziedziczy po PaymentProcessor, ale spełnia SupportsPay."""
    def __init__(self, address: str) -> None:
        self._address = address

    def pay(self, amount: float) -> str:
        return f"Crypto ({self._address[:6]}...): {amount:.4f} ETH"


def process_payment(processor: SupportsPay, amount: float) -> None:
    print(processor.pay(amount))


def main() -> None:
    processors: list[PaymentProcessor] = [
        CardProcessor("1234567890123456"),
        BLIKProcessor("+48 600 100 200"),
        CashProcessor(),
    ]
    for p in processors:
        print(p.receipt(49.99))

    print("\n--- Protocol (duck typing) ---")
    crypto = CryptoWallet("0xAbCd1234EfGh5678")
    print(isinstance(crypto, SupportsPay))   # True – runtime_checkable
    process_payment(crypto, 0.025)

    # Próba instancji abstrakcyjnej
    try:
        PaymentProcessor()   # type: ignore
    except TypeError as e:
        print(f"\nABC chroni: {e}")


if __name__ == "__main__":
    main()
