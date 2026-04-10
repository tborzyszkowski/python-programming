"""Demonstracja zmiennej __all__ — kontrola eksportu przy import *.

Ten moduł celowo definiuje __all__, aby ograniczyć eksport.
"""

__all__ = ["publiczna_operacja", "STALA_API"]

STALA_API = 42


def publiczna_operacja(x: int) -> int:
    """Ta funkcja jest w __all__ — będzie wyeksportowana przez import *."""
    return x + STALA_API


def _prywatna_pomoc() -> str:
    """Konwencja: nazwy z _ nie są eksportowane nawet bez __all__."""
    return "wewnętrzna"


def pomocnicza_ale_nie_publiczna(x: int) -> int:
    """Nie ma _ w nazwie, ale NIE jest w __all__ — import * ją pominie."""
    return x * 2


if __name__ == "__main__":
    print(f"__all__ = {__all__}")
    print(f"publiczna_operacja(10) = {publiczna_operacja(10)}")
    print(f"pomocnicza_ale_nie_publiczna(10) = {pomocnicza_ale_nie_publiczna(10)}")
    print()
    print("Przy 'from all_demo import *' dostępne będą tylko:")
    print(f"  {', '.join(__all__)}")

