"""Demonstracja kompilacji do .pyc."""

from __future__ import annotations

import pathlib
import py_compile


def compile_file(path: str) -> pathlib.Path:
    source = pathlib.Path(path)
    py_compile.compile(str(source), cfile=None, doraise=True)
    cache_dir = source.parent / "__pycache__"
    candidates = sorted(cache_dir.glob(f"{source.stem}*.pyc"))
    if not candidates:
        raise FileNotFoundError("Nie znaleziono pliku .pyc")
    return candidates[-1]


if __name__ == "__main__":
    print(compile_file(__file__))

