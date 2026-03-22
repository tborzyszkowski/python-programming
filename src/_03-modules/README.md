# Moduł 03 - Moduły, pakiety i importy w Pythonie 3

Ten moduł jest przeznaczony dla studentów I roku informatyki. Prowadzi od podstaw (przestrzenie nazw i moduł jako plik) do praktyki projektowej (pakiety, importy, diagnoza pułapek i zarządzanie zależnościami).

## Cele dydaktyczne

Po przerobieniu modułu student powinien:
- rozumieć, jak Python wiąże nazwy i jak działa reguła LEGB,
- odróżniać skrypt uruchamiany bezpośrednio od modułu importowanego,
- świadomie wybierać style importu i diagnozować problemy z importami,
- wyjaśnić rolę `sys.path`, `PYTHONPATH`, `__pycache__` i plików `.pyc`,
- zaprojektować prosty pakiet z czytelnym API,
- unikać typowych pułapek (`circular imports`, niekontrolowane `import *`),
- stosować podstawowe praktyki zarządzania zależnościami w projekcie.

## Jak korzystać z modułu

Każdy temat ma tę samą strukturę:
- `README.md` - teoria, wyjaśnienia krok po kroku i fragmenty kodu,
- `diagrams/` - diagramy PlantUML (`.puml`) oraz wygenerowane obrazy `.png`,
- `examples/` - uruchamialne przykłady,
- `exercises/` - zadania, przykładowe rozwiązania i testy.

Sugerowana kolejność pracy dla studenta:
1. przeczytaj sekcje `Cel`, `Teoria` i `Krok po kroku` w danym temacie,
2. uruchom pliki z `examples/` i porównaj wynik z opisem,
3. rozwiąż `exercises/tasks.py`,
4. porównaj wynik z `exercises/solutions_*.py`,
5. uruchom `test_solutions.py`.

## Spis tematów

| Katalog | Zakres | Co warto opanować |
|---|---|---|
| [01-namespaces](01-namespaces/README.md) | Przestrzenie nazw, LEGB, historia namespaces | Rozumienie, skąd Python bierze wartość nazwy |
| [02-module-vs-script](02-module-vs-script/README.md) | Moduł vs skrypt, `if __name__ == "__main__"` | Oddzielenie API modułu od kodu wykonywalnego |
| [03-stdlib-batteries](03-stdlib-batteries/README.md) | Przegląd biblioteki standardowej | Dobór narzędzi z stdlib zamiast pisania wszystkiego od zera |
| [04-imports-and-symbol-tables](04-imports-and-symbol-tables/README.md) | `import`, `from-import`, absolute/relative, `builtins`, `globals()`, `locals()` | Wpływ stylu importu na czytelność i diagnostykę |
| [05-import-mechanism-pythonpath](05-import-mechanism-pythonpath/README.md) | Jak Python szuka modułów, `PYTHONPATH`, `sys.path` | Rozwiązywanie `ModuleNotFoundError` metodycznie |
| [06-compilation-pycache](06-compilation-pycache/README.md) | Kompilacja do bytecode, `__pycache__`, `.pyc` | Co dzieje się podczas importu i po co jest cache |
| [07-packages-and-init](07-packages-and-init/README.md) | Pakiety, `__init__.py`, namespace packages | Organizacja kodu wieloplikowego i API pakietu |
| [08-advanced-import-topics](08-advanced-import-topics/README.md) | Circular imports, `__all__`, `importlib` | Rozpoznawanie pułapek i refaktoryzacja zależności |
| [09-dependency-management](09-dependency-management/README.md) | PyPI, venv/conda, pip/poetry/pipenv, requirements vs pyproject | Reprodukowalne środowisko projektu |

## Uruchamianie

```bash
# testy zadań dla całego modułu (z katalogu głównego repo)
python -m pytest src/_03-modules -c src/_03-modules/pytest.ini -v

# testy pojedynczego tematu
python -m pytest src/_03-modules/01-namespaces/exercises/test_solutions.py -v

# generowanie diagramów PNG z PlantUML
python src/_03-modules/generate_diagrams.py
```

## Mini-lab: diagnostyka importów w 20 minut

### Cele
- prześledzić, gdzie Python szuka modułów,
- wykryć źródło typowego `ModuleNotFoundError`,
- utrwalić różnicę między modułem, pakietem i skryptem.

### Kroki
1. Uruchom `examples/path_inspector.py` z tematu `05-import-mechanism-pythonpath`.
2. Sprawdź wartość `PYTHONPATH` i pierwszy wpis `sys.path`.
3. Zmień katalog uruchomienia i uruchom skrypt ponownie.
4. Porównaj wyniki i zapisz, które ścieżki się zmieniły.
5. Użyj `examples/find_module.py`, aby sprawdzić pochodzenie modułu `json`.

### Oczekiwany efekt
- Student umie wyjaśnić, dlaczego ten sam import działa lub nie działa w zależności od kontekstu uruchomienia.

### Rozszerzenie
- Dodaj własny katalog do `PYTHONPATH` i sprawdź, jak zmienia się wynik wyszukiwania modułu.

## Mapa kompetencji (poziom I rok)

- **Poziom podstawowy**: 01, 02, 03
- **Poziom średni**: 04, 05, 06, 07
- **Poziom rozszerzony**: 08, 09

Dobre minimum egzaminacyjne to umiejętność:
- wytłumaczenia LEGB,
- napisania modułu z poprawnym `if __name__ == "__main__":`,
- poprawnego użycia `import` i `from ... import ...`,
- wskazania roli `venv` i `requirements.txt`.

## Literatura i źródła

- Python Docs - Tutorial: https://docs.python.org/3/tutorial/
- Python Docs - The import system: https://docs.python.org/3/reference/import.html
- Python Docs - Modules: https://docs.python.org/3/tutorial/modules.html
- Python Docs - `importlib`: https://docs.python.org/3/library/importlib.html
- Python Packaging User Guide: https://packaging.python.org/
- PEP 328 (Absolute and Relative Imports): https://peps.python.org/pep-0328/
- PEP 420 (Namespace Packages): https://peps.python.org/pep-0420/
- PEP 451 (ModuleSpec): https://peps.python.org/pep-0451/
