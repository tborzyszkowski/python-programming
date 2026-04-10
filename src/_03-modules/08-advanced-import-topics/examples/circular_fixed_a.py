"""Moduł A — poprawiona wersja bez cyklicznego importu.

Rozwiązanie: wspólna logika przeniesiona do circular_fixed_common.py.
"""

from circular_fixed_common import oblicz_a
from circular_fixed_b import oblicz_b


def polacz(x: int) -> int:
    return oblicz_b(oblicz_a(x))


if __name__ == "__main__":
    print(f"polacz(5) = {polacz(5)}")
    # oblicz_a(5) = 6, oblicz_b(6) = 6 * 2 = 12

