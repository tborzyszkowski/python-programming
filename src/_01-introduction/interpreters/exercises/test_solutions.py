"""
Testy rozwiązań – Kompilatory i interpretery
=============================================
Uruchomienie: pytest test_solutions.py -v
"""
import sys
import pytest
from solutions_interpreters import (
    policz_instrukcje_bajtkodu,
    czy_cpython,
    wersja_pythona,
    znajdz_stale_w_bajtkodzie,
    kompiluj_i_wykonaj,
)


class TestPoliczInstrukcje:
    def test_prosta_funkcja(self):
        def f(a, b): return a + b
        assert policz_instrukcje_bajtkodu(f) >= 2

    def test_wynik_int(self):
        def f(): pass
        assert isinstance(policz_instrukcje_bajtkodu(f), int)

    def test_wieksza_liczba_dla_zlozonej(self):
        def prosta(x): return x
        def zlożona(x, y, z): return (x + y) * z - x // y
        assert policz_instrukcje_bajtkodu(zlożona) >= policz_instrukcje_bajtkodu(prosta)


class TestCzyCPython:
    def test_zwraca_bool(self):
        assert isinstance(czy_cpython(), bool)

    def test_zgodnosc_z_sys(self):
        oczekiwane = sys.implementation.name == "cpython"
        assert czy_cpython() == oczekiwane


class TestWersjaPythona:
    def test_krotka_trzech_elementow(self):
        v = wersja_pythona()
        assert isinstance(v, tuple)
        assert len(v) == 3

    def test_major_to_3(self):
        major, minor, micro = wersja_pythona()
        assert major == 3

    def test_minor_wiekszy_zero(self):
        _, minor, _ = wersja_pythona()
        assert minor >= 0

    def test_zgodnosc_z_sys(self):
        vi = sys.version_info
        assert wersja_pythona() == (vi.major, vi.minor, vi.micro)


class TestZnajdzStale:
    def test_prosta_stala(self):
        # Stała jako bezpośredni literał w return – nie jest foldowana
        def f():
            x = 42
            return x
        stale = znajdz_stale_w_bajtkodzie(f)
        assert 42 in stale

    def test_brak_none(self):
        def f():
            x = 1
            return x
        assert None not in znajdz_stale_w_bajtkodzie(f)

    def test_unikalne(self):
        # Dwie osobne przypisania tej samej stałej – powinna pojawić się raz
        def f():
            a = 7
            b = 7
            return a + b
        stale = znajdz_stale_w_bajtkodzie(f)
        assert stale.count(7) == 1

    def test_wiele_stalych(self):
        # Stałe jako osobne przypisania – nie będą foldowane
        def f():
            a = 1
            b = 2
            c = 3
            return a + b + c
        stale = znajdz_stale_w_bajtkodzie(f)
        for v in [1, 2, 3]:
            assert v in stale


class TestKompilujIWykonaj:
    def test_prosta_zmienna(self):
        wynik = kompiluj_i_wykonaj("x = 2 ** 8", {})
        assert wynik["x"] == 256

    def test_kilka_instrukcji(self):
        kod = "a = 10\nb = 20\nc = a + b"
        wynik = kompiluj_i_wykonaj(kod, {})
        assert wynik["c"] == 30

    def test_istniejacy_kontekst(self):
        zmienne = {"pi": 3.14159}
        kompiluj_i_wykonaj("r = pi * 2", zmienne)
        assert abs(zmienne["r"] - 6.28318) < 1e-4

    def test_zwraca_dict(self):
        wynik = kompiluj_i_wykonaj("x = 1", {})
        assert isinstance(wynik, dict)


