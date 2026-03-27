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

## Kontekst historyczny i projektowy (rozszerzenie)

W językach z rodziny C++/Java konstruktor bywa traktowany jak „brama” tworzenia obiektu. W Pythonie mechanizm jest dwuetapowy: najpierw uruchamia się `__new__` (tworzenie obiektu), potem `__init__` (inicjalizacja stanu). Dzięki temu Python pozwala budować zarówno proste klasy domenowe, jak i bardziej zaawansowane typy.

## Dodatkowy przykład kodu

```python
account_a = BankAccount("Jan", 300.0)
account_b = BankAccount("Ewa", 100.0)
safe_transfer(account_a, account_b, 75.0)
print(account_a.balance, account_b.balance)
```

## Mini-lab rozszerzony (krok po kroku)

1. Rozszerz `BankAccount` o historię operacji (lista napisów).
2. Dodaj walidację minimalnego salda po wypłacie.
3. Napisz metodę `statement()` zwracającą historię operacji.
4. Przetestuj przypadek błędny: przelew większy niż saldo.

### Kryteria zaliczenia mini-labu

- kod przechodzi testy jednostkowe,
- kod nie miesza warstwy logiki z warstwą wejścia/wyjścia,
- student umie uzasadnić wybór konstrukcji obiektowych,
- student potrafi wskazać miejsce potencjalnej refaktoryzacji.

## Pytania egzaminacyjne

1. Jaka jest rola `__init__` i kiedy jest wywoływana?
2. Dlaczego warto walidować dane wejściowe już w metodach klasy?
3. Jak zaprojektować klasę, by była łatwa do testowania?
4. Czym różni się stan obiektu od zachowania obiektu?
5. Jakie ryzyko niesie brak wyjątków w metodach biznesowych?

## Dodatkowa literatura

- B. Meyer, *Object-Oriented Software Construction*.
- G. Booch, *Object-Oriented Analysis and Design with Applications*.
- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
