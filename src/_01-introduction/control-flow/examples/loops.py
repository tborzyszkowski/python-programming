"""
Demonstracja pętli w Pythonie 3: for, while, break, continue, else.
Uruchomienie: python loops.py
"""


def demo_for_podstawowy() -> None:
    print("=" * 55)
    print("Pętla for – podstawowe użycie")
    print("=" * 55)

    # Iteracja po liście
    owoce = ["jabłko", "banan", "wiśnia"]
    for owoc in owoce:
        print(f"  {owoc}")

    # range()
    print("\nrange(5):")
    for i in range(5):
        print(f"  {i}", end="  ")
    print()

    print("\nrange(2, 10, 2):")
    for i in range(2, 10, 2):
        print(f"  {i}", end="  ")
    print()

    # Iteracja po napisie
    print("\nIteracja po napisie 'ABC':")
    for ch in "ABC":
        print(f"  {ch}", end="  ")
    print()


def demo_enumerate_zip() -> None:
    print("\n" + "=" * 55)
    print("enumerate() i zip()")
    print("=" * 55)

    owoce = ["jabłko", "banan", "wiśnia"]
    print("enumerate(owoce, start=1):")
    for i, owoc in enumerate(owoce, start=1):
        print(f"  {i}. {owoc}")

    imiona = ["Ania", "Bartek", "Celina"]
    wieki  = [25, 30, 22]
    print("\nzip(imiona, wieki):")
    for imie, wiek in zip(imiona, wieki):
        print(f"  {imie:8} → {wiek} lat")


def demo_break_continue_else() -> None:
    print("\n" + "=" * 55)
    print("break, continue, else w pętli for")
    print("=" * 55)

    print("Pomijamy 3, zatrzymujemy przy 7:")
    for i in range(10):
        if i == 3:
            continue
        if i == 7:
            break
        print(f"  {i}", end="  ")
    print()

    print("\nBlok else (pętla bez break):")
    for i in range(5):
        print(f"  {i}", end="  ")
    else:
        print("\n  → else: pętla zakończona normalnie")

    print("\nBlok else (pętla z break – else NIE wykona się):")
    for i in range(5):
        if i == 3:
            break
    else:
        print("  → else: nie wyświetli się!")
    print("  → pętla przerwana przez break przy i=3")


def demo_while() -> None:
    print("\n" + "=" * 55)
    print("Pętla while")
    print("=" * 55)

    licznik = 0
    print("while licznik < 5:")
    while licznik < 5:
        print(f"  licznik = {licznik}")
        licznik += 1

    # while z else
    print("\nwhile z else (bez break):")
    n = 3
    while n > 0:
        print(f"  n = {n}")
        n -= 1
    else:
        print("  → else: warunek stał się False")

    # Szukanie elementu z while
    print("\nSzukanie pierwszej parzystej > 7:")
    dane = [1, 3, 5, 8, 11, 14]
    i = 0
    while i < len(dane):
        if dane[i] > 7 and dane[i] % 2 == 0:
            print(f"  Znaleziono: {dane[i]} (indeks {i})")
            break
        i += 1


def demo_iteracja_slownik() -> None:
    print("\n" + "=" * 55)
    print("Iteracja po słowniku")
    print("=" * 55)

    oceny = {"Ania": 5, "Bartek": 4, "Celina": 5, "Dawid": 3}

    print("Klucze:")
    for imie in oceny:              # domyślnie klucze
        print(f"  {imie}")

    print("\nPary klucz-wartość:")
    for imie, ocena in oceny.items():
        print(f"  {imie:8}: {ocena}")

    print("\nFiltrowanie (ocena >= 5):")
    celujacy = {k: v for k, v in oceny.items() if v >= 5}
    for k, v in celujacy.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    demo_for_podstawowy()
    demo_enumerate_zip()
    demo_break_continue_else()
    demo_while()
    demo_iteracja_slownik()

