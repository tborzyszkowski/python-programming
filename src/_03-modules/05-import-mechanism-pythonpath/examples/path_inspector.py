"""Inspekcja sys.path i PYTHONPATH."""

from __future__ import annotations

import os
import sys


def read_environment() -> dict[str, str]:
    return {
        "PYTHONPATH": os.environ.get("PYTHONPATH", "<not-set>"),
        "first_sys_path": sys.path[0] if sys.path else "<empty>",
    }


def path_contains(fragment: str) -> bool:
    return any(fragment in entry for entry in sys.path)


if __name__ == "__main__":
    print(read_environment())
    print("contains src:", path_contains("src"))

