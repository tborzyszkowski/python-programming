"""Rozwiązania: wyjątki wbudowane."""


def safe_ratio(numerator: str, denominator: str) -> float | None:
    try:
        top = float(numerator)
        bottom = float(denominator)
        return top / bottom
    except (ValueError, ZeroDivisionError):
        return None

