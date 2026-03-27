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
