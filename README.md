# python-programming

Materiały dydaktyczne do kursu **programowania w Pythonie 3**.

## Wymagania

- Python **3.11** lub nowszy (zalecany 3.13) — [python.org](https://www.python.org/downloads/)
- Nie jest wymagana żadna zewnętrzna instalacja poza standardowym Pythonem

## Szybki start

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/<user>/python-programming.git
cd python-programming
```

### 2. Utwórz i aktywuj środowisko wirtualne

**Windows (PowerShell):**
```powershell
# Jednorazowa konfiguracja (tworzy .venv i instaluje zależności)
.\scripts\setup_venv.ps1

# Aktywacja w bieżącej sesji
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS / Git Bash:**
```bash
bash scripts/setup_venv.sh
source .venv/bin/activate
```

**Ręcznie (każdy system):**
```bash
python -m venv .venv
# Windows:
.venv\Scripts\pip install -r requirements.txt
# Linux/macOS:
.venv/bin/pip install -r requirements.txt
```

### 3. Uruchom testy

```powershell
# Z katalogu głównego projektu (Windows):
.venv\Scripts\python.exe -m pytest src\_01-introduction -v
.venv\Scripts\python.exe -m pytest src\_02-functions -v
.venv\Scripts\python.exe -m pytest src\_03-modules -c src\_03-modules\pytest.ini -v

# Po aktywacji venv (każdy system):
python -m pytest src/_01-introduction -v
python -m pytest src/_02-functions -v
python -m pytest src/_03-modules -c src/_03-modules/pytest.ini -v
```

### 4. Wygeneruj diagramy PNG z plików PlantUML

```powershell
# Wymaga połączenia z Internetem (używa plantuml.com)
.venv\Scripts\python.exe src\_01-introduction\generate_diagrams.py
.venv\Scripts\python.exe src\_02-functions\generate_diagrams.py
.venv\Scripts\python.exe src\_03-modules\generate_diagrams.py
```

## Moduły kursu

- [`src/_01-introduction/README.md`](src/_01-introduction/README.md) - wprowadzenie do Pythona 3 (typy, sterowanie, uruchamianie, mutowalność)
- [`src/_02-functions/README.md`](src/_02-functions/README.md) - funkcje w Pythonie 3 (definicje, argumenty, lambda, SRP)
- [`src/_03-modules/README.md`](src/_03-modules/README.md) - moduly, importy, pakiety, pycache i zarzadzanie zaleznosciami

## Jak wybrać moduł na start?

Dla studentów I roku polecana kolejność pracy:

1. **`_01-introduction`** - fundamenty składni i modelu działania Pythona.
2. **`_02-functions`** - budowanie modularnego kodu, funkcje wyższego rzędu i dobre praktyki projektowe.
3. **`_03-modules`** - praca z modulami i pakietami, import system i dobre praktyki ekosystemu.

Sugerowany rytm nauki:
- najpierw przeczytaj `README.md` wybranego tematu,
- uruchom przykłady z `examples/`,
- na końcu rozwiąż zadania z `exercises/` i sprawdź je testami `pytest`.

## Struktura projektu

```
python-programming/
├── .venv/                        # środowisko wirtualne (ignorowane przez git)
├── requirements.txt              # zależności projektu
├── pyproject.toml                # konfiguracja narzędzi (pytest, ruff, mypy)
├── scripts/
│   ├── setup_venv.ps1            # skrypt konfiguracyjny (Windows PowerShell)
│   └── setup_venv.sh             # skrypt konfiguracyjny (Linux/macOS)
└── src/
    ├── _01-introduction/
    │   ├── pytest.ini            # konfiguracja pytest dla modułu
    │   ├── requirements.txt      # zależności modułu
    │   ├── generate_diagrams.py  # generator PNG z .puml
    │   ├── control-flow/         # instrukcje sterujące
    │   ├── data-types/           # typy danych
    │   ├── interpreters/         # kompilatory i interpretery
    │   ├── mutability/           # mutowalność / niemutowalność
    │   └── running-python/       # sposoby uruchamiania kodu
    ├── _02-functions/
        ├── pytest.ini            # konfiguracja pytest dla modułu
        ├── generate_diagrams.py  # generator PNG z .puml
        ├── 01-definition/        # definicja funkcji
        ├── 02-arguments/         # argumenty pozycyjne, nazwane, *args, **kwargs
        ├── 03-lambda-calculus/   # rachunek lambda i podstawy teoretyczne
        ├── 04-lambda-usage/      # praktyczne użycie lambda (map/filter/reduce)
        └── 05-srp/               # zasada pojedynczej odpowiedzialności dla funkcji
    └── _03-modules/
        ├── pytest.ini            # konfiguracja pytest dla modulu
        ├── generate_diagrams.py  # generator PNG z .puml
        ├── 01-namespaces/        # przestrzenie nazw i LEGB
        ├── 02-module-vs-script/  # __name__ == "__main__"
        ├── 03-stdlib-batteries/  # biblioteka standardowa
        ├── 04-imports-and-symbol-tables/
        ├── 05-import-mechanism-pythonpath/
        ├── 06-compilation-pycache/
        ├── 07-packages-and-init/
        ├── 08-advanced-import-topics/
        └── 09-dependency-management/
```

## Zależności

| Pakiet       | Wersja  | Opis                               |
|--------------|---------|------------------------------------|
| pytest       | ≥ 7.4   | framework do testów jednostkowych  |
| pytest-cov   | ≥ 4.1   | pokrycie kodu testami              |
| plantuml     | ≥ 0.3   | generowanie diagramów PNG z .puml  |
