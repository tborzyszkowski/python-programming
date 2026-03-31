# 06 - Metody specjalne (`dunder methods`)

## Cel

Opanować metody specjalne i zrozumieć, jak integrują klasy z protokołami języka.

## Teoria

### Czym są metody specjalne?

Metody otoczone podwójnymi podkreślnikami (`__init__`, `__str__`, `__add__`) są
wywoływane przez Pythona automatycznie — nigdy nie wołasz ich bezpośrednio.

```
len(v)    →  v.__len__()
str(v)    →  v.__str__()
v1 + v2   →  v1.__add__(v2)
v1 == v2  →  v1.__eq__(v2)
repr(v)   →  v.__repr__()
```

### Kluczowe metody i ich rola

| Metoda | Kiedy wywoływana | Zwraca |
|---|---|---|
| `__new__(cls)` | Tworzenie obiektu w pamięci | nowy pusty obiekt |
| `__init__(self)` | Inicjalizacja po `__new__` | `None` |
| `__str__(self)` | `str(obj)`, `print(obj)` | czytelny napis |
| `__repr__(self)` | `repr(obj)`, REPL | jednoznaczny napis (eval-able) |
| `__len__(self)` | `len(obj)` | `int >= 0` |
| `__eq__(self, other)` | `==` | `bool` |
| `__add__(self, other)` | `+` | nowy obiekt |
| `__lt__`, `__le__`… | `<`, `<=`… | `bool` |

### `__str__` vs `__repr__`

```python
v = Vector2D(3.0, 4.0)
print(str(v))   # "Vector2D(x=3.0, y=4.0)"   — dla użytkownika
print(repr(v))  # "Vector2D(x=3.0, y=4.0)"   — dla programisty (eval-able)
```

Zasada: `repr` powinien pozwalać odtworzyć obiekt przez `eval(repr(obj))`.

### `@property` — kontrolowany dostęp

```python
@property
def magnitude(self) -> float:
    return math.sqrt(self.x**2 + self.y**2)
```

`@property` sprawia, że obliczana wartość wygląda jak atrybut:
`v.magnitude` zamiast `v.magnitude()`.

Diagram: `diagrams/topic_06.png`

![Metody specjalne](diagrams/topic_06.png)

## Krok po kroku na kodzie

Plik: `examples/dunder_demo.py` — rozszerzona klasa `Vector2D`:
- `__new__` / `__init__` / `__str__` / `__repr__`
- `__len__` / `__eq__` / `__add__` / `__mul__`
- `@property magnitude`

```python
v1 = Vector2D(3, 4)
v2 = Vector2D(1, -1)
print(str(v1))               # __str__
print(repr(v1))              # __repr__
print(len(v1))               # __len__
print(v1 == Vector2D(3, 4))  # __eq__
print(v1 + v2)               # __add__
print(f"{v1.magnitude:.2f}") # @property
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/dunder_demo.py`.
2. Sprawdź `v1 == v2` i `v1 == Vector2D(3, 4)` — dlaczego różny wynik?
3. Dodaj `__mul__` po prawej stronie (`__rmul__`) tak, by `2 * v` działało.
4. Dopisz `__neg__` zwracający wektor o przeciwnych współrzędnych.
5. Napisz test `assert eval(repr(v1)) == v1` i sprawdź czy przechodzi.

### Oczekiwany efekt

- Student rozumie, kiedy Python wywołuje poszczególne metody specjalne.
- Student potrafi implementować operatory i protokoły dla własnych klas.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_06.py`
- testy: `exercises/test_solutions.py`

Zadanie: dopisz metodę `__repr__` zwracającą napis `Vector2D(x=..., y=...)`.

## Pytania egzaminacyjne

1. Jaka jest różnica między `__str__` a `__repr__`?
2. Kiedy należy nadpisać `__new__`?
3. Dlaczego `__eq__` wymaga też implementacji `__hash__`?
4. Co robi `return NotImplemented` w `__eq__`?
5. Jak `@property` pomaga ukryć szczegóły implementacji?

## Literatura

- https://docs.python.org/3/reference/datamodel.html
- https://docs.python.org/3/library/functions.html#property
- L. Ramalho, *Fluent Python*, rozdz. „A Pythonic Object".
