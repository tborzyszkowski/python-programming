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

## Kontekst historyczny i projektowy (rozszerzenie)

Początki programowania obiektowego wiążą się z językiem **Simula 67**, gdzie pojęcie obiektu miało modelować byty świata rzeczywistego (np. klientów banku, procesy, pojazdy). W **Smalltalku** obiekt stał się podstawową jednostką organizacji programu. Python przejął wiele intuicji z tej tradycji, ale zachował pragmatyzm: klasy i obiekty współistnieją tu z funkcjami, modułami i stylem proceduralnym.

## Dodatkowy przykład kodu

```python
students = [Student("Ala", 1), Student("Olek", 2), Student("Iga", 1)]
first_year = [s for s in students if s.year == 1]
print([describe_student(s) for s in first_year])
```

## Mini-lab rozszerzony (krok po kroku)

1. Utwórz klasę `Course` z polami `name` i `ects`.
2. Utwórz 3 obiekty tej klasy i zapisz je na liście.
3. Napisz funkcję filtrującą kursy o `ects >= 5`.
4. Dodaj czytelny opis kursu przez metodę `__str__`.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Wyjaśnij różnicę semantyczną między pojęciami: klasa, obiekt, instancja.
2. Dlaczego modelowanie obiektowe bywa korzystne przy dużych projektach?
3. Podaj przykład problemu, który lepiej opisać obiektami niż samymi funkcjami.
4. Czym różni się nazwa klasy od obiektu utworzonego przez tę klasę?
5. Jak przetestować poprawność tworzenia obiektów dla danej klasy?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
