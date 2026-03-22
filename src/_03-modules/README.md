# Modul 03 - Moduly, pakiety i importy w Pythonie 3

Ten modul jest przeznaczony dla studentow I roku informatyki. Material prowadzi od podstaw (przestrzenie nazw i modul jako plik) do praktyki projektowej (pakiety, importy, diagnoza pulapek i zarzadzanie zaleznosciami).

Kazdy temat ma te sama strukture:
- `README.md` - teoria, kod, diagramy i literatura,
- `diagrams/` - diagramy PlantUML (`.puml`) i wygenerowane pliki `.png`,
- `examples/` - uruchamialne przyklady,
- `exercises/` - zadania, przykladowe rozwiazania i testy.

## Spis tematow

| Katalog | Zakres |
|---|---|
| [01-namespaces](01-namespaces/README.md) | Przestrzenie nazw, LEGB, historia namespaces |
| [02-module-vs-script](02-module-vs-script/README.md) | Modul vs skrypt, `if __name__ == "__main__"` |
| [03-stdlib-batteries](03-stdlib-batteries/README.md) | Przeglad biblioteki standardowej |
| [04-imports-and-symbol-tables](04-imports-and-symbol-tables/README.md) | `import`, `from-import`, absolute/relative, `builtins`, `globals()`, `locals()` |
| [05-import-mechanism-pythonpath](05-import-mechanism-pythonpath/README.md) | Jak Python szuka modulow, `PYTHONPATH`, `sys.path` |
| [06-compilation-pycache](06-compilation-pycache/README.md) | Kompilacja do bytecode, `__pycache__`, `.pyc` |
| [07-packages-and-init](07-packages-and-init/README.md) | Pakiety, `__init__.py`, namespace packages |
| [08-advanced-import-topics](08-advanced-import-topics/README.md) | Circular imports, `__all__`, `importlib` |
| [09-dependency-management](09-dependency-management/README.md) | PyPI, venv/conda, pip/poetry/pipenv, requirements vs pyproject |

## Uruchamianie

```bash
# testy zadan dla calego modulu (z katalogu glownego repo)
python -m pytest src/_03-modules -c src/_03-modules/pytest.ini -v

# testy pojedynczego tematu
python -m pytest src/_03-modules/01-namespaces/exercises/test_solutions.py -v

# generowanie diagramow PNG z PlantUML
python src/_03-modules/generate_diagrams.py
```

## Literatura i zrodla

- Python Docs - Tutorial: https://docs.python.org/3/tutorial/
- Python Docs - The import system: https://docs.python.org/3/reference/import.html
- Python Docs - Modules: https://docs.python.org/3/tutorial/modules.html
- Python Docs - `importlib`: https://docs.python.org/3/library/importlib.html
- Python Packaging User Guide: https://packaging.python.org/
- PEP 328 (Absolute and Relative Imports): https://peps.python.org/pep-0328/
- PEP 420 (Namespace Packages): https://peps.python.org/pep-0420/
- PEP 451 (ModuleSpec): https://peps.python.org/pep-0451/

