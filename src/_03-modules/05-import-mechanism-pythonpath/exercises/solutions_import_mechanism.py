"""Rozwiązania: mechanizm importu."""


def classify_spec_origin(origin: str | None) -> str:
    if origin is None:
        return "not-found"
    if origin in {"built-in", "frozen"}:
        return "built-in"
    return "file"


def is_visible_on_path(path_entries: list[str], module_dir: str) -> bool:
    normalized = [entry.rstrip("\\/") for entry in path_entries]
    return module_dir.rstrip("\\/") in normalized


def diagnose_import_error(module_name: str, sys_path: list[str], sys_modules: dict) -> str:
    if module_name in sys_modules:
        return "cached"
    if any("site-packages" in entry for entry in sys_path):
        return "found"
    return "not-found"

