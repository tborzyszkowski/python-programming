# 07 - Pakiety i `__init__.py`

## Cel

Wyjasnic czym jest pakiet, jak go budowac i jak zmienilo sie znaczenie pliku `__init__.py` po Python 3.3 (namespace packages).

## Definicje

- **Modul**: pojedynczy plik `.py`.
- **Pakiet**: katalog grupujacy moduly.
- **`__init__.py`**:
  - dawniej wymagany, aby katalog byl pakietem,
  - dzis opcjonalny dla namespace packages (PEP 420),
  - nadal przydatny do definiowania API pakietu.

Diagram: `diagrams/package_layout.png`

![Package layout](diagrams/package_layout.png)

## Kod referencyjny

- Prosty pakiet: `examples/basic_pkg/`.
- Wiekszy przyklad warstwowy: `examples/school/`.
- Zadania: `exercises/tasks.py`.

## Literatura

- https://docs.python.org/3/tutorial/modules.html#packages
- https://peps.python.org/pep-0420/

