"""
Testy jednostkowe dla instrukcji sterujących w Pythonie 3.
Uruchomienie: pytest tests/ -v
"""


class TestWarunki:
    def test_if_dodatnia(self):
        x = 5
        wynik = "dodatnia" if x > 0 else ("zero" if x == 0 else "ujemna")
        assert wynik == "dodatnia"

    def test_if_ujemna(self):
        x = -3
        wynik = "dodatnia" if x > 0 else ("zero" if x == 0 else "ujemna")
        assert wynik == "ujemna"

    def test_if_zero(self):
        x = 0
        wynik = "dodatnia" if x > 0 else ("zero" if x == 0 else "ujemna")
        assert wynik == "zero"

    def test_lancuchowanie_porownania(self):
        assert 1 < 5 < 10
        assert not (1 < 15 < 10)

    def test_falsy_values(self):
        falsy = [False, 0, 0.0, 0j, "", [], {}, set(), (), None]
        for v in falsy:
            assert not v, f"{v!r} powinno być falsy"

    def test_truthy_values(self):
        truthy = [True, 1, -1, 0.001, "x", [0], {0: 0}, {0}, (0,)]
        for v in truthy:
            assert v, f"{v!r} powinno być truthy"


class TestForLoop:
    def test_sum_range(self):
        total = sum(i for i in range(1, 6))
        assert total == 15

    def test_enumerate(self):
        wyniki = [(i, v) for i, v in enumerate(["a", "b", "c"], start=1)]
        assert wyniki == [(1, "a"), (2, "b"), (3, "c")]

    def test_zip(self):
        wyniki = list(zip([1, 2, 3], ["a", "b", "c"]))
        assert wyniki == [(1, "a"), (2, "b"), (3, "c")]

    def test_break(self):
        znalezione = None
        for i in [1, 3, 5, 8, 11]:
            if i % 2 == 0:
                znalezione = i
                break
        assert znalezione == 8

    def test_continue(self):
        wynik = []
        for i in range(5):
            if i % 2 == 0:
                continue
            wynik.append(i)
        assert wynik == [1, 3]

    def test_else_bez_break(self):
        """Blok else pętli for wykonuje się gdy nie było break."""
        wykonano_else = False
        for i in range(3):
            pass
        else:
            wykonano_else = True
        assert wykonano_else

    def test_else_z_break(self):
        """Blok else NIE wykonuje się gdy był break."""
        wykonano_else = False
        for i in range(5):
            if i == 2:
                break
        else:
            wykonano_else = True
        assert not wykonano_else


class TestWhileLoop:
    def test_podstawowy(self):
        wyniki = []
        i = 0
        while i < 5:
            wyniki.append(i)
            i += 1
        assert wyniki == [0, 1, 2, 3, 4]

    def test_break(self):
        i = 0
        wyniki = []
        while True:
            if i >= 3:
                break
            wyniki.append(i)
            i += 1
        assert wyniki == [0, 1, 2]

    def test_else_bez_break(self):
        n = 3
        wykonano_else = False
        while n > 0:
            n -= 1
        else:
            wykonano_else = True
        assert wykonano_else


class TestComprehensions:
    def test_list_kwadraty(self):
        kwadraty = [x ** 2 for x in range(1, 6)]
        assert kwadraty == [1, 4, 9, 16, 25]

    def test_list_filtr(self):
        parzyste = [x for x in range(10) if x % 2 == 0]
        assert parzyste == [0, 2, 4, 6, 8]

    def test_dict_comprehension(self):
        kwadraty = {x: x ** 2 for x in range(1, 4)}
        assert kwadraty == {1: 1, 2: 4, 3: 9}

    def test_set_comprehension(self):
        uniq = {x % 3 for x in range(10)}
        assert uniq == {0, 1, 2}

    def test_generator_expression(self):
        # Generator nie tworzy listy – oblicza leniwie
        gen = (x ** 2 for x in range(5))
        assert list(gen) == [0, 1, 4, 9, 16]

    def test_flatten(self):
        nested = [[1, 2], [3, 4], [5]]
        flat = [x for sub in nested for x in sub]
        assert flat == [1, 2, 3, 4, 5]


class TestMatchCase:
    @staticmethod
    def klasyfikuj_punkt(punkt):
        match punkt:
            case (0, 0):
                return "środek"
            case (x, 0):
                return f"oś X, x={x}"
            case (0, y):
                return f"oś Y, y={y}"
            case (x, y):
                return f"ogólny ({x}, {y})"

    def test_srodek(self):
        assert self.klasyfikuj_punkt((0, 0)) == "środek"

    def test_os_x(self):
        assert self.klasyfikuj_punkt((3, 0)) == "oś X, x=3"

    def test_os_y(self):
        assert self.klasyfikuj_punkt((0, -4)) == "oś Y, y=-4"

    def test_ogolny(self):
        assert self.klasyfikuj_punkt((2, 5)) == "ogólny (2, 5)"


