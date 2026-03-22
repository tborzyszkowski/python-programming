# 09 - Zarządzanie zależnościami

## Cel

Wprowadzić praktyki ekosystemu Python:
- PyPI,
- izolacja środowisk (`venv`, `conda`),
- narzędzia (`pip`, `poetry`, `pipenv`),
- różnica `requirements.txt` vs `pyproject.toml`.

## Dlaczego globalna instalacja to błąd?

- konflikty wersji między projektami,
- trudniejsza reprodukowalność,
- ryzyko „działa u mnie”.

Dla studentów najważniejsza zasada: **jeden projekt = jedno środowisko**.

## Minimalny workflow (pip + venv)

1. `python -m venv .venv`
2. aktywacja środowiska
3. `python -m pip install -r requirements.txt`
4. `python -m pip freeze > requirements-lock.txt` (opcjonalnie)

Diagram: `diagrams/dependency_workflow.png`

![Dependency workflow](diagrams/dependency_workflow.png)

## `requirements.txt` vs `pyproject.toml`

### `requirements.txt`
- prosta lista pakietów do instalacji,
- dobry format do szybkiego odtworzenia środowiska,
- często wykorzystywany przez CI i deployment.

### `pyproject.toml`
- nowoczesny standard konfiguracji projektu,
- opisuje metadane, zależności i narzędzia,
- współpracuje z narzędziami typu Poetry.

W praktyce projekty edukacyjne często mają oba pliki: jeden dla szybkiej instalacji, drugi dla pełnej konfiguracji.

## Krok po kroku na kodzie

Plik: `examples/version_report.py`

```python
def read_version(distribution: str) -> str:
    try:
        return importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        return "not-installed"
```

Interpretacja:
- kod pozwala sprawdzić stan środowiska,
- łatwiej wykryć brakujące zależności.

Plik: `examples/spec_compare.py`

```python
def compare_specs(requirements: set[str], pyproject: set[str]) -> dict[str, set[str]]:
    return {
        "only_requirements": requirements - pyproject,
        "only_pyproject": pyproject - requirements,
        "common": requirements & pyproject,
    }
```

Interpretacja: ten schemat pomaga wykryć rozjazd między deklaracjami zależności.

## Mini-lab: odtwarzalne środowisko projektu

### Cele
- przygotować powtarzalne środowisko,
- sprawdzić spójność deklaracji zależności,
- uniknąć problemu „działa u mnie”.

### Kroki
1. Utwórz nowe środowisko `venv`.
2. Zainstaluj pakiety z `requirements.txt`.
3. Uruchom `examples/version_report.py` i zapisz raport.
4. Porównaj deklaracje przez `examples/spec_compare.py`.
5. Uzupełnij brakujące wpisy i powtórz porównanie.

### Oczekiwany efekt
- Student umie przygotować projekt tak, by inna osoba mogła odtworzyć środowisko bez zgadywania wersji pakietów.

### Rozszerzenie
- Dodaj lockfile i porównaj proces instalacji z użyciem Poetry.

## Krótkie porównanie narzędzi

- `pip` + `venv`: najlepsze na start i do nauki,
- `poetry`: wygodne zarządzanie zależnościami i publikacja,
- `pipenv`: połączenie lockfile + workflow,
- `conda`: często wybierane w data science (także pakiety spoza Pythona).

## Powiązane zadania

- `exercises/tasks.py` - wybór narzędzia i normalizacja wpisów dependency,
- `exercises/solutions_dependencies.py` - rozwiązania,
- `exercises/test_solutions.py` - testy.

## Typowe pułapki

- brak przypiętych wersji w projektach zespołowych,
- mieszanie aktywnego venv i globalnego interpretera,
- instalacje przez `pip` bez sprawdzania, który interpreter jest aktywny.

## Pytania kontrolne

1. Dlaczego `venv` ogranicza problemy z konfliktem wersji?
2. Kiedy warto mieć jednocześnie `requirements.txt` i `pyproject.toml`?
3. Jak sprawdzić, czy pakiet jest zainstalowany w aktywnym środowisku?

## Literatura

- https://pypi.org/
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- https://python-poetry.org/docs/
- https://pipenv.pypa.io/en/latest/
