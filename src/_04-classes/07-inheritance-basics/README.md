# 07 - Dziedziczenie w OOP i w Pythonie

## Cel

Wyjaśnić relację „jest-rodzajem” oraz nadpisywanie metod w klasach pochodnych.

## Teoria i intuicja

Dziedziczenie umożliwia ponowne użycie kodu i modelowanie hierarchii pojęć domenowych.

W praktyce warto myśleć o tym temacie na trzech poziomach:
1. model pojęciowy (co chcemy opisać),
2. składnia Pythona (jak to zapisać),
3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

Diagram: `diagrams/topic_07.png`

![Diagram tematu](diagrams/topic_07.png)

## Krok po kroku na kodzie

Plik: `examples/inheritance_demo.py`

```python
class Vehicle:
    def move(self) -> str:
        return "Pojazd przemieszcza się"

class Bike(Vehicle):
    def move(self) -> str:
        return "Rower jedzie"

class Car(Vehicle):
    def move(self) -> str:
        return "Samochód jedzie"
```

Uruchomienie:

```bash
python src/_04-classes/07-inheritance-basics/examples/inheritance_demo.py
```

## Zadanie do samodzielnego rozwiązania

Dodaj klasę `Train(Vehicle)` i nadpisz `move()`.

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_07.py`
- testy: `exercises/test_solutions.py`

## Pytania kontrolne

1. Jaki problem projektowy rozwiązuje ten mechanizm?
2. Jak wyglądałaby wersja bez użycia klas?
3. Jak przetestować to zachowanie jednostkowo?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/reference/datamodel.html

## Kontekst historyczny i projektowy (rozszerzenie)

Dziedziczenie było centralną osią klasycznego OOP. Współcześnie traktuje się je ostrożniej: to narzędzie silne, ale wymagające dobrego modelu domeny. W Pythonie dziedziczenie dobrze działa, gdy relacja „jest-rodzajem” jest rzeczywista i stabilna.

## Dodatkowy przykład kodu

```python
fleet = [Bike(), Car()]
for vehicle in fleet:
    print(vehicle.move())
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj wspólne pole `max_speed` w klasie bazowej.
2. Nadpisz to pole w klasach potomnych.
3. Dodaj metodę bazową `describe()` i rozszerz ją w potomnych.
4. Porównaj kod z dziedziczeniem i bez dziedziczenia.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Kiedy relacja dziedziczenia jest uzasadniona projektowo?
2. Co oznacza nadpisywanie metody (`override`)?
3. Jakie problemy powoduje zbyt głęboka hierarchia klas?
4. Dlaczego kompozycja bywa alternatywą dla dziedziczenia?
5. Podaj przykład poprawnego i błędnego użycia dziedziczenia.

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
