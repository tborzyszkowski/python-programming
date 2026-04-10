"""Demonstracja aliasów importu i kolizji nazw."""

import math as m
from math import sqrt as pierwiastek


def demo_alias() -> float:
    """Użycie aliasu modułu — krótszy zapis bez utraty czytelności."""
    return m.pi * m.e


def demo_symbol_alias(x: float) -> float:
    """Alias symbolu — przydatny przy kolizji lub dla czytelności."""
    return pierwiastek(x)


# ── Kolizja nazw ──────────────────────────────────────────────────

def demo_shadowing() -> str:
    """Pokazuje, jak lokalna zmienna przesłania zaimportowaną nazwę."""
    # Wyobraź sobie, że ktoś nieopatrznie nadpisze wbudowaną nazwę:
    # list = [1, 2, 3]   # ← NIGDY tego nie rób!

    # Bezpieczny wariant: import z aliasem unika kolizji
    from datetime import date as dt_date

    dzisiaj = dt_date.today()
    return f"Dzisiaj: {dzisiaj.isoformat()}"


def demo_builtin_shadowing() -> str:
    """Celowe nadpisanie builtina i przywrócenie."""
    import builtins

    # Zapisujemy oryginalną funkcję:
    original_len = builtins.len

    # „Nadpisujemy" len w lokalnym scope:
    len_local = lambda seq: f"długość={original_len(seq)}"  # noqa: E731

    wynik = len_local([1, 2, 3])

    # Oryginalna len nadal działa (nie nadpisaliśmy builtins):
    assert builtins.len([1, 2, 3]) == 3

    return wynik


if __name__ == "__main__":
    print("Alias modułu:", demo_alias())
    print("Alias symbolu:", demo_symbol_alias(49))
    print(demo_shadowing())
    print("Builtin shadowing:", demo_builtin_shadowing())

