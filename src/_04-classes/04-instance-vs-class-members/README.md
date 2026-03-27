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

## Kontekst historyczny i projektowy (rozszerzenie)

Rozróżnienie „co należy do obiektu, a co do klasy” to jedna z kluczowych decyzji projektowych w OOP. W praktyce przemysłowej pomylenie tych poziomów jest częstym źródłem trudnych błędów, zwłaszcza przy licznikach, cache i konfiguracji globalnej.

## Dodatkowy przykład kodu

```python
s1 = Session("adam")
s2 = Session("ewa")
print(Session.active_sessions())
print(Session.is_valid_username("xy"))
```

## Mini-lab rozszerzony (krok po kroku)

1. Dodaj limit aktywnych sesji na poziomie klasy.
2. Zablokuj tworzenie nowej sesji po przekroczeniu limitu.
3. Dodaj metodę klasową zwracającą konfigurację limitu.
4. Sprawdź testami, że stan klasowy jest wspólny.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Kiedy atrybut powinien być instancyjny, a kiedy klasowy?
2. Czym różni się `@classmethod` od `@staticmethod`?
3. Jakie ryzyko niesie mutowalny atrybut klasowy?
4. Jak zaprojektować licznik obiektów tworzonych przez klasę?
5. Dlaczego stan współdzielony wymaga ostrożności projektowej?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
