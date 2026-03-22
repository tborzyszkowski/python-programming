"""Konfiguracja testow dla modulu _03-modules."""

from __future__ import annotations

import pathlib
import sys

BASE_DIR = pathlib.Path(__file__).resolve().parent


def _inject_topic_paths() -> None:
    """Dodaje katalogi topic/exercises i topic/examples do sys.path."""
    for topic_dir in BASE_DIR.iterdir():
        if not topic_dir.is_dir() or not topic_dir.name[:2].isdigit():
            continue
        for sub in ("exercises", "examples"):
            candidate = topic_dir / sub
            if candidate.is_dir():
                path_value = str(candidate)
                if path_value not in sys.path:
                    sys.path.insert(0, path_value)


_inject_topic_paths()
