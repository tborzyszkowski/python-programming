"""
Zadania – Podstawowe typy danych
=================================

Uruchomienie: pytest test_solutions.py -v
"""
from decimal import Decimal  # noqa: F401 – potrzebny w zadaniu 6


# ---------------------------------------------------------------------------
# Zadanie 1
# ---------------------------------------------------------------------------
def statystyki(liczby: list[float]) -> dict:
    """
    Zadanie 1: Statystyki numeryczne
    ---------------------------------
    Dla niepustej listy liczb zwróć słownik z kluczami:
        "min"     – wartość minimalna
        "max"     – wartość maksymalna
        "suma"    – suma wszystkich wartości
        "srednia" – średnia arytmetyczna (float)
        "zakres"  – różnica max - min

    Nie używaj zewnętrznych bibliotek (tylko wbudowane funkcje Pythona).
    Rzuć ValueError gdy lista jest pusta.

    Przykład:
        statystyki([1, 2, 3, 4, 5])
        # → {"min": 1, "max": 5, "suma": 15, "srednia": 3.0, "zakres": 4}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 2
# ---------------------------------------------------------------------------
def analizuj_napis(tekst: str) -> dict:
    """
    Zadanie 2: Analiza napisu
    --------------------------
    Dla podanego napisu `tekst` zwróć słownik z kluczami:
        "dlugosc"       – liczba znaków (int)
        "slowa"         – lista słów (po podziale na spacje/whitespace) (list[str])
        "liczba_slow"   – liczba słów (int)
        "unikalne_znaki"– zbiór unikalnych liter (lowercase, bez spacji i znaków
                         interpunkcyjnych) (set[str])
        "czy_palindrom" – True jeśli napis (po usunięciu spacji, lowercase)
                         jest palindromem (bool)

    Przykład:
        analizuj_napis("Ala ma kota")
        # → {"dlugosc": 11, "slowa": ["Ala","ma","kota"],
        #    "liczba_slow": 3, "unikalne_znaki": {"a","l","m","k","o","t"},
        #    "czy_palindrom": False}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 3
# ---------------------------------------------------------------------------
def zlicz_wystapienia(sekwencja: list) -> dict:
    """
    Zadanie 3: Zliczanie wystąpień
    --------------------------------
    Zwróć słownik mapujący każdy unikalny element listy `sekwencja`
    na liczbę jego wystąpień. Wynik posortuj malejąco wg wartości (liczby wystąpień),
    przy remisach zachowując kolejność alphabetyczną kluczy.

    Nie używaj collections.Counter.

    Przykład:
        zlicz_wystapienia(["a","b","a","c","b","a"])
        # → {"a": 3, "b": 2, "c": 1}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 4
# ---------------------------------------------------------------------------
def zbuduj_macierz(wiersze: int, kolumny: int, wartosc=0) -> list[list]:
    """
    Zadanie 4: Macierz 2D bez pułapki mutowalności
    ------------------------------------------------
    Zbuduj i zwróć macierz (listę list) o wymiarach wiersze × kolumny,
    wypełnioną wartością `wartosc`.

    UWAGA: Popularne, ale BŁĘDNE podejście to:
        [[wartosc] * kolumny] * wiersze   ← wszystkie wiersze to ten sam obiekt!

    Twoja implementacja musi tworzyć NIEZALEŻNE wiersze – modyfikacja
    jednego wiersza nie powinna wpływać na inne.

    Przykład:
        m = zbuduj_macierz(2, 3)
        # → [[0, 0, 0], [0, 0, 0]]
        m[0][0] = 99
        m[1][0]  # musi być nadal 0
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 5
# ---------------------------------------------------------------------------
def operacje_na_zbiorach(lista_a: list, lista_b: list) -> dict:
    """
    Zadanie 5: Teoria zbiorów
    --------------------------
    Dla dwóch list zwróć słownik z kluczami:
        "suma"          – elementy w A lub B (list, posortowana)
        "czesc_wspolna" – elementy w A i B (list, posortowana)
        "roznica_a_b"   – elementy w A, których nie ma w B (list, posortowana)
        "roznica_sym"   – elementy w dokładnie jednej z list (list, posortowana)
        "czy_rozlaczne" – True jeśli A i B nie mają wspólnych elementów (bool)

    Przykład:
        operacje_na_zbiorach([1,2,3,4], [3,4,5,6])
        # → {"suma": [1,2,3,4,5,6], "czesc_wspolna": [3,4],
        #    "roznica_a_b": [1,2], "roznica_sym": [1,2,5,6],
        #    "czy_rozlaczne": False}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 6
# ---------------------------------------------------------------------------
def konwersja_walut(kwota: str, kurs: str) -> str:
    """
    Zadanie 6: Precyzyjne obliczenia finansowe
    -------------------------------------------
    Używając typu Decimal (NIE float!), przelicz `kwota` (str reprezentujący
    liczbę dziesiętną, np. "19.99") przez `kurs` (str, np. "4.2137")
    i zwróć wynik zaokrąglony do 2 miejsc po przecinku jako str.

    Przykład:
        konwersja_walut("19.99", "4.2137")  # → "84.27"

    Wskazówka:
        from decimal import Decimal, ROUND_HALF_UP
        Decimal("...").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(statystyki([1, 2, 3, 4, 5]))
    print(analizuj_napis("Kayak"))
    print(zlicz_wystapienia(["a", "b", "a", "c", "b", "a"]))
    m = zbuduj_macierz(3, 3)
    m[0][0] = 99
    print("macierz:", m, "  m[1][0]:", m[1][0])
    print(operacje_na_zbiorach([1, 2, 3, 4], [3, 4, 5, 6]))
    print(konwersja_walut("19.99", "4.2137"))

