# 02 - Moduł vs skrypt i `__main__`

## Cel

Wyjaśnić, kiedy plik `.py` działa jako moduł importowany, a kiedy jako skrypt uruchamiany bezpośrednio. Zrozumieć rolę atrybutu `__name__` i konsekwencje efektów ubocznych przy imporcie.

## Kluczowa zasada

Każdy plik `.py` jest modułem. Różnica dotyczy sposobu uruchomienia:
- `python file.py` → `__name__ == "__main__"`,
- `import file` → `__name__ == "file"`.

Dzięki temu można oddzielić:
- API (funkcje do importu),
- kod uruchamiany interaktywnie lub z CLI.

### Czym jest `__name__`?

`__name__` to **wbudowany atrybut** każdego modułu Pythona. Interpreter nadaje mu wartość automatycznie:

| Sposób uruchomienia | Wartość `__name__` |
|---|---|
| `python moj_plik.py` | `"__main__"` |
| `python -m moj_pakiet.moj_plik` | `"__main__"` |
| `import moj_plik` (z innego modułu) | `"moj_plik"` |
| `from moj_pakiet import moj_plik` | `"moj_pakiet.moj_plik"` |

Wartość `__name__` możemy sprawdzić w dowolnym miejscu modułu:

```python
# sprawdz_name.py
print(f"Wartość __name__ w tym pliku: {__name__!r}")
```

Uruchomienie bezpośrednie:
```
$ python sprawdz_name.py
Wartość __name__ w tym pliku: '__main__'
```

Import z innego pliku:
```python
>>> import sprawdz_name
Wartość __name__ w tym pliku: 'sprawdz_name'
```

### Co dokładnie robi interpreter przy imporcie?

Gdy Python napotka instrukcję `import modul`, wykonuje następujące kroki:

1. **Sprawdza cache** — czy `modul` istnieje już w `sys.modules`. Jeśli tak, zwraca wcześniej załadowany obiekt.
2. **Szuka pliku** — przeszukuje ścieżki z `sys.path` (szczegóły w sekcji 05).
3. **Wykonuje cały kod modułu** — od góry do dołu, **raz** (przy pierwszym imporcie).
4. **Tworzy obiekt modułu** — i wstawia go do `sys.modules`.
5. **Wiąże nazwę** — w bieżącej przestrzeni nazw: `modul` wskazuje na obiekt modułu.

**Kluczowy punkt:** krok 3 oznacza, że każda instrukcja na najwyższym poziomie modułu zostanie wykonana podczas importu. To jest źródło **efektów ubocznych**.

Diagram: `diagrams/module_vs_script.png`

![Module vs script](diagrams/module_vs_script.png)

## Efekty uboczne importu — dlaczego to problem?

Efekt uboczny (ang. *side effect*) to każda akcja, która zmienia stan programu poza zwracaniem wartości: wypisanie tekstu, otwarcie pliku, modyfikacja zmiennej globalnej.

### Przykład problematyczny

```python
# zlecenie.py — ZŁY STYL
import datetime

print("Moduł zlecenie załadowany o", datetime.datetime.now())

baza_danych = []   # tworzy się przy imporcie!

def dodaj_zlecenie(nazwa: str) -> None:
    baza_danych.append(nazwa)
    print(f"Dodano: {nazwa}")

dodaj_zlecenie("testowe")   # wykonuje się przy imporcie!
```

```python
# main.py
import zlecenie   # wypisze tekst i doda "testowe" do bazy — NIESPODZIANKA!

zlecenie.dodaj_zlecenie("prawdziwe")
print(zlecenie.baza_danych)
# Wynik: ['testowe', 'prawdziwe'] — element 'testowe' dodany nieoczekiwanie
```

### Rozwiązanie — strażnik `if __name__ == "__main__":`

```python
# zlecenie.py — DOBRY STYL
import datetime

baza_danych: list[str] = []

def dodaj_zlecenie(nazwa: str) -> None:
    baza_danych.append(nazwa)
    print(f"Dodano: {nazwa}")

if __name__ == "__main__":
    # Ten blok NIE wykona się przy imporcie
    print("Moduł zlecenie załadowany o", datetime.datetime.now())
    dodaj_zlecenie("testowe")
```

Teraz `import zlecenie` importuje tylko funkcje i zmienną — bez efektów ubocznych.

## Krok po kroku na kodzie

Plik: `examples/calc_module.py`

```python
def add(a: float, b: float) -> float:
    return a + b

def multiply(a: float, b: float) -> float:
    return a * b

def main() -> None:
    print("2 + 3 =", add(2, 3))

if __name__ == "__main__":
    main()
```

Dlaczego to jest dobre podejście:
- importując moduł w innym pliku, dostajesz tylko funkcje (`add`, `multiply`),
- kod demonstracyjny `main()` nie uruchamia się „sam" przy imporcie,
- testowanie jest prostsze, bo funkcje są czyste i niezależne od CLI.

## Drugi przykład: osobny plik uruchamiający

Plik: `examples/run_as_module.py` importuje `add` i uruchamia prosty scenariusz.
To symuluje sytuację, gdy masz wiele modułów i jeden punkt wejścia programu.

## Uruchamianie z flagą `-m`

Python umożliwia uruchamianie modułu jako skryptu za pomocą flagi `-m`:

```bash
python -m pakiet.modul
```

Różnica w stosunku do `python pakiet/modul.py`:
- `-m` korzysta z systemu importów (szuka modułu na `sys.path`),
- poprawnie rozwiązuje importy wewnątrz pakietu,
- uruchamia plik `__main__.py` pakietu, jeśli istnieje.

Przykład — uruchamianie modułu z pakietu standardowego:

```bash
python -m json.tool dane.json      # ładne formatowanie JSON
python -m http.server 8000         # prosty serwer HTTP
python -m venv .venv               # tworzenie środowiska wirtualnego
```

Dla własnych pakietów: jeśli w katalogu pakietu umieścisz plik `__main__.py`, to polecenie `python -m moj_pakiet` uruchomi właśnie ten plik.

## Wzorzec: pakiet z `__main__.py`

```text
moj_pakiet/
    __init__.py
    logika.py
    __main__.py     ← punkt wejścia przy `python -m moj_pakiet`
```

```python
# moj_pakiet/__main__.py
from .logika import oblicz

def main() -> None:
    wynik = oblicz(10)
    print(f"Wynik: {wynik}")

if __name__ == "__main__":
    main()
```

## Polecane uruchomienia

```bash
python src/_03-modules/02-module-vs-script/examples/calc_module.py
python src/_03-modules/02-module-vs-script/examples/run_as_module.py
```

## Mini-lab: rozdzielenie API i CLI

### Cele
- odróżnić kod biblioteczny od kodu uruchamialnego,
- utrwalić znaczenie `__name__`,
- sprawdzić wpływ na testowalność.

### Kroki
1. Dodaj funkcję `subtract(a, b)` do `examples/calc_module.py`.
2. Użyj jej w `main()`.
3. W osobnym pliku zaimportuj `subtract` i wywołaj ją bez uruchamiania `main()`.
4. Sprawdź, że import nie uruchamia kodu demonstracyjnego.

### Oczekiwany efekt
- Student umie zaprojektować moduł, który jest jednocześnie wygodny do importu i uruchamiania.

### Rozszerzenie
- Dodaj `argparse` w `main()` i obsłuż argumenty z wiersza poleceń.

## Zadania i rozszerzenia

- `exercises/tasks.py` — klasyfikacja trybu uruchomienia,
- `exercises/solutions_module_vs_script.py` — referencyjna implementacja,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- umieszczanie całej logiki programu w bloku `if __name__ == "__main__":` (zamiast w oddzielnych funkcjach),
- importowanie z plików, które mają efekty uboczne już przy imporcie (np. `print`, zapis do pliku),
- mieszanie kodu bibliotecznego i kodu prezentacyjnego w jednej funkcji,
- zapominanie, że `__name__` zmienia wartość w zależności od kontekstu uruchomienia.

## Pytania kontrolne

1. Co dokładnie oznacza wartość `__name__` podczas importu?
2. Dlaczego blok `if __name__ == "__main__":` poprawia testowalność?
3. Kiedy warto wydzielić oddzielny plik „runner"?
4. Czym różni się `python plik.py` od `python -m modul`?
5. Co to jest efekt uboczny importu i jak go uniknąć?
6. Jak działa `__main__.py` w pakiecie?

## Literatura

- https://docs.python.org/3/library/__main__.html
- https://docs.python.org/3/tutorial/modules.html
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
- https://realpython.com/if-name-main-python/
