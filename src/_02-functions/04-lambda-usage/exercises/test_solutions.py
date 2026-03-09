import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_lambda_usage import (
    agreguj_kwoty,
    filtruj_transakcje,
    mapuj_kwoty_brutto,
    ranking_studentow,
    sortuj_produkty,
)


PRODUKTY = [
    {"nazwa": "Mysz", "cena": 80},
    {"nazwa": "Laptop", "cena": 4200},
    {"nazwa": "Klawiatura", "cena": 250},
]

TRANSAKCJE = [
    {"id": 1, "kwota": 100.0},
    {"id": 2, "kwota": 250.0},
    {"id": 3, "kwota": 80.0},
]

STUDENCI = [
    {"imie": "Ala", "srednia": 4.5},
    {"imie": "Bartek", "srednia": 3.8},
    {"imie": "Celina", "srednia": 4.9},
]


def test_sortuj_produkty():
    out = sortuj_produkty(PRODUKTY, "cena")
    assert [p["nazwa"] for p in out] == ["Mysz", "Klawiatura", "Laptop"]


def test_filtruj_transakcje():
    out = filtruj_transakcje(TRANSAKCJE, 100.0)
    assert [t["id"] for t in out] == [1, 2]


def test_mapuj_kwoty_brutto():
    out = mapuj_kwoty_brutto(TRANSAKCJE, vat=0.23)
    assert out == [123.0, 307.5, 98.4]


def test_agreguj_kwoty():
    assert agreguj_kwoty(TRANSAKCJE) == 430.0


def test_ranking_studentow():
    assert ranking_studentow(STUDENCI) == ["Celina", "Ala", "Bartek"]
