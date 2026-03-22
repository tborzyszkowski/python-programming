# 08 - Zaawansowane tematy importu i pułapki

## Cel

Pokazać trzy praktyczne obszary:
1. circular imports,
2. kontrola eksportu przez `__all__`,
3. dynamiczne importowanie przez `importlib`.

## Circular imports - skąd bierze się problem?

Problem pojawia się, gdy moduł A importuje B, a B importuje A podczas inicjalizacji.
Objaw: `ImportError`, brak symbolu lub komunikat o „partially initialized module”.

Dlaczego tak się dzieje:
- import wykonuje kod modułu,
- drugi moduł próbuje użyć symbolu, który jeszcze nie został zdefiniowany,
- powstaje cykl zależności na etapie startu.

Typowe rozwiązania:
- przeniesienie importu do funkcji,
- wydzielenie wspólnej logiki do trzeciego modułu,
- uproszczenie zależności (SRP, SoC).

## `__all__` - kontrola eksportu

`__all__` określa, co zostanie wyeksportowane przez `from module import *`.
To przydatne, gdy chcesz jasno zdefiniować publiczne API modułu.

## Dynamiczne importy (`importlib`)

`importlib.import_module(name)` pozwala ładować moduł po nazwie przekazanej jako string.
Najczęstsze zastosowanie: pluginy i rozszerzenia ładowane w runtime.

Diagram: `diagrams/advanced_imports.png`

![Advanced imports](diagrams/advanced_imports.png)

## Krok po kroku na kodzie

### Lokalny import jako obejście

Plik: `examples/circular_safe.py`

```python
def orchestrate(value: int) -> int:
    from circular_safe import from_a, from_b
    return from_b(from_a(value))
```

To pokazuje technikę lokalnego importu. Jest użyteczna, ale w dłuższej perspektywie zwykle lepiej przebudować zależności.

### Dynamiczne ładowanie pluginu

Plik: `examples/dynamic_loader.py`

```python
def call_transform(module_name: str, value: int) -> int:
    module = importlib.import_module(module_name)
    return int(module.transform(value))
```

Interpretacja:
- nazwa modułu jest parametrem,
- kod nie jest na sztywno związany z jednym pluginem,
- łatwiej budować architekturę rozszerzeń.

## Mini-lab: naprawa cyklicznego importu

### Cele
- rozpoznać objawy circular import,
- zastosować jedną z technik naprawy,
- utrwalić rolę `__all__` i `importlib`.

### Kroki
1. Przygotuj dwa moduły importujące się wzajemnie i wywołaj je.
2. Zanotuj komunikat błędu.
3. Przenieś wspólną funkcję do trzeciego modułu.
4. Powtórz uruchomienie i sprawdź, że błąd zniknął.
5. Opcjonalnie załaduj jeden z modułów dynamicznie przez `importlib.import_module`.

### Oczekiwany efekt
- Student potrafi zaproponować refaktoryzację zamiast „maskowania” problemu.

### Rozszerzenie
- Dodaj prosty mechanizm pluginów oparty na nazwach modułów z listy konfiguracyjnej.

## Powiązane zadania

- `exercises/tasks.py` - rozpoznawanie symptomów circular import i reguły `__all__`,
- `exercises/solutions_advanced_imports.py` - rozwiązania,
- `exercises/test_solutions.py` - testy.

## Typowe pułapki

- nadużywanie lokalnych importów zamiast refaktoryzacji,
- stosowanie `import *` bez kontroli `__all__`,
- dynamiczny import bez walidacji nazwy i obsługi błędów.

## Pytania kontrolne

1. Co oznacza „partially initialized module”?
2. Kiedy `__all__` poprawia czytelność API?
3. Jakie ryzyko niesie `importlib.import_module` przy nazwie z wejścia użytkownika?

## Literatura

- https://docs.python.org/3/library/importlib.html
- https://docs.python.org/3/reference/import.html

