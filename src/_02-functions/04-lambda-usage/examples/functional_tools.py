"""
Demonstracja narzędzi funkcyjnych w Pythonie: map, filter, reduce.
"""
from functools import reduce
from operator import add


def demo_sortowanie():
    """Użycie lambdy jako klucza sortowania."""
    print("--- Sortowanie ---")
    dane = [
        {"imie": "Jan", "wiek": 30},
        {"imie": "Anna", "wiek": 25},
        {"imie": "Piotr", "wiek": 40},
    ]

    # Sortowanie po wieku
    posortowane = sorted(dane, key=lambda x: x["wiek"])
    print(f"Posortowane po wieku: {posortowane}")


def demo_map_filter_reduce():
    """Klasyczne funkcje wyższego rzędu."""
    print("\n--- Map / Filter / Reduce ---")
    liczby = range(1, 11)  # 1..10

    # Map: kwadraty liczb
    # W Pythonie 3 map zwraca iterator, więc konwertujemy na listę dla print
    kwadraty = list(map(lambda x: x ** 2, liczby))
    print(f"Kwadraty (map): {kwadraty}")

    # Porównanie z List Comprehension (często preferowane w Pythonie)
    kwadraty_lc = [x ** 2 for x in liczby]
    print(f"Kwadraty (list compl): {kwadraty_lc}")

    # Filter: tylko parzyste
    parzyste = list(filter(lambda x: x % 2 == 0, liczby))
    print(f"Parzyste (filter): {parzyste}")

    # Reduce: suma wszystkich (wymaga importu z functools)
    suma = reduce(lambda a, b: a + b, liczby)
    print(f"Suma (reduce): {suma}")
    # To samo co sum(liczby), ale pokazuje mechanizm

    # Reduce: iloczyn
    iloczyn = reduce(lambda a, b: a * b, liczby)
    print(f"Iloczyn (reduce): {iloczyn}")  # 10! (silnia)


if __name__ == "__main__":
    demo_sortowanie()
    demo_map_filter_reduce()

