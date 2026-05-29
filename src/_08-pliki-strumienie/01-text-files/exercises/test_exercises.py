"""Zadania do tematu 01 – pliki tekstowe.

Uruchom testy:
    python -m pytest src/_08-pliki-strumienie/01-text-files/exercises/ -v
"""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Import rozwiązań
# ---------------------------------------------------------------------------
from solutions import (
    licz_linie,
    filtruj_linie,
    zamien_slowo,
    statystyki_pliku,
    znajdz_pliki,
    csv_do_slownikow,
)

# ---------------------------------------------------------------------------
# Fixture: tymczasowy katalog z plikami testowymi
# ---------------------------------------------------------------------------
@pytest.fixture()
def tmp_dir(tmp_path: Path) -> Path:
    (tmp_path / "tekst.txt").write_text(
        "Ala ma kota\nKot ma Alę\nAla lubi koty\n",
        encoding="utf-8",
    )
    (tmp_path / "log.txt").write_text(
        "INFO start\nERROR crash\nINFO end\nERROR timeout\n",
        encoding="utf-8",
    )
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "a.txt").write_text("a", encoding="utf-8")
    (sub / "b.csv").write_text("x,y\n1,2\n", encoding="utf-8")
    (tmp_path / "dane.csv").write_text(
        "imie,wiek,ocena\nAnna,20,5\nPiotr,21,4\nMaria,19,5\n",
        encoding="utf-8",
    )
    return tmp_path


# ---------------------------------------------------------------------------
# Testy
# ---------------------------------------------------------------------------
def test_licz_linie(tmp_dir: Path) -> None:
    assert licz_linie(tmp_dir / "tekst.txt") == 3


def test_licz_linie_pusty(tmp_path: Path) -> None:
    p = tmp_path / "pusty.txt"
    p.write_text("", encoding="utf-8")
    assert licz_linie(p) == 0


def test_filtruj_linie(tmp_dir: Path) -> None:
    wynik = filtruj_linie(tmp_dir / "log.txt", "ERROR")
    assert len(wynik) == 2
    assert all("ERROR" in l for l in wynik)


def test_filtruj_linie_brak(tmp_dir: Path) -> None:
    assert filtruj_linie(tmp_dir / "log.txt", "CRITICAL") == []


def test_zamien_slowo(tmp_dir: Path, tmp_path: Path) -> None:
    zrodlo = tmp_dir / "tekst.txt"
    cel = tmp_path / "wynik.txt"
    n = zamien_slowo(zrodlo, cel, "Ala", "Basia")
    assert n == 2
    zawartosc = cel.read_text(encoding="utf-8")
    assert "Ala" not in zawartosc
    assert "Basia" in zawartosc


def test_zamien_slowo_brak(tmp_dir: Path, tmp_path: Path) -> None:
    zrodlo = tmp_dir / "tekst.txt"
    cel = tmp_path / "kopia.txt"
    n = zamien_slowo(zrodlo, cel, "NIEISTNIEJE", "X")
    assert n == 0
    # plik powinien być kopią oryginału
    assert cel.read_text(encoding="utf-8") == zrodlo.read_text(encoding="utf-8")


def test_statystyki_pliku(tmp_dir: Path) -> None:
    stat = statystyki_pliku(tmp_dir / "tekst.txt")
    assert stat["linie"] == 3
    assert stat["slowa"] > 0
    assert stat["znaki"] > 0
    assert "unikalne_slowa" in stat


def test_znajdz_pliki(tmp_dir: Path) -> None:
    txt = znajdz_pliki(tmp_dir, "*.txt")
    assert len(txt) >= 2   # tekst.txt, log.txt, sub/a.txt
    csv_pliki = znajdz_pliki(tmp_dir, "*.csv")
    assert any(p.name == "b.csv" for p in csv_pliki)


def test_csv_do_slownikow(tmp_dir: Path) -> None:
    wiersze = csv_do_slownikow(tmp_dir / "dane.csv")
    assert len(wiersze) == 3
    assert wiersze[0]["imie"] == "Anna"
    assert wiersze[1]["wiek"] == "21"
    assert wiersze[2]["ocena"] == "5"

