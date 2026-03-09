"""Zadania: argumenty pozycyjne, nazwane, *args, **kwargs."""


def policz_statystyki(*args: float) -> dict:
    """Zwraca słownik: min, max, suma, srednia.

    Dla braku argumentów rzuć ValueError.
    """
    raise NotImplementedError("Zaimplementuj policz_statystyki")


def zbuduj_url(base: str, **query) -> str:
    """Buduje URL z parametrami query.

    Przykład:
    zbuduj_url("https://x.pl", a=1, q="python")
    -> "https://x.pl?a=1&q=python"
    """
    raise NotImplementedError("Zaimplementuj zbuduj_url")


def skaluj_wyniki(*args: int, mnoznik: int = 2) -> list[int]:
    """Zwraca listę elementów args przemnożonych przez mnoznik."""
    raise NotImplementedError("Zaimplementuj skaluj_wyniki")


def polacz_konfiguracje(**kwargs) -> dict:
    """Zwraca nowy słownik konfiguracji z domyślnymi wartościami.

    Domyślne pola:
    {"debug": False, "timeout": 30, "retries": 3}
    """
    raise NotImplementedError("Zaimplementuj polacz_konfiguracje")


def wywolaj_funkcje(func, *args, **kwargs):
    """Wywołuje przekazaną funkcję z argumentami i zwraca wynik."""
    raise NotImplementedError("Zaimplementuj wywolaj_funkcje")

