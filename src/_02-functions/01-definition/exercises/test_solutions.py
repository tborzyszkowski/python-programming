import pathlib
import sys

import pytest

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_definition import (
    bezpieczne_dzielenie,
    normalizuj_imie,
    opisz_studenta,
    policz_srednia,
    wyznacz_range,
)


def test_normalizuj_imie():
    assert normalizuj_imie("  aNNa ") == "Anna"


def test_bezpieczne_dzielenie():
    assert bezpieczne_dzielenie(10, 2) == 5
    assert bezpieczne_dzielenie(10, 0) is None
    assert bezpieczne_dzielenie(10, 0, -1) == -1


def test_policz_srednia():
    assert policz_srednia([3, 4, 5]) == 4
    with pytest.raises(ValueError):
        policz_srednia([])


def test_opisz_studenta():
    assert opisz_studenta("Ala", 12345) == "Student Ala (nr 12345) - Informatyka"


def test_wyznacz_range():
    assert wyznacz_range([4, 10, -2]) == (-2, 10, 12)
    with pytest.raises(ValueError):
        wyznacz_range([])
