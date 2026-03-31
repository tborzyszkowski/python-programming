# 08 - Dziedziczenie wielokrotne i MRO

## Cel

Pokazać mechanizm MRO (Method Resolution Order) i bezpieczne użycie `super()` przy wielu klasach bazowych.

## Teoria

### Problem „diamentu" i algorytm C3

Gdy klasa dziedziczy po dwóch klasach, które mają wspólnego przodka, powstaje problem
**„diamentu"** — niejednoznaczność, z której klasy pochodzi metoda.

```
     Base
    /    \
  A        B
    \    /
      C
```

Python rozwiązuje to przez **liniaryzację C3** (Python 2.3+), która tworzy
jednoznaczną **listę przeszukiwania (MRO)**:

```python
class Base: pass
class A(Base): pass
class B(Base): pass
class C(A, B): pass

print(C.mro())
# [<C>, <A>, <B>, <Base>, <object>]
```

Metoda jest szukana **od lewej do prawej** w tej liście.

### `super()` w wielodziedziczeniu

`super()` nie wywołuje „klasy nadrzędnej" — wywołuje **następną klasę w MRO**:

```python
class LoggerMixin:
    def describe(self) -> str:
        return f"[LOG] {super().describe()}"

class TimestampMixin:
    def describe(self) -> str:
        return f"[TS] {super().describe()}"

class Base:
    def describe(self) -> str:
        return "base"

class Event(LoggerMixin, TimestampMixin, Base):
    pass

print(Event().describe())
# [LOG] [TS] base
```

Każde `super()` przekazuje wywołanie dalej wzdłuż MRO — to umożliwia **mixin-based composition**.

### Mixiny — dobra praktyka

Mixin to klasa **bez własnego stanu** (bez `__init__`), dostarczająca tylko zachowanie:

```python
class JsonMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)
```

Diagram: `diagrams/topic_08.png`

![MRO i mixiny](diagrams/topic_08.png)

## Krok po kroku na kodzie

Plik: `examples/multiple_inheritance.py`

```python
class Event(LoggerMixin, TimestampMixin):
    @classmethod
    def describe_chain(cls) -> list[str]:
        return [c.__name__ for c in cls.mro()]

    @classmethod
    def source(cls) -> str:
        return cls.mro()[1].__name__   # pierwszy mixin po samej klasie
```

```python
print(Event.describe_chain())   # ['Event', 'LoggerMixin', 'TimestampMixin', 'object']
print(Event.source())           # 'LoggerMixin'
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/multiple_inheritance.py`.
2. Dodaj trzeci mixin i przeanalizuj nowe MRO.
3. Zmień kolejność klas bazowych — obserwuj jak zmienia się MRO.
4. Zastosuj `super()` w łańcuchu `describe` wszystkich mixinów.
5. Sprawdź co się stanie gdy dwa mixiny mają metodę o tej samej nazwie.

### Oczekiwany efekt

- Student rozumie MRO i potrafi go odczytać przez `ClassName.mro()`.
- Student potrafi bezpiecznie łączyć mixiny z klasą domenową.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_08.py`
- testy: `exercises/test_solutions.py`

Zadanie: zaimplementuj metodę `source()` zwracającą nazwę pierwszego mixinu w MRO.

## Pytania egzaminacyjne

1. Co to jest MRO i jak działa algorytm C3?
2. Dlaczego kolejność klas bazowych ma znaczenie?
3. Jak `super()` zachowuje się w wielodziedziczeniu?
4. Czym jest mixin i kiedy go stosować?
5. Kiedy lepiej użyć kompozycji zamiast wielodziedziczenia?

## Literatura

- https://docs.python.org/3/reference/datamodel.html#mro
- https://www.python.org/download/releases/2.3/mro/
- L. Ramalho, *Fluent Python*, rozdz. „Multiple Inheritance and Method Resolution Order".
