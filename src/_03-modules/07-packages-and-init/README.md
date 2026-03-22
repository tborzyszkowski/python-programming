# 07 - Pakiety i `__init__.py`

## Cel

Wyjaśnić, czym jest pakiet, jak go budować i jak zmieniło się znaczenie pliku `__init__.py` po Python 3.3 (namespace packages).

## Definicje

- **Moduł**: pojedynczy plik `.py`.
- **Pakiet**: katalog grupujący moduły.
- **`__init__.py`**:
  - dawniej wymagany, aby katalog był pakietem,
  - dziś opcjonalny dla namespace packages (PEP 420),
  - nadal przydatny do definiowania API pakietu.

Diagram: `diagrams/package_layout.png`

![Package layout](diagrams/package_layout.png)

## Po co pakiety?

Pakiety rozwiązują trzy typowe problemy:
1. porządkują dużą bazę kodu,
2. ograniczają kolizje nazw,
3. pozwalają projektować publiczne API.

## Krok po kroku na kodzie

### Prosty pakiet: `examples/basic_pkg/`

Plik: `examples/basic_pkg/__init__.py`

```python
from .math_ops import add, mean

__all__ = ["add", "mean"]
```

Interpretacja:
- `__init__.py` definiuje, co jest „oficjalnym” API pakietu,
- użytkownik pakietu importuje wygodnie: `from basic_pkg import add`.

### Większy przykład: `examples/school/`

- `core/grade_model.py` - logika obliczeń,
- `ui/renderer.py` - formatowanie wyniku.

To mini-przykład separacji odpowiedzialności wewnątrz pakietu.

### Uruchomienie całości

Plik `examples/package_demo.py` łączy oba pakiety i pokazuje prosty przepływ:
1. obliczenia,
2. prezentacja,
3. wynik dla użytkownika.

## Mini-lab: własny pakiet z API

### Cele
- zbudować mały pakiet z czytelnym interfejsem,
- użyć `__init__.py` do kontrolowania eksportu,
- oddzielić logikę od warstwy prezentacji.

### Kroki
1. Dodaj w `examples/basic_pkg/math_ops.py` nową funkcję `median(values)`.
2. Wyeksportuj ją w `examples/basic_pkg/__init__.py`.
3. Użyj nowej funkcji w `examples/package_demo.py`.
4. Uruchom skrypt i sprawdź wynik.

### Oczekiwany efekt
- Student umie zaprojektować prosty pakiet i świadomie wystawić publiczne API.

### Rozszerzenie
- Rozbij `school/` na dodatkową warstwę usług i oceń wpływ na testowalność.

## Namespace packages (Python 3.3+)

Możliwe są pakiety bez `__init__.py`, ale:
- są bardziej zaawansowane,
- wymagają dobrego zrozumienia import system,
- na początku kursu zwykle wygodniej stosować klasyczne pakiety z `__init__.py`.

## Powiązane zadania

- `exercises/tasks.py` - API pakietu i rozpoznawanie namespace package,
- `exercises/solutions_packages.py` - rozwiązania,
- `exercises/test_solutions.py` - testy.

## Typowe pułapki

- brak jasnego API w `__init__.py`,
- importowanie z głębokich modułów zamiast z publicznej warstwy,
- mieszanie logiki domenowej i prezentacji w jednym module.

## Pytania kontrolne

1. Kiedy warto użyć `__all__`?
2. Dlaczego pakiet bez `__init__.py` może być trudniejszy dla początkujących?
3. Jak SRP wspiera projektowanie pakietów?

## Literatura

- https://docs.python.org/3/tutorial/modules.html#packages
- https://peps.python.org/pep-0420/
