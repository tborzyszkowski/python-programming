"""Moduł A — demonstracja cyklicznego importu (wersja z błędem).

UWAGA: Ten plik celowo zawiera cykliczny import!
Uruchomienie spowoduje ImportError.
Poprawiona wersja: circular_fixed/
"""

from circular_broken_b import oblicz_b  # ← importuje moduł B, który importuje nas z powrotem


def oblicz_a(x: int) -> int:
    return x + 1


def polacz(x: int) -> int:
    return oblicz_b(oblicz_a(x))


if __name__ == "__main__":
    print(polacz(5))

