"""Zadania: mechanizm importu."""


def classify_spec_origin(origin: str | None) -> str:
    """Zwroc not-found/built-in/file."""
    raise NotImplementedError


def is_visible_on_path(path_entries: list[str], module_dir: str) -> bool:
    """Sprawdz czy katalog modulu jest widoczny na sys.path."""
    raise NotImplementedError

