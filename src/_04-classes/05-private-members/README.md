# 05 - Komponenty prywatne w Pythonie

## Cel

Wyjaśnić konwencje prywatności (`_name`) i name mangling (`__name`).

## Teoria i intuicja

Python preferuje konwencje prywatności. `__name` uruchamia name mangling i ogranicza przypadkowy dostęp.

W praktyce warto myśleć o tym temacie na trzech poziomach:
1. model pojęciowy (co chcemy opisać),
2. składnia Pythona (jak to zapisać),
3. konsekwencje projektowe (testowalność, czytelność, rozszerzalność).

Diagram: `diagrams/topic_05.png`

![Diagram tematu](diagrams/topic_05.png)

## Krok po kroku na kodzie

Plik: `examples/private_members.py`

```python
class TemperatureSensor:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius
        self.__calibration_offset = 0.0

    def set_calibration(self, delta: float) -> None:
        self.__calibration_offset = delta

    def read(self) -> float:
        return self._celsius + self.__calibration_offset
```

Uruchomienie:

```bash
python src/_04-classes/05-private-members/examples/private_members.py
```

## Zadanie do samodzielnego rozwiązania

Dodaj metodę `is_overheated(threshold)` opartą o odczyt z `read()`.

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_05.py`
- testy: `exercises/test_solutions.py`

## Pytania kontrolne

1. Jaki problem projektowy rozwiązuje ten mechanizm?
2. Jak wyglądałaby wersja bez użycia klas?
3. Jak przetestować to zachowanie jednostkowo?

## Literatura

- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/reference/datamodel.html

## Kontekst historyczny i projektowy (rozszerzenie)

Python stosuje zasadę „consenting adults”: zamiast twardych barier dostępu preferuje konwencje. Dlatego `_name` sygnalizuje „użytek wewnętrzny”, a `__name` uruchamia mechanizm *name mangling*, który chroni głównie przed przypadkowym nadpisaniem.

## Dodatkowy przykład kodu

```python
sensor = TemperatureSensor(65.0)
sensor.set_calibration(1.5)
print(sensor.read())
print(sensor.is_overheated(66.0))
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj właściwość tylko-do-odczytu dla bieżącej temperatury.
2. Zaimplementuj walidację kalibracji (zakres wartości).
3. Pokaż w kodzie, jak działa name mangling dla `__calibration_offset`.
4. Porównaj `_pole` i `__pole` pod względem bezpieczeństwa API.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Czy Python ma prawdziwie prywatne pola? Uzasadnij.
2. Po co używa się konwencji `_name`?
3. Co robi mechanizm name mangling i jakie ma ograniczenia?
4. Jak projektować API klasy, by nie ujawniać zbędnych szczegółów?
5. Kiedy lepiej użyć metody niż bezpośredniego dostępu do pola?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
