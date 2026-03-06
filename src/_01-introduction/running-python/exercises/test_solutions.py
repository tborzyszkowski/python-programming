"""
Testy rozwiązań – Sposoby uruchamiania kodu w Pythonie
======================================================
Uruchomienie: pytest test_solutions.py -v
"""
import sys
import pytest
from solutions_running_python import (
    info_o_module,
    lazy_import,
    uruchom_kod_jako_modul,
    znajdz_modul_w_sys_path,
    lista_modulow_z_prefiksem,
)


class TestInfoOModule:
    def test_klucze(self):
        wynik = info_o_module("math")
        assert set(wynik.keys()) == {"nazwa", "plik", "pakiet", "atrybuty"}

    def test_nazwa(self):
        assert info_o_module("math")["nazwa"] == "math"

    def test_atrybuty_dodatnie(self):
        assert info_o_module("math")["atrybuty"] > 0

    def test_os_ma_plik(self):
        plik = info_o_module("os")["plik"]
        assert plik is not None
        assert plik.endswith(".py")

    def test_sys_wbudowany(self):
        # sys jest modułem wbudowanym – __file__ może być None
        wynik = info_o_module("sys")
        assert wynik["nazwa"] == "sys"


class TestLazyImport:
    def test_zwraca_modul(self):
        import math
        assert lazy_import("math") is math

    def test_nie_importuje_ponownie(self):
        import os
        modul = lazy_import("os")
        assert modul is sys.modules["os"]

    def test_importuje_nowy(self):
        # fractions może nie być załadowany
        modul = lazy_import("fractions")
        assert modul is not None
        assert hasattr(modul, "Fraction")


class TestUruchomKodJakoModul:
    def test_zmienna(self):
        ns = uruchom_kod_jako_modul("x = 6 * 7")
        assert ns["x"] == 42

    def test_funkcja(self):
        ns = uruchom_kod_jako_modul("def podwoj(n): return n * 2")
        assert ns["podwoj"](5) == 10

    def test_wiele_instrukcji(self):
        kod = "a = 3\nb = 4\nc = (a**2 + b**2) ** 0.5"
        ns = uruchom_kod_jako_modul(kod)
        assert abs(ns["c"] - 5.0) < 1e-9

    def test_zwraca_dict(self):
        assert isinstance(uruchom_kod_jako_modul("x=1"), dict)


class TestZnajdzModulWSysPath:
    def test_os_py_istnieje(self):
        wynik = znajdz_modul_w_sys_path("os.py")
        assert wynik is not None
        assert wynik.endswith("os.py")

    def test_nieistniejacy(self):
        assert znajdz_modul_w_sys_path("_xxxxnieistnieje_xyz.py") is None

    def test_zwraca_string_lub_none(self):
        wynik = znajdz_modul_w_sys_path("os.py")
        assert isinstance(wynik, str)


class TestListaModulowZPrefiksem:
    def test_sys_jest_na_liscie(self):
        lista = lista_modulow_z_prefiksem("sys")
        assert "sys" in lista

    def test_os_jest_na_liscie(self):
        import os, os.path  # noqa: E401 – upewniamy się, że załadowany
        lista = lista_modulow_z_prefiksem("os")
        assert "os" in lista

    def test_posortowana(self):
        lista = lista_modulow_z_prefiksem("os")
        assert lista == sorted(lista)

    def test_brak_none_modulow(self):
        lista = lista_modulow_z_prefiksem("")
        # żadna wartość nie powinna być None (sys.modules może mieć None)
        for name in lista:
            assert sys.modules[name] is not None


