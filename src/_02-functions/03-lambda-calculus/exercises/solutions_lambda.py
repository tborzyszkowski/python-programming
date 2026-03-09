"""Przykładowe rozwiązania: lambda-calculus."""


def zastosuj(f, x):
    return f(x)


def stworz_mnoznik(n: int):
    return lambda x: x * n


def kompozycja(f, g):
    return lambda x: f(g(x))


def curry_add(x: int):
    return lambda y: x + y


def mapuj_i_filtruj(dane: list[int], mapper, predykat) -> list[int]:
    mapped = map(mapper, dane)
    return [y for y in mapped if predykat(y)]

