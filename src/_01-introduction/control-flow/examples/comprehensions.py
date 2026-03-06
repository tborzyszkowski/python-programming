"""
Demonstracja wyrażeń listowych (comprehensions) i generatorów w Pythonie 3.
Uruchomienie: python comprehensions.py
"""
import sys
import time


def demo_list_comprehension() -> None:
    print("=" * 55)
    print("List Comprehension")
    print("=" * 55)

    # Podstawowy
    kwadraty = [x ** 2 for x in range(1, 11)]
    print(f"Kwadraty 1-10: {kwadraty}")

    # Z filtrem
    parzyste = [x for x in range(20) if x % 2 == 0]
    print(f"Parzyste 0-19: {parzyste}")

    # Transformacja napisów
    imiona = ["anna", "bartek", "celina"]
    wielkie = [s.capitalize() for s in imiona]
    print(f"Wielkie litery: {wielkie}")

    # Zagnieżdżone
    macierz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print("Tabliczka mnożenia 3x3:")
    for wiersz in macierz:
        print(f"  {wiersz}")

    # Spłaszczanie (flatten)
    zagniezdzone = [[1, 2], [3, 4], [5, 6]]
    plaskie = [x for podlista in zagniezdzone for x in podlista]
    print(f"Spłaszczone: {plaskie}")


def demo_dict_set_comprehension() -> None:
    print("\n" + "=" * 55)
    print("Dict i Set Comprehension")
    print("=" * 55)

    # Dict comprehension
    kwadraty = {x: x ** 2 for x in range(1, 6)}
    print(f"Dict kwadraty: {kwadraty}")

    # Odwrócony słownik
    oryginal = {"a": 1, "b": 2, "c": 3}
    odwrocony = {v: k for k, v in oryginal.items()}
    print(f"Odwrócony dict: {odwrocony}")

    # Set comprehension
    unikalne_ostatnie = {imie[-1] for imie in ["Anna", "Ola", "Ela", "Ania"]}
    print(f"Unikalne ostatnie litery imion: {sorted(unikalne_ostatnie)}")


def demo_generator() -> None:
    print("\n" + "=" * 55)
    print("Generator Expression – leniwa ewaluacja")
    print("=" * 55)

    n = 1_000_000

    # Generator – nie tworzy listy w pamięci
    gen = (x ** 2 for x in range(n))

    # Lista – zajmuje pamięć od razu
    # lst = [x ** 2 for x in range(n)]  # dużo więcej pamięci!

    print(f"Typ generatora: {type(gen)}")

    # Rozmiar generatora vs listy
    gen_size = sys.getsizeof(gen)
    lst_size = sys.getsizeof([x ** 2 for x in range(100)])
    print(f"Rozmiar generatora (n=1M): {gen_size} bajtów")
    print(f"Rozmiar listy (n=100):      {lst_size} bajtów")

    # Wydajność sum()
    t0 = time.perf_counter()
    wynik = sum(x ** 2 for x in range(n))
    t1 = time.perf_counter()
    print(f"\nSuma kwadratów 0..{n}: {wynik}")
    print(f"Czas (generator):    {(t1 - t0)*1000:.1f} ms")


if __name__ == "__main__":
    demo_list_comprehension()
    demo_dict_set_comprehension()
    demo_generator()

