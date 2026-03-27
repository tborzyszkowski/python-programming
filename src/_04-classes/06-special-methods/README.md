    # 06 - Metody specjalne (`dunder methods`)

    ## Cel

    Praktycznie używać `__init__`, `__new__`, `__len__`, `__str__`, getter/setter przez `property`.

    ## Teoria i intuicja

    Metody specjalne integrują klasy z protokołami języka (`len`, `str`, iteracja, porównania, kontekst).

    W praktyce warto myśleć o tym temacie na trzech poziomach:
    1. model pojęciowy (co chcemy opisać),
    2. składnia Pythona (jak to zapisać),
    3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

    Diagram: `diagrams/topic_06.png`

    ![Diagram tematu](diagrams/topic_06.png)

    ## Krok po kroku na kodzie

    Plik: `examples/dunder_demo.py`

    ```python
    class Vector2D:
def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

def __len__(self) -> int:
    return 2

def __str__(self) -> str:
    return f"Vector2D(x={self.x}, y={self.y})"

@property
def magnitude_hint(self) -> float:
    return abs(self.x) + abs(self.y)
    ```

    Uruchomienie:

    ```bash
    python src/_04-classes/06-special-methods/examples/dunder_demo.py
    ```

    ## Zadanie do samodzielnego rozwiązania

    Dodaj metodę `__repr__` zwracającą jednoznaczny zapis obiektu.

    - szablon: `exercises/tasks.py`
    - przykładowe rozwiązanie: `exercises/solutions_06.py`
    - testy: `exercises/test_solutions.py`

    ## Pytania kontrolne

    1. Jaki problem projektowy rozwiązuje ten mechanizm?
    2. Jak wyglądałaby wersja bez użycia klas?
    3. Jak przetestować to zachowanie jednostkowo?

    ## Literatura

    - https://docs.python.org/3/tutorial/classes.html
    - https://docs.python.org/3/reference/datamodel.html
