"""Większy przykład: prosty dispatcher komend CLI.

Pokazuje *args/**kwargs i przekazywanie funkcji.
"""


def cmd_add(*args: str) -> str:
    liczby = [float(x) for x in args]
    return str(sum(liczby))


def cmd_mul(*args: str) -> str:
    wynik = 1.0
    for x in args:
        wynik *= float(x)
    return str(wynik)


def cmd_greet(*args: str, prefix: str = "Cześć") -> str:
    if not args:
        return f"{prefix}!"
    return f"{prefix}, {' '.join(args)}!"


def execute(command: str, *args: str, **kwargs: str) -> str:
    """Wywołuje komendę po nazwie."""
    table = {
        "add": cmd_add,
        "mul": cmd_mul,
        "greet": cmd_greet,
    }
    if command not in table:
        raise ValueError(f"Nieznana komenda: {command}")
    return table[command](*args, **kwargs)


if __name__ == "__main__":
    print("add 2 3 4 ->", execute("add", "2", "3", "4"))
    print("mul 2 3 4 ->", execute("mul", "2", "3", "4"))
    print("greet Jan ->", execute("greet", "Jan", prefix="Witaj"))

