# 05 - Komponenty prywatne w Pythonie

## Cel

Wyjaśnić konwencje prywatności (`_name`, `__name`) i mechanizm name mangling.

## Teoria

### Trzy poziomy widoczności

Python nie ma twardych modyfikatorów dostępu jak `private` w Javie.
Zamiast tego stosuje **konwencje i ograniczenia techniczne**:

| Notacja | Znaczenie | Dostępność |
|---|---|---|
| `name` | Publiczny | Wszędzie |
| `_name` | Wewnętrzny (umowna prywatność) | Wszędzie technicznie, ale konwencja mówi: nie dotykaj spoza klasy |
| `__name` | Mocno prywatny (name mangling) | Dostępny tylko jako `_ClassName__name` |

### Name mangling — co to jest?

```python
class TemperatureSensor:
    def __init__(self) -> None:
        self.__calibration = 0.0   # Python zamienia na _TemperatureSensor__calibration
```

```python
sensor = TemperatureSensor()
print(sensor.__calibration)              # AttributeError!
print(sensor._TemperatureSensor__calibration)  # 0.0 — technicznie możliwe
```

Cel: **ochrona przed przypadkowym nadpisaniem** w podklasach, nie przed celowym dostępem.

### Właściwości (`@property`) jako czyste API

```python
class TemperatureSensor:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def temperature(self) -> float:
        """Odczyt temperatury (tylko do odczytu)."""
        return self._celsius

    @temperature.setter
    def temperature(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Poniżej zera absolutnego")
        self._celsius = value
```

`@property` umożliwia **kontrolowany dostęp** bez zmiany API (pole wygląda jak atrybut,
a wewnętrznie jest obliczane lub walidowane).

Diagram: `diagrams/topic_05.png`

![Prywatność i name mangling](diagrams/topic_05.png)

## Krok po kroku na kodzie

Plik: `examples/private_members.py`

```python
class TemperatureSensor:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius
        self.__calibration_offset = 0.0

    def set_calibration(self, delta: float) -> None:
        self.__calibration_offset = delta

    def read(self) -> float:
        return self._celsius + self.__calibration_offset

    def is_overheated(self, threshold: float) -> bool:
        return self.read() > threshold
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/private_members.py`.
2. Spróbuj uzyskać `sensor.__calibration_offset` spoza klasy — sprawdź błąd.
3. Uzyj `dir(sensor)` i znajdź zniekształconą nazwę.
4. Dodaj `@property` dla bieżącej temperatury z walidacją w setterze.
5. Napisz test sprawdzający, że walidacja blokuje temperaturę < −273.

### Oczekiwany efekt

- Student rozumie różnicę między `_x` i `__x`.
- Student potrafi używać `@property` do budowania czytelnego API.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_05.py`
- testy: `exercises/test_solutions.py`

Zadanie: dopisz metodę `is_overheated(threshold: float) -> bool`.

## Pytania egzaminacyjne

1. Czy Python ma prawdziwie prywatne pola? Uzasadnij.
2. Po co używa się konwencji `_name`?
3. Co robi name mangling i jakie ma ograniczenia?
4. Jak `@property` pomaga ukryć szczegóły implementacji?
5. Kiedy użyć `__name` zamiast `_name`?

## Literatura

- https://docs.python.org/3/tutorial/classes.html#private-variables
- https://docs.python.org/3/library/functions.html#property
