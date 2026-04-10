"""Moduł B — poprawiona wersja bez cyklicznego importu.

Importuje wspólną logikę z circular_fixed_common.py zamiast z moduł A.
"""

from circular_fixed_common import oblicz_a


def oblicz_b(x: int) -> int:
    return oblicz_a(x) * 2

