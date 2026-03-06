"""
Demonstracja typów niemutowalnych w Pythonie 3.
Uruchomienie: python immutable_demo.py
"""


def demo_str_niemutowalnosc() -> None:
    print("=" * 55)
    print("STR – niemutowalność napisów")
    print("=" * 55)

    s = "Python"
    print(f"s = {s!r},  id(s) = {id(s)}")

    # Operacja += tworzy NOWY obiekt
    id_przed = id(s)
    s += " 3"
    print(f"Po s += ' 3': s = {s!r},  id(s) = {id(s)}")
    print(f"Id zmienione? {id_przed != id(s)}")

    # Próba bezpośredniej modyfikacji – TypeError
    try:
        s[0] = "X"  # type: ignore
    except TypeError as e:
        print(f"Próba modyfikacji s[0] → TypeError: {e}")


def demo_int_niemutowalnosc() -> None:
    print("\n" + "=" * 55)
    print("INT – referencje i internowanie małych liczb")
    print("=" * 55)

    # Internowanie małych liczb (-5 do 256)
    a = 100
    b = 100
    print(f"a=100, b=100: a is b = {a is b}  (internowane)")

    # Duże liczby – osobne obiekty
    x = 1000
    y = 1000
    print(f"x=1000, y=1000: x is y = {x is y}  (prawdopodobnie False)")
    print(f"x == y = {x == y}")   # wartość jest ta sama


def demo_tuple_niemutowalnosc() -> None:
    print("\n" + "=" * 55)
    print("TUPLE – niemutowalna sekwencja")
    print("=" * 55)

    t = (1, 2, 3)
    print(f"t = {t},  id(t) = {id(t)}")

    try:
        t[0] = 99  # type: ignore
    except TypeError as e:
        print(f"Próba t[0]=99 → TypeError: {e}")

    # UWAGA: krotka z mutowalnym elementem!
    t2 = (1, [2, 3], 4)
    print(f"\nt2 = {t2}")
    t2[1].append(99)   # lista wewnątrz krotki MOŻE być zmieniana
    print(f"Po t2[1].append(99): t2 = {t2}")
    print("(krotka sama w sobie nie zmieniła struktury – ten sam list object)")


def demo_wspoldzielenie() -> None:
    print("\n" + "=" * 55)
    print("Współdzielenie referencji – niemutowalne vs mutowalne")
    print("=" * 55)

    # Niemutowalne – bezpieczne współdzielenie
    a = "hello"
    b = a
    print(f"a={a!r}, b={b!r}, a is b = {a is b}")
    b += " world"  # tworzy nowy obiekt
    print(f"Po b += ' world': a={a!r}, b={b!r}  (a niezmienione!)")

    # Mutowalne – niebezpieczne współdzielenie
    lista_a = [1, 2, 3]
    lista_b = lista_a   # obie zmienne → ten sam obiekt
    print(f"\nlista_a={lista_a}, lista_b={lista_b}, is: {lista_a is lista_b}")
    lista_b.append(4)
    print(f"Po lista_b.append(4): lista_a={lista_a}  (zmienione!)")

    # Rozwiązanie: kopia
    lista_c = lista_a.copy()
    lista_c.append(99)
    print(f"\nPo lista_c = lista_a.copy() i append(99):")
    print(f"  lista_a = {lista_a}  (niezmienione)")
    print(f"  lista_c = {lista_c}")


if __name__ == "__main__":
    demo_str_niemutowalnosc()
    demo_int_niemutowalnosc()
    demo_tuple_niemutowalnosc()
    demo_wspoldzielenie()

