        # 01 - Klasa a obiekt: intuicja i historia

        ## Cel

        Zrozumieć różnicę między klasą (opis typu) a obiektem (konkretna instancja) oraz historyczne źródła OOP.

        ## Teoria i intuicja

        W klasycznych językach obiektowych (Simula, Smalltalk) klasa była przepisem, a obiekt egzemplarzem.

        W praktyce warto myśleć o tym temacie na trzech poziomach:
        1. model pojęciowy (co chcemy opisać),
        2. składnia Pythona (jak to zapisać),
        3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

        Diagram: `diagrams/topic_01.png`

        ![Diagram tematu](diagrams/topic_01.png)

        ## Krok po kroku na kodzie

        Plik: `examples/class_object_story.py`

        ```python
        from dataclasses import dataclass


@dataclass
class Student:
    name: str
    year: int


def describe_student(student: Student) -> str:
    return f"{student.name} (rok {student.year})"


if __name__ == "__main__":
    print(describe_student(Student("Jan", 1)))
        ```

        Uruchomienie:

        ```bash
        python src/_04-classes/01-class-vs-object/examples/class_object_story.py
        ```

        ## Zadanie do samodzielnego rozwiązania

        Napisz funkcję `count_first_year(students)`, która policzy studentów z pierwszego roku.

        - szablon: `exercises/tasks.py`
        - przykładowe rozwiązanie: `exercises/solutions_01.py`
        - testy: `exercises/test_solutions.py`

        ## Pytania kontrolne

        1. Jaki problem projektowy rozwiązuje ten mechanizm?
        2. Jak wyglądałaby wersja bez użycia klas?
        3. Jak przetestować to zachowanie jednostkowo?

        ## Literatura

        - https://docs.python.org/3/tutorial/classes.html
        - https://docs.python.org/3/reference/datamodel.html
