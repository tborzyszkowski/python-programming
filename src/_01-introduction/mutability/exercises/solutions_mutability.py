"""
Wzorcowe rozwiązania – Typy mutowalne i niemutowalne
====================================================
"""
import copy
from functools import wraps


def bezpieczna_aktualizacja(slownik: dict, klucz: str, wartosc) -> dict:
    nowy = slownik.copy()
    nowy[klucz] = wartosc
    return nowy


def usun_duplikaty_zachowujac_kolejnosc(lista: list) -> list:
    widziane: set = set()
    wynik: list = []
    for elem in lista:
        if elem not in widziane:
            widziane.add(elem)
            wynik.append(elem)
    return wynik


def rozbuduj_cache(func):
    cache: dict = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache  # type: ignore[attr-defined]
    return wrapper


def gleboka_aktualizacja(cel: dict, zrodlo: dict) -> dict:
    for klucz, wartosc in zrodlo.items():
        if klucz in cel and isinstance(cel[klucz], dict) and isinstance(wartosc, dict):
            gleboka_aktualizacja(cel[klucz], wartosc)
        else:
            cel[klucz] = wartosc
    return cel


def zamroz_strukture(obj):
    if isinstance(obj, list):
        return tuple(zamroz_strukture(elem) for elem in obj)
    if isinstance(obj, dict):
        return frozenset((k, zamroz_strukture(v)) for k, v in obj.items())
    if isinstance(obj, set):
        return frozenset(zamroz_strukture(elem) for elem in obj)
    return obj


if __name__ == "__main__":
    d = {"a": 1}
    print(bezpieczna_aktualizacja(d, "b", 2), "| oryg:", d)
    print(usun_duplikaty_zachowujac_kolejnosc([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

    @rozbuduj_cache
    def kwadrat(n): return n * n
    print(kwadrat(4), kwadrat(4), kwadrat.cache)

    cel = {"a": 1, "b": {"x": 10, "y": 20}}
    print(gleboka_aktualizacja(cel, {"b": {"y": 99, "z": 30}, "c": 3}))
    print(zamroz_strukture([1, [2, 3], {4, 5}]))

