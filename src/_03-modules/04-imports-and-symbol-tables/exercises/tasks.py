"""Zadania: importy i tablice symboli."""


def import_style_result(value: float) -> float:
    """Oblicz pierwiastek przez import modułowy."""
    raise NotImplementedError


def symbol_lifetime() -> tuple[bool, bool]:
    """Zwróć (czy_lokalna_w_locals, czy_globalna_w_globals)."""
    raise NotImplementedError


def detect_builtin_shadowing(names: list[str]) -> list[str]:
    """Wykryj nazwy, które przesłaniają wbudowane builtiny.

    Sprawdź, czy nazwy z listy istnieją w module builtins.
    Zwróć te, które kolidują (są zarazem w builtins i na liście).

    Przykład:
        detect_builtin_shadowing(["list", "x", "sum", "my_var"])  ->  ["list", "sum"]
    """
    raise NotImplementedError


def categorize_name_origin(name: str, local_ns: dict, global_ns: dict) -> str:
    """Określ, skąd pochodzi nazwa: 'local', 'global' lub 'builtin-or-missing'.

    Sprawdzaj w kolejności: local → global → reszta.

    Przykład:
        categorize_name_origin("x", {"x": 1}, {"y": 2})  ->  "local"
        categorize_name_origin("y", {"x": 1}, {"y": 2})  ->  "global"
        categorize_name_origin("z", {"x": 1}, {"y": 2})  ->  "builtin-or-missing"
    """
    raise NotImplementedError

