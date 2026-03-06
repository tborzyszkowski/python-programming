"""
Demonstracja list, krotek, słowników i zbiorów w Pythonie 3.
Uruchomienie: python collections_demo.py
"""


def demo_list() -> None:
    print("=" * 50)
    print("LIST – mutowalna, uporządkowana sekwencja")
    print("=" * 50)

    owoce: list[str] = ["jabłko", "banan", "wiśnia"]
    print(f"Oryginalna: {owoce}")

    owoce.append("mango")
    print(f"Po append:  {owoce}")

    owoce.insert(1, "agrest")
    print(f"Po insert:  {owoce}")

    owoce.remove("banan")
    print(f"Po remove:  {owoce}")

    wyciagniety = owoce.pop(0)
    print(f"Po pop(0):  {owoce}, wyciagniety={wyciagniety!r}")

    liczby = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nliczby: {liczby}")
    print(f"sorted():  {sorted(liczby)}")
    liczby.sort(reverse=True)
    print(f"sort(desc): {liczby}")

    print(f"\nWycinek [1:3]: {liczby[1:3]}")
    print(f"Długość: {len(liczby)}")
    print(f"Min/Max: {min(liczby)} / {max(liczby)}")
    print(f"Suma: {sum(liczby)}")

    # list comprehension
    kwadraty = [x ** 2 for x in range(1, 6)]
    print(f"\nList comprehension: {kwadraty}")
    parzyste = [x for x in range(10) if x % 2 == 0]
    print(f"Parzyste 0-9: {parzyste}")


def demo_tuple() -> None:
    print("\n" + "=" * 50)
    print("TUPLE – niemutowalna, uporządkowana sekwencja")
    print("=" * 50)

    punkt = (3, 4)
    rgb   = (255, 128, 0)
    jeden = (42,)    # WAŻNE: przecinek przy jednym elemencie!
    pusta = ()

    print(f"punkt = {punkt}, type = {type(punkt)}")
    print(f"rgb   = {rgb}")
    print(f"jeden = {jeden}  (uwaga na przecinek!)")
    print(f"pusta = {pusta}")

    # Rozpakowywanie
    x, y = punkt
    print(f"\nRozpakowanie punktu: x={x}, y={y}")

    # swap
    a, b = 1, 2
    a, b = b, a
    print(f"Swap a,b: a={a}, b={b}")

    # rozszerzone rozpakowywanie (Python 3)
    pierwszy, *reszta, ostatni = (1, 2, 3, 4, 5)
    print(f"pierwszy={pierwszy}, reszta={reszta}, ostatni={ostatni}")

    # jako klucz słownika
    pozycje = {(0, 0): "środek", (1, 0): "prawo", (0, 1): "góra"}
    print(f"\nKrotka jako klucz: {pozycje[(1, 0)]}")

    # namedtuple
    from collections import namedtuple
    Punkt2D = namedtuple("Punkt2D", ["x", "y"])
    p = Punkt2D(3, 4)
    print(f"namedtuple: {p}, p.x={p.x}, p.y={p.y}")


def demo_dict() -> None:
    print("\n" + "=" * 50)
    print("DICT – mutowalny, zachowuje kolejność wstawiania")
    print("=" * 50)

    osoba: dict = {"imie": "Ania", "wiek": 25, "miasto": "Kraków"}
    print(f"Słownik: {osoba}")

    print(f"\nosoba['imie']            = {osoba['imie']}")
    print(f"osoba.get('email', '?') = {osoba.get('email', 'brak')}")

    osoba["email"] = "ania@example.com"
    print(f"Po dodaniu email: {osoba}")

    del osoba["miasto"]
    print(f"Po usunięciu miasto: {osoba}")

    print(f"\nKlucze:   {list(osoba.keys())}")
    print(f"Wartości: {list(osoba.values())}")

    # iteracja
    print("\nIteracja items():")
    for k, v in osoba.items():
        print(f"  {k:8s} → {v}")

    # dict comprehension
    kwadraty = {x: x ** 2 for x in range(1, 6)}
    print(f"\nDict comprehension: {kwadraty}")

    # scalanie słowników (Python 3.9+)
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 99, "c": 3}
    scalony = d1 | d2
    print(f"d1 | d2 = {scalony}")


def demo_set() -> None:
    print("\n" + "=" * 50)
    print("SET – mutowalny, nieuporządkowany zbiór unikalnych wartości")
    print("=" * 50)

    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    print(f"s1 = {s1}")
    print(f"s2 = {s2}")

    print(f"\nSuma (|):         {s1 | s2}")
    print(f"Część wspólna (&): {s1 & s2}")
    print(f"Różnica (s1-s2):  {s1 - s2}")
    print(f"Różnica sym. (^): {s1 ^ s2}")

    s1.add(10)
    print(f"\nPo add(10): {s1}")
    s1.discard(999)  # nie rzuca błędu gdy brak elementu
    print(f"Po discard(999): {s1}")

    # Usuwanie duplikatów z listy
    lista = [1, 2, 2, 3, 3, 3, 4]
    unikalne = list(set(lista))
    unikalne.sort()
    print(f"\nUsuwanie duplikatów: {lista} → {unikalne}")

    # frozenset – niemutowalny zbiór (może być kluczem dict)
    fs = frozenset({1, 2, 3})
    print(f"\nfrozenset: {fs}, type={type(fs)}")

    # set comprehension
    podzielne = {x for x in range(20) if x % 3 == 0}
    print(f"Podzielne przez 3 (0-19): {sorted(podzielne)}")


if __name__ == "__main__":
    demo_list()
    demo_tuple()
    demo_dict()
    demo_set()

