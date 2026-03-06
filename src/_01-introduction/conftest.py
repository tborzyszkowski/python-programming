"""
conftest.py – konfiguracja pytest dla całego modułu _01-introduction.
Dodaje katalogi examples/ i exercises/ do sys.path, aby testy mogły
importować lokalne moduły bez instalacji pakietu.
"""
import sys
import os

_base = os.path.dirname(__file__)

_dirs = [
    # examples/
    os.path.join(_base, "data-types",     "examples"),
    os.path.join(_base, "mutability",     "examples"),
    os.path.join(_base, "control-flow",   "examples"),
    os.path.join(_base, "running-python", "examples"),
    os.path.join(_base, "interpreters",   "examples"),
    # exercises/
    os.path.join(_base, "interpreters",   "exercises"),
    os.path.join(_base, "running-python", "exercises"),
    os.path.join(_base, "data-types",     "exercises"),
    os.path.join(_base, "mutability",     "exercises"),
    os.path.join(_base, "control-flow",   "exercises"),
]

for _d in _dirs:
    if _d not in sys.path:
        sys.path.insert(0, _d)

