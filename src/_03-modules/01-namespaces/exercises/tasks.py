"""Zadania: przestrzenie nazw (namespaces)."""

from collections.abc import Callable


def find_in_legb(local_value: str, enclosing_value: str, global_value: str) -> tuple[str, str, str]:
    """Zwróć wartości odpowiadające poziomom L, E i G."""
    raise NotImplementedError


def merge_symbol_tables(local_table: dict, global_table: dict) -> dict:
    """Scal słowniki symboli; lokalne mają pierwszeństwo przy konflikcie."""
    raise NotImplementedError


def make_call_counter() -> Callable[[], int]:
    """Zwróć funkcję, która przy każdym wywołaniu zwraca kolejną liczbę (1, 2, 3, ...).

    Wskazówka: użyj nonlocal, aby zmodyfikować zmienną z zakresu otaczającego.
    """
    raise NotImplementedError


def is_name_global(name: str, namespace: dict) -> bool:
    """Zwróć True, jeśli 'name' występuje w podanym słowniku namespace (symulacja globals()).

    Przykład:
        is_name_global("VALUE", {"VALUE": 42, "x": 1})  ->  True
        is_name_global("y",     {"VALUE": 42, "x": 1})  ->  False
    """
    raise NotImplementedError


