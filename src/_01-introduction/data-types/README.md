# Podstawowe typy danych w Pythonie 3

> **Cel:** Poznanie wbudowanych typów danych Pythona: liczb, napisów i typów strukturalnych (list, krotek, słowników, zbiorów) oraz operacji na nich.

---

## System typów w Pythonie

Python jest językiem **dynamicznie typowanym** – typ zmiennej jest określany w czasie wykonania, nie deklaracji.

```python
x = 42          # int
x = 3.14        # teraz float – ta sama zmienna!
x = "Python"    # teraz str
```

Każda wartość w Pythonie jest **obiektem** posiadającym:
- **typ** (`type(x)`)
- **tożsamość** (`id(x)`) – adres w pamięci
- **wartość**

```python
x = 42
print(type(x))   # <class 'int'>
print(id(x))     # np. 140710927381520
```

![Hierarchia typów numerycznych](diagrams/numeric_hierarchy.png)

---

## Liczby całkowite – `int`

Typ `int` w Pythonie ma **nieograniczoną precyzję** (brak przepełnienia jak w C/Java).

```python
a = 42
b = -7
duza = 10 ** 100      # googol – działa!
szesnastkowy = 0xFF   # 255
osemkowy     = 0o17   # 15
binarny      = 0b1010 # 10

print(type(a))        # <class 'int'>
```

### Python 3 vs Python 2 – rozmiar liczb całkowitych

W **Pythonie 2** istniały dwa odrębne typy:
- `int` – liczba stałej długości (zwykle 32 lub 64 bity), czyli zakres ±2 147 483 647 lub ±9 223 372 036 854 775 807.
- `long` – liczba arbitralnej długości (nieograniczona precyzja), zapisywana z sufiksem `L`, np. `99999999999999L`.

W **Pythonie 3** te dwa typy zostały **scalone** – istnieje tylko jeden `int` z nieograniczoną precyzją:

```python
# Python 3 – brak przepełnienia, brak typu "long"
x = 2 ** 100
print(x)              # 1267650600228229401496703205376
print(type(x))        # <class 'int'>

# Obliczenia na bardzo dużych liczbach – np. silnia
import math
print(math.factorial(100))  # 100! – liczba z 158 cyframi, bez problemu

# Liczba bitów potrzebna do reprezentacji
print((2**31 - 1).bit_length())   # 31  (max int32)
print((2**63 - 1).bit_length())   # 63  (max int64)
print((10**100).bit_length())     # 333 (googol)
```

> ⚠️ **Cena elastyczności:** operacje na bardzo dużych liczbach (`10**10_000`) są wolniejsze niż na 64-bitowych `int`, bo wymagają obsługi wielu słów maszynowych. W kodzie numerycznym krytycznym wydajnościowo używaj biblioteki `numpy` z typami o stałej szerokości (`np.int64`).

### Pełny przegląd operacji na liczbach całkowitych

```python
a, b = 17, 5

# Podstawowe działania
print(a + b)    # 22  – dodawanie
print(a - b)    # 12  – odejmowanie
print(a * b)    # 85  – mnożenie
print(a ** b)   # 1419857 – potęgowanie (a do potęgi b)

# Dzielenie
print(a / b)    # 3.4  – "prawdziwe" dzielenie (zawsze float!)
print(a // b)   # 3    – dzielenie całkowite (podłoga)
print(a % b)    # 2    – reszta z dzielenia (modulo)

# Dzielenie całkowite z liczbami ujemnymi – uwaga!
print(-17 // 5)  # -4  (podłoga, NIE obcięcie do zera jak w C!)
print(-17 % 5)   #  3  (zawsze nieujemne gdy dzielnik > 0)

# Funkcje wbudowane
print(abs(-42))          # 42
print(divmod(17, 5))     # (3, 2)  – (iloraz, reszta) jednocześnie
print(pow(2, 10))        # 1024
print(pow(2, 10, 1000))  # 24  – szybkie potęgowanie modulo (kryptografia)

# Konwersje
print(int("42"))         # 42
print(int("FF", 16))     # 255 – z napisu szesnastkowego
print(int("1010", 2))    # 10  – z napisu binarnego
print(bin(255))          # '0b11111111'
print(oct(255))          # '0o377'
print(hex(255))          # '0xff'
```

### Przykłady algorytmów na liczbach całkowitych

```python
# NWD algorytmem Euklidesa
def nwd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

print(nwd(48, 18))  # 6

# NWW
def nww(a: int, b: int) -> int:
    return a * b // nwd(a, b)

print(nww(4, 6))    # 12

# Silnia iteracyjna
def silnia(n: int) -> int:
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

print(silnia(10))   # 3628800

# Cyfry sumy cyfr
def suma_cyfr(n: int) -> int:
    return sum(int(c) for c in str(abs(n)))

print(suma_cyfr(12345))   # 15
```

---

## Liczby zmiennoprzecinkowe – `float`

Standard **IEEE 754** (64-bit double precision):

```python
pi = 3.14159
e  = 2.71828
inf = float('inf')     # nieskończoność
nan = float('nan')     # Not a Number

print(0.1 + 0.2)       # 0.30000000000000004  (!)
print(round(0.1 + 0.2, 10))  # 0.3
```

> ⚠️ Zmiennoprzecinkowe **nie są dokładne** w systemie binarnym.

Dla obliczeń finansowych używaj `Decimal`:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
```

### Zakres i dokładność

Typ `float` w Pythonie to 64-bitowa liczba double precision wg IEEE 754, złożona z:
- 1 bitu znaku
- 11 bitów wykładnika
- 52 bitów mantysy (+ 1 niejawny)

```python
import sys

print(sys.float_info.max)       # ~1.8e+308  – max wartość
print(sys.float_info.min)       # ~2.2e-308  – min wartość normalna
print(sys.float_info.epsilon)   # ~2.2e-16   – epsilon maszynowy
print(sys.float_info.dig)       # 15         – cyfry dziesiętne precyzji
```

**Epsilon maszynowy** (`ε`) to najmniejsza liczba taka, że `1.0 + ε != 1.0`. Wyznaczamy go ręcznie:

```python
eps = 1.0
while 1.0 + eps != 1.0:
    eps /= 2
eps *= 2   # cofamy ostatni krok
print(eps)  # ~2.220446049250313e-16

# Potwierdzenie
print(eps == sys.float_info.epsilon)  # True
```

**Najmniejsza dodatnia liczba zmiennoprzecinkowa** (subnormal):

```python
tiny = sys.float_info.min           # min normalna: ~2.225e-308
tiny_sub = 5e-324                   # min subnormalna (denormalized)
print(tiny_sub > 0)                 # True
print(tiny_sub / 2 == 0.0)         # True – underflow do zera

# Ręczne wyznaczenie metodą bisekcji
x = 1.0
while x / 2 > 0:
    x /= 2
print(x)  # ~5e-324
```

### Porównywanie wyników obliczeń zmiennoprzecinkowych

Błędy zaokrąglenia sprawiają, że bezpośrednie `==` na floatach jest **niebezpieczne**:

```python
a = 0.1 + 0.2
b = 0.3
print(a == b)          # False (!)
print(abs(a - b))      # 5.551115123125783e-17

# Poprawne podejście – porównanie z tolerancją
import math

# Tolerancja absolutna (dla wartości bliskich 0)
print(abs(a - b) < 1e-9)          # True

# Tolerancja względna + absolutna (math.isclose)
print(math.isclose(a, b))                     # True (domyślnie rel_tol=1e-09)
print(math.isclose(a, b, rel_tol=1e-9))       # True
print(math.isclose(1e10, 1e10 + 1, rel_tol=1e-9))  # True  (~ 0 względnie)
print(math.isclose(0.0, 1e-15, abs_tol=1e-9))      # True  (bliskie zera)

# Specjalne wartości
print(math.isinf(float('inf')))    # True
print(math.isnan(float('nan')))    # True
print(float('nan') == float('nan'))  # False  (NaN != NaN!)
```

### Przykłady algorytmów na liczbach rzeczywistych

```python
import math

# 1. Pierwiastek kwadratowy metodą Newtona-Raphsona
def pierwiastek_newton(n: float, eps: float = 1e-10) -> float:
    """Wyznacza sqrt(n) bez użycia math.sqrt."""
    if n < 0:
        raise ValueError("Argument ujemny")
    x = n
    while True:
        nastepny = (x + n / x) / 2
        if abs(x - nastepny) < eps:
            return nastepny
        x = nastepny

print(pierwiastek_newton(2))   # 1.4142135623730951

# 2. Liczba PI metodą Leibniza (wolna, ale czytelna)
def pi_leibniz(n_iter: int = 1_000_000) -> float:
    """π/4 = 1 - 1/3 + 1/5 - 1/7 + ..."""
    pi4 = sum((-1)**k / (2*k + 1) for k in range(n_iter))
    return 4 * pi4

print(f"π ≈ {pi_leibniz():.6f}")  # π ≈ 3.141593

# 3. Suma ciągu harmonicznego – kumulacja błędów
def szereg_harmoniczny(n: int) -> float:
    return sum(1.0 / k for k in range(1, n + 1))

print(szereg_harmoniczny(1000))   # 7.485470860550343

# 4. Rozwiązanie równania kwadratowego (uwaga na dyskryminantę)
def rowna_kwadratowe(a: float, b: float, c: float):
    delta = b**2 - 4*a*c
    if delta < 0:
        return ()
    if delta == 0:
        return (-b / (2*a),)
    sq = math.sqrt(delta)
    return ((-b - sq) / (2*a), (-b + sq) / (2*a))

print(rowna_kwadratowe(1, -3, 2))   # (1.0, 2.0)
print(rowna_kwadratowe(1, 0, 1))    # ()
```

---

## Liczby zespolone – `complex`

### Do czego służą?

Liczby zespolone (postać `a + bj`, gdzie `j = √−1`) są niezbędne w:
- **elektronice i telekomunikacji** – analiza sygnałów (FFT), impedancja
- **fizyce** – mechanika kwantowa, optyka
- **grafice i geometrii** – obroty i skalowanie w 2D (mnożenie = obrót!)
- **sterowaniu** – transmitancja, odpowiedź układu
- **rozwiązywaniu równań** – każde równanie wielomianowe ma rozwiązania w ℂ

### Składnia i operacje

```python
z1 = 3 + 4j              # literał
z2 = complex(1, -2)      # konstruktor: 1 - 2j
z3 = complex(5)          # 5 + 0j

print(z1.real)    # 3.0    – część rzeczywista
print(z1.imag)    # 4.0    – część urojona
print(abs(z1))    # 5.0    – moduł: sqrt(3²+4²)
print(z1.conjugate())  # (3-4j) – sprzężenie

# Działania arytmetyczne
print(z1 + z2)    # (4+2j)
print(z1 - z2)    # (2+6j)
print(z1 * z2)    # (11+2j)   – (3+4j)(1-2j) = 3-6j+4j-8j² = 3-2j+8 = 11+2j
print(z1 / z2)    # (-1+2j)   – dzielenie przez sprzężenie mianownika

# Potęgowanie i funkcje matematyczne
import cmath

print(cmath.sqrt(-1))           # 1j
print(cmath.sqrt(-4))           # 2j
print(cmath.phase(z1))          # 0.9272... rad – argument (kąt)
print(cmath.polar(z1))          # (5.0, 0.927...) – (moduł, argument)
print(cmath.rect(5, cmath.pi/4))  # z z modułu i argumentu

# Wzór Eulera: e^(iπ) + 1 = 0
import math
print(cmath.exp(1j * math.pi))  # (-1+1.2246e-16j) ≈ -1  (błąd zaokrąglenia)
print(cmath.isclose(cmath.exp(1j * math.pi), -1))  # True
```

### Ograniczenia

```python
# Brak operatora < i > – liczby zespolone nie mają porządku liniowego
z = 1 + 2j
# z > 0  # TypeError: '>' not supported between 'complex' and 'int'

# Część rzeczywista i urojona to float – dziedziczą jego niedokładności
print((1+1j) ** 2)   # (1.2246467991473532e-16+2j) ≈ 2j
print(cmath.isclose((1+1j)**2, 2j))  # True

# Konwersja do int/float jest możliwa tylko gdy część urojona ≈ 0
z_real = complex(5, 0)
print(float(z_real.real))  # 5.0
# float(z_real)  # TypeError – nie można bezpośrednio
```

### Przykład: obrót punktu w 2D

Mnożenie przez `e^(iθ)` obraca punkt o kąt `θ`:

```python
import cmath, math

def obrot_2d(punkt: complex, kat_rad: float) -> complex:
    """Obraca punkt o zadany kąt (radianach) wokół zera."""
    return punkt * cmath.exp(1j * kat_rad)

p = 1 + 0j            # punkt (1, 0) na osi X
p90 = obrot_2d(p, math.pi / 2)
print(f"({p90.real:.6f}, {p90.imag:.6f})")  # (0.000000, 1.000000)  → (0, 1)

# Wielokrotny obrót – sześciokąt foremny
n = 6
wierzcholki = [obrot_2d(1+0j, 2*math.pi*k/n) for k in range(n)]
for v in wierzcholki:
    print(f"({v.real:+.3f}, {v.imag:+.3f})")
```

---

## Typ logiczny – `bool`

`bool` jest podklasą `int`: `True == 1`, `False == 0`.

```python
print(True + True)    # 2
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool("tekst"))  # True
print(bool([0]))      # True
```

### Wartości truthy i falsy – które typy i wartości zachowują się jak `False`?

Każdy obiekt w Pythonie może być użyty w warunku `if`. Python wywołuje wewnętrznie `bool(x)`:

| Wartość | Typ | Wartość logiczna |
|---|---|---|
| `False`, `None` | `bool`, `NoneType` | **False** |
| `0`, `0.0`, `0j` | `int`, `float`, `complex` | **False** |
| `""`, `b""` | `str`, `bytes` | **False** |
| `[]`, `()`, `{}`, `set()` | kolekcje puste | **False** |
| Wszystko inne | dowolny | **True** |

```python
# Idiom: zamiast if len(lista) > 0:  pisz:
lista = []
if not lista:
    print("Lista jest pusta")      # wypisuje

# Niespodzianki!
print(bool(0.0))           # False
print(bool(0.00001))       # True
print(bool([False]))       # True  – lista z jednym elementem!
print(bool(()))            # False – pusta krotka
print(bool((False,)))      # True  – krotka z jednym elementem

# Definiowanie zachowania własnych klas przez __bool__ / __len__
class Pojemnik:
    def __init__(self, elementy):
        self.elementy = elementy
    def __bool__(self):
        return len(self.elementy) > 0

p = Pojemnik([])
print(bool(p))              # False
p.elementy.append(1)
print(bool(p))              # True
```

### Spójniki logiczne: `and`, `or`, `not` – leniwa ewaluacja (short-circuit)

Python **nie oblicza całego wyrażenia**, jeśli wynik jest już znany:
- `A and B` – jeśli `A` jest falsy, `B` **nie jest obliczane** → wynik to `A`
- `A or B`  – jeśli `A` jest truthy, `B` **nie jest obliczane** → wynik to `A`

```python
# and: drugi operand NIE jest obliczany gdy pierwszy jest falsy
print(0 and 1/0)      # 0   – brak ZeroDivisionError!
print(1 and 2)        # 2   – oba truthy → ostatni
print(0 and 2)        # 0   – pierwszy falsy → zwraca go
print("" and "abc")   # ""  – pierwszy falsy

# or: drugi operand NIE jest obliczany gdy pierwszy jest truthy
print(1 or 1/0)       # 1   – brak ZeroDivisionError!
print(0 or 42)        # 42  – pierwszy truthy znaleziony
print("" or "domyślny")  # "domyślny"
print(None or [] or 0)   # 0  – wszystkie falsy → ostatni

# not zawsze zwraca bool
print(not 0)       # True
print(not "abc")   # False
print(not not 42)  # True  – podwójne negowanie = konwersja do bool
```

**Praktyczne idiomy** z leniwą ewaluacją:

```python
# Wartość domyślna gdy None lub falsy
def pobierz_imie(dane: dict) -> str:
    return dane.get("imie") or "Anonim"

print(pobierz_imie({"imie": "Ania"}))  # "Ania"
print(pobierz_imie({}))                # "Anonim"
# Uwaga: puste "" też da "Anonim" – czy to pożądane?

# Bezpieczniejsze – tylko None pomijamy:
def pobierz_imie_v2(dane: dict) -> str:
    wartosc = dane.get("imie")
    return wartosc if wartosc is not None else "Anonim"

# Leniwa inicjalizacja – otwieraj plik tylko jeśli istnieje
import os
plik = "config.txt"
zawartosc = os.path.exists(plik) and open(plik).read()
```

### Algorytmy z wyrażeniami logicznymi

```python
# 1. Rok przestępny – złożony warunek logiczny
def jest_przestepen(rok: int) -> bool:
    return (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0

for r in [1900, 2000, 2024, 2100]:
    print(f"{r}: {jest_przestepen(r)}")
# 1900: False, 2000: True, 2024: True, 2100: False

# 2. Walidacja z łańcuchowaniem warunków
def waliduj_haslo(haslo: str) -> bool:
    return (
        len(haslo) >= 8
        and any(c.isupper() for c in haslo)
        and any(c.islower() for c in haslo)
        and any(c.isdigit() for c in haslo)
    )

print(waliduj_haslo("krótkie"))    # False
print(waliduj_haslo("Bezcyfry!"))  # False
print(waliduj_haslo("Silne1!Ab"))  # True

# 3. Filtrowanie z wyrażeniami logicznymi
liczby = range(-5, 6)
parzyste_niezerowe = [x for x in liczby if x and x % 2 == 0]
print(parzyste_niezerowe)   # [-4, -2, 2, 4]

# 4. Zliczanie True (bool jest int!)
oceny = [5, 3, 4, 2, 5, 5, 3]
celujacych = sum(o == 5 for o in oceny)   # sum([True, False, False, ...])
print(f"Oceny 5: {celujacych}")           # 3

# 5. any() i all() – leniwe wersje or/and
print(any(x > 0 for x in [-3, -1, 2]))   # True  (znajdzie 2)
print(all(x > 0 for x in [1, 2, -1]))    # False (znajdzie -1)
print(all(x > 0 for x in []))            # True  (vacuously true)
print(any(x > 0 for x in []))            # False
```

---

## Napisy – `str`

Napisy (łańcuchy znaków) są **niemutowalne** i **sekwencjami znaków Unicode**.

```python
s1 = 'Witaj'
s2 = "Świecie"
s3 = """Tekst
wieloliniowy"""
raw = r"C:\nowy\folder"   # surowy napis (r-string)
```

Konkatenacja i powtarzanie:

```python
pełny = s1 + ", " + s2 + "!"
echo  = "ha" * 3          # "hahaha"
```

![Operacje na napisach str](diagrams/string_operations.png)

---

## Napisy – f-stringi i formatowanie

```python
imie = "Anna"
wiek = 30
pi   = 3.14159

# f-string (Python 3.6+)
print(f"Witaj, {imie}! Masz {wiek} lat.")
print(f"Pi ≈ {pi:.2f}")        # Pi ≈ 3.14
print(f"Szesnastkowo: {255:#x}")  # 0xff

# format()
print("Witaj, {}! Masz {} lat.".format(imie, wiek))

# %-formatowanie (stary styl)
print("Witaj, %s! Masz %d lat." % (imie, wiek))
```

---

## Napisy – przydatne metody

```python
s = "  Python 3 jest super!  "

print(s.strip())              # "Python 3 jest super!"
print(s.lower())              # "  python 3 jest super!  "
print(s.upper())              # "  PYTHON 3 JEST SUPER!  "
print(s.replace("super", "świetny"))
print(s.split())              # ['Python', '3', 'jest', 'super!']
print(",".join(["a", "b"]))   # "a,b"
print("Python".startswith("Py"))  # True
print("Python" in "Python 3")     # True
print(len("Python"))          # 6
```

Indeksowanie i wycinki:

```python
s = "Python"
print(s[0])     # 'P'
print(s[-1])    # 'n'
print(s[1:4])   # 'yth'
print(s[::-1])  # 'nohtyP'
```

---

## Lista – `list`

Lista to **mutowalna**, **uporządkowana** sekwencja obiektów dowolnego typu.

```python
owoce = ["jabłko", "banan", "wiśnia"]
mieszana = [1, "dwa", 3.0, True, [5, 6]]

owoce.append("mango")         # dodanie na koniec
owoce.insert(1, "agrest")     # wstawienie na pozycję
owoce.remove("banan")         # usunięcie pierwszego wystąpienia
usuniety = owoce.pop(0)       # usunięcie i zwrot elementu
owoce.sort()                  # sortowanie w miejscu
print(sorted(owoce))          # nowa posortowana lista
print(owoce[:2])              # wycinek – pierwsze 2 elementy
print(len(owoce))             # długość
```

![Wbudowane typy kolekcyjne](diagrams/builtin_collections.png)

---

## Krotka – `tuple`

Krotka to **niemutowalna**, **uporządkowana** sekwencja – "zamrożona lista".

```python
punkt   = (3, 4)
rgb     = (255, 128, 0)
jeden   = (42,)           # krotka jednoelementowa – WAŻNY przecinek!
pusta   = ()

# rozpakowywanie (unpacking)
x, y = punkt
print(f"x={x}, y={y}")

# swap
a, b = 1, 2
a, b = b, a

# jako klucz słownika (listy nie mogą!)
d = {(0, 0): "środek", (1, 0): "prawo"}
```

---

## Słownik – `dict`

Słownik to **mutowalny**, **nieuporządkowany** (od Python 3.7 – zachowuje kolejność wstawiania) zbiór par **klucz–wartość**.

```python
osoba = {"imie": "Ania", "wiek": 25, "miasto": "Kraków"}

print(osoba["imie"])              # "Ania"
print(osoba.get("email", "brak")) # bezpieczny dostęp
osoba["email"] = "ania@example.com"
del osoba["miasto"]

for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")

print(list(osoba.keys()))         # ['imie', 'wiek', 'email']
print(list(osoba.values()))
```

---

## Zbiór – `set`

Zbiór to **mutowalny**, **nieuporządkowany** zbiór **unikalnych** wartości.

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 | s2)   # suma:         {1, 2, 3, 4, 5, 6}
print(s1 & s2)   # część wspólna: {3, 4}
print(s1 - s2)   # różnica:       {1, 2}
print(s1 ^ s2)   # różnica sym.:  {1, 2, 5, 6}

s1.add(10)
s1.discard(1)    # usuwa, nie rzuca błędu gdy brak

# Usuwanie duplikatów z listy
unikalne = list(set([1, 2, 2, 3, 3, 3]))
```

`frozenset` – niemutowalna wersja zbioru.

---

## Mutowalność i niemutowalność typów danych

**Mutowalność** to zdolność obiektu do zmiany swojego stanu po utworzeniu.

| Mutowalny (można modyfikować) | Niemutowalny (każda "zmiana" = nowy obiekt) |
|---|---|
| `list`, `dict`, `set`, `bytearray` | `int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes` |

```python
# Niemutowalny – próba zmiany tworzy NOWY obiekt
s = "Python"
s2 = s + " 3"        # nowy napis; s nadal wskazuje na "Python"
print(s is s2)       # False

# Mutowalny – modyfikacja w miejscu
lst = [1, 2, 3]
lst2 = lst           # obie zmienne WSKAZUJĄ na TEN SAM obiekt!
lst2.append(4)
print(lst)           # [1, 2, 3, 4]  – lst też się zmieniło!

# Bezpieczna kopia mutowanego obiektu
import copy
lst3 = copy.copy(lst)     # płytka kopia – niezależna na poziomie 1
lst4 = copy.deepcopy(lst) # głęboka kopia – niezależna rekurencyjnie
```

**Dlaczego mutowalność ma znaczenie?**
- Niemutowalne obiekty są **bezpieczne do współdzielenia** (brak ukrytych efektów ubocznych)
- Niemutowalne typy mogą być **kluczami słownika** i **elementami zbioru** (muszą być hashowalne)
- Mutowalne typy pozwalają **modyfikować duże struktury danych bez kopiowania** (wydajność)

> 🔍 Szerzej omówione w module: [mutability/README.md](../mutability/README.md)

---

## Jak wybrać właściwą strukturę danych?

Dobór struktury danych to jedna z ważniejszych decyzji projektowych. Poniższy przewodnik pomoże wybrać właściwy typ:

### Diagram decyzyjny

```
Mam kolekcję elementów...
│
├─ Czy musi pamiętać kolejność?
│   ├─ TAK → Czy może się zmieniać?
│   │         ├─ TAK  → list
│   │         └─ NIE  → tuple  (niemutowalna, hashowalna)
│   └─ NIE → Czy elementy muszą być unikalne?
│             ├─ TAK  → set / frozenset
│             └─ NIE  → list (ale rozważ set dla szybkiego wyszukiwania)
│
Mam pary klucz–wartość...
└─ dict  (klucze muszą być hashowalne: str, int, tuple)
```

### Porównanie złożoności czasowej

| Operacja | `list` | `set` | `dict` |
|---|---|---|---|
| Dostęp po indeksie | O(1) | – | – |
| Dostęp po kluczu | – | – | O(1) |
| Wyszukiwanie `x in ...` | **O(n)** | **O(1)** | O(1) (klucze) |
| Dodanie elementu | O(1) amort. | O(1) amort. | O(1) amort. |
| Usunięcie elementu | O(n) | O(1) amort. | O(1) amort. |

### Kiedy co wybrać – praktyczne wskazówki

```python
# LIST – gdy ważna kolejność i możliwe duplikaty
kolejka_zadan = ["task1", "task2", "task3"]
historia_krokow = [1, 1, 2, 3, 5, 8]     # duplikaty OK

# TUPLE – gdy dane są stałe lub mają być kluczem
punkt = (3.0, 4.0)                  # stały punkt 2D
kolor_rgb = (255, 128, 0)           # niemutowalny
mapa = {(0,0): "start", (5,5): "meta"}   # krotka jako klucz dict!

# SET – gdy zależy na unikalności lub szybkim wyszukiwaniu
odwiedzeni_uzytkownicy = set()
odwiedzeni_uzytkownicy.add("user_42")
if "user_42" in odwiedzeni_uzytkownicy:   # O(1) – super szybkie!
    print("Znany użytkownik")

# Usuwanie duplikatów z listy (bez zachowania kolejności)
unikalne = list(set([3, 1, 4, 1, 5, 9, 2, 6, 5]))

# DICT – gdy potrzebujesz mapowania klucz→wartość
cache = {}                          # memoizacja
counter = {}                        # zliczanie wystąpień
for slowo in ["a", "b", "a", "c", "b", "a"]:
    counter[slowo] = counter.get(slowo, 0) + 1
# {'a': 3, 'b': 2, 'c': 1}

# FROZENSET – gdy potrzebujesz unikalnych elementów ALE niemutowalnych
# np. klucz słownika będący zbiorem
relacje = {frozenset({"Ania", "Bartek"}): "znajomi"}

# collections.deque zamiast list – gdy dużo operacji na początku
from collections import deque
kolejka = deque([1, 2, 3])
kolejka.appendleft(0)    # O(1) – list.insert(0,...) to O(n)!
```

### Kiedy NIE używać danego typu

```python
# ŹLE: lista jako zbiór (wolne wyszukiwanie)
niedozwolone_emaile = ["spam@x.com", "hack@y.com", ...]
if email in niedozwolone_emaile:   # O(n) – wolne!
    ...

# DOBRZE: zbiór
niedozwolone_emaile = {"spam@x.com", "hack@y.com", ...}
if email in niedozwolone_emaile:   # O(1) – szybkie!
    ...

# ŹLE: słownik zamiast krotki dla stałych danych punktu
punkt = {"x": 3.0, "y": 4.0}   # mutowalny, więcej pamięci

# DOBRZE: krotka lub namedtuple
from collections import namedtuple
Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(3.0, 4.0)
print(p.x, p.y)    # czytelna składnia + niemutowalność
```

---

## Przegląd wbudowanych typów

| Typ | Przykład | Mutowalny | Uporządkowany | Unikalność |
|---|---|---|---|---|
| `int`, `float`, `complex` | `42`, `3.14`, `2j` | ✗ | – | – |
| `str` | `"Python"` | ✗ | ✓ | – |
| `list` | `[1, 2, 3]` | ✓ | ✓ | – |
| `tuple` | `(1, 2, 3)` | ✗ | ✓ | – |
| `dict` | `{"a": 1}` | ✓ | ✓ (3.7+) | klucze |
| `set` | `{1, 2, 3}` | ✓ | ✗ | ✓ |
| `frozenset` | `frozenset({1})` | ✗ | ✗ | ✓ |
| `bool` | `True`, `False` | ✗ | – | – |
| `bytes` | `b"data"` | ✗ | ✓ | – |

---

## Zadania do samodzielnego rozwiązania

Pliki zadań: [`exercises/tasks.py`](exercises/tasks.py) | Rozwiązania: [`exercises/solutions_data_types.py`](exercises/solutions_data_types.py)

```bash
pytest data-types/exercises/test_solutions.py -v
```

### Zadanie 1 – Statystyki numeryczne

Oblicz min, max, sumę, średnią i zakres listy liczb. Rzuć `ValueError` dla pustej listy.

```python
def statystyki(liczby: list[float]) -> dict:
    # {"min": ..., "max": ..., "suma": ..., "srednia": ..., "zakres": ...}
    ...
```

### Zadanie 2 – Analiza napisu

Zbuduj słownik z metadanymi napisu: długość, lista słów, unikalne znaki, czy palindrom.

```python
def analizuj_napis(tekst: str) -> dict:
    # Wskazówka: tekst.split(), set comprehension, oczyszczony[::-1]
    ...

analizuj_napis("Kayak")["czy_palindrom"]  # → True
```

### Zadanie 3 – Zliczanie wystąpień (bez Counter)

Zbuduj słownik `{element: liczba_wystąpień}` posortowany malejąco po wartości.

```python
def zlicz_wystapienia(sekwencja: list) -> dict:
    # Nie używaj collections.Counter!
    ...

zlicz_wystapienia(["a","b","a","c","b","a"])  # → {"a":3, "b":2, "c":1}
```

### Zadanie 4 – Macierz 2D bez pułapki mutowalności

Utwórz macierz `wiersze × kolumny` z **niezależnymi** wierszami (nie `[[0]*n]*m`!).

```python
def zbuduj_macierz(wiersze: int, kolumny: int, wartosc=0) -> list[list]:
    # Użyj list comprehension: [[wartosc]*kolumny for _ in range(wiersze)]
    ...

m = zbuduj_macierz(3, 3)
m[0][0] = 99
assert m[1][0] == 0   # wiersze są niezależne!
```

### Zadanie 5 – Operacje teoriomnogościowe

Oblicz sumę, część wspólną, różnicę i różnicę symetryczną dwóch list jako zbiorów.

```python
def operacje_na_zbiorach(lista_a: list, lista_b: list) -> dict:
    # Użyj operatorów: |, &, -, ^, isdisjoint()
    ...
```

### Zadanie 6 – Precyzyjne obliczenia finansowe

Przelicz kwotę przez kurs używając `Decimal` (nie `float`!) z zaokrągleniem `ROUND_HALF_UP`.

```python
from decimal import Decimal, ROUND_HALF_UP

def konwersja_walut(kwota: str, kurs: str) -> str:
    # Decimal(kwota) * Decimal(kurs) → .quantize(Decimal("0.01"), ...)
    ...
```

---

## Referencje

### Przykłady kodu w tym module
- [`examples/numeric_types.py`](examples/numeric_types.py) – wszystkie typy liczbowe: int, float, epsilon, algorytmy, complex, Decimal
- [`examples/strings.py`](examples/strings.py) – napisy i operacje na napisach
- [`examples/collections_demo.py`](examples/collections_demo.py) – list, tuple, dict, set

### Literatura
- Lutz, M. (2013). *Learning Python*, 5th ed. O'Reilly. Część II: Types and Operations.
- Beazley, D., Jones, B.K. (2013). *Python Cookbook*, 3rd ed. O'Reilly. Rozdział 1 (Data Structures).
- Ramalho, L. (2022). *Fluent Python*, 2nd ed. O'Reilly. Rozdział 2 (Sequences).
- Goldberg, D. (1991). *What Every Computer Scientist Should Know About Floating-Point Arithmetic*. ACM Computing Surveys.

### Źródła internetowe
- [Built-in Types – Python 3 docs](https://docs.python.org/3/library/stdtypes.html)
- [Python Data Types (realpython.com)](https://realpython.com/python-data-types/)
- [Python f-strings](https://realpython.com/python-f-strings/)
- [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [decimal – Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html)
- [cmath – Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
- [Python int – arbitrary precision (realpython.com)](https://realpython.com/python-numbers/#integers)
- [math.isclose – porównywanie floatów](https://docs.python.org/3/library/math.html#math.isclose)

