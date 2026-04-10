# 04 - Importy i tablice symboli

## Cel

Praktycznie porównać:
- `import module_name` vs `from module_name import symbol`,
- importy bezwzględne i względne,
- aliasy (`import ... as ...`),
- przestrzeń `builtins`,
- działanie `globals()` i `locals()` oraz czas życia nazw.

## Teoria

### `import module_name`

Instrukcja `import math` wykonuje następujące kroki:
1. Ładuje moduł `math` (lub pobiera z cache `sys.modules`).
2. Tworzy **jedną nazwę** `math` w bieżącej przestrzeni nazw.
3. `math` jest obiektem modułu — dostęp do symboli przez kropkę: `math.sqrt(4)`.

**Zalety:**
- jawne wywołanie (`math.sqrt()`) — od razu wiadomo, skąd pochodzi funkcja,
- mniejsze ryzyko kolizji nazw,
- IDE lepiej wspiera autouzupełnianie.

**Wady:**
- dłuższy zapis przy częstym użyciu.

### `from module_name import symbol`

Instrukcja `from math import sqrt` importuje **konkretny symbol** bezpośrednio do bieżącej przestrzeni nazw:
1. Ładuje moduł `math`.
2. Pobiera z niego atrybut `sqrt`.
3. Wiąże nazwę `sqrt` w bieżącym zakresie.

**Zalety:**
- krótszy kod: `sqrt(4)` zamiast `math.sqrt(4)`.

**Wady:**
- łatwiej o kolizję nazw przy dużych plikach,
- trudniej zidentyfikować pochodzenie symbolu w dużym kodzie.

### Aliasy: `import ... as ...`

Aliasy pozwalają nadać importowanemu modułowi lub symbolowi inną nazwę:

```python
import numpy as np             # skrócona nazwa modułu
from datetime import datetime as dt   # unikamy kolizji z nazwą modułu
import collections as col
```

Typowe konwencje w ekosystemie Pythona:
- `import numpy as np`
- `import pandas as pd`
- `import matplotlib.pyplot as plt`

Alias nie zmienia samego modułu — to jedynie lokalna nazwa w bieżącej przestrzeni.

### `from module import *` — dlaczego unikać?

```python
from os.path import *     # importuje WSZYSTKIE publiczne nazwy z os.path
from math import *        # importuje WSZYSTKIE publiczne nazwy z math
```

**Problemy:**
- nie wiadomo, jakie nazwy trafiły do bieżącej przestrzeni,
- dwa moduły mogą eksportować tę samą nazwę — kolizja:

```python
from os.path import join
from mypackage.utils import join   # KOLIZJA! nadpisano os.path.join
```

- utrudnia debugowanie — `grep` po kodzie nie pokaże, skąd pochodzi symbol,
- kontrola: moduł może definiować `__all__`, aby ograniczyć eksport (szczegóły w sekcji 08).

**Zasada:** używaj `import *` najwyżej w konsoli interaktywnej, nigdy w kodzie produkcyjnym.

### `builtins` — przestrzeń wbudowana

Python posiada specjalną przestrzeń nazw `builtins`, w której znajdują się fundamentalne funkcje i typy:

```python
import builtins

# Te funkcje nie wymagają importu:
print(len([1, 2, 3]))       # len z builtins
print(type(42))              # type z builtins
print(sum([1, 2, 3]))       # sum z builtins
print(isinstance(42, int))  # isinstance z builtins
```

Pełna lista wbudowanych nazw:

```python
print(dir(builtins))
# ['ArithmeticError', 'AssertionError', ..., 'abs', 'all', 'any', ...,
#  'len', 'list', 'map', ..., 'print', ..., 'sum', 'super', 'type', ...]
```

#### Niebezpieczeństwo cieniowania builtinów

```python
# ZŁE — nadpisanie wbudowanej nazwy:
list = [1, 2, 3]         # teraz "list" to nasza lista, nie typ list!
print(list("abc"))        # TypeError: 'list' object is not callable

# Przywrócenie:
del list                  # usuwa lokalne nadpisanie
print(list("abc"))        # ['a', 'b', 'c'] — znów działa

# Inny przykład:
id = 42                   # nadpisanie wbudowanego id()
print(id("test"))         # TypeError!
```

**Wskazówka:** nigdy nie nazywaj zmiennych `list`, `dict`, `set`, `type`, `id`, `sum`, `min`, `max`, `len`, `open`, `print`, `input`, `map`, `filter`.

### `globals()` i `locals()`

```python
def inspect():
    local_var = "tu"
    print("local_var" in locals())   # True
    print("local_var" in globals())  # False
    print("inspect" in globals())    # True — funkcja widoczna globalnie
```

- `globals()` zwraca **słownik modułu** — zawiera wszystkie nazwy zdefiniowane na poziomie pliku.
- `locals()` zwraca **kopię** słownika bieżącego zakresu (np. wnętrze funkcji).

**Uwaga:** `locals()` zwraca **kopię**, nie referencję! Modyfikacja tego słownika **nie zmienia** zmiennych lokalnych:

```python
def test_locals():
    x = 10
    locals()["x"] = 999   # NIE zmieni x!
    print(x)               # 10

test_locals()
```

Natomiast `globals()` zwraca **referencję** do słownika modułu, więc modyfikacje przez `globals()` mają efekt:

```python
globals()["nowa_zmienna"] = 42
print(nowa_zmienna)   # 42 — zadziałało
```

### Czas życia nazw

Nazwy lokalne (w funkcji) istnieją tylko **podczas wykonywania** tej funkcji:

```python
def oblicz():
    wynik = 2 + 2       # "wynik" istnieje od tego momentu
    return wynik         # po return — "wynik" jest niszczony

# Po zakończeniu oblicz():
# - "wynik" nie istnieje w żadnej przestrzeni nazw
# - obiekt 4 (int) może zostać zwolniony przez garbage collector,
#   chyba że ktoś go jeszcze referencjonuje
```

Nazwy globalne (modułowe) żyją **tak długo, jak moduł jest załadowany** (zwykle do końca programu).

Diagram: `diagrams/import_styles.png`

![Import styles](diagrams/import_styles.png)

## Krok po kroku na kodzie

Plik: `examples/import_styles.py`

```python
import math
from math import sqrt

def using_import(x: float) -> float:
    return math.sqrt(x)

def using_from_import(x: float) -> float:
    return sqrt(x)
```

Obie funkcje robią to samo. Różnica dotyczy ergonomii i ryzyka kolizji.

Plik: `examples/symbol_tables.py`

```python
def inspect_tables() -> dict[str, bool]:
    local_name = "inside"
    return {
        "local_name_in_locals": "local_name" in locals(),
        "inspect_tables_in_globals": "inspect_tables" in globals(),
        "len_in_globals": "len" in globals(),
    }
```

Interpretacja:
- lokalna nazwa występuje w `locals()`,
- nazwa funkcji istnieje globalnie (zakres modułu),
- `len` nie musi być w `globals()`, bo pochodzi z `builtins`.

## Mini-lab: porównanie stylów importu

### Cele
- dobrać styl importu do kontekstu,
- rozpoznać wpływ importu na przestrzeń nazw,
- przećwiczyć diagnostykę kolizji nazw.

### Kroki
1. Uruchom `examples/import_styles.py`.
2. Dodaj lokalną zmienną `sqrt = 10` i sprawdź, co się stanie w `using_from_import()`.
3. Zostaw `using_import()` bez zmian i porównaj zachowanie.
4. Uruchom `examples/symbol_tables.py` i przeanalizuj wynik.
5. Spróbuj nadpisać `len = 42` na poziomie modułu — co zwróci `len([1, 2, 3])`?

### Oczekiwany efekt
- Student umie wskazać, kiedy pełny import modułu jest bezpieczniejszy.

### Rozszerzenie
- Dodaj przykład importu względnego w małym pakiecie i porównaj czytelność z importem bezwzględnym.

## Importy bezwzględne i względne

### Import bezwzględny (absolute)

```python
from package.subpkg import module
import package.subpkg.module
```

Preferowane w większych projektach — ścieżka importu jest pełna i jednoznaczna.

### Import względny (relative)

```python
from . import module           # z bieżącego pakietu
from .. import other_module    # z pakietu nadrzędnego
from .sub import helper        # z podpakietu
```

Wygodne w pakietach, ale **wymagają poprawnej struktury pakietu** (z `__init__.py` lub jako namespace package). Nie działają w skryptach uruchamianych bezpośrednio.

Dla studentów: na początku trzymaj się importów bezwzględnych, bo są prostsze diagnostycznie.

## Powiązane zadania

- `exercises/tasks.py` — zadania o stylu importu i życiu symboli,
- `exercises/solutions_imports.py` — implementacje referencyjne,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- `from x import *` — trudne debugowanie i kolizje nazw,
- nadpisanie nazwy funkcji importowanej lokalną zmienną (np. `sqrt = 10`),
- nadpisanie wbudowanej nazwy zmienną (np. `list = [...]`, `id = 5`),
- mylenie `locals()` z `globals()` podczas analizy błędu,
- zapis do `locals()` — **nie modyfikuje** bieżącego scope (to kopia!).

## Pytania kontrolne

1. Kiedy `import module_name` jest lepsze od `from module_name import symbol`?
2. Dlaczego `len` działa mimo braku w `globals()`?
3. Co staje się z lokalnymi nazwami po zakończeniu funkcji?
4. Co to jest alias importu i kiedy warto go użyć?
5. Dlaczego `from module import *` jest niebezpieczne?
6. Czym różni się import bezwzględny od względnego?
7. Co się stanie, jeśli nazwiemy zmienną `list`?

## Literatura

- https://docs.python.org/3/reference/import.html
- https://docs.python.org/3/library/functions.html#globals
- https://docs.python.org/3/library/functions.html#locals
- https://docs.python.org/3/library/builtins.html
- PEP 328 — Absolute and Relative Imports: https://peps.python.org/pep-0328/
