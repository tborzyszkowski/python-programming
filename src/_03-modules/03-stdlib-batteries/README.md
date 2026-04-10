# 03 - Standardowa biblioteka (batteries included)

## Cel

Pokazać, że Python posiada bogaty zestaw gotowych narzędzi: pracę z plikami, strukturami danych, JSON, datami, iteratorami i metadanymi. Nauczyć studenta **strategii dobierania modułu** ze standardowej biblioteki zamiast pisania wszystkiego od zera.

## Co oznacza „batteries included"?

Filozofia Pythona zakłada, że razem z interpreterem dostarczana jest bogata biblioteka standardowa (ang. *standard library*, *stdlib*). Wyrażenie „batteries included" pochodzi z oficjalnej dokumentacji i oznacza:

> Python jest dostarczany z bogatym zestawem modułów gotowych do użycia — nie musisz instalować dodatkowych pakietów, żeby zrealizować wiele typowych zadań.

W wielu językach (np. JavaScript, C) trzeba od razu instalować zewnętrzne biblioteki do podstawowych zadań. W Pythonie dużą część tych potrzeb pokrywa biblioteka standardowa, co daje:
- mniej zależności zewnętrznych,
- mniejsze ryzyko konfliktów wersji,
- szybszy start projektu,
- gwarancję jakości — moduły standardowe są dobrze przetestowane i utrzymywane.

### Jak duża jest stdlib?

Biblioteka standardowa Pythona 3.12 zawiera ponad **300 modułów**. Obejmuje m.in.:
- typy danych i kolekcje (`collections`, `heapq`, `array`, `enum`),
- obsługę plików i katalogów (`pathlib`, `os`, `shutil`, `glob`),
- formaty danych (`json`, `csv`, `xml`, `configparser`, `sqlite3`),
- narzędzia tekstowe i wyrażenia regularne (`re`, `string`, `textwrap`),
- daty i czas (`datetime`, `time`, `calendar`, `zoneinfo`),
- sieć i protokoły (`http`, `urllib`, `socket`, `email`),
- narzędzia programisty (`unittest`, `logging`, `pdb`, `dis`),
- matematykę i losowość (`math`, `random`, `statistics`, `decimal`, `fractions`),
- programowanie współbieżne (`threading`, `multiprocessing`, `asyncio`),
- narzędzia funkcyjne (`functools`, `itertools`, `operator`).

Pełna lista: https://docs.python.org/3/library/

## Krok po kroku na kodzie

Plik: `examples/stdlib_showcase.py`

### 1) Zliczanie słów przez `Counter`

```python
from collections import Counter

def count_words(text: str) -> Counter:
    words = [w.lower() for w in text.split()]
    return Counter(words)

# Użycie:
wynik = count_words("Python python modules Python")
print(wynik)            # Counter({'python': 3, 'modules': 1})
print(wynik.most_common(1))  # [('python', 3)]
```

Interpretacja: `Counter` to słownik „element → liczba wystąpień".
Dobry do histogramów, analizy logów i prostych statystyk. Dziedziczy po `dict`, więc wspiera wszystkie operacje słownikowe, a dodatkowo oferuje metody jak `most_common()`, `elements()` i operatory arytmetyczne (`+`, `-`).

### 2) Kombinacje przez `itertools`

```python
from itertools import combinations

def choose_pairs(items: list[str]) -> list[tuple[str, str]]:
    return list(combinations(items, 2))

# Użycie:
print(choose_pairs(["A", "B", "C"]))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

Interpretacja: `itertools` pozwala pisać kod deklaratywnie i bez ręcznego zagnieżdżania pętli. Zamiast dwóch pętli `for i ... for j > i ...` mamy jedną czytelną funkcję.

Inne przydatne narzędzia z `itertools`:
- `permutations(iterable, r)` — permutacje,
- `product(A, B)` — iloczyn kartezjański,
- `chain(it1, it2)` — łączenie iteratorów,
- `groupby(iterable, key)` — grupowanie.

### 3) Serializacja danych przez `json`

```python
import json

def to_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True)

# Użycie:
print(to_json({"temat": "stdlib", "gotowe": True}))
# {"gotowe": true, "temat": "stdlib"}
```

Interpretacja: to podstawa przy API, konfiguracji i zapisie wyników eksperymentów.

Uwaga na parametr `ensure_ascii=False` — bez niego polskie znaki będą zakodowane jako `\uXXXX`.

### 4) Operacje na ścieżkach przez `pathlib`

```python
from pathlib import Path

# Zamiast: os.path.join(os.path.dirname(__file__), "..", "data", "input.txt")
sciezka = Path(__file__).parent / ".." / "data" / "input.txt"

# Odczyt pliku:
tekst = sciezka.read_text(encoding="utf-8")

# Sprawdzenie istnienia:
print(sciezka.exists())

# Rozszerzenie pliku:
print(sciezka.suffix)   # ".txt"
```

`Path` daje obiektowy interfejs do ścieżek i jest czytelniejszy niż ręczne składanie stringów za pomocą `os.path`.

### 5) Daty i czas przez `datetime`

```python
from datetime import datetime, timedelta

teraz = datetime.now()
print(f"Teraz: {teraz:%Y-%m-%d %H:%M}")     # 2026-04-10 14:30

# Ile dni do końca semestru?
koniec_semestru = datetime(2026, 6, 30)
pozostalo = koniec_semestru - teraz
print(f"Pozostało dni: {pozostalo.days}")

# Dodawanie czasu:
za_tydzien = teraz + timedelta(weeks=1)
print(f"Za tydzień: {za_tydzien:%Y-%m-%d}")
```

Moduł `datetime` jest podstawą pracy z datami. Dla stref czasowych od Pythona 3.9 dostępny jest `zoneinfo`.

### 6) Porównanie: `os.path` vs `pathlib`

```python
# Stary styl (os.path)
import os
nazwa = os.path.join(os.path.expanduser("~"), "dokumenty", "raport.txt")
istnieje = os.path.exists(nazwa)

# Nowy styl (pathlib) — czytelniejszy, obiektowy
from pathlib import Path
nazwa = Path.home() / "dokumenty" / "raport.txt"
istnieje = nazwa.exists()
```

Od Pythona 3.6 rekomenduje się `pathlib` zamiast `os.path`.

### 7) Dekoratory i cache z `functools`

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))   # 832040 — szybko dzięki cache
```

`functools` oferuje też `partial` (częściowe aplikowanie argumentów), `reduce`, `wraps` i inne narzędzia funkcyjne.

Diagram: `diagrams/stdlib_map.png`

![Stdlib map](diagrams/stdlib_map.png)

## Jak znaleźć odpowiedni moduł?

### Strategia wyszukiwania

1. **Dokumentacja** — https://docs.python.org/3/library/ — przeglądaj spis treści wg kategorii.
2. **`help()` w REPL** — `help(modul)` lub `help(modul.funkcja)`.
3. **`dir(modul)`** — lista dostępnych nazw w module.
4. **PyMOTW** (Python Module of the Week) — https://pymotw.com/3/ — znakomite tutoriale do każdego modułu stdlib.

### Podręczna tabela doboru

| Zadanie | Moduł |
|---|---|
| Analiza tekstu | `re`, `string`, `collections` |
| Pliki i katalogi | `pathlib`, `shutil`, `os`, `glob` |
| Daty i czas | `datetime`, `zoneinfo`, `calendar` |
| Formaty danych | `json`, `csv`, `xml`, `sqlite3` |
| Matematyka | `math`, `statistics`, `decimal`, `fractions` |
| Losowość | `random`, `secrets` |
| Iteratory i funkcje | `itertools`, `functools`, `operator` |
| Testowanie | `unittest`, `doctest` |
| Debugowanie | `pdb`, `logging`, `traceback` |
| Sieć | `urllib`, `http.server`, `socket` |

**Zasada praktyczna:** najpierw sprawdź stdlib, dopiero potem PyPI.

## Mini-lab: narzędzia stdlib w jednym scenariuszu

### Cele
- dobrać moduł standardowy do zadania,
- przetworzyć dane tekstowe i zapisać wynik,
- porównać kod „ręczny" z kodem opartym o stdlib.

### Kroki
1. Użyj `count_words()` do policzenia słów w krótkim tekście.
2. Wygeneruj pary elementów przez `choose_pairs()`.
3. Zapisz wynik do JSON przez `to_json()`.
4. Porównaj czytelność z wersją napisaną bez `Counter` i `itertools`.

### Oczekiwany efekt
- Student umie uzasadnić, dlaczego użycie stdlib skraca i upraszcza kod.

### Rozszerzenie
- Dodaj obsługę pliku wejściowego i użyj `pathlib.Path.read_text()`.

## Powiązane zadania

- `exercises/tasks.py` — implementacja histogramu i par,
- `exercises/solutions_stdlib.py` — wzorcowe rozwiązanie,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- implementowanie od zera tego, co już jest w stdlib (NIH — *Not Invented Here*),
- ignorowanie dokumentacji i parametrów funkcji (np. `json.dumps` ma wiele przydatnych opcji),
- nadmierne importy `*` zamiast precyzyjnego importowania,
- mylenie `os.path` z `pathlib` — oba działają, ale `pathlib` jest nowocześniejszy i czytelniejszy.

## Pytania kontrolne

1. Dlaczego `Counter` jest lepszy od ręcznego licznika w wielu przypadkach?
2. Czym różni się `itertools.combinations` od zagnieżdżonej pętli?
3. Kiedy `json.dumps` może zwrócić wynik inny niż oczekiwany bez `sort_keys=True`?
4. Jak znaleźć odpowiedni moduł w bibliotece standardowej?
5. Czym `pathlib.Path` różni się od `os.path.join`?
6. Do czego służy `@lru_cache`?

## Literatura

- https://docs.python.org/3/library/
- https://docs.python.org/3/library/pathlib.html
- https://docs.python.org/3/library/collections.html
- https://docs.python.org/3/library/itertools.html
- https://docs.python.org/3/library/json.html
- https://docs.python.org/3/library/datetime.html
- https://docs.python.org/3/library/functools.html
- https://pymotw.com/3/ — Python Module of the Week
