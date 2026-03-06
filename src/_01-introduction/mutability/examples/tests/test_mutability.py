"""
Testy jednostkowe dla tematu mutability.
Uruchomienie: pytest tests/ -v
"""
import copy


class TestNiemutowalnosc:
    def test_str_nowy_obiekt_przy_konkatenacji(self):
        s = "hello"
        id_przed = id(s)
        s += " world"
        # id powinno się zmienić – nowy obiekt
        assert s == "hello world"
        # (id może, ale nie musi być różne w CPython REPL, ale wartość musi być nowa)

    def test_str_nie_mozna_modyfikowac(self):
        s = "abc"
        try:
            s[0] = "X"  # type: ignore
            assert False, "Powinien rzucić TypeError"
        except TypeError:
            pass

    def test_tuple_nie_mozna_modyfikowac(self):
        t = (1, 2, 3)
        try:
            t[0] = 99  # type: ignore
            assert False, "Powinien rzucić TypeError"
        except TypeError:
            pass

    def test_int_internowanie(self):
        # Małe int (-5..256) są internowane w CPython
        a = 100
        b = 100
        assert a is b

    def test_frozenset_nie_mozna_modyfikowac(self):
        fs = frozenset({1, 2, 3})
        try:
            fs.add(4)  # type: ignore
            assert False, "Powinien rzucić AttributeError"
        except AttributeError:
            pass


class TestMutowalnosc:
    def test_lista_in_place(self):
        lst = [1, 2, 3]
        id_przed = id(lst)
        lst.append(4)
        assert id(lst) == id_przed  # ten sam obiekt
        assert lst == [1, 2, 3, 4]

    def test_wspoldzielenie_referencji(self):
        a = [1, 2, 3]
        b = a   # ta sama referencja
        b.append(4)
        assert a == [1, 2, 3, 4]  # a też się zmieniło!
        assert a is b

    def test_kopia_plytka(self):
        a = [1, 2, 3]
        b = a.copy()
        b.append(4)
        assert a == [1, 2, 3]   # a niezmienione
        assert a is not b

    def test_kopia_gleboka_zagniezdzenia(self):
        oryginal = [[1, 2], [3, 4]]
        plytka = oryginal.copy()
        gleboka = copy.deepcopy(oryginal)

        oryginal[0].append(99)

        # Płytka kopia "widzi" zmianę w zagnieżdżonej liście
        assert plytka[0] == [1, 2, 99]

        # Głęboka kopia jest niezależna
        assert gleboka[0] == [1, 2]

    def test_dict_wspoldzielenie(self):
        d = {"a": 1}
        ref = d
        ref["b"] = 2
        assert d == {"a": 1, "b": 2}

    def test_dict_kopia(self):
        d = {"a": 1}
        kopia = d.copy()
        kopia["b"] = 2
        assert "b" not in d

    def test_set_in_place(self):
        s = {1, 2, 3}
        id_przed = id(s)
        s.add(4)
        assert id(s) == id_przed
        assert 4 in s


class TestPulapkaDomyslnyArgument:
    def test_none_jako_domyslny_argument(self):
        """Poprawny wzorzec: None zamiast mutowalnego obiektu."""

        def dodaj(element, lista=None):
            if lista is None:
                lista = []
            lista.append(element)
            return lista

        wynik1 = dodaj(1)
        wynik2 = dodaj(2)
        wynik3 = dodaj(3)

        assert wynik1 == [1]
        assert wynik2 == [2]   # nie [1, 2]!
        assert wynik3 == [3]


class TestHashowalnosc:
    def test_tuple_jako_klucz(self):
        d = {(1, 2): "wartość"}
        assert d[(1, 2)] == "wartość"

    def test_lista_nie_jest_hashowalna(self):
        try:
            d = {[1, 2]: "wartość"}  # type: ignore
            assert False, "Powinien rzucić TypeError"
        except TypeError:
            pass

    def test_frozenset_jako_klucz(self):
        fs = frozenset({1, 2})
        d = {fs: "ok"}
        assert d[fs] == "ok"

