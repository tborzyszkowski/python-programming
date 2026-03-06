"""
Testy rozwiązań – Instrukcje sterujące
========================================
Uruchomienie: pytest test_solutions.py -v
"""
import pytest
from solutions_control_flow import (
    sito_eratostenesa,
    spasuj_nawiasy,
    generuj_tabliczke_mnozenia,
    grupuj_po_dlugosci,
    interpretuj_wyrazenie,
    fizzbuzz_zaawansowany,
)


class TestSitoEratostenesa:
    def test_do_20(self):
        assert sito_eratostenesa(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_do_2(self):
        assert sito_eratostenesa(2) == [2]

    def test_do_1(self):
        assert sito_eratostenesa(1) == []

    def test_do_0(self):
        assert sito_eratostenesa(0) == []

    def test_50(self):
        wynik = sito_eratostenesa(50)
        assert 47 in wynik
        assert 49 not in wynik  # 49 = 7*7

    def test_wszystkie_pierwsze(self):
        for p in sito_eratostenesa(100):
            assert all(p % i != 0 for i in range(2, p)), f"{p} nie jest pierwsza!"


class TestSpasujNawiasy:
    def test_poprawne_mieszane(self):
        assert spasuj_nawiasy("([{}])") is True

    def test_niepoprawna_kolejnosc(self):
        assert spasuj_nawiasy("([)]") is False

    def test_niezamkniety(self):
        assert spasuj_nawiasy("{[") is False

    def test_pusty_napis(self):
        assert spasuj_nawiasy("") is True

    def test_bez_nawiasow(self):
        assert spasuj_nawiasy("abc 123") is True

    def test_same_zamykajace(self):
        assert spasuj_nawiasy(")") is False

    def test_zagniezdzony(self):
        assert spasuj_nawiasy("{[()]}") is True

    def test_kod_python(self):
        assert spasuj_nawiasy("if (x > 0): print(x)") is True


class TestGenerujTabliczkeMnozenia:
    def test_rozmiar(self):
        m = generuj_tabliczke_mnozenia(5)
        assert len(m) == 5
        assert all(len(w) == 5 for w in m)

    def test_wartosci_3x3(self):
        assert generuj_tabliczke_mnozenia(3) == [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9],
        ]

    def test_przekatna(self):
        n = 4
        m = generuj_tabliczke_mnozenia(n)
        for i in range(n):
            assert m[i][i] == (i + 1) ** 2

    def test_symetria(self):
        m = generuj_tabliczke_mnozenia(5)
        for i in range(5):
            for j in range(5):
                assert m[i][j] == m[j][i]


class TestGrupujPoDlugosci:
    def test_podstawowy(self):
        wynik = grupuj_po_dlugosci(["kot", "pies", "lis", "ryba", "osa"])
        assert wynik == {3: ["kot", "lis", "osa"], 4: ["pies", "ryba"]}

    def test_posortowane_slowa(self):
        wynik = grupuj_po_dlugosci(["banan", "arbuz", "chleb"])
        assert wynik[5] == ["arbuz", "banan", "chleb"]

    def test_jedna_grupa(self):
        assert grupuj_po_dlugosci(["ab", "cd"]) == {2: ["ab", "cd"]}

    def test_pusta_lista(self):
        assert grupuj_po_dlugosci([]) == {}

    def test_posortowane_klucze(self):
        wynik = grupuj_po_dlugosci(["a", "bb", "ccc", "dd"])
        assert list(wynik.keys()) == sorted(wynik.keys())


class TestInterpretujWyrazenie:
    def test_dodawanie(self):
        assert interpretuj_wyrazenie("3 4 +") == 7.0

    def test_zlozone(self):
        assert interpretuj_wyrazenie("5 1 2 + 4 * + 3 -") == 14.0

    def test_mnozenie_i_dodawanie(self):
        assert interpretuj_wyrazenie("2 3 * 4 +") == 10.0

    def test_odejmowanie(self):
        assert interpretuj_wyrazenie("10 3 -") == 7.0

    def test_dzielenie(self):
        assert abs(interpretuj_wyrazenie("10 4 /") - 2.5) < 1e-9

    def test_dzielenie_przez_zero(self):
        with pytest.raises(ValueError):
            interpretuj_wyrazenie("5 0 /")

    def test_liczba_zmiennoprzecinkowa(self):
        assert abs(interpretuj_wyrazenie("1.5 2.5 +") - 4.0) < 1e-9


class TestFizzbuzzZaawansowany:
    def test_klasyczny_15(self):
        wynik = fizzbuzz_zaawansowany(15, {3: "Fizz", 5: "Buzz"})
        assert wynik[0] == "1"
        assert wynik[2] == "Fizz"    # 3
        assert wynik[4] == "Buzz"    # 5
        assert wynik[14] == "FizzBuzz"  # 15

    def test_bez_dopasowania(self):
        wynik = fizzbuzz_zaawansowany(5, {7: "Seven"})
        assert wynik == ["1", "2", "3", "4", "5"]

    def test_trzy_zasady(self):
        wynik = fizzbuzz_zaawansowany(30, {3: "Fizz", 5: "Buzz", 7: "Bazz"})
        assert wynik[20] == "FizzBazz"   # 21 = 3*7 → FizzBazz
        assert wynik[4]  == "Buzz"       # 5  = 5   → Buzz
        assert wynik[14] == "FizzBuzz"   # 15 = 3*5 → FizzBuzz

    def test_dlugosc(self):
        assert len(fizzbuzz_zaawansowany(10, {3: "Fizz"})) == 10

    def test_pusta_zasady(self):
        wynik = fizzbuzz_zaawansowany(3, {})
        assert wynik == ["1", "2", "3"]



