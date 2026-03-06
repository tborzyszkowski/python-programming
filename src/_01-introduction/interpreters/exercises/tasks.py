"""
Zadania – Kompilatory i interpretery
=====================================

Uruchomienie zadań (sprawdzenie czy kod się wykonuje):
    python tasks.py

Uruchomienie testów rozwiązań:
    pytest test_solutions.py -v

Każde zadanie to funkcja z docstringiem opisującym co należy zaimplementować.
Uzupełnij ciało funkcji zastępując `raise NotImplementedError(...)`.
"""
import dis       # noqa: F401 – potrzebny w zadaniach 1 i 4
import sys       # noqa: F401 – potrzebny w zadaniach 2 i 3


# ---------------------------------------------------------------------------
# Zadanie 1
# ---------------------------------------------------------------------------
def policz_instrukcje_bajtkodu(func) -> int:
    """
    Zadanie 1: Analiza bajtkodu
    ---------------------------
    Korzystając z modułu `dis`, zlicz i zwróć liczbę unikalnych nazw
    instrukcji bajtkodowych (opname) w podanej funkcji `func`.

    Wskazówka:
        dis.get_instructions(func)  zwraca iterator obiektów Instruction.
        Każdy obiekt ma atrybut .opname (str).

    Przykład:
        def add(a, b): return a + b
        policz_instrukcje_bajtkodu(add)  # → liczba unikalnych opname, np. 3
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 2
# ---------------------------------------------------------------------------
def czy_cpython() -> bool:
    """
    Zadanie 2: Wykrywanie implementacji
    ------------------------------------
    Zwróć True jeśli bieżący interpreter to CPython, False w przeciwnym razie.

    Wskazówka: sys.implementation.name
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 3
# ---------------------------------------------------------------------------
def wersja_pythona() -> tuple[int, int, int]:
    """
    Zadanie 3: Wersja interpretera
    ------------------------------
    Zwróć krotkę (major, minor, micro) bieżącej wersji Pythona.

    Przykład: Python 3.11.2 → (3, 11, 2)

    Wskazówka: sys.version_info
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 4
# ---------------------------------------------------------------------------
def znajdz_stale_w_bajtkodzie(func) -> list[object]:
    """
    Zadanie 4: Stałe w bajtkodzie
    ------------------------------
    Zwróć listę wszystkich wartości stałych (argval) ładowanych instrukcją
    LOAD_CONST z bajtkodu funkcji `func`. Zachowaj kolejność wystąpień,
    ale usuń duplikaty (zachowując pierwsze wystąpienie każdej wartości).

    Przykład:
        def f(): return 42 + 42 + 0
        znajdz_stale_w_bajtkodzie(f)  # → [42, 0]  (None z RETURN pomijamy)

    Wskazówka:
        Filtruj instrukcje z opname == 'LOAD_CONST'.
        None jest automatycznie dodawane jako stała przez kompilator – wyklucz go.
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 5
# ---------------------------------------------------------------------------
def kompiluj_i_wykonaj(kod: str, zmienne: dict) -> dict:
    """
    Zadanie 5: Dynamiczna kompilacja kodu
    --------------------------------------
    Skompiluj podany łańcuch `kod` za pomocą wbudowanej funkcji `compile()`,
    a następnie wykonaj go przez `exec()` w kontekście słownika `zmienne`.
    Zwróć słownik `zmienne` po wykonaniu (będzie zawierał zdefiniowane nazwy).

    Przykład:
        wynik = kompiluj_i_wykonaj("x = 2 ** 8", {})
        wynik["x"]  # → 256

    Wskazówka:
        compile(kod, "<string>", "exec")  – tryb "exec" dla wielu instrukcji.
        exec(code_obj, zmienne)
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Szybki test ręczny – uruchom aby sprawdzić swoje rozwiązania
    def przyklad(a, b):
        return a + b

    print("Zadanie 1:", policz_instrukcje_bajtkodu(przyklad))
    print("Zadanie 2:", czy_cpython())
    print("Zadanie 3:", wersja_pythona())
    print("Zadanie 4:", znajdz_stale_w_bajtkodzie(lambda: 1 + 2 + 1))
    print("Zadanie 5:", kompiluj_i_wykonaj("wynik = 6 * 7", {}))

