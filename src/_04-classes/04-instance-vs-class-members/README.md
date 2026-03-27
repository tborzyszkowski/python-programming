    # 04 - Komponenty instancyjne i klasowe/statyczne

    ## Cel

    Odróżniać atrybuty instancji, atrybuty klasy, metody klasowe i statyczne.

    ## Teoria i intuicja

    Atrybut klasowy jest współdzielony. Atrybut instancji należy do konkretnego obiektu.

    W praktyce warto myśleć o tym temacie na trzech poziomach:
    1. model pojęciowy (co chcemy opisać),
    2. składnia Pythona (jak to zapisać),
    3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

    Diagram: `diagrams/topic_04.png`

    ![Diagram tematu](diagrams/topic_04.png)

    ## Krok po kroku na kodzie

    Plik: `examples/members_demo.py`

    ```python
    class Session:
active_count = 0

def __init__(self, user: str) -> None:
    self.user = user
    Session.active_count += 1

@classmethod
def active_sessions(cls) -> int:
    return cls.active_count

@staticmethod
def is_valid_username(name: str) -> bool:
    return len(name) >= 3
    ```

    Uruchomienie:

    ```bash
    python src/_04-classes/04-instance-vs-class-members/examples/members_demo.py
    ```

    ## Zadanie do samodzielnego rozwiązania

    Dodaj metodę klasową `reset_counter`, która zeruje licznik aktywnych sesji.

    - szablon: `exercises/tasks.py`
    - przykładowe rozwiązanie: `exercises/solutions_04.py`
    - testy: `exercises/test_solutions.py`

    ## Pytania kontrolne

    1. Jaki problem projektowy rozwiązuje ten mechanizm?
    2. Jak wyglądałaby wersja bez użycia klas?
    3. Jak przetestować to zachowanie jednostkowo?

    ## Literatura

    - https://docs.python.org/3/tutorial/classes.html
    - https://docs.python.org/3/reference/datamodel.html
