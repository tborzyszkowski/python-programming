import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_lambda import (
    curry_add,
    kompozycja,
    mapuj_i_filtruj,
    stworz_mnoznik,
    zastosuj,
)


def test_zastosuj():
    assert zastosuj(lambda x: x + 1, 10) == 11


def test_stworz_mnoznik():
    razy_3 = stworz_mnoznik(3)
    assert razy_3(7) == 21


def test_kompozycja():
    f = lambda x: x + 1
    g = lambda x: x * 2
    h = kompozycja(f, g)
    assert h(5) == 11


def test_curry_add():
    add10 = curry_add(10)
    assert add10(4) == 14


def test_mapuj_i_filtruj():
    out = mapuj_i_filtruj([1, 2, 3, 4], lambda x: x * x, lambda y: y > 5)
    assert out == [9, 16]
