# 09 - Zarządzanie zależnościami

## Cel

Wprowadzić praktyki ekosystemu Python:
- PyPI — globalne repozytorium pakietów,
- izolacja środowisk (`venv`, `conda`),
- narzędzia (`pip`, `poetry`, `pipenv`, `uv`),
- różnica `requirements.txt` vs `pyproject.toml`.

## Dlaczego globalna instalacja to błąd?

Wyobraź sobie dwa projekty na tym samym komputerze:
- **Projekt A** wymaga `requests==2.28.0`
- **Projekt B** wymaga `requests==2.31.0`

Przy globalnej instalacji tylko jedna wersja może być zainstalowana jednocześnie. Efekty:
- konflikty wersji między projektami,
- trudniejsza reprodukowalność — na innym komputerze mogą być inne wersje,
- ryzyko syndromu „działa u mnie" — bo zależności nie są jawne,
- ryzyko uszkodzenia systemowego Pythona (Linux/macOS).

**Zasada najważniejsza dla studentów: jeden projekt = jedno środowisko wirtualne.**

## Środowiska wirtualne (`venv`)

### Co to jest `venv`?

`venv` to wbudowany moduł Pythona, który tworzy **izolowane środowisko** — osobny katalog z kopią interpretera i własną przestrzenią na pakiety.

### Kompletny cykl pracy z `venv`

```bash
# 1. Tworzenie środowiska
python -m venv .venv

# 2. Aktywacja
#    Linux / macOS:
source .venv/bin/activate
#    Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
#    Windows (cmd):
.\.venv\Scripts\activate.bat

# 3. Weryfikacja — upewnij się, że używasz właściwego interpretera:
python --version
pip --version
# Powinno wskazywać na ścieżkę wewnątrz .venv/

# 4. Instalacja zależności
python -m pip install requests flask

# 5. Zapis stanu środowiska
python -m pip freeze > requirements.txt

# 6. Dezaktywacja
deactivate
```

### Odtworzenie środowiska na innym komputerze

```bash
python -m venv .venv
source .venv/bin/activate       # lub .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

To jest **fundamentalny workflow** — każdy student powinien go opanować.

### Co zawiera katalog `.venv`?

```
.venv/
    bin/ (lub Scripts/ na Windows)
        python              ← kopia/symlink interpretera
        pip
        activate
    lib/
        python3.12/
            site-packages/  ← tu trafiają zainstalowane pakiety
    pyvenv.cfg              ← konfiguracja środowiska
```

> **Wskazówka:** dodaj `.venv/` do `.gitignore` — środowisko **nie powinno** być commitowane do repozytorium.

## `pip` — menedżer pakietów

### Podstawowe polecenia

```bash
# Instalacja pakietu
python -m pip install requests

# Instalacja konkretnej wersji
python -m pip install requests==2.31.0

# Instalacja z pliku requirements
python -m pip install -r requirements.txt

# Lista zainstalowanych pakietów
python -m pip list

# Zamrożenie stanu (z wersjami)
python -m pip freeze

# Informacje o pakiecie
python -m pip show requests

# Aktualizacja pakietu
python -m pip install --upgrade requests

# Usunięcie pakietu
python -m pip uninstall requests
```

### `pip freeze` vs `pip list`

| Polecenie | Format | Zastosowanie |
|---|---|---|
| `pip list` | Tabelka czytelna dla człowieka | Szybki przegląd |
| `pip freeze` | Format `pakiet==wersja` | Zapis do `requirements.txt` |

### `pip install -e .` — tryb editable (deweloperski)

Jeśli tworzysz pakiet z `pyproject.toml`, możesz zainstalować go w trybie edytowalnym:

```bash
python -m pip install -e .
```

Dzięki temu:
- zmiany w kodzie źródłowym są **natychmiast widoczne** bez reinstalacji,
- importy działają poprawnie z dowolnego katalogu,
- testy mogą importować pakiet bez manipulacji `sys.path`.

## `requirements.txt` vs `pyproject.toml`

### `requirements.txt`

```text
requests==2.31.0
flask>=3.0,<4.0
pytest>=8.0
```

- prosta lista pakietów do instalacji,
- dobry format do szybkiego odtworzenia środowiska,
- często wykorzystywany przez CI i wdrażanie,
- **nie opisuje** metadanych projektu (nazwa, autor, opis).

### `pyproject.toml`

```toml
[project]
name = "moj-projekt"
version = "1.0.0"
description = "Przykładowy projekt"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "flask>=3.0",
]

[project.optional-dependencies]
dev = ["pytest>=8.0", "mypy"]

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.backends._legacy:_Backend"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- **nowoczesny standard** konfiguracji projektu (PEP 621),
- opisuje metadane, zależności, narzędzia i system budowania,
- jeden plik zamiast wielu (`setup.py`, `setup.cfg`, `MANIFEST.in`),
- współpracuje z narzędziami typu Poetry, Flit, Hatch.

### Kiedy co stosować?

| Scenariusz | Zalecany format |
|---|---|
| Szybki skrypt / eksperyment | `requirements.txt` |
| Projekt zespołowy / produkcyjny | `pyproject.toml` + opcjonalnie `requirements.txt` |
| Biblioteka do publikacji na PyPI | `pyproject.toml` (obowiązkowy) |
| CI/CD | `requirements.txt` (szybki `pip install -r`) |

W praktyce projekty edukacyjne często mają oba pliki: jeden dla szybkiej instalacji, drugi dla pełnej konfiguracji.

## PyPI — Python Package Index

https://pypi.org/ — globalne repozytorium pakietów Pythona.

- Ponad **500 000** pakietów (stan na 2026),
- `pip install nazwa` pobiera pakiet z PyPI,
- każdy może opublikować własny pakiet,
- wersje pakietów są niezmienne (nie można nadpisać opublikowanej wersji).

## Krótkie porównanie narzędzi

| Narzędzie | Opis | Kiedy wybrać |
|---|---|---|
| `pip` + `venv` | Wbudowane w Pythona | Na start i do nauki |
| `poetry` | Zarządzanie zależnościami + publikacja | Średnie i duże projekty |
| `pipenv` | Lockfile + workflow | Projekty webowe |
| `conda` | Pakiety spoza Pythona (C, Fortran) | Data science, ML |
| `uv` | Bardzo szybki menedżer (napisany w Rust) | Gdy zależy na szybkości |

### `uv` — nowe narzędzie (od 2024)

`uv` to menedżer pakietów i środowisk napisany w Rust, **10-100× szybszy** od `pip`:

```bash
# Instalacja uv
pip install uv

# Tworzenie środowiska i instalacja
uv venv .venv
uv pip install requests flask

# Kompilacja lockfile'a
uv pip compile requirements.in -o requirements.txt
```

`uv` jest kompatybilny z `pip` i `requirements.txt`, ale znacząco szybszy. Zyskuje popularność w ekosystemie.

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
- kod pozwala sprawdzić stan środowiska programowo,
- łatwiej wykryć brakujące zależności,
- `importlib.metadata` jest w stdlib od Pythona 3.8.

Plik: `examples/spec_compare.py`

```python
def compare_specs(requirements: set[str], pyproject: set[str]) -> dict[str, set[str]]:
    return {
        "only_requirements": requirements - pyproject,
        "only_pyproject": pyproject - requirements,
        "common": requirements & pyproject,
    }
```

Interpretacja: ten schemat pomaga wykryć rozbieżności między deklaracjami zależności.

## Mini-lab: odtwarzalne środowisko projektu

### Cele
- przygotować powtarzalne środowisko,
- sprawdzić spójność deklaracji zależności,
- uniknąć problemu „działa u mnie".

### Kroki
1. Utwórz nowe środowisko `python -m venv .lab_venv`.
2. Aktywuj je i zainstaluj pakiety z `requirements.txt`.
3. Uruchom `examples/version_report.py` i zapisz raport.
4. Porównaj deklaracje przez `examples/spec_compare.py`.
5. Uzupełnij brakujące wpisy i powtórz porównanie.
6. Użyj `pip freeze > requirements-lock.txt` i porównaj z oryginalnym `requirements.txt`.

### Oczekiwany efekt
- Student umie przygotować projekt tak, by inna osoba mogła odtworzyć środowisko bez zgadywania wersji pakietów.

### Rozszerzenie
- Dodaj lockfile i porównaj proces instalacji z użyciem Poetry.

## Powiązane zadania

- `exercises/tasks.py` — wybór narzędzia i normalizacja wpisów dependency,
- `exercises/solutions_dependencies.py` — rozwiązania,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- brak przypiętych wersji w projektach zespołowych (`requests` zamiast `requests==2.31.0`),
- mieszanie aktywnego venv i globalnego interpretera,
- instalacje przez `pip` bez sprawdzania, który interpreter jest aktywny (`which python`),
- commitowanie katalogu `.venv` do repozytorium,
- zapominanie o aktualizacji `requirements.txt` po dodaniu pakietu.

## Pytania kontrolne

1. Dlaczego `venv` ogranicza problemy z konfliktem wersji?
2. Kiedy warto mieć jednocześnie `requirements.txt` i `pyproject.toml`?
3. Jak sprawdzić, czy pakiet jest zainstalowany w aktywnym środowisku?
4. Czym różni się `pip freeze` od `pip list`?
5. Do czego służy `pip install -e .`?
6. Jakie zalety ma `pyproject.toml` w porównaniu z `setup.py`?

## Literatura

- https://pypi.org/
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- https://packaging.python.org/en/latest/specifications/pyproject-toml/
- https://python-poetry.org/docs/
- https://pipenv.pypa.io/en/latest/
- https://github.com/astral-sh/uv — uv (szybki menedżer pakietów)
- PEP 621 — Storing project metadata in pyproject.toml: https://peps.python.org/pep-0621/
