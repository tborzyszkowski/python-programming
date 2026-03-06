"""
Demonstracja typów mutowalnych i pułapek z nimi związanych.
Uruchomienie: python mutable_demo.py
"""
import copy


def demo_lista_mutuje() -> None:
    print("=" * 55)
    print("LIST – modyfikacja w miejscu (in-place)")
    print("=" * 55)

    lst = [1, 2, 3]
    print(f"id przed append: {id(lst)}")
    lst.append(4)
    print(f"id po    append: {id(lst)}  (TEN SAM)")
    print(f"lst = {lst}")


def demo_pulapka_domyslny_argument() -> None:
    print("\n" + "=" * 55)
    print("PUŁAPKA: Mutowalny domyślny argument funkcji")
    print("=" * 55)

    # ŹLE – lista tworzona raz przy definicji funkcji
    def dodaj_zle(element, lista=[]):  # noqa: B006 – celowe, pokazujemy błąd!
        lista.append(element)
        return lista

    print("Funkcja ze ŹLE zdefiniowanym argumentem domyślnym:")
    print(f"  dodaj_zle(1) = {dodaj_zle(1)}")
    print(f"  dodaj_zle(2) = {dodaj_zle(2)}  (oczekiwano [2], dostano [1,2]!)")
    print(f"  dodaj_zle(3) = {dodaj_zle(3)}")

    # DOBRZE – None jako domyślna wartość
    def dodaj_dobrze(element, lista=None):
        if lista is None:
            lista = []
        lista.append(element)
        return lista

    print("\nFunkcja z POPRAWNIE zdefiniowanym argumentem domyślnym:")
    print(f"  dodaj_dobrze(1) = {dodaj_dobrze(1)}")
    print(f"  dodaj_dobrze(2) = {dodaj_dobrze(2)}")
    print(f"  dodaj_dobrze(3) = {dodaj_dobrze(3)}")


def demo_plytka_vs_gleboka_kopia() -> None:
    print("\n" + "=" * 55)
    print("Płytka vs głęboka kopia")
    print("=" * 55)

    oryginal = [[1, 2], [3, 4], [5, 6]]

    plytka = oryginal.copy()       # lub oryginal[:]
    gleboka = copy.deepcopy(oryginal)

    # Modyfikacja zagnieżdżonego obiektu
    oryginal[0].append(99)

    print(f"Oryginał:     {oryginal}")
    print(f"Płytka kopia: {plytka}   ← zmieniła się (!)  – lista wewnętrzna jest współdzielona")
    print(f"Głęboka kopia:{gleboka}  ← niezmieniona ✓")


def demo_dict_mutuje() -> None:
    print("\n" + "=" * 55)
    print("DICT – modyfikacja w miejscu")
    print("=" * 55)

    d = {"a": 1}
    ref = d   # ta sama referencja!
    ref["b"] = 2
    print(f"d = {d}  (zmodyfikowane przez 'ref')")

    # Bezpieczna kopia
    d2 = {"x": 1}
    kopia = d2.copy()
    kopia["y"] = 99
    print(f"d2    = {d2}    (niezmienione)")
    print(f"kopia = {kopia}")


def demo_set_mutuje() -> None:
    print("\n" + "=" * 55)
    print("SET vs FROZENSET")
    print("=" * 55)

    s = {1, 2, 3}
    s.add(4)
    s.discard(1)
    print(f"set po modyfikacji: {s}")

    # frozenset – niemutowalny, może być kluczem słownika
    fs = frozenset({10, 20, 30})
    print(f"frozenset: {fs}")
    try:
        fs.add(99)  # type: ignore
    except AttributeError as e:
        print(f"frozenset.add() → AttributeError: {e}")


if __name__ == "__main__":
    demo_lista_mutuje()
    demo_pulapka_domyslny_argument()
    demo_plytka_vs_gleboka_kopia()
    demo_dict_mutuje()
    demo_set_mutuje()

