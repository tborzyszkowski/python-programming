"""
Przykłady algorytmów ilustrujące instrukcje sterujące w Pythonie 3.

Pokazuje współdziałanie: if/elif/else, for, while, break, continue,
for…else, match/case oraz wyrażeń listowych.

Uruchomienie:  python algorithms.py
"""
from math import isqrt, sqrt


# ---------------------------------------------------------------------------
# 1. Sprawdzanie pierwszości  (if + for + break/else)
# ---------------------------------------------------------------------------
def jest_pierwsza(n: int) -> bool:
    """Sprawdza, czy n jest liczbą pierwszą.

    Wzorzec for…else: blok else wykonuje się TYLKO gdy pętla zakończyła się
    bez break, co oznacza brak dzielnika – liczba jest pierwsza.
    """
    if n < 2:
        return False
    for dzielnik in range(2, isqrt(n) + 1):
        if n % dzielnik == 0:
            break          # znaleziono dzielnik → nie jest pierwsza
    else:
        return True        # pętla zakończyła się BEZ break → pierwsza
    return False


def demo_pierwszosc() -> None:
    print("=" * 55)
    print("1. Sprawdzanie pierwszości (for + break/else)")
    print("=" * 55)
    kandydaci = [1, 2, 3, 4, 5, 16, 17, 97, 100, 101]
    for n in kandydaci:
        status = "pierwsza" if jest_pierwsza(n) else "złożona"
        print(f"  {n:4d}: {status}")


# ---------------------------------------------------------------------------
# 2. Algorytm Euklidesa – NWD  (while)
# ---------------------------------------------------------------------------
def nwd(a: int, b: int) -> int:
    """Największy wspólny dzielnik algorytmem Euklidesa."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def nww(a: int, b: int) -> int:
    """Najmniejsza wspólna wielokrotność."""
    return abs(a * b) // nwd(a, b)


def demo_nwd_nww() -> None:
    print("\n" + "=" * 55)
    print("2. NWD i NWW algorytmem Euklidesa (while)")
    print("=" * 55)
    pary = [(48, 18), (100, 75), (13, 17), (12, 18), (0, 5)]
    for a, b in pary:
        print(f"  nwd({a}, {b}) = {nwd(a, b):3d}   nww = {nww(a, b) if b else '-'}")


# ---------------------------------------------------------------------------
# 3. Ciąg Collatza  (while + if/else)
# ---------------------------------------------------------------------------
def collatz(n: int) -> list[int]:
    """Ciąg Collatza od n do 1.

    Hipoteza: dla każdej liczby > 0 ciąg zawsze osiąga 1.
    """
    ciag = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        ciag.append(n)
    return ciag


def demo_collatz() -> None:
    print("\n" + "=" * 55)
    print("3. Ciąg Collatza (while + if/else)")
    print("=" * 55)
    for start in [6, 11, 27]:
        ciag = collatz(start)
        print(f"  collatz({start:2d}): {len(ciag):3d} kroków, "
              f"max = {max(ciag)}")
    print(f"\n  collatz(27) pierwsze 10: {collatz(27)[:10]}…")


# ---------------------------------------------------------------------------
# 4. Konwersja na system binarny  (while + lista)
# ---------------------------------------------------------------------------
def na_binarny(n: int) -> str:
    """Konwertuje nieujemną liczbę całkowitą na napis binarny."""
    if n == 0:
        return "0"
    bity: list[str] = []
    while n > 0:
        bity.append(str(n % 2))
        n //= 2
    return "".join(reversed(bity))


def demo_binarny() -> None:
    print("\n" + "=" * 55)
    print("4. Konwersja binarny (while + lista)")
    print("=" * 55)
    for liczba in [0, 1, 5, 10, 42, 255]:
        wynik = na_binarny(liczba)
        wbudowane = bin(liczba)[2:]
        zgodny = "OK" if wynik == wbudowane else "!!"
        print(f"  {liczba:4d} -> {wynik:>10s}   {zgodny}")


# ---------------------------------------------------------------------------
# 5. Wyszukiwanie binarne  (while + if/elif/else)
# ---------------------------------------------------------------------------
def wyszukiwanie_binarne(lista: list[int], cel: int) -> int:
    """Zwraca indeks celu w posortowanej liście lub -1."""
    lewy, prawy = 0, len(lista) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == cel:
            return srodek
        elif lista[srodek] < cel:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1


def demo_wyszukiwanie() -> None:
    print("\n" + "=" * 55)
    print("5. Wyszukiwanie binarne (while + if/elif/else)")
    print("=" * 55)
    posortowana = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"  Lista: {posortowana}")
    for cel in [23, 2, 91, 10, 56]:
        idx = wyszukiwanie_binarne(posortowana, cel)
        wynik = f"indeks {idx}" if idx != -1 else "nie znaleziono"
        print(f"  szukam {cel:3d}: {wynik}")


# ---------------------------------------------------------------------------
# 6. Trójkąt Pascala  (for + list comprehension)
# ---------------------------------------------------------------------------
def trojkat_pascala(wierszy: int) -> list[list[int]]:
    """Generuje trójkąt Pascala z podaną liczbą wierszy."""
    trojkat: list[list[int]] = [[1]]
    for _ in range(1, wierszy):
        poprzedni = trojkat[-1]
        nowy = ([1]
                + [poprzedni[j] + poprzedni[j + 1]
                   for j in range(len(poprzedni) - 1)]
                + [1])
        trojkat.append(nowy)
    return trojkat


def demo_pascal() -> None:
    print("\n" + "=" * 55)
    print("6. Trójkąt Pascala (for + list comprehension)")
    print("=" * 55)
    for wiersz in trojkat_pascala(7):
        print("  " + "  ".join(f"{x:3d}" for x in wiersz))


# ---------------------------------------------------------------------------
# 7. Klasyfikacja z match/case  (Python 3.10+)
# ---------------------------------------------------------------------------
def klasyfikuj_wynik(punkty: int) -> str:
    """Klasyfikuje wynik testu na ocenę literową."""
    match punkty:
        case p if p >= 90:
            return "A (celujący)"
        case p if p >= 75:
            return "B (b. dobry)"
        case p if p >= 60:
            return "C (dobry)"
        case p if p >= 50:
            return "D (dostateczny)"
        case _:
            return "F (niedostateczny)"


def demo_match() -> None:
    print("\n" + "=" * 55)
    print("7. Klasyfikacja match/case (Python 3.10+)")
    print("=" * 55)
    for pkt in [95, 80, 65, 52, 30, 100, 0]:
        print(f"  {pkt:3d} pkt → {klasyfikuj_wynik(pkt)}")


# ---------------------------------------------------------------------------
# 8. Korzeń cyfrowy  (while + generator)
# ---------------------------------------------------------------------------
def suma_cyfr(n: int) -> int:
    """Suma cyfr liczby całkowitej."""
    return sum(int(c) for c in str(abs(n)))


def rdzen_cyfrowy(n: int) -> int:
    """Redukuje liczbę do jednej cyfry przez iteracyjne sumowanie cyfr."""
    while n >= 10:
        n = suma_cyfr(n)
    return n


def demo_rdzen() -> None:
    print("\n" + "=" * 55)
    print("8. Korzeń cyfrowy (while + generator sum)")
    print("=" * 55)
    for liczba in [0, 9, 493, 1234, 99999, 999_999_999]:
        print(f"  {liczba:>12d} → rdzeń: {rdzen_cyfrowy(liczba)}")


# ---------------------------------------------------------------------------
# 9. Pierwiastek Newtona  (while + if)
# ---------------------------------------------------------------------------
def pierwiastek_newton(n: float, eps: float = 1e-10) -> float:
    """Pierwiastek kwadratowy metodą Newtona-Raphsona (bez math.sqrt)."""
    if n < 0:
        raise ValueError("Ujemny argument")
    if n == 0:
        return 0.0
    x = n
    while True:
        nastepny = (x + n / x) / 2
        if abs(x - nastepny) < eps:
            return nastepny
        x = nastepny


def demo_newton() -> None:
    print("\n" + "=" * 55)
    print("9. Pierwiastek metodą Newtona (while + if)")
    print("=" * 55)
    for v in [2, 9, 144, 0.5, 1e8]:
        wynik = pierwiastek_newton(v)
        dokladny = sqrt(v)
        blad = abs(wynik - dokladny)
        print(f"  sqrt({v}) = {wynik:.10f}  błąd = {blad:.2e}")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    demo_pierwszosc()
    demo_nwd_nww()
    demo_collatz()
    demo_binarny()
    demo_wyszukiwanie()
    demo_pascal()
    demo_match()
    demo_rdzen()
    demo_newton()



