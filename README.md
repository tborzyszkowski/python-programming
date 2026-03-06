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

# Po aktywacji venv (każdy system):
python -m pytest src/_01-introduction -v
```

### 4. Wygeneruj diagramy PNG z plików PlantUML

```powershell
# Wymaga połączenia z Internetem (używa plantuml.com)
.venv\Scripts\python.exe src\_01-introduction\generate_diagrams.py
```

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
    └── _01-introduction/
        ├── pytest.ini            # konfiguracja pytest dla modułu
        ├── requirements.txt      # zależności modułu
        ├── generate_diagrams.py  # generator PNG z .puml
        ├── control-flow/         # instrukcje sterujące
        ├── data-types/           # typy danych
        ├── interpreters/         # kompilatory i interpretery
        ├── mutability/           # mutowalność / niemutowalność
        └── running-python/       # sposoby uruchamiania kodu
```

## Zależności

| Pakiet       | Wersja  | Opis                               |
|--------------|---------|------------------------------------|
| pytest       | ≥ 7.4   | framework do testów jednostkowych  |
| pytest-cov   | ≥ 4.1   | pokrycie kodu testami              |
| plantuml     | ≥ 0.3   | generowanie diagramów PNG z .puml  |
