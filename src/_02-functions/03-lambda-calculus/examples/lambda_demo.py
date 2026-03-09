"""
Demonstracja funkcji lambda i ich zastosowań.
"""


def zrob_cos(funkcja):
    """Przyjmuje funkcję jako argument i wywołuje ją na przykładowym argumencie."""
    return funkcja(10)


def generuj_mnoiznik(n):
    """Zwraca funkcję, która mnoży swój argument przez n."""
    return lambda x: x * n


if __name__ == "__main__":
    # Prosta lambda
    kwadrat = lambda x: x * x
    print(f"Kwadrat liczby 5: {kwadrat(5)}")

    # Przekazywanie funkcji jako argumentu
    wynik = zrob_cos(lambda x: x + 1)
    print(f"Wynik z funkcji: {wynik}")  # 11

    # Wywołanie lambdy bezpośrednio po definicji (IIFE style w Pythonie)
    # IIFE - Immediately Invoked Function Expression
    wynik2 = (lambda x, y: x + y)(3, 7)
    print(f"Bezpośrednie wywołanie: {wynik2}")

    # Domknięcia (Closures)
    razy_dwa = generuj_mnoiznik(2)
    razy_trzy = generuj_mnoiznik(3)

    print(f"10 * 2 = {razy_dwa(10)}")
    print(f"10 * 3 = {razy_trzy(10)}")

