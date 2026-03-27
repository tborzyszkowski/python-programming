# 12 - Wzorce projektowe oparte na polimorfizmie i dziedziczeniu

## Cel

Przedstawić wzorce Strategy, Template Method i Factory Method na krótkich przykładach.

## Teoria i intuicja

Wzorce pokazują, jak ograniczyć rozbudowane instrukcje warunkowe przez delegowanie zachowania do obiektów.

W praktyce warto myśleć o tym temacie na trzech poziomach:
1. model pojęciowy (co chcemy opisać),
2. składnia Pythona (jak to zapisać),
3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

Diagram: `diagrams/topic_12.png`

![Diagram tematu](diagrams/topic_12.png)

## Krok po kroku na kodzie

Plik: `examples/patterns_demo.py`

```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        raise NotImplementedError

class StudentDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.8

class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price

def checkout(price: float, strategy: DiscountStrategy) -> float:
    return strategy.apply(price)
```

Uruchomienie:

```bash
python src/_04-classes/12-design-patterns-polymorphism/examples/patterns_demo.py
```

## Zadanie do samodzielnego rozwiązania

Dodaj strategię `VipDiscount` i fabrykę `build_discount(kind)`.

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_12.py`
- testy: `exercises/test_solutions.py`

## Pytania kontrolne

1. Jaki problem projektowy rozwiązuje ten mechanizm?
2. Jak wyglądałaby wersja bez użycia klas?
3. Jak przetestować to zachowanie jednostkowo?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/reference/datamodel.html

## Kontekst historyczny i projektowy (rozszerzenie)

Wzorce projektowe nie są „przepisami do kopiowania”, lecz wspólnym językiem opisu rozwiązań. W kontekście OOP najczęściej opierają się na polimorfizmie i delegowaniu odpowiedzialności. Python pozwala realizować je zwięźle, bez nadmiernej ceremonii.

## Dodatkowy przykład kodu

```python
strategy = build_discount("vip")
print(checkout(100.0, strategy))
print(checkout(100.0, StudentDiscount()))
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj trzecią strategię rabatu i podepnij ją w fabryce.
2. Zaimplementuj prostą wersję Template Method dla raportu.
3. Porównaj kod przed i po wprowadzeniu wzorca Strategy.
4. Opisz kompromisy: prostota vs elastyczność architektury.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Na czym polega wzorzec Strategy i kiedy go stosować?
2. Czym różni się Factory Method od prostego `if/elif`?
3. Jak polimorfizm redukuje złożoność kodu klienta?
4. Jakie koszty wprowadza nadmierna liczba klas wzorców?
5. Podaj przykład wzorca, który nie byłby tu opłacalny.

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
