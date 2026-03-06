# Instrukcje sterujące w Pythonie 3

> **Cel:** Poznanie podstawowych instrukcji sterujących przepływem programu: warunków, pętli, dopasowania wzorców i wyrażeń listowych.

---

## Instrukcja warunkowa – `if / elif / else`

```python
x = 42

if x > 0:
    print("Dodatnia")
elif x == 0:
    print("Zero")
else:
    print("Ujemna")
```

Python używa **wcięć** (4 spacje) zamiast nawiasów klamrowych – to część składni.

Wyrażenie warunkowe (ternary / conditional expression):

```python
status = "dorosły" if wiek >= 18 else "niepełnoletni"
```

![Diagram if/elif/else](diagrams/if_elif_else.png)

---

## Wartości logiczne i operatory

**Operatory porównania:** `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in`

**Operatory logiczne:** `and`, `or`, `not`

```python
# Łączenie warunków
x = 5
if 0 < x < 10:           # Python pozwala na łańcuchowanie!
    print("Jednocyfrowy")

# Wartości "falsy" – traktowane jako False
if not []:               # pusta lista
    print("Pusta lista!")
if not "" or not 0 or not None:
    print("Falsy values")
```

Wartości **falsy**: `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`, `None`

---

## Pętla `for` – iteracja po sekwencji

```python
owoce = ["jabłko", "banan", "wiśnia"]

for owoc in owoce:
    print(owoc)
```

Z funkcją `range()`:

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)
```

Z `enumerate()` – indeks i wartość:

```python
for i, owoc in enumerate(owoce, start=1):
    print(f"{i}. {owoc}")
```

Z `zip()` – iteracja po wielu sekwencjach równolegle:

```python
imiona = ["Ania", "Bartek"]
wieki  = [25, 30]
for imie, wiek in zip(imiona, wieki):
    print(f"{imie} ma {wiek} lat")
```

![Diagram pętli for](diagrams/for_loop.png)

---

## Pętla `for` – `break`, `continue`, `else`

```python
for i in range(10):
    if i == 3:
        continue    # pomiń i=3
    if i == 7:
        break       # zatrzymaj pętlę przy i=7
    print(i)
else:
    # wykonuje się, jeśli pętla zakończyła się BEZ break
    print("Pętla zakończona normalnie")
```

> Blok `else` po pętli `for` wykonuje się tylko jeśli pętla **nie** została przerwana przez `break`.

---

## Pętla `while`

```python
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1
```

Typowe wzorce:

```python
# Pętla nieskończona z break
while True:
    dane = input("Podaj liczbę (q=koniec): ")
    if dane == "q":
        break
    print(f"Podałeś: {dane}")
```

![Diagram pętli while](diagrams/while_loop.png)

---

## `match / case` – dopasowanie wzorców (Python 3.10+)

Strukturalne dopasowanie wzorców – potężniejsze niż `switch/case` z C/Java.

```python
komenda = "wyjdź"

match komenda:
    case "start":
        print("Uruchamiam...")
    case "stop" | "wyjdź":
        print("Zatrzymuję.")
    case _:
        print(f"Nieznana komenda: {komenda}")
```

Dopasowanie struktury:

```python
punkt = (1, 0)

match punkt:
    case (0, 0):
        print("Środek układu")
    case (x, 0):
        print(f"Na osi X, x={x}")
    case (0, y):
        print(f"Na osi Y, y={y}")
    case (x, y):
        print(f"Punkt ({x}, {y})")
```

![Diagram match/case](diagrams/match_statement.png)

---

## List / Dict / Set Comprehensions

**List comprehension** – zwięzły sposób tworzenia list:

```python
kwadraty = [x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

parzyste = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Zagnieżdżone
macierz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
```

**Dict comprehension:**

```python
kwadraty = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Set comprehension:**

```python
podzielne_3 = {x for x in range(20) if x % 3 == 0}
# {0, 3, 6, 9, 12, 15, 18}
```

**Generator expression** (leniwa ewaluacja, oszczędność pamięci):

```python
suma = sum(x ** 2 for x in range(1_000_000))
```

---

## Obsługa wyjątków – `try / except`

```python
try:
    wynik = 10 / 0
except ZeroDivisionError:
    print("Dzielenie przez zero!")
except (TypeError, ValueError) as e:
    print(f"Błąd: {e}")
else:
    print("Sukces!")     # wykonuje się gdy NIE ma wyjątku
finally:
    print("Zawsze!")     # wykonuje się zawsze
```

---

## Podsumowanie

| Instrukcja | Opis |
|---|---|
| `if/elif/else` | Warunkowe wykonanie bloków kodu |
| `for` | Iteracja po sekwencji / iterowalnym |
| `while` | Pętla z warunkiem logicznym |
| `break` | Przerwanie pętli |
| `continue` | Pominięcie bieżącej iteracji |
| `match/case` | Dopasowanie wzorców (Python 3.10+) |
| `[x for x in ...]` | Wyrażenia listowe |
| `try/except` | Obsługa wyjątków |

---

## Zadania do samodzielnego rozwiązania

Pliki zadań: [`exercises/tasks.py`](exercises/tasks.py) | Rozwiązania: [`exercises/solutions_control_flow.py`](exercises/solutions_control_flow.py)

```bash
pytest control-flow/exercises/test_solutions.py -v
```

### Zadanie 1 – Sito Eratostenesa

Znajdź wszystkie liczby pierwsze ≤ n klasycznym algorytmem z użyciem pętli `for` i `while`.

```python
def sito_eratostenesa(n: int) -> list[int]:
    # 1. [True]*(n+1), ustaw [0],[1]=False
    # 2. for p in range(2, isqrt(n)+1): if [p]: wyzeruj wielokrotności
    # 3. return [i for i, v in enumerate(lista) if v]
    ...

sito_eratostenesa(20)  # → [2, 3, 5, 7, 11, 13, 17, 19]
```

### Zadanie 2 – Sprawdzanie parowania nawiasów

Używając listy jako **stosu**, sprawdź czy nawiasy `()`, `[]`, `{}` są poprawnie sparowane.

```python
def spasuj_nawiasy(tekst: str) -> bool:
    stos = []
    pary = {")": "(", "]": "[", "}": "{"}
    for znak in tekst: ...
    return len(stos) == 0

spasuj_nawiasy("([{}])")  # → True
spasuj_nawiasy("([)]")    # → False
```

### Zadanie 3 – Tabliczka mnożenia (list comprehension)

Zbuduj macierz `n×n` jednym zagnieżdżonym wyrażeniem listowym.

```python
def generuj_tabliczke_mnozenia(n: int) -> list[list[int]]:
    return [[(i+1)*(j+1) for j in range(n)] for i in range(n)]
```

### Zadanie 4 – Grupowanie słów według długości

Pogrupuj słowa wg długości w słowniku `{długość: [posortowane_słowa]}`.

```python
def grupuj_po_dlugosci(slowa: list[str]) -> dict[int, list[str]]:
    # setdefault(), sorted(), dict comprehension
    ...

grupuj_po_dlugosci(["kot","pies","lis","ryba"])
# → {3: ["kot","lis"], 4: ["pies","ryba"]}
```

### Zadanie 5 – Interpreter wyrażeń RPN

Zaimplementuj kalkulator Odwrotnej Notacji Polskiej (stos + pętla `for` + `match/case`).

```python
def interpretuj_wyrazenie(wyrazenie: str) -> float:
    # Token liczba → stos.append, token operator → pop dwa, oblicz, push
    ...

interpretuj_wyrazenie("5 1 2 + 4 * + 3 -")  # → 14.0
```

### Zadanie 6 – FizzBuzz z konfigurowalnymi zasadami

Generuj listę FizzBuzz z dowolnymi zasadami podanymi w słowniku `{dzielnik: etykieta}`.

```python
def fizzbuzz_zaawansowany(n: int, zasady: dict[int, str]) -> list[str]:
    # sorted(zasady.items()) → join etykiet → lub str(liczba)
    ...

fizzbuzz_zaawansowany(15, {3: "Fizz", 5: "Buzz"})
# → ["1","2","Fizz","4","Buzz",...,"FizzBuzz"]
```

---

## Referencje

### Literatura
- Lutz, M. (2013). *Learning Python*, 5th ed. O'Reilly. Część III (Statements and Syntax).
- Beazley, D., Jones, B.K. (2013). *Python Cookbook*, 3rd ed. Rozdział 4 (Iterators).
- Ramalho, L. (2022). *Fluent Python*, 2nd ed. Rozdział 17 (Iterators, Generators).

### Źródła internetowe
- [Python Tutorial – Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [PEP 634 – Structural Pattern Matching](https://peps.python.org/pep-0634/)
- [Python Comprehensions (realpython.com)](https://realpython.com/list-comprehension-python/)
- [Python for Loops (realpython.com)](https://realpython.com/python-for-loop/)
- [Python Exceptions (realpython.com)](https://realpython.com/python-exceptions/)

