# 08 - Dziedziczenie wielokrotne i MRO

## Cel

Pokazać mechanizm MRO i bezpieczne użycie `super()` przy wielu klasach bazowych.

## Teoria i intuicja

W Pythonie porządek rozwiązywania metod (MRO) jest deterministyczny i opiera się o algorytm C3.

W praktyce warto myśleć o tym temacie na trzech poziomach:
1. model pojęciowy (co chcemy opisać),
2. składnia Pythona (jak to zapisać),
3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

Diagram: `diagrams/topic_08.png`

![Diagram tematu](diagrams/topic_08.png)

## Krok po kroku na kodzie

Plik: `examples/multiple_inheritance.py`

```python
class LoggerMixin:
    def describe(self) -> str:
        return "logger"

class TimestampMixin:
    def describe(self) -> str:
        return "timestamp"

class Event(LoggerMixin, TimestampMixin):
    @classmethod
    def describe_chain(cls) -> list[str]:
        return [c.__name__ for c in cls.mro()]
```

Uruchomienie:

```bash
python src/_04-classes/08-multiple-inheritance/examples/multiple_inheritance.py
```

## Zadanie do samodzielnego rozwiązania

Zaimplementuj `source()` zwracające pierwszą klasę mixin z MRO.

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_08.py`
- testy: `exercises/test_solutions.py`

## Pytania kontrolne

1. Jaki problem projektowy rozwiązuje ten mechanizm?
2. Jak wyglądałaby wersja bez użycia klas?
3. Jak przetestować to zachowanie jednostkowo?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/reference/datamodel.html

## Kontekst historyczny i projektowy (rozszerzenie)

Dziedziczenie wielokrotne pojawiło się m.in. w CLOS i C++. Python wspiera je w pełni, ale rozwiązuje konflikty metod przez liniaryzację C3 (MRO). Dzięki temu porządek wyszukiwania metod jest jednoznaczny i przewidywalny.

## Dodatkowy przykład kodu

```python
print(Event.describe_chain())
print(Event.source())
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj trzeci mixin i przeanalizuj nowe MRO.
2. Zastosuj `super()` w łańcuchu metod inicjalizujących.
3. Porównaj wynik wywołań przy zmianie kolejności klas bazowych.
4. Opisz, kiedy mixiny są dobrym wyborem architektonicznym.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Co to jest MRO i jak działa w Pythonie?
2. Dlaczego kolejność klas bazowych ma znaczenie?
3. Jak poprawnie łączyć mixiny z klasą domenową?
4. Jakie pułapki pojawiają się bez `super()` w wielodziedziczeniu?
5. Kiedy lepiej użyć kompozycji zamiast wielodziedziczenia?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
