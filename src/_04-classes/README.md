# Moduł 04 - Klasy i programowanie obiektowe w Pythonie 3

Ten moduł rozwija paradygmat obiektowy krok po kroku: od intuicji „klasa vs obiekt”, przez składnię i `self`, aż do dziedziczenia, polimorfizmu, interfejsów i wzorców projektowych.

## Cele dydaktyczne

Po przerobieniu modułu student powinien:
- wyjaśniać, czym różni się klasa od obiektu i skąd pochodzi ta koncepcja,
- poprawnie definiować klasy, tworzyć obiekty i używać `self`,
- odróżniać komponenty instancyjne od klasowych/statycznych,
- świadomie korzystać z metod specjalnych (`__init__`, `__new__`, `__len__`, `__str__`, property),
- modelować relacje dziedziczenia i stosować polimorfizm,
- rozumieć realizację interfejsów przez `ABC` i `Protocol`,
- rozpoznawać wzorce projektowe oparte na polimorfizmie.

## Struktura każdego tematu

Każdy katalog tematyczny zawiera:
- `README.md` - teoria, mini-lab i literatura,
- `diagrams/` - plik `.puml` i wygenerowany `.png`,
- `examples/` - uruchamialny kod demonstrujący koncepcje,
- `exercises/` - zadania, przykładowe rozwiązania, testy.

## Spis tematów

1. [01-class-vs-object](01-class-vs-object/README.md)
2. [02-class-definition-and-object-creation](02-class-definition-and-object-creation/README.md)
3. [03-self-parameter](03-self-parameter/README.md)
4. [04-instance-vs-class-members](04-instance-vs-class-members/README.md)
5. [05-private-members](05-private-members/README.md)
6. [06-special-methods](06-special-methods/README.md)
7. [07-inheritance-basics](07-inheritance-basics/README.md)
8. [08-multiple-inheritance](08-multiple-inheritance/README.md)
9. [09-polymorphism](09-polymorphism/README.md)
10. [10-large-example-inheritance-polymorphism](10-large-example-inheritance-polymorphism/README.md)
11. [11-interfaces-in-python](11-interfaces-in-python/README.md)
12. [12-design-patterns-polymorphism](12-design-patterns-polymorphism/README.md)

## Uruchamianie

```bash
python -m pytest src/_04-classes -c src/_04-classes/pytest.ini -v
python src/_04-classes/generate_diagrams.py
```

## Literatura przekrojowa

- Python Docs - Classes: https://docs.python.org/3/tutorial/classes.html
- Python Docs - Data model: https://docs.python.org/3/reference/datamodel.html
- Python Docs - `abc`: https://docs.python.org/3/library/abc.html
- Python Docs - `typing.Protocol`: https://docs.python.org/3/library/typing.html#typing.Protocol
- E. Gamma i in., *Design Patterns*, Addison-Wesley.
- B. Meyer, *Object-Oriented Software Construction*.
