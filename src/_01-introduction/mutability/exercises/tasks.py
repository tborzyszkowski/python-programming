"""
Zadania – Typy mutowalne i niemutowalne
========================================

Uruchomienie: pytest test_solutions.py -v
"""
import copy  # noqa: F401 – potrzebny w zadaniu 5 (copy.deepcopy)


# ---------------------------------------------------------------------------
# Zadanie 1
# ---------------------------------------------------------------------------
def bezpieczna_aktualizacja(slownik: dict, klucz: str, wartosc) -> dict:
    """
    Zadanie 1: Aktualizacja bez mutacji oryginału
    ----------------------------------------------
    Zwróć NOWY słownik będący kopią `slownik` z dodanym/zaktualizowanym
    kluczem `klucz` o wartości `wartosc`. Oryginalny słownik NIE może
    być zmieniony.

    Przykład:
        d = {"a": 1}
        nowy = bezpieczna_aktualizacja(d, "b", 2)
        # nowy == {"a": 1, "b": 2}
        # d    == {"a": 1}   ← niezmieniony!
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 2
# ---------------------------------------------------------------------------
def usun_duplikaty_zachowujac_kolejnosc(lista: list) -> list:
    """
    Zadanie 2: Usuwanie duplikatów z zachowaniem kolejności
    -------------------------------------------------------
    Zwróć nową listę zawierającą elementy z `lista` bez duplikatów,
    zachowując kolejność pierwszego wystąpienia każdego elementu.

    Nie modyfikuj oryginalnej listy.

    Przykład:
        usun_duplikaty_zachowujac_kolejnosc([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
        # → [3, 1, 4, 5, 9, 2, 6]
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 3
# ---------------------------------------------------------------------------
def rozbuduj_cache(func):
    """
    Zadanie 3: Prosty cache z użyciem słownika (memoizacja)
    --------------------------------------------------------
    Zaimplementuj dekorator, który cachuje wyniki wywołań funkcji `func`.
    Klucz cache to krotka argumentów pozycyjnych.
    Przy powtórnym wywołaniu z tymi samymi argumentami zwróć wynik z cache
    bez ponownego wywołania funkcji.

    Wymaganie: dekorator musi dodać atrybut `.cache` (dict) do zwróconej
    funkcji, umożliwiający inspekcję zawartości cache.

    Przykład:
        @rozbuduj_cache
        def kwadrat(n):
            return n * n

        kwadrat(4)   # → 16  (obliczone)
        kwadrat(4)   # → 16  (z cache)
        kwadrat.cache  # → {(4,): 16}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 4
# ---------------------------------------------------------------------------
def gleboka_aktualizacja(cel: dict, zrodlo: dict) -> dict:
    """
    Zadanie 4: Głęboka aktualizacja słownika
    -----------------------------------------
    Scal rekurencyjnie słownik `zrodlo` do słownika `cel`.
    Jeśli ten sam klucz istnieje w obu słownikach i oba mają wartość będącą
    słownikiem – scal je rekurencyjnie (nie nadpisuj).
    W pozostałych przypadkach wartość ze `zrodlo` nadpisuje wartość z `cel`.
    Operacja MODYFIKUJE `cel` in-place i zwraca go.

    Przykład:
        cel = {"a": 1, "b": {"x": 10, "y": 20}}
        zrodlo = {"b": {"y": 99, "z": 30}, "c": 3}
        gleboka_aktualizacja(cel, zrodlo)
        # → {"a": 1, "b": {"x": 10, "y": 99, "z": 30}, "c": 3}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 5
# ---------------------------------------------------------------------------
def zamroz_strukture(obj):
    """
    Zadanie 5: Zamrożenie mutowalnej struktury
    -------------------------------------------
    Przekształć rekurencyjnie mutowalną strukturę danych na niemutowalną:
        list  → tuple
        dict  → frozenset par (key, value) – tylko gdy wartości są hashowalne
        set   → frozenset
    Inne typy pozostaw bez zmian.

    Przykład:
        zamroz_strukture([1, [2, 3], {4, 5}])
        # → (1, (2, 3), frozenset({4, 5}))

        zamroz_strukture({"a": [1, 2], "b": 3})
        # → frozenset({("a", (1, 2)), ("b", 3)})
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    d = {"a": 1}
    print(bezpieczna_aktualizacja(d, "b", 2), "| oryg:", d)

    print(usun_duplikaty_zachowujac_kolejnosc([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

    @rozbuduj_cache
    def kwadrat(n): return n * n
    print(kwadrat(4), kwadrat(4), kwadrat.cache)

    cel = {"a": 1, "b": {"x": 10, "y": 20}}
    print(gleboka_aktualizacja(cel, {"b": {"y": 99, "z": 30}, "c": 3}))

    print(zamroz_strukture([1, [2, 3], {4, 5}]))

