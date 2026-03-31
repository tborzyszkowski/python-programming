"""Wzorce projektowe: Strategy, Template Method, Factory Method."""
from __future__ import annotations

from abc import ABC, abstractmethod


# ──────────────────────────────────────────────
# Wzorzec Strategy (strategia rabatu)
# ──────────────────────────────────────────────

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        raise NotImplementedError


class StudentDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.8


class VipDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.7


class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price


def checkout(price: float, strategy: DiscountStrategy) -> float:
    return strategy.apply(price)


# ──────────────────────────────────────────────
# Wzorzec Factory Method
# ──────────────────────────────────────────────

def build_discount(kind: str) -> DiscountStrategy:
    registry: dict[str, type[DiscountStrategy]] = {
        "student": StudentDiscount,
        "vip": VipDiscount,
        "none": NoDiscount,
    }
    if kind not in registry:
        raise ValueError(f"Nieznany typ zniżki: {kind!r}")
    return registry[kind]()


# ──────────────────────────────────────────────
# Wzorzec Template Method (raport z oceny)
# ──────────────────────────────────────────────

class ReportTemplate(ABC):
    def generate(self, name: str, score: float) -> str:
        lines = [
            self._header(name),
            self._body(score),
            self._footer(),
        ]
        return "\n".join(lines)

    def _header(self, name: str) -> str:
        return f"=== Raport: {name} ==="

    @abstractmethod
    def _body(self, score: float) -> str:
        raise NotImplementedError

    def _footer(self) -> str:
        return "=== Koniec raportu ==="


class PassFailReport(ReportTemplate):
    def _body(self, score: float) -> str:
        result = "ZALICZONE" if score >= 50 else "NIEZALICZONE"
        return f"Wynik: {score:.1f} → {result}"


class GradedReport(ReportTemplate):
    def _body(self, score: float) -> str:
        grade = int(score // 10)
        return f"Wynik: {score:.1f} → ocena {min(grade, 10)}/10"


def main() -> None:
    print("--- Strategy ---")
    for kind in ("student", "vip", "none"):
        strategy = build_discount(kind)
        print(f"{kind}: {checkout(100.0, strategy):.2f}")

    print("\n--- Template Method ---")
    for report_cls in (PassFailReport, GradedReport):
        report = report_cls()
        print(report.generate("Jan Kowalski", 73.5))
        print()


if __name__ == "__main__":
    main()
