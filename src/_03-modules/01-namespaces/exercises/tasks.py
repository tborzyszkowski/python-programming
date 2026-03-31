"""Zadania: namespaces."""

from collections.abc import Callable


def find_in_legb(local_value: str, enclosing_value: str, global_value: str) -> tuple[str, str, str]:
    """Zwroc wartosci odpowiadajace poziomom L, E i G."""
    raise NotImplementedError


def merge_symbol_tables(local_table: dict, global_table: dict) -> dict:
    """Scal slowniki symboli; lokalne maja pierwszenstwo przy konflikcie."""
    raise NotImplementedError


def make_call_counter() -> Callable[[], int]:
    """Zwroc funkcje, ktora przy kazdym wywolaniu zwraca kolejna liczbe (1, 2, 3, ...).

    Wskazowka: uzyj nonlocal, aby zmodyfikowac zmienna z zakresu otaczajacego.
    """
    raise NotImplementedError


def is_name_global(name: str, namespace: dict) -> bool:
    """Zwroc True, jesli 'name' wystepuje w podanym slowniku namespace (symulacja globals()).

    Przyklad:
        is_name_global("VALUE", {"VALUE": 42, "x": 1})  ->  True
        is_name_global("y",     {"VALUE": 42, "x": 1})  ->  False
    """
    raise NotImplementedError


