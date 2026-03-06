"""
Wzorcowe rozwiązania – Podstawowe typy danych
=============================================
"""
from decimal import Decimal, ROUND_HALF_UP


def statystyki(liczby: list[float]) -> dict:
    if not liczby:
        raise ValueError("Lista nie może być pusta")
    return {
        "min":     min(liczby),
        "max":     max(liczby),
        "suma":    sum(liczby),
        "srednia": sum(liczby) / len(liczby),
        "zakres":  max(liczby) - min(liczby),
    }


def analizuj_napis(tekst: str) -> dict:
    slowa = tekst.split()
    # unikalne litery: tylko a-z (po lowercase), bez spacji i interpunkcji
    unikalne = {ch for ch in tekst.lower() if ch.isalpha()}
    # palindrom: porównaj z odwróconą wersją (bez spacji, lowercase)
    oczyszczony = "".join(ch for ch in tekst.lower() if ch.isalpha())
    return {
        "dlugosc":        len(tekst),
        "slowa":          slowa,
        "liczba_slow":    len(slowa),
        "unikalne_znaki": unikalne,
        "czy_palindrom":  oczyszczony == oczyszczony[::-1],
    }


def zlicz_wystapienia(sekwencja: list) -> dict:
    licznik: dict = {}
    for elem in sekwencja:
        licznik[elem] = licznik.get(elem, 0) + 1
    # sortuj: malejąco wg wartości, rosnąco wg klucza przy remisach
    return dict(sorted(licznik.items(), key=lambda kv: (-kv[1], str(kv[0]))))


def zbuduj_macierz(wiersze: int, kolumny: int, wartosc=0) -> list[list]:
    # list comprehension tworzy NOWY wiersz w każdej iteracji
    return [[wartosc] * kolumny for _ in range(wiersze)]


def operacje_na_zbiorach(lista_a: list, lista_b: list) -> dict:
    a, b = set(lista_a), set(lista_b)
    return {
        "suma":          sorted(a | b),
        "czesc_wspolna": sorted(a & b),
        "roznica_a_b":   sorted(a - b),
        "roznica_sym":   sorted(a ^ b),
        "czy_rozlaczne": a.isdisjoint(b),
    }


def konwersja_walut(kwota: str, kurs: str) -> str:
    wynik = Decimal(kwota) * Decimal(kurs)
    zaokraglony = wynik.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return str(zaokraglony)


if __name__ == "__main__":
    print(statystyki([1, 2, 3, 4, 5]))
    print(analizuj_napis("Kayak"))
    print(zlicz_wystapienia(["a", "b", "a", "c", "b", "a"]))
    m = zbuduj_macierz(3, 3)
    m[0][0] = 99
    print("macierz:", m, "  m[1][0]:", m[1][0])
    print(operacje_na_zbiorach([1, 2, 3, 4], [3, 4, 5, 6]))
    print(konwersja_walut("19.99", "4.2137"))

