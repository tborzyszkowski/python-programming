# 06 - Kompilacja modulow, __pycache__, .pyc

## Cel

Pokazac, co Python kompiluje podczas importu i jaki jest sens plikow `.pyc`.

## Kluczowe fakty

- Python kompiluje kod zrodlowy `.py` do bytecode.
- Bytecode trafia do cache: katalog `__pycache__/`.
- Nazwa pliku `.pyc` zawiera tag wersji interpretera, np. `module.cpython-313.pyc`.
- Cache przyspiesza kolejne importy, ale nie zmienia logiki programu.

Diagram: `diagrams/pycache_flow.png`

![Pycache flow](diagrams/pycache_flow.png)

## Kod referencyjny

- `examples/compile_demo.py` - jawna kompilacja przez `py_compile`.
- `examples/cache_info.py` - analiza sciezek cache.

## Literatura

- https://docs.python.org/3/library/py_compile.html
- https://docs.python.org/3/reference/import.html

