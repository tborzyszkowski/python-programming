"""Narzędzia do inspekcji __pycache__."""

from __future__ import annotations

import pathlib


def list_pyc_files(directory: str) -> list[str]:
    base = pathlib.Path(directory)
    return sorted(str(path) for path in base.rglob("*.pyc"))


if __name__ == "__main__":
    for item in list_pyc_files(pathlib.Path(__file__).resolve().parent.as_posix()):
        print(item)

