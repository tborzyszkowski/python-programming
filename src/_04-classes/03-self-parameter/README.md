# 03 - Rola `self` w Pythonie

## Cel

Zrozumieć, że `self` wskazuje bieżący obiekt, wiąże metodę z konkretną instancją i dlaczego jest jawny.

## Teoria

### Dlaczego `self` jest jawny?

W C++/Java bieżący obiekt kryje się pod **ukrytym** `this`.
Python czyni to powiązanie **jawnym**: każda metoda instancji dostaje jako pierwszy parametr
referencję do wywołującego obiektu. Nazwa `self` to konwencja, nie słowo kluczowe.

```python
class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> int:
        self.value += 1
        return self.value
```

Wywołanie `c.increment()` to syntaktyczny cukier na `Counter.increment(c)`:

```python
c = Counter()
c.increment()             # wywołanie przez obiekt
Counter.increment(c)      # wywołanie przez klasę — identyczny efekt
```

### Niezależność stanu instancji

Każdy obiekt ma **własną kopię** atrybutów instancji:

```python
a = Counter()
b = Counter()
a.increment()
a.increment()
b.increment()
print(a.value)  # 2
print(b.value)  # 1  — stany niezależne!
```

Diagram: `diagrams/topic_03.png`

![Self – powiązanie metoda–instancja](diagrams/topic_03.png)

### Typowy błąd: brak `self`

```python
class Broken:
    def __init__(self):
        value = 0        # lokalna zmienna, nie atrybut!

    def get(self):
        return self.value   # AttributeError!
```

## Krok po kroku na kodzie

Plik: `examples/self_usage.py`

```python
class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> int:
        self.value += 1
        return self.value

    def add_many(self, n: int) -> int:
        self.value += n
        return self.value
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/self_usage.py`.
2. Stwórz dwa liczniki; zwiększ każdy inną liczbę razy i sprawdź niezależność stanów.
3. Dodaj metodę `reset()` — zeruje `self.value`.
4. Usuń `self` z sygnatury `increment` i sprawdź, co wypisze Python.
5. Napisz test jednostkowy sprawdzający, że dwa liczniki nie wpływają na siebie.

### Oczekiwany efekt

- Student rozumie mechanizm wiązania metody z instancją.
- Student umie wytłumaczyć, dlaczego `self` jest jawny w Pythonie.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_03.py`
- testy: `exercises/test_solutions.py`

Zadanie: dopisz metodę `add_many(self, n: int) -> int` do klasy `Counter`.

## Pytania egzaminacyjne

1. Dlaczego `self` w Pythonie jest parametrem jawnym?
2. Co oznacza „wiązanie metody z instancją" w praktyce?
3. Jaka jest różnica między `c.increment()` a `Counter.increment(c)`?
4. Dlaczego dwie instancje tej samej klasy mają niezależny stan?
5. Jakie błędy pojawiają się przy pominięciu `self` w ciele metody?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/faq/design.html#why-must-self-be-used-explicitly-in-method-definitions-and-calls
