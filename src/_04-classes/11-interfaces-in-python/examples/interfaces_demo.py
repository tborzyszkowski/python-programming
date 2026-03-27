from abc import ABC, abstractmethod
from typing import Protocol


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        raise NotImplementedError


class SupportsPay(Protocol):
    def pay(self, amount: float) -> str:
        ...


class CardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"card:{amount:.2f}"
