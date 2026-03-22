"""Dynamiczne ladowanie modulu przez importlib."""

from __future__ import annotations

import importlib


def call_transform(module_name: str, value: int) -> int:
    module = importlib.import_module(module_name)
    return int(module.transform(value))


if __name__ == "__main__":
    print(call_transform("plugin_pkg.math_plugin", 7))

