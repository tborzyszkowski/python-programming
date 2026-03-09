# Moduł 02 – Funkcje w Pythonie 3

Niniejszy moduł omawia zagadnienia związane z funkcjami w języku Python 3, od podstawowych definicji, przez zaawansowaną obsługę argumentów, aż po elementy programowania funkcyjnego z użyciem wyrażeń lambda.

Każdy temat umieszczony jest w osobnym podkatalogu zawierającym:
- `README.md` – wyczerpujące omówienie koncepcji, fragmenty kodu, diagramy i referencje
- `diagrams/` – pliki PlantUML (`.puml`) ilustrujące omawiane zagadnienia
- `examples/` – uruchamialne skrypty Python 3 i testy jednostkowe

## Spis treści

| Katalog | Temat | Kluczowe zagadnienia |
|---|---|---|
| [01-definition/](01-definition/README.md) | Definicja funkcji | Składnia `def`, nagłówek, parametry, `docstring`, typowanie statyczne (Type Hints), wartość zwracana `return` |
| [02-arguments/](02-arguments/README.md) | Zmienna liczba argumentów | `*args` (krotka), `**kwargs` (słownik), kolejność parametrów, rozpakowywanie argumentów (`*`, `**`) |
| [03-lambda-calculus/](03-lambda-calculus/README.md) | Rachunek lambda | Podstawy teoretyczne (Alonzo Church), funkcje anonimowe `lambda`, ograniczenia (jedno wyrażenie) |
| [04-lambda-usage/](04-lambda-usage/README.md) | Zastosowanie lambd | Sortowanie z kluczem (`key`), funkcje wyższego rzędu: `map`, `filter`, `reduce`, przykład introspekcji (API Helper) |

## Wymagania

```
Python >= 3.10
pytest >= 7.4    # do uruchamiania testów w examples/
plantuml         # do wizualizacji diagramów .puml
```

## Uruchamianie przykładów i testów

```bash
# Uruchomienie przykładów z danego tematu
python src/_02-functions/01-definition/examples/basic_functions.py
python src/_02-functions/02-arguments/examples/variable_args_demo.py
python src/_02-functions/03-lambda-calculus/examples/lambda_demo.py
python src/_02-functions/04-lambda-usage/examples/functional_tools.py

# Uruchomienie testów jednostkowych
python -m pytest src/_02-functions/01-definition/examples/test_functions.py
```

## Diagramy PlantUML

W podkatalogach `diagrams/` znajdują się pliki źródłowe `.puml`.

| Diagram | Opis | Plik |
|---|---|---|
| **Struktura funkcji** | Elementy składowe definicji funkcji | `01-definition/diagrams/function_structure.puml` |
| **Kolejność argumentów** | Hierarchia parametrów pozycyjnych, domyślnych i zmiennych | `02-arguments/diagrams/argument_order.puml` |
| **Funkcja Lambda** | Składnia i prostota wyrażenia lambda | `03-lambda-calculus/diagrams/lambda_diagram.puml` |
| **Map / Filter / Reduce** | Przepływ danych w funkcjach wyższego rzędu | `04-lambda-usage/diagrams/higher_order.puml` |

## Przykładowy kod

W module znajdują się gotowe do uruchomienia przykłady ilustrujące omawiane zagadnienia:

- **`basic_functions.py`** – funkcje z parametrami obowiązkowymi, opcjonalnymi i domyślnymi.
- **`variable_args_demo.py`** – łączenie `*args` i `**kwargs` w jednej funkcji, generowanie raportów.
- **`lambda_demo.py`** – proste lambdy, IIFE (Immediately Invoked Function Expression), domknięcia (closures).
- **`functional_tools.py`** – porównanie `map`/`filter`/`reduce` z list comprehensions.
- **`apihelper.py`** – zaawansowany przykład introspekcji obiektu i dynamicznego formatowania dokumentacji (inspirowane *Dive Into Python*).

---

Autor materiałów: Zespół Dydaktyczny
Licencja: MIT

