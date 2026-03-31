# Moduł 05 - Wyjątki, pliki i serializacja w Pythonie 3

Ten moduł wyjaśnia, jak w Pythonie obsługiwać sytuacje błędne w sposób kontrolowany, jak bezpiecznie pracować z plikami oraz jak serializować dane obiektowe.

## Cele dydaktyczne

Po przerobieniu modułu student powinien:
- odróżniać wyjątek od błędu logicznego i błędu składni,
- stosować `try-except-else-finally` świadomie i przewidywać przepływ sterowania,
- projektować oraz używać własnych klas wyjątków,
- rozpoznawać i interpretować najczęstsze wyjątki wbudowane,
- czytać i zapisywać pliki tekstowe oraz binarne,
- implementować prosty program szyfrujący plik (szyfr Cezara),
- serializować i deserializować obiekty modułem `pickle` oraz rozumieć relację do kopii głębokiej.

## Struktura każdego tematu

Każdy katalog tematyczny zawiera:
- `README.md` - teoria, mini-lab, pytania kontrolne i literatura,
- `diagrams/` - plik `.puml` i wygenerowany `.png`,
- `examples/` - uruchamialny kod,
- `exercises/` - zadania, przykładowe rozwiązania i testy.

## Spis tematów

1. [01-exception-vs-error](01-exception-vs-error/README.md)
2. [02-try-except-else-finally](02-try-except-else-finally/README.md)
3. [03-custom-exceptions](03-custom-exceptions/README.md)
4. [04-built-in-exceptions](04-built-in-exceptions/README.md)
5. [05-file-handling-caesar-cipher](05-file-handling-caesar-cipher/README.md)
6. [06-pickle-and-serialization](06-pickle-and-serialization/README.md)

## Uruchamianie

```bash
python -m pytest src/_05-exceptions -c src/_05-exceptions/pytest.ini -v
python src/_05-exceptions/generate_diagrams.py
```

## Literatura przekrojowa

- Python Docs - Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html
- Python Docs - Built-in Exceptions: https://docs.python.org/3/library/exceptions.html
- Python Docs - Input and Output: https://docs.python.org/3/tutorial/inputoutput.html
- Python Docs - `pathlib`: https://docs.python.org/3/library/pathlib.html
- Python Docs - `pickle`: https://docs.python.org/3/library/pickle.html
- M. Lutz, *Learning Python*.
- L. Ramalho, *Fluent Python*.

