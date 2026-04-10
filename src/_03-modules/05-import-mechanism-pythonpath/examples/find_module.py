"""Wyszukiwanie informacji o module przez importlib."""

from __future__ import annotations

import importlib.util


def find_module_origin(module_name: str) -> str | None:
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        return None
    return spec.origin


if __name__ == "__main__":
    print(find_module_origin("json"))

