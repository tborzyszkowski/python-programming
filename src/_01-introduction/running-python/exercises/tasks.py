"""
Zadania – Sposoby uruchamiania kodu w Pythonie
===============================================

Uruchomienie: pytest test_solutions.py -v
"""
import sys               # noqa: F401 – potrzebny w zadaniach 2, 4, 5
import importlib         # noqa: F401 – potrzebny w zadaniach 1 i 2
import importlib.util    # noqa: F401 – potrzebny w zadaniu 4


# ---------------------------------------------------------------------------
# Zadanie 1
# ---------------------------------------------------------------------------
def info_o_module(nazwa_modulu: str) -> dict:
    """
    Zadanie 1: Introspekcja modułu
    --------------------------------
    Dla podanej nazwy modułu ze standardowej biblioteki (np. "os", "sys", "math")
    zwróć słownik z następującymi kluczami:
        "nazwa"    – nazwa modułu (str)
        "plik"     – ścieżka do pliku źródłowego lub None jeśli wbudowany (str | None)
        "pakiet"   – nazwa pakietu nadrzędnego lub "" jeśli na poziomie głównym (str)
        "atrybuty" – liczba publicznych atrybutów (nie zaczynających się od '_') (int)

    Wskazówka:
        importlib.import_module(nazwa_modulu)
        getattr(modul, "__file__", None)
        getattr(modul, "__package__", "")
        dir(modul)
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 2
# ---------------------------------------------------------------------------
def lazy_import(nazwa_modulu: str):
    """
    Zadanie 2: Leniwy import
    -------------------------
    Zaimportuj moduł o podanej nazwie TYLKO jeśli nie jest jeszcze w sys.modules.
    Zwróć zaimportowany (lub już istniejący) obiekt modułu.

    Wskazówka:
        Sprawdź sys.modules najpierw, potem użyj importlib.import_module.
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 3
# ---------------------------------------------------------------------------
def uruchom_kod_jako_modul(kod: str, nazwa: str = "__dynamic__") -> dict:
    """
    Zadanie 3: Tworzenie modułu w locie
    -------------------------------------
    Utwórz nowy obiekt modułu o podanej `nazwa`, wykonaj w nim podany `kod`
    (łańcuch znaków) i zwróć __dict__ tego modułu (przestrzeń nazw).

    Wskazówka:
        import types
        m = types.ModuleType(nazwa)
        exec(compile(kod, nazwa, "exec"), m.__dict__)
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 4
# ---------------------------------------------------------------------------
def znajdz_modul_w_sys_path(nazwa_pliku: str) -> str | None:
    """
    Zadanie 4: Wyszukiwanie modułu w sys.path
    ------------------------------------------
    Przeszukaj wszystkie katalogi z sys.path i sprawdź, czy plik o podanej
    nazwie (np. "os.py") istnieje w którymkolwiek z nich.
    Zwróć pełną ścieżkę do pierwszego znalezionego pliku, lub None jeśli
    plik nie istnieje w żadnym katalogu z sys.path.

    Wskazówka:
        import pathlib
        for katalog in sys.path: ...
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 5
# ---------------------------------------------------------------------------
def lista_modulow_z_prefiksem(prefiks: str) -> list[str]:
    """
    Zadanie 5: Moduły z sys.modules
    ---------------------------------
    Zwróć posortowaną listę nazw wszystkich aktualnie załadowanych modułów
    (z sys.modules), których nazwa zaczyna się od podanego `prefiks`.
    Pomiń moduły z wartością None (zdarza się przy nieudanych importach).

    Przykład:
        lista_modulow_z_prefiksem("os")  # → ["os", "os.path", ...]
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("info_o_module('math'):", info_o_module("math"))
    import os
    print("lazy_import('os') is os:", lazy_import("os") is os)
    ns = uruchom_kod_jako_modul("x = 6 * 7\ndef double(n): return n * 2")
    print("uruchom_kod_jako_modul: x =", ns.get("x"))
    print("znajdz_modul_w_sys_path('os.py'):", znajdz_modul_w_sys_path("os.py"))
    print("lista_modulow_z_prefiksem('sys'):", lista_modulow_z_prefiksem("sys"))

