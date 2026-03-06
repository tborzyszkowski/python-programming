"""
Testy rozwiązań – Typy mutowalne i niemutowalne
================================================
Uruchomienie: pytest test_solutions.py -v
"""
import pytest
from solutions_mutability import (
    bezpieczna_aktualizacja,
    usun_duplikaty_zachowujac_kolejnosc,
    rozbuduj_cache,
    gleboka_aktualizacja,
    zamroz_strukture,
)


class TestBezpiecznaAktualizacja:
    def test_dodaje_klucz(self):
        wynik = bezpieczna_aktualizacja({"a": 1}, "b", 2)
        assert wynik == {"a": 1, "b": 2}

    def test_oryginal_niezmieniony(self):
        d = {"a": 1}
        bezpieczna_aktualizacja(d, "b", 2)
        assert d == {"a": 1}

    def test_aktualizuje_istniejacy(self):
        wynik = bezpieczna_aktualizacja({"a": 1, "b": 0}, "b", 99)
        assert wynik["b"] == 99

    def test_nowy_obiekt(self):
        d = {"a": 1}
        assert bezpieczna_aktualizacja(d, "b", 2) is not d


class TestUsunDuplikaty:
    def test_podstawowy(self):
        wynik = usun_duplikaty_zachowujac_kolejnosc([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
        assert wynik == [3, 1, 4, 5, 9, 2, 6]

    def test_bez_duplikatow(self):
        assert usun_duplikaty_zachowujac_kolejnosc([1, 2, 3]) == [1, 2, 3]

    def test_wszystkie_takie_same(self):
        assert usun_duplikaty_zachowujac_kolejnosc([7, 7, 7]) == [7]

    def test_pusta_lista(self):
        assert usun_duplikaty_zachowujac_kolejnosc([]) == []

    def test_oryginal_niezmieniony(self):
        lista = [1, 2, 1]
        usun_duplikaty_zachowujac_kolejnosc(lista)
        assert lista == [1, 2, 1]


class TestRozbudujCache:
    def test_poprawny_wynik(self):
        @rozbuduj_cache
        def kwadrat(n): return n * n
        assert kwadrat(5) == 25

    def test_cache_uzywany(self):
        licznik = [0]

        @rozbuduj_cache
        def f(x):
            licznik[0] += 1
            return x * 2

        f(3)
        f(3)
        assert licznik[0] == 1, "Funkcja powinna być wywołana tylko raz"

    def test_atrybut_cache(self):
        @rozbuduj_cache
        def g(x): return x
        g(10)
        assert hasattr(g, "cache")
        assert (10,) in g.cache

    def test_rozne_argumenty(self):
        @rozbuduj_cache
        def h(x): return x ** 2
        assert h(3) == 9
        assert h(4) == 16
        assert len(h.cache) == 2


class TestGleebokaAktualizacja:
    def test_podstawowy(self):
        cel = {"a": 1, "b": {"x": 10, "y": 20}}
        gleboka_aktualizacja(cel, {"b": {"y": 99, "z": 30}, "c": 3})
        assert cel == {"a": 1, "b": {"x": 10, "y": 99, "z": 30}, "c": 3}

    def test_nie_nadpisuje_slownika(self):
        cel = {"sub": {"a": 1, "b": 2}}
        gleboka_aktualizacja(cel, {"sub": {"b": 99}})
        assert cel["sub"]["a"] == 1  # ocalało

    def test_nowy_klucz(self):
        cel = {"a": 1}
        gleboka_aktualizacja(cel, {"b": 2})
        assert cel["b"] == 2

    def test_nadpisuje_nie_slownik(self):
        cel = {"a": [1, 2, 3]}
        gleboka_aktualizacja(cel, {"a": [4, 5]})
        assert cel["a"] == [4, 5]

    def test_zwraca_cel(self):
        cel = {"x": 1}
        wynik = gleboka_aktualizacja(cel, {"y": 2})
        assert wynik is cel


class TestZamrozStrukture:
    def test_lista_na_tuple(self):
        assert zamroz_strukture([1, 2, 3]) == (1, 2, 3)

    def test_zagniezdzona_lista(self):
        assert zamroz_strukture([1, [2, 3]]) == (1, (2, 3))

    def test_set_na_frozenset(self):
        wynik = zamroz_strukture({1, 2, 3})
        assert isinstance(wynik, frozenset)
        assert wynik == frozenset({1, 2, 3})

    def test_dict_na_frozenset(self):
        wynik = zamroz_strukture({"a": 1, "b": 2})
        assert isinstance(wynik, frozenset)
        assert ("a", 1) in wynik

    def test_wartosc_prosta(self):
        assert zamroz_strukture(42) == 42
        assert zamroz_strukture("hello") == "hello"

    def test_wynik_jest_hashable(self):
        wynik = zamroz_strukture([1, [2, 3], {4, 5}])
        # Jeśli wynik jest krotką niemutowalnych obiektów, powinna być hashowalna
        assert hash(wynik) is not None


