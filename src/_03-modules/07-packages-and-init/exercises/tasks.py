"""Zadania: pakiety i __init__.py."""


def package_public_api(all_list: list[str]) -> tuple[str, ...]:
    """Zamień listę __all__ na niemutowalną krotkę."""
    raise NotImplementedError


def is_namespace_package(has_init_file: bool) -> bool:
    """Zwróć True, gdy katalog może być namespace package."""
    raise NotImplementedError


def build_init_content(public_names: list[str], module_name: str) -> str:
    """Wygeneruj zawartość pliku __init__.py importującego podane nazwy z modułu.

    Przykład:
        build_init_content(["add", "mean"], "math_ops")
        ->  'from .math_ops import add, mean\\n\\n__all__ = ["add", "mean"]\\n'
    """
    raise NotImplementedError


def resolve_import_path(package_parts: list[str], module_name: str) -> str:
    """Zbuduj pełną ścieżkę importu z listy części pakietu i nazwy modułu.

    Przykład:
        resolve_import_path(["school", "core"], "grade_model")
        ->  "school.core.grade_model"
        resolve_import_path([], "utils")
        ->  "utils"
    """
    raise NotImplementedError
