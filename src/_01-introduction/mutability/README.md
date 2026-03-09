# Typy mutowalne i niemutowalne w Pythonie 3

> **Cel:** Zrozumienie modelu pamięci Pythona, różnicy między obiektami mutowalnymi a niemutowalnymi oraz konsekwencji dla pisania bezpiecznego i przewidywalnego kodu.

---

## Model obiektowy Pythona

W Pythonie **każda wartość jest obiektem**. Zmienna to tylko **etykieta (referencja)** przywiązana do obiektu w pamięci, nie pojemnik na wartość.

```python
x = 42
y = x       # y wskazuje NA TEN SAM obiekt co x

print(id(x) == id(y))   # True – ten sam obiekt!
print(x is y)           # True
```

Kluczowe funkcje:
- `id(obj)` – unikalny identyfikator obiektu (adres w pamięci)
- `type(obj)` – typ obiektu
- `obj is obj2` – czy to ten **sam obiekt** (nie: ta sama wartość!)
- `obj == obj2` – czy ta sama **wartość**

![Model pamięci – stos i sterta](diagrams/memory_model.png)

---

## Dlaczego mutowalność istnieje w językach programowania?

Rozróżnienie na typy mutowalne i niemutowalne to **świadoma decyzja projektowa**, która pojawia się w większości nowoczesnych języków (Python, Rust, Kotlin, Swift, Scala, Haskell…). Wynika z fundamentalnego kompromisu:

### Niemutowalność – stabilność i bezpieczeństwo

Jeśli obiekt **nigdy nie zmienia wartości** po utworzeniu:
- Można go **bezpiecznie współdzielić** między wątkami bez blokad (thread-safe bez mutexów)
- Można go używać jako **klucza słownika** lub elementu zbioru (hash pozostaje stały)
- Łatwiej rozumować o programie: wartość w miejscu A nie zmieni się przez kod w miejscu B
- Można go **buforować (memoizować)** – te same argumenty dają zawsze ten sam wynik
- Język może go **internować** (współdzielić jeden egzemplarz w pamięci – np. małe `int`, krótkie `str`)

```python
# Niemutowalny obiekt bezpiecznie współdzielony jako klucz
punkt = (3, 4)
mapa = {punkt: "punkt startowy"}   # OK – krotka jest niemutowalna

# Memoizacja działa tylko dla niemutowalnych argumentów
from functools import lru_cache
@lru_cache
def odleglosc(p1: tuple, p2: tuple) -> float:
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2) ** 0.5
```

### Mutowalność – wydajność i wygoda

Jeśli obiekt **może być modyfikowany w miejscu**:
- Unikamy kopiowania dużych struktur danych przy każdej zmianie (wydajność O(1) vs O(n))
- Można budować struktury dynamiczne (listy, słowniki) inkrementalnie
- Algorytmy in-place (sortowanie, przetwarzanie buforów) są prostsze i szybsze

```python
# Mutowalność pozwala modyfikować duże struktury bez kopiowania
bufor = bytearray(1_000_000)   # 1 MB mutowalnych bajtów
bufor[0] = 0xFF                # O(1) – bez kopiowania całości!

# Porównaj z niemutowalnym bytes:
dane = b"\x00" * 1_000_000
nowe_dane = bytes([0xFF]) + dane[1:]   # O(n) – tworzy nowy obiekt!
```

### Zasada projektowania: domyślnie niemutowalne

Wiele nowoczesnych języków (Rust, Kotlin, Swift) przyjmuje zasadę: **zmienne są domyślnie niemutowalne**, a mutowalność trzeba jawnie zadeklarować (`var` vs `val`, `mut`). Python nie wymusza tego, ale dobry styl kodu powinien:
- preferować `tuple` zamiast `list` gdy dane są stałe
- preferować `frozenset` zamiast `set` gdy zbiór się nie zmienia
- unikać modyfikacji argumentów funkcji (funkcje czyste)

---

## Niemutowalne (immutable)

Obiekt **niemutowalny** po utworzeniu **nie może zostać zmieniony**. Każda "modyfikacja" tworzy **nowy obiekt**.

Typy niemutowalne:
- `int`, `float`, `complex`, `bool`
- `str`
- `tuple`
- `frozenset`
- `bytes`

```python
s = "Python"
print(id(s))       # np. 140234567890

s += " 3"          # NIE modyfikuje obiektu "Python" –
                   # tworzy NOWY napis "Python 3"
print(id(s))       # INNY id!
```

![Mutowalny vs niemutowalny – model pamięci](diagrams/mutable_vs_immutable.png)

---

## Mutowalne (mutable)

Obiekt **mutowalny** może być zmieniany **w miejscu** (in-place) – bez tworzenia nowego obiektu.


Typy mutowalne:
- `list`
- `dict`
- `set`
- `bytearray` ← mutowalna sekwencja bajtów (patrz niżej)
- Instancje klas (domyślnie)

```python
lst = [1, 2, 3]
print(id(lst))       # np. 140234999000

lst.append(4)        # MODYFIKUJE istniejący obiekt
print(id(lst))       # TEN SAM id!
print(lst)           # [1, 2, 3, 4]
```

### `bytes` vs `bytearray` – niemutowalna i mutowalna sekwencja bajtów

Typ `bytes` to **niemutowalna** sekwencja bajtów (0–255) – odpowiednik `str` dla danych binarnych.  
Typ `bytearray` to **mutowalna** wersja `bytes` – można modyfikować poszczególne bajty w miejscu.

```python
# bytes – niemutowalny (jak str)
b = b"Python"
print(type(b))           # <class 'bytes'>
print(b[0])              # 80  (kod ASCII 'P')
# b[0] = 112            # TypeError: 'bytes' object does not support item assignment

# bytearray – mutowalny
ba = bytearray(b"Python")
print(type(ba))          # <class 'bytearray'>
ba[0] = 112              # 'p' – modyfikacja w miejscu!
print(ba)                # bytearray(b'python')
ba.append(33)            # dodanie bajtu '!'
print(bytes(ba))         # b'python!'

# Typowe zastosowania bytearray:
# - buforowanie odczytów z pliku / sieci (unikamy tworzenia nowych obiektów)
# - modyfikacja surowych danych binarnych (obrazy, protokoły sieciowe)
# - algorytmy kryptograficzne działające na bajtach

# Konwersja
ba2 = bytearray(b"hello")
frozen = bytes(ba2)          # bytearray → bytes (niemutowalny)
ba3 = bytearray(frozen)      # bytes → bytearray (mutowalny)
```

> **Kiedy `bytearray` zamiast `bytes`?** Gdy wielokrotnie modyfikujesz dane binarne (np. bufor sieciowy) – `bytearray` robi to **w miejscu**, `bytes` tworzyłby nowy obiekt przy każdej zmianie.

---

## Pułapka: współdzielone referencje

```python
a = [1, 2, 3]
b = a           # b wskazuje NA TEN SAM obiekt!

b.append(4)
print(a)        # [1, 2, 3, 4]  (!)
print(a is b)   # True
```

Rozwiązanie – płytka kopia:

```python
b = a.copy()        # lub a[:]  lub list(a)
b.append(4)
print(a)            # [1, 2, 3]  – niezmienione
print(a is b)       # False
```

Głęboka kopia (dla zagnieżdżonych struktur):

```python
import copy
b = copy.deepcopy(a)
```

---

## Kopia płytka i kopia głęboka

### Definicje

**Kopia płytka** (`shallow copy`) tworzy nowy obiekt kontenera, ale jego **elementy są nadal referencjami do tych samych obiektów co oryginał**. Działa na „jednym poziomie głębokości".

**Kopia głęboka** (`deep copy`) tworzy nowy obiekt kontenera **i rekurencyjnie kopiuje wszystkie zagnieżdżone obiekty**. Wynik jest w pełni niezależny od oryginału.

### Różnica wizualnie

```
Oryginał:   lista_a → [obj1, obj2, [nested_a, nested_b]]
                                    ↑
Płytka:     lista_b → [obj1, obj2, <ta sama referencja>]
                                    ↑ (współdzielona!)
Głęboka:    lista_c → [obj1, obj2, [nested_a_kopia, nested_b_kopia]]
                                    ↑ (nowy, niezależny obiekt)
```

### Jak uzyskać kopię

```python
import copy

oryg = [[1, 2], [3, 4], [5, 6]]

# 1. PŁYTKA KOPIA – sposoby
plytka_a = oryg.copy()           # metoda .copy() (list, dict, set)
plytka_b = oryg[:]               # wycinek (tylko listy i sekwencje)
plytka_c = list(oryg)            # konstruktor kolekcji
plytka_d = copy.copy(oryg)       # moduł copy – działa dla każdego obiektu

# Sprawdzenie: kontenery są różne, ale elementy wspólne
print(plytka_a is oryg)          # False – różne listy
print(plytka_a[0] is oryg[0])    # True  – TEN SAM zagnieżdżony obiekt!

oryg[0].append(99)               # modyfikacja zagnieżdżonego obiektu
print(plytka_a[0])               # [1, 2, 99]  – WIDOCZNE w kopii płytkiej!

# 2. GŁĘBOKA KOPIA
gleboka = copy.deepcopy(oryg)

print(gleboka is oryg)           # False
print(gleboka[0] is oryg[0])     # False – RÓŻNE zagnieżdżone obiekty!

oryg[1].append(99)
print(gleboka[1])                # [3, 4]  – kopia głęboka NIE widzi zmian!
```

### Płytka kopia słownika i zbioru

```python
import copy

# dict
d = {"a": [1, 2, 3], "b": [4, 5, 6]}
plytka = d.copy()           # lub dict(d) lub {**d}
gleboka = copy.deepcopy(d)

d["a"].append(99)
print(plytka["a"])          # [1, 2, 99]   – płytka widzi zmianę!
print(gleboka["a"])         # [1, 2, 3]    – głęboka nie!

# set
s = {1, 2, 3}
kopia_s = s.copy()          # set nie ma zagnieżdżeń → płytka = głęboka
```

### Kiedy płytka, a kiedy głęboka?

| Sytuacja | Zalecenie |
|---|---|
| Elementy to liczby, napisy, krotki (niemutowalne) | Płytka kopia wystarczy |
| Kolekcja zawiera listy, słowniki, inne mutowalne obiekty | **Głęboka kopia** |
| Chcesz uniezależnić całą strukturę drzewa/grafu | **Głęboka kopia** |
| Zależy Ci na wydajności (duże dane) | Płytka kopia + świadome zarządzanie referencjami |
| Przekazujesz dane do funkcji, która może je modyfikować | Przekaż kopię (płytką lub głęboką) |

### Wydajność i pułapki `deepcopy`

```python
import copy, time

# deepcopy jest WOLNIEJSZY od copy – unikaj dla dużych niezmiennych struktur
duza_lista = list(range(100_000))

t0 = time.perf_counter()
_ = copy.copy(duza_lista)
print(f"copy:     {time.perf_counter()-t0:.4f}s")

t0 = time.perf_counter()
_ = copy.deepcopy(duza_lista)
print(f"deepcopy: {time.perf_counter()-t0:.4f}s")   # ~10x wolniej

# deepcopy obsługuje cykliczne referencje (copy ich nie!)
a = [1, 2]
a.append(a)    # cykliczna referencja!
b = copy.deepcopy(a)    # OK – deepcopy to wykrywa i obsługuje
# copy.copy(a)          # pętla nieskończona (bez obsługi cykli)
```

### Dlaczego kopia płytka/głęboka jest ważna?

1. **Unikanie ukrytych efektów ubocznych** – funkcja modyfikująca "swoją" kopię danych nie powinna zmieniać danych wywołującego.
2. **Bezpieczne testowanie** – testy operują na niezależnych kopiach stanu.
3. **Wzorzec Command/Undo** – historia operacji przechowuje głębokie kopie stanów.
4. **Wielowątkowość** – niezależne kopie danych eliminują wyścigi (race conditions).

```python
# Wzorzec: funkcja czysta – nie modyfikuje wejścia
import copy

def dodaj_element_czysto(lista: list, element) -> list:
    """Zwraca NOWĄ listę z dodanym elementem – oryginał niezmieniony."""
    nowa = copy.copy(lista)   # lub lista + [element]
    nowa.append(element)
    return nowa

oryginalna = [1, 2, 3]
nowa = dodaj_element_czysto(oryginalna, 4)
print(oryginalna)   # [1, 2, 3]   – niezmieniona!
print(nowa)         # [1, 2, 3, 4]
```

---

## Niemutowalność a słowniki i zbiory

Klucze słownika i elementy zbioru muszą być **hashowalne** (co implikuje niemutowalność):

```python
d = {(1, 2): "punkt"}  # OK – krotka jest niemutowalna
# d = {[1, 2]: "lista"} # TypeError: unhashable type: 'list'

s = {frozenset({1, 2}), frozenset({3, 4})}  # OK
# s = {{1, 2}, {3, 4}}  # TypeError: unhashable type: 'set'
```

---

## Pułapka: mutowalny domyślny argument funkcji

To jeden z najczęstszych błędów w Pythonie:

```python
# ŹLE – domyślna lista tworzona RAZ przy definicji funkcji!
def dodaj(element, lista=[]):
    lista.append(element)
    return lista

print(dodaj(1))   # [1]
print(dodaj(2))   # [1, 2]  (!) – nie [2]
print(dodaj(3))   # [1, 2, 3]  (!)
```

Poprawna wersja – użyj `None` jako wartości domyślnej:

```python
# DOBRZE
def dodaj(element, lista=None):
    if lista is None:
        lista = []
    lista.append(element)
    return lista

print(dodaj(1))   # [1]
print(dodaj(2))   # [2]  ✓
```

---

## Internowanie obiektów (interning)

CPython optymalizuje pamięć przez **współdzielenie małych obiektów**:

```python
# Małe liczby całkowite (-5 do 256) są internowane
a = 256
b = 256
print(a is b)   # True  – ten sam obiekt

a = 257
b = 257
print(a is b)   # False – różne obiekty (poza CPython REPL może być True)

# Internowanie napisów (krótkie, identyfikatoropodobne)
s1 = "python"
s2 = "python"
print(s1 is s2)  # True – najczęściej (nie gwarantowane!)
```

> ⚠️ Nie polegaj na `is` do porównywania wartości – używaj `==`.

---

## Niemutowalność jako wzorzec projektowy

**Zalety niemutowalności:**
- Bezpieczeństwo w programowaniu wielowątkowym (thread-safe)
- Obiekty mogą być kluczami słownika / elementami zbioru
- Łatwiejsze rozumowanie o kodzie (brak ukrytych modyfikacji)
- Możliwość buforowania (memoizacja)

### Memoizacja z `@lru_cache` – wyjaśnienie

`@lru_cache(maxsize=None)` to **dekorator** z modułu `functools`, który **zapamiętuje wyniki** wywołań funkcji w wewnętrznym słowniku (cache). Gdy funkcja zostanie wywołana ponownie z tymi samymi argumentami, zwraca **zapamiętany wynik** zamiast ponownie wykonywać obliczenia.

Rozkład składni:
- **`@`** – operator dekorowania: `lru_cache(maxsize=None)(fibonacci)` w skróconej formie
- **`lru_cache`** – *Least Recently Used cache* – cache słownikowy usuwający najdawniej używane wpisy gdy jest pełny
- **`maxsize=None`** – brak limitu rozmiaru cache (przechowuj wszystkie wyniki); `maxsize=128` ograniczyłoby do 128 ostatnich wywołań

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Rekurencyjna Fibonacci z memoizacją – O(n) zamiast O(2^n)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))   # 12586269025 – szybko, dzięki cache
print(fibonacci(100))  # obliczone w mikrosekundach

# Statystyki cache
info = fibonacci.cache_info()
print(info)   # CacheInfo(hits=149, misses=101, maxsize=None, currsize=101)
#   hits   – ile razy wynik był już w cache
#   misses – ile razy trzeba było naprawdę obliczyć
#   currsize – ile wyników jest teraz w cache

fibonacci.cache_clear()   # czyszczenie cache
```

**Dlaczego niemutowalność argumentów jest KONIECZNA dla cache?**

Cache używa argumentów jako **klucza słownika**. Klucze muszą być hashowalne → niemutowalne. Dlatego `lru_cache` działa tylko dla funkcji przyjmujących niemutowalne argumenty:

```python
# OK – int jest niemutowalny i hashowalny
@lru_cache(maxsize=128)
def potega(podstawa: int, wykladnik: int) -> int:
    return podstawa ** wykladnik

# ŹLE – lista jest mutowalna, nie można jej użyć jako klucza
@lru_cache(maxsize=128)
def suma_listy(lst: list) -> int:   # TypeError przy wywołaniu!
    return sum(lst)

# OBEJŚCIE – konwertuj na tuple (niemutowalną)
@lru_cache(maxsize=128)
def suma_krotki(t: tuple) -> int:
    return sum(t)

print(suma_krotki((1, 2, 3, 4)))   # OK
```

**Nowoczesny skrót (Python 3.9+):** `@cache` = `@lru_cache(maxsize=None)`:

```python
from functools import cache

@cache
def silnia(n: int) -> int:
    return 1 if n == 0 else n * silnia(n - 1)
```

---

## Podsumowanie

| Cecha | Niemutowalne | Mutowalne |
|---|---|---|
| Modyfikacja | Tworzy nowy obiekt | Zmiana w miejscu |
| Hashowalne (klucz dict) | ✓ | ✗ |
| Współdzielenie referencji | Bezpieczne | Wymaga ostrożności |
| Typy | `int`, `str`, `tuple`, `frozenset` | `list`, `dict`, `set` |

---

## Zadania do samodzielnego rozwiązania

Pliki zadań: [`exercises/tasks.py`](exercises/tasks.py) | Rozwiązania: [`exercises/solutions_mutability.py`](exercises/solutions_mutability.py)

```bash
pytest mutability/exercises/test_solutions.py -v
```

### Zadanie 1 – Aktualizacja bez mutacji oryginału

Zwróć **nowy** słownik z dodanym kluczem, nie zmieniając oryginału.

```python
def bezpieczna_aktualizacja(slownik: dict, klucz: str, wartosc) -> dict:
    # slownik.copy() → dodaj klucz → zwróć nowy
    ...

d = {"a": 1}
nowy = bezpieczna_aktualizacja(d, "b", 2)
assert d == {"a": 1}   # oryginał niezmieniony!
```

### Zadanie 2 – Usuwanie duplikatów z zachowaniem kolejności

Usuń duplikaty z listy zachowując kolejność pierwszego wystąpienia. Nie modyfikuj oryginału.

```python
def usun_duplikaty_zachowujac_kolejnosc(lista: list) -> list:
    # set() do śledzenia widzianych, lista do budowania wyniku
    ...

usun_duplikaty_zachowujac_kolejnosc([3,1,4,1,5,9,2,6,5,3])
# → [3, 1, 4, 5, 9, 2, 6]
```

### Zadanie 3 – Dekorator cache (memoizacja)

Zaimplementuj dekorator cachujący wyniki wywołań funkcji w słowniku `wrapper.cache`.

```python
def rozbuduj_cache(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper
```

### Zadanie 4 – Głęboka aktualizacja słownika

Scal rekurencyjnie dwa słowniki: dla zagnieżdżonych słowników scalaj, dla pozostałych nadpisuj.

```python
def gleboka_aktualizacja(cel: dict, zrodlo: dict) -> dict:
    # isinstance(v, dict) → rekurencja, else → nadpisz
    ...

cel = {"b": {"x": 10, "y": 20}}
gleboka_aktualizacja(cel, {"b": {"y": 99, "z": 30}})
# → {"b": {"x": 10, "y": 99, "z": 30}}   # x ocalało!
```

### Zadanie 5 – Zamrożenie struktury danych

Przekształć rekurencyjnie: `list → tuple`, `dict → frozenset par`, `set → frozenset`.

```python
def zamroz_strukture(obj):
    # isinstance(obj, list) → tuple(...)
    # isinstance(obj, dict) → frozenset(...)
    # isinstance(obj, set)  → frozenset(...)
    ...

zamroz_strukture([1, [2, 3], {4, 5}])
# → (1, (2, 3), frozenset({4, 5}))
```

---

## Referencje

### Przykłady kodu w tym module
- [`examples/mutable_demo.py`](examples/mutable_demo.py) – demonstracja typów mutowalnych
- [`examples/immutable_demo.py`](examples/immutable_demo.py) – demonstracja typów niemutowalnych, internowanie, memoizacja

### Literatura
- Lutz, M. (2013). *Learning Python*, 5th ed. O'Reilly. Rozdział 6 (Mutable/Immutable).
- Ramalho, L. (2022). *Fluent Python*, 2nd ed. O'Reilly. Rozdział 2 i 8.
- Beazley, D., Jones, B.K. (2013). *Python Cookbook*, 3rd ed. Rozdział 8.

### Źródła internetowe
- [Python Data Model – objects, values, types](https://docs.python.org/3/reference/datamodel.html)
- [Mutable vs Immutable Objects in Python (realpython.com)](https://realpython.com/python-mutable-vs-immutable/)
- [Python's `is` vs `==` (realpython.com)](https://realpython.com/python-is-identity-vs-equality/)
- [Shallow vs Deep Copy – docs.python.org](https://docs.python.org/3/library/copy.html)
- [Common Python gotchas – mutable default arguments](https://docs.python-guide.org/writing/gotchas/)
- [functools.lru_cache – dokumentacja](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [Memoization in Python (realpython.com)](https://realpython.com/lru-cache-python/)
- [bytearray – dokumentacja](https://docs.python.org/3/library/stdtypes.html#bytearray)
- [Python Shallow vs Deep Copy (realpython.com)](https://realpython.com/copying-python-objects/)


