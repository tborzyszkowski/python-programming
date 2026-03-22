# 08 - Zaawansowane tematy importu i pulapki

## Cel

Pokazac trzy praktyczne obszary:
1. circular imports,
2. kontrola eksportu przez `__all__`,
3. dynamiczne importowanie przez `importlib`.

## Circular imports

Problem pojawia sie, gdy modul A importuje B, a B importuje A podczas inicjalizacji. Objaw: `ImportError` lub brak oczekiwanego symbolu.

Typowe rozwiazania:
- przeniesienie importu do funkcji,
- wydzielenie wspolnej logiki do trzeciego modulu,
- uproszczenie zaleznosci (SRP, SoC).

## `__all__`

`__all__` okresla, co zostanie wyeksportowane przez `from module import *`.

## Dynamiczne importy

`importlib.import_module(name)` pozwala ladowac modul po nazwie przekazanej jako string, np. pluginy.

Diagram: `diagrams/advanced_imports.png`

![Advanced imports](diagrams/advanced_imports.png)

## Literatura

- https://docs.python.org/3/library/importlib.html
- https://docs.python.org/3/reference/import.html

