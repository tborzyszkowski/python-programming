# 02 - Modul vs skrypt i `__main__`

## Cel

Wyjasnic kiedy plik `.py` dziala jako modul importowany, a kiedy jako skrypt uruchamiany bezposrednio.

## Kluczowa zasada

Kazdy plik `.py` jest modulem. Roznica dotyczy sposobu uruchomienia:
- `python file.py` -> `__name__ == "__main__"`,
- `import file` -> `__name__ == "file"`.

Dzieki temu mozna oddzielic API modulu od logiki demonstracyjnej CLI.

Diagram: `diagrams/module_vs_script.png`

![Module vs script](diagrams/module_vs_script.png)

## Kod referencyjny

- `examples/calc_module.py` - funkcje i blok `if __name__ == "__main__"`.
- `examples/run_as_module.py` - uruchamianie przez `python -m`.
- `exercises/tasks.py` - zadania.

## Polecane uruchomienia

```bash
python src/_03-modules/02-module-vs-script/examples/calc_module.py
python -m src._03-modules.02-module-vs-script.examples.run_as_module
```

## Literatura

- https://docs.python.org/3/library/__main__.html
- https://docs.python.org/3/tutorial/modules.html

