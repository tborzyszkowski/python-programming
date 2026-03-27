# 09 - Polimorfizm: jedna operacja, wiele implementacji

## Cel

Zrozumieć polimorfizm dynamiczny i ideę „programuj do interfejsu, nie implementacji”.

## Teoria i intuicja

Polimorfizm oznacza, że ten sam komunikat (`area`) może mieć różne implementacje zależnie od typu obiektu.

W praktyce warto myśleć o tym temacie na trzech poziomach:
1. model pojęciowy (co chcemy opisać),
2. składnia Pythona (jak to zapisać),
3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

Diagram: `diagrams/topic_09.png`

![Diagram tematu](diagrams/topic_09.png)

## Krok po kroku na kodzie

Plik: `examples/polymorphism_demo.py`

```python
class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return 3.14159 * self.r * self.r
```

Uruchomienie:

```bash
python src/_04-classes/09-polymorphism/examples/polymorphism_demo.py
```

## Zadanie do samodzielnego rozwiązania

Dodaj klasę `Triangle` z metodą `area`.

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_09.py`
- testy: `exercises/test_solutions.py`

## Pytania kontrolne

1. Jaki problem projektowy rozwiązuje ten mechanizm?
2. Jak wyglądałaby wersja bez użycia klas?
3. Jak przetestować to zachowanie jednostkowo?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/reference/datamodel.html

## Kontekst historyczny i projektowy (rozszerzenie)

Polimorfizm wywodzi się z idei późnego wiązania (late binding): klient wywołuje operację, ale konkretna implementacja zależy od typu obiektu w czasie wykonania. W Pythonie ten mechanizm jest naturalny dzięki dynamicznemu modelowi obiektów.

## Dodatkowy przykład kodu

```python
shapes = [Rectangle(3, 4), Circle(2)]
areas = [shape.area() for shape in shapes]
print(areas)
print(sum(areas))
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj nową figurę `Triangle` i oblicz jej pole.
2. Napisz funkcję przyjmującą listę obiektów `Shape`.
3. Sprawdź, że funkcja działa bez zmian po dodaniu nowej klasy.
4. Zastanów się, jak to wspiera zasadę Open/Closed.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Zdefiniuj polimorfizm i podaj przykład w Pythonie.
2. Dlaczego polimorfizm redukuje liczbę instrukcji `if/elif`?
3. Co to znaczy „programuj do interfejsu”?
4. Jak testować kod oparty o polimorfizm?
5. Jakie zależności projektowe zmniejsza polimorfizm?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
