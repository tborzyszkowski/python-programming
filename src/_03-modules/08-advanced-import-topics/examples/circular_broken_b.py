"""Moduł B — demonstracja cyklicznego importu (wersja z błędem).

UWAGA: Ten plik celowo zawiera cykliczny import!
"""

from circular_broken_a import oblicz_a  # ← importuje moduł A, który importuje nas z powrotem


def oblicz_b(x: int) -> int:
    return oblicz_a(x) * 2

