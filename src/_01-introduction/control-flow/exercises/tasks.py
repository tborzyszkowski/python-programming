"""
Zadania – Instrukcje sterujące
================================

Uruchomienie: pytest test_solutions.py -v
"""


# ---------------------------------------------------------------------------
# Zadanie 1
# ---------------------------------------------------------------------------
def sito_eratostenesa(n: int) -> list[int]:
    """
    Zadanie 1: Sito Eratostenesa
    -----------------------------
    Zwróć posortowaną listę wszystkich liczb pierwszych <= n.
    Zaimplementuj klasyczny algorytm Sita Eratostenesa z użyciem pętli.

    Algorytm:
    1. Utwórz listę booleanów [True] * (n+1), indeks = liczba.
    2. Ustaw [0] i [1] na False.
    3. Dla każdego p od 2 do sqrt(n): jeśli [p] jest True,
       wyzeruj wszystkie wielokrotności p (od p*p do n).
    4. Zwróć indeksy wartości True.

    Przykład:
        sito_eratostenesa(20) → [2, 3, 5, 7, 11, 13, 17, 19]
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 2
# ---------------------------------------------------------------------------
def spasuj_nawiasy(tekst: str) -> bool:
    """
    Zadanie 2: Sprawdzanie parowania nawiasów
    ------------------------------------------
    Sprawdź czy nawiasy w podanym `tekst` są poprawnie sparowane i zagnieżdżone.
    Obsługuj trzy typy: ( ), [ ], { }.
    Zwróć True jeśli poprawne, False w przeciwnym razie.

    Przykład:
        spasuj_nawiasy("([{}])")   → True
        spasuj_nawiasy("([)]")     → False
        spasuj_nawiasy("{[")       → False

    Wskazówka: użyj listy jako stosu (append / pop).
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 3
# ---------------------------------------------------------------------------
def generuj_tabliczke_mnozenia(n: int) -> list[list[int]]:
    """
    Zadanie 3: Tabliczka mnożenia n×n
    ----------------------------------
    Zwróć tabliczkę mnożenia jako listę list (macierz n×n),
    gdzie element [i][j] = (i+1) * (j+1)  (indeksowanie od 1).

    Użyj zagnieżdżonych wyrażeń listowych (list comprehensions).

    Przykład:
        generuj_tabliczke_mnozenia(3)
        # → [[1, 2, 3],
        #    [2, 4, 6],
        #    [3, 6, 9]]
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 4
# ---------------------------------------------------------------------------
def grupuj_po_dlugosci(slowa: list[str]) -> dict[int, list[str]]:
    """
    Zadanie 4: Grupowanie słów według długości
    -------------------------------------------
    Pogrupuj słowa z listy `slowa` według ich długości.
    Zwróć słownik {długość: [posortowane_słowa]}.
    Grupy posortuj rosnąco wg klucza (długości).

    Przykład:
        grupuj_po_dlugosci(["kot", "pies", "lis", "ryba", "osa"])
        # → {3: ["kot", "lis", "osa"], 4: ["pies", "ryba"]}
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 5
# ---------------------------------------------------------------------------
def interpretuj_wyrazenie(wyrazenie: str) -> float:
    """
    Zadanie 5: Interpreter prostych wyrażeń RPN
    ---------------------------------------------
    Oblicz wartość wyrażenia w Odwrotnej Notacji Polskiej (ONP / RPN).
    Wyrażenie to łańcuch tokenów oddzielonych spacjami.
    Tokeny to liczby (int/float) lub operatory: + - * /

    Algorytm (stos):
    - Jeśli token jest liczbą → odłóż na stos.
    - Jeśli token jest operatorem → zdejmij dwa elementy ze stosu,
      wykonaj operację (drugi_zdejty OP pierwszy_zdejty), wynik odłóż.
    - Na końcu na stosie jest dokładnie jeden element – wynik.

    Rzuć ValueError przy dzieleniu przez zero lub błędnym wyrażeniu.

    Przykład:
        interpretuj_wyrazenie("3 4 +")       → 7.0
        interpretuj_wyrazenie("5 1 2 + 4 * + 3 -")  → 14.0
        interpretuj_wyrazenie("2 3 * 4 +")   → 10.0
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
# Zadanie 6
# ---------------------------------------------------------------------------
def fizzbuzz_zaawansowany(n: int, zasady: dict[int, str]) -> list[str]:
    """
    Zadanie 6: FizzBuzz z konfigurowalnymi zasadami
    ------------------------------------------------
    Generuj listę n elementów (dla liczb 1..n):
    - Dla każdej liczby sprawdź wszystkie klucze ze słownika `zasady`
      (posortowane rosnąco). Jeśli liczba jest podzielna przez klucz,
      dołącz odpowiednią wartość do wyniku dla tej liczby.
    - Jeśli żaden klucz nie pasuje, wstaw reprezentację liczbową jako str.

    Przykład (klasyczny FizzBuzz):
        fizzbuzz_zaawansowany(15, {3: "Fizz", 5: "Buzz"})
        # → ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz",
        #    "Buzz","11","Fizz","13","14","FizzBuzz"]
    """
    raise NotImplementedError("Uzupełnij implementację")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Liczby pierwsze:", sito_eratostenesa(50))
    print("Nawiasy OK:", spasuj_nawiasy("([{}])"))
    print("Nawiasy ZLE:", spasuj_nawiasy("([)]"))
    print("Tabliczka 3x3:", generuj_tabliczke_mnozenia(3))
    print("Grupowanie:", grupuj_po_dlugosci(["kot", "pies", "lis", "ryba", "osa"]))
    print("RPN:", interpretuj_wyrazenie("5 1 2 + 4 * + 3 -"))
    print("FizzBuzz:", fizzbuzz_zaawansowany(15, {3: "Fizz", 5: "Buzz"}))

