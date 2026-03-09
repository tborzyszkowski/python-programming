import pathlib
import sys
import pytest

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_arguments import (
    policz_statystyki,
    polacz_konfiguracje,
    skaluj_wyniki,
    wywolaj_funkcje,
    zbuduj_url,
)


def test_policz_statystyki():
    out = policz_statystyki(1, 2, 3)
    assert out["min"] == 1
    assert out["max"] == 3
    assert out["suma"] == 6
    assert out["srednia"] == 2
    with pytest.raises(ValueError):
        policz_statystyki()


def test_zbuduj_url():
    assert zbuduj_url("https://x.pl") == "https://x.pl"
    assert zbuduj_url("https://x.pl", q="py", page=2) == "https://x.pl?q=py&page=2"


def test_skaluj_wyniki():
    assert skaluj_wyniki(1, 2, 3) == [2, 4, 6]
    assert skaluj_wyniki(1, 2, 3, mnoznik=3) == [3, 6, 9]


def test_polacz_konfiguracje():
    cfg = polacz_konfiguracje(timeout=10, debug=True)
    assert cfg["timeout"] == 10
    assert cfg["debug"] is True
    assert cfg["retries"] == 3


def test_wywolaj_funkcje():
    def add(a, b):
        return a + b

    assert wywolaj_funkcje(add, 2, 5) == 7
