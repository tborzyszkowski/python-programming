"""Zadania: lambda i funkcje wyższego rzędu."""


def zastosuj(f, x):
    """Zastosuj funkcję f do argumentu x i zwróć wynik."""
    raise NotImplementedError("Zaimplementuj zastosuj")


def stworz_mnoznik(n: int):
    """Zwróć funkcję (lambda), która mnoży przez n."""
    raise NotImplementedError("Zaimplementuj stworz_mnoznik")


def kompozycja(f, g):
    """Zwróć funkcję złożoną f(g(x))."""
    raise NotImplementedError("Zaimplementuj kompozycja")


def curry_add(x: int):
    """Zwróć funkcję, która dodaje x do swojego argumentu."""
    raise NotImplementedError("Zaimplementuj curry_add")


def mapuj_i_filtruj(dane: list[int], mapper, predykat) -> list[int]:
    """Najpierw mapuj, potem filtruj.

    Zwróć listę wartości y=mapper(x), dla których predykat(y) jest True.
    """
    raise NotImplementedError("Zaimplementuj mapuj_i_filtruj")

