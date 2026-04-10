"""Demonstracja modułu dis — inspekcja bytecode Pythona."""

import dis


def dodaj(a: int, b: int) -> int:
    """Prosta funkcja do inspekcji bytecode."""
    return a + b


def silnia(n: int) -> int:
    """Rekurencyjna silnia — bardziej rozbudowany bytecode."""
    if n <= 1:
        return 1
    return n * silnia(n - 1)


def petla_sumujaca(n: int) -> int:
    """Suma 1..n w pętli — bytecode z instrukcjami skoku."""
    wynik = 0
    for i in range(1, n + 1):
        wynik += i
    return wynik


if __name__ == "__main__":
    print("=" * 60)
    print("Bytecode funkcji dodaj(a, b):")
    print("=" * 60)
    dis.dis(dodaj)

    print()
    print("=" * 60)
    print("Bytecode funkcji silnia(n):")
    print("=" * 60)
    dis.dis(silnia)

    print()
    print("=" * 60)
    print("Bytecode funkcji petla_sumujaca(n):")
    print("=" * 60)
    dis.dis(petla_sumujaca)

    print()
    print("=" * 60)
    print("Obiekt kodu (code object) funkcji dodaj:")
    print("=" * 60)
    code = dodaj.__code__
    print(f"  co_varnames  = {code.co_varnames}")
    print(f"  co_consts    = {code.co_consts}")
    print(f"  co_stacksize = {code.co_stacksize}")

