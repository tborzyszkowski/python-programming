"""Rozwiazania: pycache i pyc."""


def pyc_filename(module_name: str, tag: str) -> str:
    return f"{module_name}.{tag}.pyc"


def should_recompile(source_mtime: int, pyc_mtime: int) -> bool:
    return source_mtime > pyc_mtime

