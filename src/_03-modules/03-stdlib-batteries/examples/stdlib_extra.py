"""Dodatkowe przykłady z biblioteki standardowej: datetime, pathlib, functools."""

from datetime import datetime, timedelta
from functools import lru_cache
from pathlib import Path


# ── datetime ──────────────────────────────────────────────────────

def dni_do_daty(rok: int, miesiac: int, dzien: int) -> int:
    """Oblicza liczbę dni od dziś do podanej daty."""
    cel = datetime(rok, miesiac, dzien)
    roznica = cel - datetime.now()
    return roznica.days


def formatuj_date(dt: datetime, fmt: str = "%Y-%m-%d %H:%M") -> str:
    """Formatuje datę do czytelnego napisu."""
    return dt.strftime(fmt)


def daty_tygodnia() -> list[str]:
    """Zwraca daty kolejnych 7 dni od dziś."""
    dzis = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    return [formatuj_date(dzis + timedelta(days=i), "%Y-%m-%d") for i in range(7)]


# ── pathlib ───────────────────────────────────────────────────────

def znajdz_pliki_py(katalog: str) -> list[str]:
    """Znajduje rekursywnie wszystkie pliki .py w katalogu."""
    return sorted(str(p) for p in Path(katalog).rglob("*.py"))


def informacje_o_pliku(sciezka: str) -> dict[str, str]:
    """Zwraca podstawowe informacje o pliku."""
    p = Path(sciezka)
    return {
        "nazwa": p.name,
        "rozszerzenie": p.suffix,
        "katalog": str(p.parent),
        "istnieje": str(p.exists()),
        "rozmiar_bajtow": str(p.stat().st_size) if p.exists() else "N/A",
    }


# ── functools.lru_cache ──────────────────────────────────────────

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """Oblicza n-ty wyraz ciągu Fibonacciego z pamięcią podręczną."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("=== datetime ===")
    print(f"Dni do Nowego Roku: {dni_do_daty(2027, 1, 1)}")
    print(f"Teraz: {formatuj_date(datetime.now())}")
    print(f"Kolejne 7 dni: {daty_tygodnia()}")

    print("\n=== pathlib ===")
    print(f"Info o tym pliku: {informacje_o_pliku(__file__)}")

    print("\n=== functools.lru_cache ===")
    for i in [10, 20, 30, 40]:
        print(f"fibonacci({i}) = {fibonacci(i)}")
    print(f"Cache info: {fibonacci.cache_info()}")

