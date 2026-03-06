"""
Testy jednostkowe dla modułów data-types.
Uruchomienie: pytest tests/ -v
"""
import math
from decimal import Decimal
from fractions import Fraction


# ── TESTY LICZB ────────────────────────────────────────────────────────────────

class TestInt:
    def test_duza_liczba(self):
        assert 10 ** 100 > 10 ** 99

    def test_dzielenie_calkowite(self):
        assert 17 // 5 == 3

    def test_modulo(self):
        assert 17 % 5 == 2

    def test_potegowanie(self):
        assert 2 ** 10 == 1024

    def test_systemy_zapisu(self):
        assert 0xFF == 255
        assert 0o17 == 15
        assert 0b1010 == 10


class TestFloat:
    def test_blad_reprezentacji(self):
        # 0.1 + 0.2 NIE jest równe 0.3 w float
        assert 0.1 + 0.2 != 0.3

    def test_isclose(self):
        assert math.isclose(0.1 + 0.2, 0.3)

    def test_inf(self):
        assert float('inf') > 1e308
        assert math.isinf(float('inf'))

    def test_nan(self):
        nan = float('nan')
        assert math.isnan(nan)
        # NaN != NaN – właściwość IEEE 754
        assert nan != nan


class TestDecimal:
    def test_dokladnosc(self):
        assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")

    def test_fraction(self):
        assert Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)


# ── TESTY NAPISÓW ──────────────────────────────────────────────────────────────

class TestStr:
    def test_indeksowanie(self):
        s = "Python"
        assert s[0] == "P"
        assert s[-1] == "n"

    def test_wycinek(self):
        s = "Python"
        assert s[1:4] == "yth"
        assert s[::-1] == "nohtyP"

    def test_konkatenacja(self):
        assert "Py" + "thon" == "Python"

    def test_powtarzanie(self):
        assert "ha" * 3 == "hahaha"

    def test_metody(self):
        assert "  hello  ".strip() == "hello"
        assert "hello".upper() == "HELLO"
        assert "HELLO".lower() == "hello"
        assert "hello world".title() == "Hello World"
        assert "a,b,c".split(",") == ["a", "b", "c"]
        assert ",".join(["a", "b", "c"]) == "a,b,c"
        assert "hello".replace("l", "r") == "herro"

    def test_fstring(self):
        imie = "Python"
        assert f"Witaj, {imie}!" == "Witaj, Python!"

    def test_niezmiennikosc(self):
        s = "abc"
        try:
            s[0] = "X"  # type: ignore
            assert False, "Powinien rzucić TypeError"
        except TypeError:
            pass


# ── TESTY KOLEKCJI ─────────────────────────────────────────────────────────────

class TestList:
    def test_append(self):
        lst = [1, 2, 3]
        lst.append(4)
        assert lst == [1, 2, 3, 4]

    def test_insert(self):
        lst = [1, 3]
        lst.insert(1, 2)
        assert lst == [1, 2, 3]

    def test_remove(self):
        lst = [1, 2, 3]
        lst.remove(2)
        assert lst == [1, 3]

    def test_pop(self):
        lst = [1, 2, 3]
        val = lst.pop()
        assert val == 3
        assert lst == [1, 2]

    def test_sort(self):
        lst = [3, 1, 2]
        lst.sort()
        assert lst == [1, 2, 3]

    def test_comprehension(self):
        kwadraty = [x ** 2 for x in range(1, 6)]
        assert kwadraty == [1, 4, 9, 16, 25]

    def test_mutowalnosc(self):
        lst = [1, 2, 3]
        lst[0] = 99
        assert lst[0] == 99


class TestTuple:
    def test_dostep(self):
        t = (1, 2, 3)
        assert t[0] == 1
        assert t[-1] == 3

    def test_niezmiennikosc(self):
        t = (1, 2, 3)
        try:
            t[0] = 99  # type: ignore
            assert False, "Powinien rzucić TypeError"
        except TypeError:
            pass

    def test_rozpakowywanie(self):
        x, y = (3, 4)
        assert x == 3 and y == 4

    def test_jeden_element(self):
        t = (42,)
        assert len(t) == 1
        assert isinstance(t, tuple)

    def test_extended_unpacking(self):
        pierwszy, *srodek, ostatni = (1, 2, 3, 4, 5)
        assert pierwszy == 1
        assert srodek == [2, 3, 4]
        assert ostatni == 5


class TestDict:
    def test_dostep(self):
        d = {"a": 1, "b": 2}
        assert d["a"] == 1

    def test_get_default(self):
        d = {"a": 1}
        assert d.get("brak", 99) == 99

    def test_dodawanie(self):
        d = {}
        d["klucz"] = "wartość"
        assert "klucz" in d

    def test_usuwanie(self):
        d = {"a": 1, "b": 2}
        del d["a"]
        assert "a" not in d

    def test_comprehension(self):
        kwadraty = {x: x ** 2 for x in range(1, 4)}
        assert kwadraty == {1: 1, 2: 4, 3: 9}

    def test_scalanie(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        scalony = d1 | d2
        assert scalony == {"a": 1, "b": 2}


class TestSet:
    def test_unikalne(self):
        s = {1, 2, 2, 3, 3}
        assert s == {1, 2, 3}

    def test_operacje(self):
        s1 = {1, 2, 3}
        s2 = {2, 3, 4}
        assert s1 | s2 == {1, 2, 3, 4}
        assert s1 & s2 == {2, 3}
        assert s1 - s2 == {1}
        assert s1 ^ s2 == {1, 4}

    def test_add_discard(self):
        s = {1, 2}
        s.add(3)
        assert 3 in s
        s.discard(999)  # nie rzuca błędu
        assert 999 not in s

    def test_frozenset_hashable(self):
        fs = frozenset({1, 2})
        d = {fs: "wartość"}
        assert d[fs] == "wartość"

