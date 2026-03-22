"""Rozwiazania: mechanizm importu."""


def classify_spec_origin(origin: str | None) -> str:
    if origin is None:
        return "not-found"
    if origin in {"built-in", "frozen"}:
        return "built-in"
    return "file"


def is_visible_on_path(path_entries: list[str], module_dir: str) -> bool:
    normalized = [entry.rstrip("\\/") for entry in path_entries]
    return module_dir.rstrip("\\/") in normalized

