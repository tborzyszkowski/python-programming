"""Zadania: zaawansowane importy."""


def detect_circular_hint(message: str) -> bool:
    """Zwróć True, gdy komunikat sugeruje partially initialized module."""
    raise NotImplementedError


def exported_by_star(all_list: list[str], symbol: str) -> bool:
    """Sprawdź, czy symbol będzie wyeksportowany przez import *."""
    raise NotImplementedError


def validate_plugin_name(name: str, allowed: set[str]) -> bool:
    """Sprawdź, czy nazwa pluginu jest dozwolona do dynamicznego importu.

    Zwróć True, jeśli nazwa jest w zbiorze dozwolonych nazw.
    Porównanie case-sensitive.

    Przykład:
        validate_plugin_name("math_plugin", {"math_plugin", "text_plugin"})  ->  True
        validate_plugin_name("evil_module", {"math_plugin", "text_plugin"})  ->  False
    """
    raise NotImplementedError


def suggest_fix_for_circular(module_a: str, module_b: str) -> str:
    """Zaproponuj nazwę trzeciego modułu do wydzielenia wspólnej logiki.

    Zwróć nazwę w formacie '{a}_{b}_common' (oba lowercase, posortowane alfabetycznie).

    Przykład:
        suggest_fix_for_circular("orders", "inventory")
        ->  "inventory_orders_common"
        suggest_fix_for_circular("B", "A")
        ->  "a_b_common"
    """
    raise NotImplementedError
