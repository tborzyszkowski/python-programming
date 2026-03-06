"""
Demonstracja uruchamiania skryptu Python z argumentami linii poleceń.

Uruchomienie:
    python run_as_script.py Ania 25
    python run_as_script.py
"""
import sys


def powitaj(imie: str, wiek: int) -> str:
    return f"Witaj, {imie}! Masz {wiek} lat."


def main() -> None:
    print(f"Nazwa skryptu (sys.argv[0]): {sys.argv[0]}")
    print(f"Wszystkie argumenty:         {sys.argv}")

    if len(sys.argv) == 3:
        imie = sys.argv[1]
        wiek = int(sys.argv[2])
        print(powitaj(imie, wiek))
    else:
        print("Użycie: python run_as_script.py <imię> <wiek>")
        print(powitaj("Świat", 0))


# Ten blok wykonuje się TYLKO gdy plik jest uruchomiony bezpośrednio,
# a NIE gdy jest importowany jako moduł.
if __name__ == "__main__":
    main()

