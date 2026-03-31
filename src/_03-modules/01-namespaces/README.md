# 01 - Przestrzenie nazw

## Cel

Zrozumienie, czym są przestrzenie nazw (`namespaces`), jak działa reguła LEGB oraz jak używać `global` i `nonlocal`.

## Kontekst historyczny

Problem kolizji nazw jest stary jak programowanie. W językach proceduralnych (C, Pascal) jedynym
mechanizmem były zasięgi bloków. **Moduły Lispa** i **packages Ada** jako pierwsze dały nazwy
przestrzeniom. Python od wersji 1.x oparł cały model na słowniku: każde środowisko wykonania
(moduł, funkcja, klasa) to oddzielny słownik nazw.

## Teoria

### Przestrzeń nazw jako słownik

```python
x = 42
print(globals()["x"])   # 42 — nazwa "x" to klucz w słowniku modułu
```

Przestrzeń nazw to **mapowanie klucz→wartość**:
- klucz: napis (nazwa zmiennej, funkcji, klasy),
- wartość: dowolny obiekt Pythona.

Nazwy **nie przechowują** wartości — są etykietami wskazującymi obiekty.

### Reguła LEGB — cztery poziomy szukania

| Poziom | Skrót | Opis | Przykład |
|---|---|---|---|
| Lokalny | **L** | Ciało bieżącej funkcji | zmienna w `def f():` |
| Zewnętrzny | **E** | Funkcja otaczająca (closure) | zmienna w `def outer():` wewnątrz której jest `f` |
| Globalny | **G** | Moduł | `VALUE = "global"` na poziomie pliku |
| Wbudowany | **B** | `builtins` | `len`, `sum`, `print`, `type` |

Python szuka nazwy **od L do B**, zatrzymując się przy pierwszym znalezieniu. Ten mechanizm
nazywamy **cieniowaniem** (ang. *shadowing*): lokalna definicja zasłania zewnętrzną.

Diagram: `diagrams/legb_lookup.png`

![LEGB](diagrams/legb_lookup.png)

### Przykład LEGB w kodzie

Plik: `examples/namespace_demo.py`

```python
VALUE = "global-value"

def legb_demo() -> tuple[str, str, str]:
    value = "enclosing-value"

    def inner() -> tuple[str, str, str]:
        value = "local-value"          # przesłania enclosing i global
        return value, VALUE, str(len([1, 2, 3]))

    return inner()
```

- `value` w `inner` → poziom **L**
- `VALUE` → poziom **G** (moduł)
- `len` → poziom **B** (builtins)
- `value = "enclosing-value"` → poziom **E**, przesłonięty przez **L**

### Słowa kluczowe `global` i `nonlocal`

Domyślnie przypisanie wewnątrz funkcji **tworzy zmienną lokalną**. Jeśli chcemy zmodyfikować
zmienną z wyższego poziomu, trzeba to zadeklarować jawnie:

```python
counter = 0

def increment_global() -> None:
    global counter          # bez tego "counter = ..." tworzy lokalną zmienną
    counter += 1

increment_global()
print(counter)   # 1
```

```python
def make_counter():
    value = 0

    def increment() -> int:
        nonlocal value      # bez tego błąd UnboundLocalError
        value += 1
        return value

    return increment

cnt = make_counter()
print(cnt(), cnt())   # 1  2
```

**Zasada projektowa:** `global` i `nonlocal` są uzasadnione rzadko. Częste ich użycie
sygnalizuje, że warto zamienić zmienną na argument lub encapsulate w klasie.

### `locals()` i `globals()`

```python
def inspect():
    local_var = "tu"
    print("local_var" in locals())   # True
    print("local_var" in globals())  # False
    print("inspect" in globals())    # True — funkcja widoczna globalnie
```

`globals()` zwraca słownik modułu. `locals()` — bieżącego scope (kopia, nie referencja!).

## Krok po kroku na kodzie

Plik: `examples/namespace_demo.py` — uruchom i przeanalizuj wynik.

```bash
python src/_03-modules/01-namespaces/examples/namespace_demo.py
```

## Mini-lab (krok po kroku)

1. Uruchom `examples/namespace_demo.py` i sprawdź wynik `LEGB:`.
2. Usuń lokalną zmienną `value` z `inner()` — jaką wartość teraz widać?
3. Dodaj `global VALUE` w `legb_demo()` i przypisz `VALUE = "changed"` — co się dzieje?
4. Napisz closure z `nonlocal` liczące wywołania funkcji.
5. Spróbuj `len = 10` na poziomie modułu — co się stanie przy wywołaniu `len([])`?

### Oczekiwany efekt

- Student potrafi wskazać, z którego poziomu LEGB pochodzi każda nazwa.
- Student rozumie, kiedy i jak używać `global` i `nonlocal`.

## Zadania

- `exercises/tasks.py` — zadania do samodzielnego rozwiązania,
- `exercises/solutions_namespaces.py` — przykładowe rozwiązania,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- oczekiwanie, że `globals()` zawiera symbole lokalne funkcji,
- przypadkowe cieniowanie builtinów (np. `list = [...]`, `id = 5`),
- zapis do `locals()` — **nie modyfikuje** bieżącego scope (to kopia!),
- `global` bez potrzeby — utrudnia testowanie i rozumienie o stanie.

## Pytania egzaminacyjne

1. Wyjaśnij regułę LEGB i podaj przykład dla każdego poziomu.
2. Co to jest cieniowanie nazw? Kiedy jest zamierzone, a kiedy jest błędem?
3. Jaka jest różnica między `global` a `nonlocal`?
4. Dlaczego `len` działa bez importu?
5. Co zwróci `"x" in locals()` wywołane poza funkcją?
6. Dlaczego modyfikacja słownika z `locals()` nie zmienia zmiennych lokalnych?

## Literatura

- https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
- https://realpython.com/python-scope-legb-rule/
- https://docs.python.org/3/reference/executionmodel.html#naming-and-binding
