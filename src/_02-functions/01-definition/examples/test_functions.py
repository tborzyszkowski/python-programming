"""
Testy jednostkowe dla funkcji w module 01-definition.
Uruchomienie: pytest
"""

import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from basic_functions import powitaj, oblicz_pole_trojkata


def test_powitaj():
    assert powitaj("Anna", 25) == "Witaj, Anna! Masz 25 lat."


def test_powitaj_default():
    assert powitaj("Bartek") == "Witaj, Bartek! Masz 18 lat."


def test_oblicz_pole():
    assert oblicz_pole_trojkata(10.0, 5.0) == 25.0
    assert oblicz_pole_trojkata(0, 5) == 0.0

