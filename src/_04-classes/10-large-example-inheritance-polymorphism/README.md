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

## Kontekst historyczny i projektowy (rozszerzenie)

W większych systemach dziedziczenie i polimorfizm warto łączyć z separacją odpowiedzialności. Strategia oceniania to klasyczny przykład: algorytm można zmieniać bez modyfikacji klasy, która go używa.

## Dodatkowy przykład kodu

```python
course_mean = Course("Analiza", MeanPolicy())
course_best = Course("Algebra", BestOfTwoPolicy())
print(course_mean.evaluate([3.0, 4.0, 5.0]))
print(course_best.evaluate([3.0, 4.0, 5.0]))
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj politykę `WeightedPolicy` z wagami.
2. Dodaj walidację liczby punktów wejściowych.
3. Dopis test porównujący 3 strategie na tych samych danych.
4. Przeanalizuj, które klasy realizują SRP, a które nie.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Dlaczego wzorzec Strategy poprawia rozszerzalność systemu?
2. Jak oddzielić logikę domenową od prezentacji wyników?
3. Które elementy tego przykładu są polimorficzne?
4. Jak dodać nową politykę bez modyfikacji klasy `Course`?
5. Jak zaprojektować testy dla wielu strategii jednocześnie?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
