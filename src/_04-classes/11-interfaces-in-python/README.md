        # 11 - Interfejsy w Pythonie (`ABC` i `Protocol`)

        ## Cel

        Pokazać dwa sposoby modelowania interfejsów: nominalnie (`ABC`) i strukturalnie (`Protocol`).

        ## Teoria i intuicja

        `ABC` wymusza implementację metod, a `Protocol` wspiera duck typing i statyczną analizę typów.

        W praktyce warto myśleć o tym temacie na trzech poziomach:
        1. model pojęciowy (co chcemy opisać),
        2. składnia Pythona (jak to zapisać),
        3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

        Diagram: `diagrams/topic_11.png`

        ![Diagram tematu](diagrams/topic_11.png)

        ## Krok po kroku na kodzie

        Plik: `examples/interfaces_demo.py`

        ```python
        from abc import ABC, abstractmethod
from typing import Protocol


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        raise NotImplementedError


class SupportsPay(Protocol):
    def pay(self, amount: float) -> str:
        ...


class CardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"card:{amount:.2f}"
        ```

        Uruchomienie:

        ```bash
        python src/_04-classes/11-interfaces-in-python/examples/interfaces_demo.py
        ```

        ## Zadanie do samodzielnego rozwiązania

        Dodaj `BlikProcessor` zgodny z interfejsem płatności.

        - szablon: `exercises/tasks.py`
        - przykładowe rozwiązanie: `exercises/solutions_11.py`
        - testy: `exercises/test_solutions.py`

        ## Pytania kontrolne

        1. Jaki problem projektowy rozwiązuje ten mechanizm?
        2. Jak wyglądałaby wersja bez użycia klas?
        3. Jak przetestować to zachowanie jednostkowo?

        ## Literatura

        - https://docs.python.org/3/tutorial/classes.html
        - https://docs.python.org/3/reference/datamodel.html
