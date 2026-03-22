"""Zadania: pycache i pyc."""


def pyc_filename(module_name: str, tag: str) -> str:
    """Zbuduj nazwe jak dla module.cpython-313.pyc."""
    raise NotImplementedError


def should_recompile(source_mtime: int, pyc_mtime: int) -> bool:
    """Zwroc True gdy zrodlo jest nowsze od cache."""
    raise NotImplementedError

