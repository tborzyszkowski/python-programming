# 05 - Mechanizm importowania i PYTHONPATH

## Cel

Wyjasnic jak interpreter odnajduje modul i pakiet, jaka role maja `sys.path`, katalog roboczy i zmienna `PYTHONPATH`.

## Jak Python szuka modulu?

W uproszczeniu:
1. sprawdza cache `sys.modules`,
2. przechodzi po wpisach `sys.meta_path`,
3. przeszukuje sciezki w `sys.path` (m.in. katalog skryptu i katalogi z `PYTHONPATH`).

Diagram: `diagrams/import_resolution.png`

![Import resolution](diagrams/import_resolution.png)

## Kod referencyjny

- `examples/path_inspector.py` - podglad `sys.path` i `PYTHONPATH`.
- `examples/find_module.py` - `importlib.util.find_spec`.

## Literatura

- https://docs.python.org/3/reference/import.html
- https://docs.python.org/3/library/sys.html#sys.path
- https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH

