# Moduł 01 – Wprowadzenie do Pythona 3

Niniejszy moduł stanowi wprowadzenie do języka Python 3.
Każdy temat umieszczony jest w osobnym podkatalogu zawierającym:
- `README.md` – wyczerpujące omówienie koncepcji, fragmenty kodu, diagramy i referencje
- `diagrams/` – pliki PlantUML (`.puml`) ze źródłem diagramów oraz wygenerowane `.png`
- `examples/` – uruchamialne skrypty Python 3 i testy jednostkowe

## Spis treści

| Katalog | Temat | Diagramy | Zadania |
|---|---|---|---|
| [interpreters/](interpreters/README.md) | Kompilatory i interpretery – jak działa Python? | 2 | 5 |
| [running-python/](running-python/README.md) | Sposoby uruchamiania kodu w Pythonie | 2 | 5 |
| [data-types/](data-types/README.md) | Podstawowe typy danych i operacje | 3 | 6 |
| [mutability/](mutability/README.md) | Typy mutowalne i niemutowalne | 2 | 5 |
| [control-flow/](control-flow/README.md) | Instrukcje sterujące | 4 | 6 |

## Wymagania

```
Python >= 3.10
pytest >= 7.4    # do testów jednostkowych
plantuml         # do regenerowania diagramów PNG
```

Instalacja zależności:

```bash
pip install -r requirements.txt
```

## Uruchamianie testów

```bash
# z katalogu src/_01-introduction/
python -m pytest                          # wszystkie testy (examples + exercises)
python -m pytest data-types/exercises/   # tylko zadania z jednego tematu
python -m pytest -k "TestSito"           # tylko testy pasujące do nazwy
```

## Zadania do samodzielnego rozwiązania

Każdy temat zawiera podkatalog `exercises/` z trzema plikami:

| Plik | Opis |
|---|---|
| `tasks.py` | Treść zadań – szablony funkcji z docstringami, `raise NotImplementedError` |
| `solutions_<temat>.py` | Wzorcowe rozwiązania |
| `test_solutions.py` | Testy pytest weryfikujące rozwiązania |

**Sposób pracy z zadaniami:**

1. Otwórz `exercises/tasks.py` wybranego tematu.
2. Zaimplementuj funkcje zastępując `raise NotImplementedError(...)`.
3. Uruchom testy: `pytest <temat>/exercises/test_solutions.py -v`
4. Porównaj z rozwiązaniem wzorcowym w `solutions_<temat>.py`.

### Przegląd zadań

| Temat | Zadania |
|---|---|
| **interpreters** | Analiza bajtkodu (`dis`), wykrywanie implementacji, wersja Pythona, stałe w bajtkodzie, dynamiczna kompilacja (`compile`/`exec`) |
| **running-python** | Introspekcja modułu, leniwy import, moduł w locie (`types.ModuleType`), wyszukiwanie w `sys.path`, moduły z prefiksem |
| **data-types** | Statystyki liczbowe, analiza napisu + palindrom, zliczanie wystąpień, macierz 2D (pułapka mutowalności), operacje zbiorowe, obliczenia `Decimal` |
| **mutability** | Aktualizacja bez mutacji oryginału, usuwanie duplikatów z zachowaniem kolejności, dekorator cache (memoizacja), głęboka aktualizacja słownika, zamrożenie struktury |
| **control-flow** | Sito Eratostenesa, parowanie nawiasów (stos), tabliczka mnożenia (comprehension), grupowanie wg długości, interpreter RPN, FizzBuzz z konfigurowalnymi zasadami |

## Diagramy PlantUML

Każdy katalog tematyczny zawiera podkatalog `diagrams/` z plikami `.puml` (źródło)
oraz wygenerowanymi `.png` (gotowe do wstawienia w slajdy lub dokumentację).

Aby **zregenerować wszystkie PNG** (np. po edycji `.puml`):

```bash
# z katalogu src/_01-introduction/
pip install plantuml
python generate_diagrams.py
```

Skrypt [`generate_diagrams.py`](generate_diagrams.py) wysyła każdy plik `.puml`
do publicznego serwera `plantuml.com` i zapisuje wynikowy `.png` obok pliku źródłowego.

### Wygenerowane diagramy

| Diagram | Plik PNG |
|---|---|
| Kompilator vs Interpreter | `interpreters/diagrams/compile_vs_interpret.png` |
| Pipeline wykonania CPython | `interpreters/diagrams/python_execution_pipeline.png` |
| Przepływ REPL | `running-python/diagrams/repl_flow.png` |
| Skrypt vs moduł (`__name__`) | `running-python/diagrams/script_vs_module.png` |
| Hierarchia typów numerycznych | `data-types/diagrams/numeric_hierarchy.png` |
| Operacje na napisach | `data-types/diagrams/string_operations.png` |
| Wbudowane typy kolekcyjne | `data-types/diagrams/builtin_collections.png` |
| Mutowalny vs niemutowalny | `mutability/diagrams/mutable_vs_immutable.png` |
| Model pamięci (stos/sterta) | `mutability/diagrams/memory_model.png` |
| Diagram if/elif/else | `control-flow/diagrams/if_elif_else.png` |
| Diagram pętli for | `control-flow/diagrams/for_loop.png` |
| Diagram pętli while | `control-flow/diagrams/while_loop.png` |
| Diagram match/case | `control-flow/diagrams/match_statement.png` |

## Generowanie slajdów (Pandoc)

```bash
pandoc interpreters/README.md  -o interpreters.pptx  --slide-level=2
pandoc running-python/README.md -o running-python.pptx --slide-level=2
pandoc data-types/README.md    -o data-types.pptx    --slide-level=2
pandoc mutability/README.md    -o mutability.pptx    --slide-level=2
pandoc control-flow/README.md  -o control-flow.pptx  --slide-level=2
```

> Każdy nagłówek `##` generuje nowy slajd. Obrazki PNG są automatycznie wstawiane.


