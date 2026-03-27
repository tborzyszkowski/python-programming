        # 02 - Definicja klasy i tworzenie obiektu

        ## Cel

        Opanować składnię klasy: atrybuty, konstruktor `__init__`, metody oraz tworzenie instancji.

        ## Teoria i intuicja

        Definicja klasy tworzy nowy typ. Dopiero wywołanie klasy tworzy obiekt z własnym stanem.

        W praktyce warto myśleć o tym temacie na trzech poziomach:
        1. model pojęciowy (co chcemy opisać),
        2. składnia Pythona (jak to zapisać),
        3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

        Diagram: `diagrams/topic_02.png`

        ![Diagram tematu](diagrams/topic_02.png)

        ## Krok po kroku na kodzie

        Plik: `examples/class_definition.py`

        ```python
        class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia")
        self.balance += amount


if __name__ == "__main__":
    account = BankAccount("Jan", 100.0)
    account.deposit(20.0)
    print(account.balance)
        ```

        Uruchomienie:

        ```bash
        python src/_04-classes/02-class-definition-and-object-creation/examples/class_definition.py
        ```

        ## Zadanie do samodzielnego rozwiązania

        Dodaj funkcję `safe_transfer(src, dst, amount)` wykonującą przelew między kontami.

        - szablon: `exercises/tasks.py`
        - przykładowe rozwiązanie: `exercises/solutions_02.py`
        - testy: `exercises/test_solutions.py`

        ## Pytania kontrolne

        1. Jaki problem projektowy rozwiązuje ten mechanizm?
        2. Jak wyglądałaby wersja bez użycia klas?
        3. Jak przetestować to zachowanie jednostkowo?

        ## Literatura

        - https://docs.python.org/3/tutorial/classes.html
        - https://docs.python.org/3/reference/datamodel.html
