# 09 - Polimorfizm: jedna operacja, wiele implementacji

## Cel

Zrozumieć polimorfizm dynamiczny i ideę „programuj do interfejsu, nie do implementacji".

## Teoria

### Skąd pochodzi polimorfizm?

Termin pochodzi z greki: *poly* (wiele) + *morphe* (kształt).
W OOP oznacza, że ten sam **komunikat** (`area()`) może mieć różne **implementacje** zależnie od
faktycznego typu obiektu — wybranego dopiero w czasie wykonania (*late binding*).

Alan Kay (twórca Smalltalka) powiedział: „OOP to przesyłanie komunikatów".
Polimorfizm jest fundamentem tej idei.

### Duck typing a polimorfizm w Pythonie

Python stosuje **duck typing**: obiekt nie musi dziedziczyć po określonej klasie bazowej,
wystarczy że implementuje oczekiwane metody.

```python
class Duck:
    def quack(self) -> str:
        return "Quack!"

class Person:
    def quack(self) -> str:
        return "I'm quacking like a duck!"

def make_it_quack(duck) -> None:
    print(duck.quack())   # działa dla Duck i Person
```

### Hierarchia klas + polimorfizm = otwartość na rozszerzenie

```python
class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def area(self) -> float:
        return self.w * self.h

class Circle(Shape):
    def area(self) -> float:
        return math.pi * self.r ** 2
```

Funkcja `total_area(shapes)` działa bez zmian gdy dodajemy nowe figury:

```python
def total_area(shapes: list[Shape]) -> float:
    return sum(s.area() for s in shapes)
```

To jest zasada **Open/Closed**: otwarta na rozszerzenie, zamknięta na modyfikację.

Diagram: `diagrams/topic_09.png`

![Polimorfizm figur geometrycznych](diagrams/topic_09.png)

## Krok po kroku na kodzie

Plik: `examples/polymorphism_demo.py` — rozszerzona wersja z `Triangle`, `perimeter`, `describe`, `main`.

```python
shapes: list[Shape] = [
    Rectangle(3, 4),
    Circle(2),
    Triangle(6, 4, 6, 5, 5),
]
for shape in shapes:
    print(shape.describe())   # każdy wie, jak się opisać
print(f"Łączna powierzchnia: {total_area(shapes):.2f}")
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/polymorphism_demo.py`.
2. Dodaj klasę `Square(Rectangle)` — czy `total_area` działa bez zmian?
3. Napisz funkcję `largest_shape(shapes)` zwracającą figurę o największym polu.
4. Zamień `raise NotImplementedError` w `Shape` na `@abstractmethod` z `abc`.
5. Sprawdź co się stanie przy próbie tworzenia instancji `Shape` z `abstractmethod`.

### Oczekiwany efekt

- Student rozumie polimorfizm dynamiczny i duck typing.
- Student potrafi pisać funkcje działające na kolekcjach polimorficznych obiektów.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_09.py`
- testy: `exercises/test_solutions.py`

Zadanie: napisz klasę `Triangle(Shape)` z metodą `area()` i konstruktorem `(base, height)`.

## Pytania egzaminacyjne

1. Zdefiniuj polimorfizm i podaj przykład w Pythonie.
2. Co to jest duck typing i jak różni się od polimorfizmu nominalnego?
3. Dlaczego polimorfizm redukuje liczbę instrukcji `if/elif`?
4. Jak testować kod oparty o polimorfizm?
5. Na czym polega zasada Open/Closed i jak wiąże się z polimorfizmem?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/glossary.html#term-duck-typing
- B. Meyer, *Object-Oriented Software Construction*, rozdz. „Polymorphism".
