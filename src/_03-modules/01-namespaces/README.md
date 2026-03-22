# 01 - Przestrzenie nazw

## Cel

Zrozumienie czym sa przestrzenie nazw (namespaces), jak dziala regula LEGB i dlaczego ten mechanizm porzadkuje duze programy.

## Dlaczego namespace istnieje?

Bez namespaces identyfikator `count` z jednego fragmentu kodu moglby przypadkowo nadpisac `count` z innego miejsca. Przestrzen nazw to mapowanie `nazwa -> obiekt`, a nie "pudelko na zmienna".

Historycznie podobne idee wystepowaly m.in. w:
- C++ (`::`, namespace),
- Java (pakiety),
- C# (namespace),
- Python (moduly, klasy, funkcje jako osobne scope).

## LEGB w Pythonie

Kolejnosc szukania nazwy:
1. **L**ocal - biezaca funkcja,
2. **E**nclosing - funkcja zewnetrzna (closure),
3. **G**lobal - modul,
4. **B**uiltins - `len`, `sum`, `print` itd.

Diagram: `diagrams/legb_lookup.png`

![LEGB](diagrams/legb_lookup.png)

## Kod referencyjny

- `examples/namespace_demo.py` - pokaz LEGB, `globals()`, `locals()`.
- `exercises/tasks.py` - zadania do samodzielnego rozwiazania.
- `exercises/solutions_namespaces.py` - przykladowe rozwiazania.

Przyklad:

```python
from examples.namespace_demo import legb_demo
print(legb_demo())
```

## Literatura

- https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
- https://realpython.com/python-scope-legb-rule/

