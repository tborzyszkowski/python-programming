"""
Wzorcowe rozwiązania – Kompilatory i interpretery
==================================================
"""
import dis
import sys


def policz_instrukcje_bajtkodu(func) -> int:
    """Zlicza unikalne nazwy instrukcji bajtkodowych w funkcji."""
    return len({instr.opname for instr in dis.get_instructions(func)})


def czy_cpython() -> bool:
    """Zwraca True dla CPython."""
    return sys.implementation.name == "cpython"


def wersja_pythona() -> tuple[int, int, int]:
    """Zwraca (major, minor, micro) bieżącej wersji Pythona."""
    v = sys.version_info
    return (v.major, v.minor, v.micro)


def znajdz_stale_w_bajtkodzie(func) -> list[object]:
    """Zwraca unikalne stałe (LOAD_CONST) z bajtkodu, bez None."""
    widziane: set = set()
    wynik: list = []
    for instr in dis.get_instructions(func):
        if instr.opname == "LOAD_CONST" and instr.argval is not None:
            # używamy id() bo wartości mogą być niehashowalne (rzadko, ale możliwe)
            if instr.argval not in widziane:
                widziane.add(instr.argval)
                wynik.append(instr.argval)
    return wynik


def kompiluj_i_wykonaj(kod: str, zmienne: dict) -> dict:
    """Kompiluje i wykonuje kod, zwraca słownik zmiennych po wykonaniu."""
    code_obj = compile(kod, "<string>", "exec")
    exec(code_obj, zmienne)
    return zmienne


if __name__ == "__main__":
    def przyklad(a, b):
        return a + b

    print("policz_instrukcje_bajtkodu:", policz_instrukcje_bajtkodu(przyklad))
    print("czy_cpython:               ", czy_cpython())
    print("wersja_pythona:            ", wersja_pythona())
    print("znajdz_stale:              ", znajdz_stale_w_bajtkodzie(lambda: 1 + 2 + 1))
    print("kompiluj_i_wykonaj:        ", kompiluj_i_wykonaj("wynik = 6 * 7", {}))

