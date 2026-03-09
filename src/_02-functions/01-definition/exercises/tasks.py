"""Zadania: definicja funkcji.

Uzupełnij implementacje funkcji poniżej.
"""


def normalizuj_imie(imie: str) -> str:
    """Zwraca imię z wielką literą i bez spacji z początku/końca.

    Przykład: "  aNNa " -> "Anna"
    """
    raise NotImplementedError("Zaimplementuj normalizuj_imie")


def bezpieczne_dzielenie(a: float, b: float, domyslna: float | None = None) -> float | None:
    """Dzieli a przez b.

    Jeśli b == 0, zwraca domyslna (a gdy domyslna jest None, zwraca None).
    """
    raise NotImplementedError("Zaimplementuj bezpieczne_dzielenie")


def policz_srednia(oceny: list[float]) -> float:
    """Zwraca średnią ocen.

    Dla pustej listy rzuć ValueError.
    """
    raise NotImplementedError("Zaimplementuj policz_srednia")


def opisz_studenta(imie: str, indeks: int, kierunek: str = "Informatyka") -> str:
    """Zwraca opis studenta jako jeden napis.

    Format: "Student <imie> (nr <indeks>) - <kierunek>"
    """
    raise NotImplementedError("Zaimplementuj opisz_studenta")


def wyznacz_range(liczby: list[int]) -> tuple[int, int, int]:
    """Zwraca (min, max, zakres=max-min).

    Dla pustej listy rzuć ValueError.
    """
    raise NotImplementedError("Zaimplementuj wyznacz_range")

