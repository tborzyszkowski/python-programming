"""Zadanie 12 – Wzorce projektowe oparte na polimorfizmie.

Napisz klasę VipDiscount (zniżka 30%) oraz funkcję build_discount(kind: str),
która zwraca odpowiednią strategię dla kind == "vip".
"""
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        raise NotImplementedError


class VipDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        """Zwróć cenę po zniżce 30%."""
        raise NotImplementedError


def build_discount(kind: str) -> DiscountStrategy:
    """Fabryka strategii: dla kind='vip' zwróć VipDiscount."""
    raise NotImplementedError
