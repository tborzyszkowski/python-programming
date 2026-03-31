"""Rozwiązania: try-except-else-finally."""


def to_float_or_none(value: str) -> float | None:
    try:
        result = float(value)
    except ValueError:
        return None
    else:
        return result
    finally:
        # Miejsce na sprzątanie zasobów, gdyby funkcja ich używała.
        _ = None

