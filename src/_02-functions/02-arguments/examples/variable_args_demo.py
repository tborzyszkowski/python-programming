"""
Demonstracja zmiennej liczby argumentów w Pythonie.
"""
from typing import Any


def suma_liczb(*args: int) -> int:
    """Sumuje dowolną liczbę liczb całkowitych."""
    return sum(args)


def raport(tytul: str, **dane: Any) -> None:
    """Generuje raport z przekazanych danych."""
    print(f"--- RAPORT: {tytul} ---")
    for klucz, wartosc in dane.items():
        print(f"  {klucz}: {wartosc}")
    print("-" * 20)


def funkcja_wszystkiego(a, b, *args, opcja=True, **kwargs):
    """Demonstracja wszystkich typów argumentów."""
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"opcja={opcja}")
    print(f"kwargs={kwargs}")


if __name__ == "__main__":
    print(f"Suma(1, 2, 3): {suma_liczb(1, 2, 3)}")
    print(f"Suma(): {suma_liczb()}")

    raport("Statystyki serwera", cpu="45%", ram="8GB", online=True)

    print("\nDemonstracja złożona:")
    funkcja_wszystkiego(1, 2, 3, 4, 5, x=10, y=20)
    # a=1, b=2
    # args=(3, 4, 5)
    # opcja=True
    # kwargs={'x': 10, 'y': 20}

