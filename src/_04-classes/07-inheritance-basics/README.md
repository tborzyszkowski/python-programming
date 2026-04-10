# 07 - Dziedziczenie w OOP i w Pythonie

## Cel

Zrozumieć relację „jest-rodzajem" (is-a), nadpisywanie metod i rolę `super()`.

## Teoria

### Skąd pochodzi dziedziczenie?

Dziedziczenie (ang. *inheritance*) pojawiło się w Simula jako sposób na **ponowne użycie
definicji klas** bez kopiowania kodu. W klasycznym OOP hierarchia klas modeluje
hierarchię pojęć w domenie: `Pojazd → Samochód → SportowySamochód`.

### Mechanizm dziedziczenia w Pythonie

```python
class Vehicle:
    def move(self) -> str:
        return "Pojazd przemieszcza się"

class Bike(Vehicle):        # Bike dziedziczy po Vehicle
    def move(self) -> str:  # nadpisanie (override) metody
        return "Rower jedzie"
```

Klasa pochodna:
- **dziedziczy** wszystkie metody i atrybuty klasy bazowej,
- może **nadpisać** wybrane metody,
- może **rozszerzyć** klasę bazową o nowe metody.

### `super()` — wywołanie metody klasy bazowej

```python
class Car(Vehicle):
    def __init__(self, brand: str) -> None:
        super().__init__()   # wywołanie __init__ klasy bazowej
        self.brand = brand

    def move(self) -> str:
        base = super().move()   # "Pojazd przemieszcza się"
        return f"{self.brand}: {base}"
```

Diagram: `diagrams/topic_07.png`

![Dziedziczenie](diagrams/topic_07.png)

### Kiedy dziedziczenie jest uzasadnione?

Dziedziczenie stosuj gdy zachodzi relacja **„jest-rodzajem"** (is-a):
- `Car` jest rodzajem `Vehicle` ✓
- `Stack` jest rodzajem `List` ✗ (Stack *używa* listy, ale nią nie jest)

Gdy relacja to „**ma**" (has-a), lepiej użyć **kompozycji**:

```python
# Zamiast class Stack(list):
class Stack:
    def __init__(self) -> None:
        self._items: list = []   # Stack MA listę, nie JEST listą
```

## Krok po kroku na kodzie

Plik: `examples/inheritance_demo.py`

```python
class Vehicle:
    def move(self) -> str:
        return "Pojazd przemieszcza się"

class Bike(Vehicle):
    def move(self) -> str:
        return "Rower jedzie"

class Car(Vehicle):
    def move(self) -> str:
        return "Samochód jedzie"
```

Polimorficzne użycie:

```python
fleet = [Bike(), Car()]
for vehicle in fleet:
    print(vehicle.move())   # każdy wie, jak się porusza
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/inheritance_demo.py`.
2. Dodaj klasę `Train(Vehicle)` z nadpisaną metodą `move()`.
3. Dodaj do `Vehicle` pole `max_speed` i nadpisz je w klasach pochodnych.
4. Napisz metodę `describe()` w `Vehicle` korzystającą z `self.move()`.
5. Porównaj kod: wersja z dziedziczeniem vs `if/elif` na typach.

### Oczekiwany efekt

- Student rozumie relację is-a i kiedy ją stosować.
- Student potrafi używać `super()` do rozszerzania metod bazowych.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_07.py`
- testy: `exercises/test_solutions.py`

Zadanie: napisz klasę `Train(Vehicle)` z nadpisaną metodą `move()`.

## Pytania egzaminacyjne

1. Co oznacza relacja is-a i kiedy uzasadnia dziedziczenie?
2. Jak działa `super()` i dlaczego jest ważny przy wielodziedziczeniu?
3. Jakie problemy powoduje zbyt głęboka hierarchia klas?
4. Dlaczego kompozycja bywa lepsza od dziedziczenia?
5. Podaj przykład błędnego użycia dziedziczenia.

## Literatura

- https://docs.python.org/3/tutorial/classes.html#inheritance
- E. Gamma i in., *Design Patterns*, s. „Prefer composition over inheritance".
- B. Meyer, *Object-Oriented Software Construction*, rozdz. „Inheritance".
