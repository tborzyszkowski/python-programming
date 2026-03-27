from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        raise NotImplementedError


class StudentDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.8


class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price


def checkout(price: float, strategy: DiscountStrategy) -> float:
    return strategy.apply(price)
