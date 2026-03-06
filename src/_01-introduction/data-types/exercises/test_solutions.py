"""
Testy rozwiązań – Podstawowe typy danych
=========================================
Uruchomienie: pytest test_solutions.py -v
"""
import pytest
from solutions_data_types import (
    statystyki,
    analizuj_napis,
    zlicz_wystapienia,
    zbuduj_macierz,
    operacje_na_zbiorach,
    konwersja_walut,
)


class TestStatystyki:
    def test_podstawowe(self):
        w = statystyki([1, 2, 3, 4, 5])
        assert w["min"] == 1
        assert w["max"] == 5
        assert w["suma"] == 15
        assert w["srednia"] == 3.0
        assert w["zakres"] == 4

    def test_jeden_element(self):
        w = statystyki([7])
        assert w["min"] == w["max"] == 7
        assert w["zakres"] == 0

    def test_ujemne(self):
        w = statystyki([-3, -1, 0, 2])
        assert w["min"] == -3
        assert w["max"] == 2
        assert w["suma"] == -2

    def test_pusta_lista_blad(self):
        with pytest.raises(ValueError):
            statystyki([])

    def test_srednia_float(self):
        w = statystyki([1, 2])
        assert isinstance(w["srednia"], float)
        assert w["srednia"] == 1.5


class TestAnalizujNapis:
    def test_dlugosc(self):
        assert analizuj_napis("Python")["dlugosc"] == 6

    def test_slowa(self):
        assert analizuj_napis("Ala ma kota")["slowa"] == ["Ala", "ma", "kota"]

    def test_liczba_slow(self):
        assert analizuj_napis("jeden dwa trzy")["liczba_slow"] == 3

    def test_palindrom_true(self):
        assert analizuj_napis("kayak")["czy_palindrom"] is True

    def test_palindrom_ze_spacjami(self):
        assert analizuj_napis("A man a plan a canal Panama")["czy_palindrom"] is True

    def test_palindrom_false(self):
        assert analizuj_napis("Python")["czy_palindrom"] is False

    def test_unikalne_znaki_typ(self):
        assert isinstance(analizuj_napis("abc")["unikalne_znaki"], set)

    def test_unikalne_znaki_wartosc(self):
        assert analizuj_napis("aabbcc")["unikalne_znaki"] == {"a", "b", "c"}


class TestZliczWystapienia:
    def test_podstawowy(self):
        wynik = zlicz_wystapienia(["a", "b", "a", "c", "b", "a"])
        assert wynik == {"a": 3, "b": 2, "c": 1}

    def test_posortowany_malejaco(self):
        wynik = zlicz_wystapienia([1, 1, 2, 2, 2, 3])
        klucze = list(wynik.keys())
        assert klucze[0] == 2  # najczęstszy

    def test_jeden_element(self):
        assert zlicz_wystapienia(["x"]) == {"x": 1}

    def test_pusta_lista(self):
        assert zlicz_wystapienia([]) == {}

    def test_liczby(self):
        wynik = zlicz_wystapienia([5, 5, 3])
        assert wynik[5] == 2
        assert wynik[3] == 1


class TestZbudujMacierz:
    def test_wymiary(self):
        m = zbuduj_macierz(3, 4)
        assert len(m) == 3
        assert all(len(w) == 4 for w in m)

    def test_domyslna_wartosc(self):
        m = zbuduj_macierz(2, 2)
        assert m[0][0] == 0

    def test_niestandardowa_wartosc(self):
        m = zbuduj_macierz(2, 2, wartosc=9)
        assert m[1][1] == 9

    def test_niezalezne_wiersze(self):
        m = zbuduj_macierz(3, 3)
        m[0][0] = 99
        assert m[1][0] == 0, "Wiersze są wspóldzielone! Użyj list comprehension."
        assert m[2][0] == 0

    def test_typ(self):
        m = zbuduj_macierz(2, 2)
        assert isinstance(m, list)
        assert isinstance(m[0], list)


class TestOperacjeNaZbiorach:
    def test_suma(self):
        w = operacje_na_zbiorach([1, 2, 3], [3, 4, 5])
        assert w["suma"] == [1, 2, 3, 4, 5]

    def test_czesc_wspolna(self):
        w = operacje_na_zbiorach([1, 2, 3, 4], [3, 4, 5, 6])
        assert w["czesc_wspolna"] == [3, 4]

    def test_roznica(self):
        w = operacje_na_zbiorach([1, 2, 3, 4], [3, 4, 5, 6])
        assert w["roznica_a_b"] == [1, 2]

    def test_roznica_symetryczna(self):
        w = operacje_na_zbiorach([1, 2, 3, 4], [3, 4, 5, 6])
        assert w["roznica_sym"] == [1, 2, 5, 6]

    def test_rozlaczne(self):
        w = operacje_na_zbiorach([1, 2], [3, 4])
        assert w["czy_rozlaczne"] is True

    def test_nie_rozlaczne(self):
        w = operacje_na_zbiorach([1, 2, 3], [3, 4])
        assert w["czy_rozlaczne"] is False


class TestKonwersjaWalut:
    def test_podstawowe(self):
        # 19.99 * 4.2137 = 84.231...  → zaokrąglone ROUND_HALF_UP → 84.23
        assert konwersja_walut("19.99", "4.2137") == "84.23"

    def test_wiekszy_kurs(self):
        # 100.00 * 4.2500 = 425.00
        assert konwersja_walut("100.00", "4.2500") == "425.00"

    def test_jeden(self):
        assert konwersja_walut("1.00", "1.00") == "1.00"

    def test_zaokraglenie(self):
        # 1.005 * 1 = 1.005 → zaokrąglone ROUND_HALF_UP → 1.01
        assert konwersja_walut("1.005", "1") == "1.01"

    def test_zwraca_str(self):
        assert isinstance(konwersja_walut("10.00", "2.00"), str)

    def test_dokladnosc_vs_float(self):
        # test pokazuje przewagę Decimal nad float
        wynik_float = 0.1 * 3        # 0.30000000000000004
        wynik_decimal = konwersja_walut("0.10", "3")
        assert wynik_decimal == "0.30"
        assert wynik_float != 0.30


