"""
Wzorcowe rozwiązania – Instrukcje sterujące
============================================
"""
import math


def sito_eratostenesa(n: int) -> list[int]:
    if n < 2:
        return []
    jest_pierwsza = [True] * (n + 1)
    jest_pierwsza[0] = jest_pierwsza[1] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if jest_pierwsza[p]:
            for wielokrotnosc in range(p * p, n + 1, p):
                jest_pierwsza[wielokrotnosc] = False
    return [i for i, pierwsza in enumerate(jest_pierwsza) if pierwsza]


def spasuj_nawiasy(tekst: str) -> bool:
    stos: list[str] = []
    pary = {")": "(", "]": "[", "}": "{"}
    for znak in tekst:
        if znak in "([{":
            stos.append(znak)
        elif znak in ")]}":
            if not stos or stos[-1] != pary[znak]:
                return False
            stos.pop()
    return len(stos) == 0


def generuj_tabliczke_mnozenia(n: int) -> list[list[int]]:
    return [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]


def grupuj_po_dlugosci(slowa: list[str]) -> dict[int, list[str]]:
    grupy: dict[int, list[str]] = {}
    for slowo in slowa:
        d = len(slowo)
        grupy.setdefault(d, []).append(slowo)
    # Posortuj słowa w każdej grupie i zwróć słownik posortowany wg klucza
    return {k: sorted(v) for k, v in sorted(grupy.items())}


def interpretuj_wyrazenie(wyrazenie: str) -> float:
    stos: list[float] = []
    operatory = {"+", "-", "*", "/"}
    for token in wyrazenie.split():
        if token in operatory:
            if len(stos) < 2:
                raise ValueError(f"Za mało operandów dla operatora '{token}'")
            b = stos.pop()
            a = stos.pop()
            match token:
                case "+": stos.append(a + b)
                case "-": stos.append(a - b)
                case "*": stos.append(a * b)
                case "/":
                    if b == 0:
                        raise ValueError("Dzielenie przez zero")
                    stos.append(a / b)
        else:
            try:
                stos.append(float(token))
            except ValueError:
                raise ValueError(f"Nieznany token: {token!r}")
    if len(stos) != 1:
        raise ValueError("Błędne wyrażenie RPN")
    return stos[0]


def fizzbuzz_zaawansowany(n: int, zasady: dict[int, str]) -> list[str]:
    wynik = []
    for liczba in range(1, n + 1):
        tekst = "".join(
            etykieta
            for dzielnik, etykieta in sorted(zasady.items())
            if liczba % dzielnik == 0
        )
        wynik.append(tekst if tekst else str(liczba))
    return wynik


if __name__ == "__main__":
    print("Liczby pierwsze:", sito_eratostenesa(50))
    print("Nawiasy OK:", spasuj_nawiasy("([{}])"))
    print("Nawiasy ZLE:", spasuj_nawiasy("([)]"))
    print("Tabliczka 3x3:", generuj_tabliczke_mnozenia(3))
    print("Grupowanie:", grupuj_po_dlugosci(["kot", "pies", "lis", "ryba", "osa"]))
    print("RPN:", interpretuj_wyrazenie("5 1 2 + 4 * + 3 -"))
    print("FizzBuzz:", fizzbuzz_zaawansowany(15, {3: "Fizz", 5: "Buzz"}))

