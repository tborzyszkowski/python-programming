# 11 - Interfejsy w Pythonie (`ABC` i `Protocol`)

## Cel

Pokazać dwa sposoby modelowania interfejsów: nominalny (`ABC`) i strukturalny (`Protocol`).

## Teoria

### Co to jest interfejs?

**Interfejs** to zestaw metod, który klasa **musi** zaimplementować.
W językach takich jak Java `interface` jest słowem kluczowym.
W Pythonie interfejs można wyrazić na dwa sposoby.

### Podejście 1: `ABC` + `@abstractmethod` (nominalne)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        ...
```

- Klasa dziedzicząca **musi** zaimplementować `pay`, inaczej `TypeError` przy próbie instancji.
- Sprawdzenie: `isinstance(obj, PaymentProcessor)` → `True`.

```python
class CardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"card:{amount:.2f}"
```

### Podejście 2: `Protocol` (strukturalne, duck typing ze wsparciem mypy)

```python
from typing import Protocol

class SupportsPay(Protocol):
    def pay(self, amount: float) -> str:
        ...
```

- Klasa **nie musi** po nim dziedziczyć — wystarczy, że ma metodę `pay`.
- Sprawdzenie: statycznie przez mypy/pyright, nie przez `isinstance`.
- Idealne gdy nie kontrolujemy klas zewnętrznych.

### Kiedy który?

| Kryterium | `ABC` | `Protocol` |
|---|---|---|
| Wymagana jawna deklaracja | Tak (`class Foo(ABC)`) | Nie |
| Weryfikacja runtime | `isinstance` | Brak (tylko statyczna) |
| Sprawdza zewnętrzne klasy | Nie | Tak |
| Wymusza implementację | Tak | Nie (tylko linter) |

Diagram: `diagrams/topic_11.png`

![ABC vs Protocol](diagrams/topic_11.png)

## Krok po kroku na kodzie

Plik: `examples/interfaces_demo.py`

```python
from abc import ABC, abstractmethod
from typing import Protocol

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        ...

class SupportsPay(Protocol):
    def pay(self, amount: float) -> str:
        ...

class CardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"card:{amount:.2f}"
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/interfaces_demo.py`.
2. Utwórz instancję `PaymentProcessor()` — co się dzieje?
3. Napisz `BlikProcessor` bez dziedziczenia po `PaymentProcessor`.
4. Sprawdź `isinstance(blik, PaymentProcessor)` — wynik?
5. Napisz funkcję z podpowiedzią `SupportsPay` — czy `BlikProcessor` pasuje?

### Oczekiwany efekt

- Student rozróżnia podejście nominalne i strukturalne do interfejsów.
- Student wie, kiedy użyć `ABC`, a kiedy `Protocol`.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_11.py`
- testy: `exercises/test_solutions.py`

Zadanie: napisz klasę `BlikProcessor` z metodą `pay(amount) -> str` w formacie `"blik:<kwota:.2f>"`.

## Pytania egzaminacyjne

1. Czym różni się `ABC` od `Protocol`?
2. Kiedy warto stosować nominalne interfejsy (`ABC`)?
3. Co daje typowanie strukturalne (`Protocol`) w praktyce projektowej?
4. Jak interfejsy wspierają testowanie (mockowanie)?
5. Dlaczego interfejs zmniejsza sprzężenie między modułami?

## Literatura

- https://docs.python.org/3/library/abc.html
- https://docs.python.org/3/library/typing.html#typing.Protocol
- L. Ramalho, *Fluent Python*, rozdz. „Protocols and Duck Typing".
