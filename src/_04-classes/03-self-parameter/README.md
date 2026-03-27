        # 03 - Rola `self` w Pythonie

        ## Cel

        Zrozumieć, że `self` wskazuje bieżący obiekt i wiąże metodę z konkretną instancją.

        ## Teoria i intuicja

        `self` nie jest słowem kluczowym, ale kluczową konwencją. Oznacza bieżący obiekt i jego stan.

        W praktyce warto myśleć o tym temacie na trzech poziomach:
        1. model pojęciowy (co chcemy opisać),
        2. składnia Pythona (jak to zapisać),
        3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

        Diagram: `diagrams/topic_03.png`

        ![Diagram tematu](diagrams/topic_03.png)

        ## Krok po kroku na kodzie

        Plik: `examples/self_usage.py`

        ```python
        class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> int:
        self.value += 1
        return self.value


if __name__ == "__main__":
    counter = Counter()
    print(counter.increment())
        ```

        Uruchomienie:

        ```bash
        python src/_04-classes/03-self-parameter/examples/self_usage.py
        ```

        ## Zadanie do samodzielnego rozwiązania

        Napisz metodę `add_many(self, n)`, która zwiększa licznik o `n`.

        - szablon: `exercises/tasks.py`
        - przykładowe rozwiązanie: `exercises/solutions_03.py`
        - testy: `exercises/test_solutions.py`

        ## Pytania kontrolne

        1. Jaki problem projektowy rozwiązuje ten mechanizm?
        2. Jak wyglądałaby wersja bez użycia klas?
        3. Jak przetestować to zachowanie jednostkowo?

        ## Literatura

        - https://docs.python.org/3/tutorial/classes.html
        - https://docs.python.org/3/reference/datamodel.html
