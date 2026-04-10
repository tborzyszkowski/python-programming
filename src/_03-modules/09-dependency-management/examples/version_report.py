"""Raportuje wersje wybranych pakietów."""

from __future__ import annotations

import importlib.metadata


def read_version(distribution: str) -> str:
    try:
        return importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        return "not-installed"


if __name__ == "__main__":
    for pkg in ["pytest", "plantuml", "pip"]:
        print(pkg, read_version(pkg))

