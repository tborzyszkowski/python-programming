        # 10 - Większy przykład: system ocen

        ## Cel

        Pokazać współdziałanie dziedziczenia i polimorfizmu w mini-architekturze modułu uczelnianego.

        ## Teoria i intuicja

        Przykład strategii oceniania: klasa `Course` deleguje logikę do obiektu polityki, co wspiera SRP i testowalność.

        W praktyce warto myśleć o tym temacie na trzech poziomach:
        1. model pojęciowy (co chcemy opisać),
        2. składnia Pythona (jak to zapisać),
        3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

        Diagram: `diagrams/topic_10.png`

        ![Diagram tematu](diagrams/topic_10.png)

        ## Krok po kroku na kodzie

        Plik: `examples/grading_system.py`

        ```python
        class GradePolicy:
    def final_score(self, points: list[float]) -> float:
        raise NotImplementedError


class MeanPolicy(GradePolicy):
    def final_score(self, points: list[float]) -> float:
        return sum(points) / len(points)


class BestOfTwoPolicy(GradePolicy):
    def final_score(self, points: list[float]) -> float:
        top = sorted(points, reverse=True)[:2]
        return sum(top) / len(top)


class Course:
    def __init__(self, name: str, policy: GradePolicy) -> None:
        self.name = name
        self.policy = policy

    def evaluate(self, points: list[float]) -> float:
        return self.policy.final_score(points)
        ```

        Uruchomienie:

        ```bash
        python src/_04-classes/10-large-example-inheritance-polymorphism/examples/grading_system.py
        ```

        ## Zadanie do samodzielnego rozwiązania

        Dodaj `WeightedPolicy` i przetestuj obliczenie wyniku końcowego.

        - szablon: `exercises/tasks.py`
        - przykładowe rozwiązanie: `exercises/solutions_10.py`
        - testy: `exercises/test_solutions.py`

        ## Pytania kontrolne

        1. Jaki problem projektowy rozwiązuje ten mechanizm?
        2. Jak wyglądałaby wersja bez użycia klas?
        3. Jak przetestować to zachowanie jednostkowo?

        ## Literatura

        - https://docs.python.org/3/tutorial/classes.html
        - https://docs.python.org/3/reference/datamodel.html
