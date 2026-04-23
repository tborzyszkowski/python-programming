"""Duck typing w Pythonie – historia i przykłady.

"Jeśli chodzi jak kaczka i kwacze jak kaczka, to jest kaczką."
                                    – James Whitcomb Riley (XIX w.)

W Pythonie nie sprawdzamy TYPU obiektu – sprawdzamy, czy obiekt ma
odpowiednie METODY i ATRYBUTY.  To duck typing.
"""
from __future__ import annotations

import io
import math
from typing import Protocol


# ---------------------------------------------------------------------------
# 1. Klasyczny przykład: „kaczka" i „człowiek" bez wspólnej klasy bazowej
# ---------------------------------------------------------------------------

class Duck:
    def quack(self) -> str:
        return "Quack!"

    def walk(self) -> str:
        return "Kaczka idzie: kwa, kwa…"


class Person:
    def quack(self) -> str:
        return "Jestem człowiekiem, ale potrafię kwakać!"

    def walk(self) -> str:
        return "Człowiek idzie: krok, krok…"


class RubberDuck:
    """Gumowa kaczka – też 'kwacze'."""

    def quack(self) -> str:
        return "Piiiip!"


def make_it_quack(obj) -> None:
    """Funkcja nie pyta o typ – pyta o umiejętność kwakania."""
    print(obj.quack())


# ---------------------------------------------------------------------------
# 2. Duck typing z wbudowanymi protokołami: __len__, __iter__
# ---------------------------------------------------------------------------

class NumberRange:
    """Własny zakres liczb – implementuje __len__ i __iter__."""

    def __init__(self, start: int, stop: int) -> None:
        self._start = start
        self._stop = stop

    def __len__(self) -> int:
        return max(0, self._stop - self._start)

    def __iter__(self):
        current = self._start
        while current < self._stop:
            yield current
            current += 1

    def __contains__(self, item: int) -> bool:
        return self._start <= item < self._stop


# ---------------------------------------------------------------------------
# 3. Duck typing z plikami – cokolwiek ma .write() działa jak plik
# ---------------------------------------------------------------------------

def save_report(dest, data: list[str]) -> None:
    """Zapisuje raport do *dowolnego* obiektu z metodą write()."""
    for line in data:
        dest.write(line + "\n")


# ---------------------------------------------------------------------------
# 4. Polimorfizm bez dziedziczenia – wzorzec Strategy przez duck typing
# ---------------------------------------------------------------------------

class BubbleSorter:
    """Sortuje bąbelkowo."""

    def sort(self, data: list) -> list:
        lst = list(data)
        n = len(lst)
        for i in range(n):
            for j in range(n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst


class QuickSorter:
    """Sortuje quicksortem."""

    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return list(data)
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)


class PythonBuiltinSorter:
    """Deleguje do sorted()."""

    def sort(self, data: list) -> list:
        return sorted(data)


def process_data(sorter, data: list) -> list:
    """Nie obchodzi nas typ sortera – wystarczy, że ma metodę sort()."""
    return sorter.sort(data)


# ---------------------------------------------------------------------------
# 5. Typing Protocol – formalna definicja „kaczego kontraktu" (Python 3.8+)
# ---------------------------------------------------------------------------

class Drawable(Protocol):
    """Każdy obiekt z metodą draw() spełnia ten protokół."""

    def draw(self) -> str: ...


class SVGCircle:
    def __init__(self, cx: float, cy: float, r: float) -> None:
        self.cx, self.cy, self.r = cx, cy, r

    def draw(self) -> str:
        return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}"/>'


class TerminalBox:
    def __init__(self, w: int, h: int) -> None:
        self.w, self.h = w, h

    def draw(self) -> str:
        top = "+" + "-" * self.w + "+"
        mid = "|" + " " * self.w + "|"
        return "\n".join([top] + [mid] * self.h + [top])


def render_all(drawables: list[Drawable]) -> None:
    for d in drawables:
        print(d.draw())
        print()


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("1. Klasyczny duck typing – kwakanie")
    print("=" * 60)
    for obj in [Duck(), Person(), RubberDuck()]:
        make_it_quack(obj)

    print()
    print("=" * 60)
    print("2. Własna kolekcja – __len__, __iter__, __contains__")
    print("=" * 60)
    r = NumberRange(5, 10)
    print(f"len(r) = {len(r)}")
    print(f"list(r) = {list(r)}")
    print(f"7 in r = {7 in r}")
    print(f"sum(r) = {sum(r)}")     # sum() używa __iter__ – duck typing!

    print()
    print("=" * 60)
    print("3. save_report – plik i bufor w pamięci")
    print("=" * 60)
    # Zapis do pliku w pamięci (StringIO) – zachowuje się jak plik
    buf = io.StringIO()
    save_report(buf, ["Linia 1", "Linia 2", "Linia 3"])
    print("Zawartość bufora:")
    print(buf.getvalue())

    print("=" * 60)
    print("4. Duck typing – Strategy bez dziedziczenia")
    print("=" * 60)
    data = [5, 2, 9, 1, 7, 3]
    for sorter in [BubbleSorter(), QuickSorter(), PythonBuiltinSorter()]:
        result = process_data(sorter, data)
        print(f"{type(sorter).__name__:25s}: {result}")

    print()
    print("=" * 60)
    print("5. Protocol (Drawable) – formalne duck typing")
    print("=" * 60)
    drawables: list[Drawable] = [
        SVGCircle(50, 50, 30),
        TerminalBox(10, 2),
    ]
    render_all(drawables)


if __name__ == "__main__":
    main()

