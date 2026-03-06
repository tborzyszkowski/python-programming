"""
Demonstracja instrukcji warunkowych w Pythonie 3.
Uruchomienie: python conditionals.py
"""


def demo_if_elif_else() -> None:
    print("=" * 55)
    print("if / elif / else")
    print("=" * 55)

    for liczba in [-5, 0, 7, 15]:
        if liczba > 0:
            kategoria = "dodatnia"
        elif liczba == 0:
            kategoria = "zero"
        else:
            kategoria = "ujemna"
        print(f"  {liczba:4d} → {kategoria}")


def demo_lancuchowanie() -> None:
    print("\n" + "=" * 55)
    print("Łańcuchowanie porównań")
    print("=" * 55)

    for x in [0, 5, 10, 15]:
        if 1 <= x <= 9:
            print(f"  {x} jest jednocyfrowy (dodatni)")
        else:
            print(f"  {x} NIE jest jednocyfrowy dodatnim")


def demo_falsy() -> None:
    print("\n" + "=" * 55)
    print("Wartości falsy")
    print("=" * 55)

    falsy_values = [False, 0, 0.0, 0j, "", [], {}, set(), (), None]
    for v in falsy_values:
        print(f"  bool({v!r:15}) = {bool(v)}")


def demo_ternary() -> None:
    print("\n" + "=" * 55)
    print("Wyrażenie warunkowe (ternary)")
    print("=" * 55)

    for wiek in [15, 18, 25]:
        status = "dorosły" if wiek >= 18 else "niepełnoletni"
        print(f"  wiek={wiek} → {status}")


def demo_match() -> None:
    print("\n" + "=" * 55)
    print("match / case (Python 3.10+)")
    print("=" * 55)

    komendy = ["start", "stop", "wyjdź", "nieznane", "pauza"]

    for komenda in komendy:
        match komenda:
            case "start":
                wynik = "Uruchamiam..."
            case "stop" | "wyjdź":
                wynik = "Zatrzymuję."
            case "pauza":
                wynik = "Pauza."
            case _:
                wynik = f"Nieznana komenda: {komenda!r}"
        print(f"  {komenda!r:12} → {wynik}")

    print("\nDopasowanie struktury (krotka):")
    punkty = [(0, 0), (3, 0), (0, -4), (2, 5)]
    for punkt in punkty:
        match punkt:
            case (0, 0):
                opis = "Środek układu"
            case (x, 0):
                opis = f"Na osi X, x={x}"
            case (0, y):
                opis = f"Na osi Y, y={y}"
            case (x, y):
                opis = f"Punkt ogólny ({x}, {y})"
        print(f"  {str(punkt):8} → {opis}")


if __name__ == "__main__":
    demo_if_elif_else()
    demo_lancuchowanie()
    demo_falsy()
    demo_ternary()
    demo_match()

