"""Wspólna logika — wydzielona, aby przerwać cykl zależności.

Rozwiązanie 1: przeniesienie wspólnych funkcji do trzeciego modułu.
"""


def oblicz_a(x: int) -> int:
    """Funkcja wcześniej w modul_a — teraz w module wspólnym."""
    return x + 1

