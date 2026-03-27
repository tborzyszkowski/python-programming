# 04 - Importy i tablice symboli

## Cel

Praktycznie porównać:
- `import module_name` vs `from module_name import symbol`,
- importy bezwzględne i względne,
- przestrzeń `builtins`,
- działanie `globals()` i `locals()` oraz czas życia nazw.

## Teoria w skrócie

### `import module_name`
- tworzy jedną nazwę (`module_name`) w bieżącej przestrzeni,
- wywołanie jest jawne (`module_name.funkcja()`),
- zwykle lepsza czytelność i mniejsze ryzyko kolizji.

### `from module_name import symbol`
- importuje konkretny symbol bezpośrednio,
- kod jest krótszy (`symbol()`),
- łatwiej o kolizję nazw przy dużych plikach.

### `builtins`, `globals()`, `locals()`
- `builtins` zawiera podstawowe funkcje (`len`, `sum`, `print`),
- `globals()` opisuje przestrzeń modułu,
- `locals()` opisuje bieżący scope (np. funkcji).

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
- nazwa funkcji istnieje globalnie (scope modułu),
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

### Oczekiwany efekt
- Student umie wskazać, kiedy pełny import modułu jest bezpieczniejszy.

### Rozszerzenie
- Dodaj przykład importu względnego w małym pakiecie i porównaj czytelność z importem bezwzględnym.

## Importy bezwzględne i względne

- bezwzględne: `from package.subpkg import module` - preferowane w większych projektach,
- względne: `from . import module` - wygodne w pakietach, ale wymagają poprawnej struktury.

Dla studentów: na początku trzymaj się importów bezwzględnych, bo są prostsze diagnostycznie.

## Powiązane zadania

- `exercises/tasks.py` - zadania o stylu importu i życiu symboli,
- `exercises/solutions_imports.py` - implementacje referencyjne,
- `exercises/test_solutions.py` - testy.

## Typowe pułapki

- `from x import *` (trudne debugowanie i kolizje),
- nadpisanie nazwy funkcji importowanej lokalną zmienną,
- mylenie `locals()` z `globals()` podczas analizy błędu.

## Pytania kontrolne

1. Kiedy `import module_name` jest lepsze od `from module_name import symbol`?
2. Dlaczego `len` działa mimo braku w `globals()`?
3. Co staje się z lokalnymi nazwami po zakończeniu funkcji?

## Literatura

- https://docs.python.org/3/reference/import.html
- https://docs.python.org/3/library/functions.html#globals
- https://docs.python.org/3/library/functions.html#locals

