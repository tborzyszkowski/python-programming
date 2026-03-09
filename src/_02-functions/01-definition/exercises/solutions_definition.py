"""Przykładowe rozwiązania: definicja funkcji."""


def normalizuj_imie(imie: str) -> str:
    return imie.strip().capitalize()


def bezpieczne_dzielenie(a: float, b: float, domyslna: float | None = None) -> float | None:
    if b == 0:
        return domyslna
    return a / b


def policz_srednia(oceny: list[float]) -> float:
    if not oceny:
        raise ValueError("Lista ocen nie może być pusta")
    return sum(oceny) / len(oceny)


def opisz_studenta(imie: str, indeks: int, kierunek: str = "Informatyka") -> str:
    return f"Student {imie} (nr {indeks}) - {kierunek}"


def wyznacz_range(liczby: list[int]) -> tuple[int, int, int]:
    if not liczby:
        raise ValueError("Lista liczb nie może być pusta")
    minimum = min(liczby)
    maksimum = max(liczby)
    return (minimum, maksimum, maksimum - minimum)

