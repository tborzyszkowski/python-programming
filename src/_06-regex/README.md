# Moduł 06 – Wyrażenia Regularne w Pythonie 3

Niniejszy moduł omawia wyrażenia regularne w Pythonie 3 – od teoretycznych podstaw (języki formalne, automaty skończone) przez pełne API modułu `re`, aż po zaawansowane wzorce i realistyczne zastosowania w przetwarzaniu danych.

Każdy temat umieszczony jest w osobnym podkatalogu zawierającym:
- `README.md` – wyczerpujące omówienie koncepcji, fragmenty kodu, diagramy i referencje
- `diagrams/` – pliki PlantUML (`.puml`) ilustrujące omawiane zagadnienia
- `examples/` – uruchamialne skrypty Python 3
- `exercises/` – zadania do samodzielnego rozwiązania, przykładowe rozwiązania i testy

## Spis treści

| Katalog | Temat | Kluczowe zagadnienia |
|---|---|---|
| [01-formal-languages/](01-formal-languages/README.md) | Języki formalne i automaty | Hierarchia Chomsky'ego, język regularny, NFA vs DFA, silnik NFA w Pythonie |
| [02-basic-syntax/](02-basic-syntax/README.md) | Podstawowa składnia | Literały, klasy znaków `\d \w \s`, kotwice `^ $`, kwantyfikatory, alternacja, `r"..."` |
| [03-re-module/](03-re-module/README.md) | Moduł `re` | `match`, `search`, `fullmatch`, `findall`, `finditer`, `sub`, `split`, `compile`, obiekt `Match` |
| [04-groups/](04-groups/README.md) | Grupy i przechwytywanie | `()`, `(?:)`, `(?P<name>)`, wsteczne odniesienia, `sub` z grupami |
| [05-flags/](05-flags/README.md) | Flagi i tryby | `IGNORECASE`, `MULTILINE`, `DOTALL`, `VERBOSE`, flagi inline `(?im)` |
| [06-advanced-patterns/](06-advanced-patterns/README.md) | Zaawansowane wzorce | Chciwe vs leniwe, lookahead/lookbehind, catastrophic backtracking, `re.escape` |
| [07-practical-use/](07-practical-use/README.md) | Praktyczne zastosowania | Walidacja (email, PESEL, URL), parsowanie logów, maskowanie danych osobowych |

## Wymagania

```
Python >= 3.10
pytest >= 7.4
plantuml          # do wizualizacji diagramów .puml (pip install plantuml)
```

## Uruchamianie przykładów i testów

```bash
# Przykłady
python src/_06-regex/01-formal-languages/examples/dfa_simulator.py
python src/_06-regex/02-basic-syntax/examples/syntax_explorer.py
python src/_06-regex/03-re-module/examples/re_module_tour.py
python src/_06-regex/04-groups/examples/groups_demo.py
python src/_06-regex/05-flags/examples/flags_demo.py
python src/_06-regex/06-advanced-patterns/examples/advanced_patterns.py
python src/_06-regex/07-practical-use/examples/data_validator.py
python src/_06-regex/07-practical-use/examples/log_parser.py

# Testy (wszystkie)
python -m pytest src/_06-regex/ -v

# Testy pojedynczego tematu
python -m pytest src/_06-regex/01-formal-languages/exercises/test_solutions.py
python -m pytest src/_06-regex/02-basic-syntax/exercises/test_solutions.py
python -m pytest src/_06-regex/03-re-module/exercises/test_solutions.py
python -m pytest src/_06-regex/04-groups/exercises/test_solutions.py
python -m pytest src/_06-regex/05-flags/exercises/test_solutions.py
python -m pytest src/_06-regex/06-advanced-patterns/exercises/test_solutions.py
python -m pytest src/_06-regex/07-practical-use/exercises/test_solutions.py
```

## Zadania do samodzielnego rozwiązania

| Temat | Zakres zadań |
|---|---|
| **01-formal-languages** | symulacja DFA, rozpoznawanie języków, liczenie dopasowań |
| **02-basic-syntax** | klasy znaków, kotwice, kwantyfikatory, walidacja formatu |
| **03-re-module** | wyszukiwanie, ekstrakcja, zamiana, podział, pozycje dopasowań |
| **04-groups** | wyciąganie dat, zamiana formatów, powtórzenia, parsowanie wersji |
| **05-flags** | wyszukiwanie bez wielkości, wieloliniowe kotwice, bloki wieloliniowe, VERBOSE |
| **06-advanced-patterns** | leniwe kwantyfikatory, lookahead/lookbehind, walidacja hasła, `re.escape` |
| **07-practical-use** | walidacja email/PESEL/URL, parsowanie logów Apache, maskowanie danych |

## Diagramy PlantUML

| Diagram | Opis | Plik |
|---|---|---|
| **NFA vs DFA** | Porównanie stanów i przejść automatów skończonych | `01-formal-languages/diagrams/nfa_dfa_states.puml` |
| **Mapa składni** | Mindmapa elementów składni regex | `02-basic-syntax/diagrams/syntax_map.puml` |
| **Wybór funkcji `re`** | Flowchart doboru właściwej funkcji modułu `re` | `03-re-module/diagrams/re_functions_choice.puml` |
| **Przechwytywanie grup** | Sekwencja indeksowania grup w dopasowaniu | `04-groups/diagrams/group_capture.puml` |
| **Efekty flag** | Tabela zachowań każdej flagi | `05-flags/diagrams/flags_effects.puml` |
| **Chciwy vs leniwy** | Wizualizacja cofania kwantyfikatorów | `06-advanced-patterns/diagrams/greedy_vs_lazy.puml` |
| **Pipeline walidacji** | Architektura pipeline walidacji/ekstrakcji | `07-practical-use/diagrams/validation_pipeline.puml` |

---

Autor materiałów: Tomasz Borzyszkowski
Licencja: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

