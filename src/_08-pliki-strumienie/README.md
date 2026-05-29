# Moduł 08 – Pliki i strumienie w Pythonie 3

Moduł poświęcony kompleksowej pracy z plikami i strumieniami danych w Pythonie:
od prostych operacji tekstowych, przez formaty binarne i szyfrowanie, aż po
zaawansowane techniki przetwarzania strumieniowego z generatorami.

---

## Cele dydaktyczne

Po przerobieniu modułu student powinien:

- czytać i zapisywać pliki tekstowe z uwzględnieniem kodowań (UTF-8, Latin-2),
- posługiwać się biblioteką `pathlib` do wygodnej pracy ze ścieżkami,
- rozumieć format binarny, strukturę `struct` i operować na `bytes`/`bytearray`,
- implementować proste algorytmy szyfrowania (XOR, Fernet/AES) i hashowania,
- korzystać z klas `StringIO` i `BytesIO` do operacji in-memory,
- budować potoki przetwarzania strumieni z generatorów i filtrów,
- efektywnie przetwarzać pliki większe niż dostępna RAM,
- stosować `mmap` do mapowania pliku w pamięci.

---

## Struktura każdego tematu

```
NN-nazwa/
├── README.md          # teoria, mini-lab, pytania, literatura
├── diagrams/          # pliki .puml i .png
├── examples/          # uruchamialny kod Python
└── exercises/         # zadania, rozwiązania, testy pytest
```

---

## Spis tematów

| # | Katalog | Temat |
|---|---------|-------|
| 1 | [01-text-files](01-text-files/README.md) | Pliki tekstowe – tryby, kodowania, pathlib |
| 2 | [02-binary-files](02-binary-files/README.md) | Pliki binarne – struct, bytes, mmap |
| 3 | [03-encryption](03-encryption/README.md) | Szyfrowanie plików – XOR, AES/Fernet, SHA-256 |
| 4 | [04-streams-and-io](04-streams-and-io/README.md) | Strumienie io – StringIO, BytesIO, wrappery |
| 5 | [05-stream-filtering](05-stream-filtering/README.md) | Filtrowanie strumieni – generatory, potoki |

---

## Uruchamianie

```bash
# Wszystkie testy
python -m pytest src/_08-pliki-strumienie -c src/_08-pliki-strumienie/pytest.ini -v

# Diagramy PNG
python src/_08-pliki-strumienie/generate_diagrams.py
```

---

## Literatura przekrojowa

- Python Docs – *Reading and Writing Files*: <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>
- Python Docs – `pathlib`: <https://docs.python.org/3/library/pathlib.html>
- Python Docs – `io`: <https://docs.python.org/3/library/io.html>
- Python Docs – `struct`: <https://docs.python.org/3/library/struct.html>
- Python Docs – `mmap`: <https://docs.python.org/3/library/mmap.html>
- Python Docs – `hashlib`: <https://docs.python.org/3/library/hashlib.html>
- PyPI – *cryptography*: <https://cryptography.io/en/latest/>
- M. Lutz, *Learning Python*, rozdz. „Files and I/O".
- D. Beazley & B. Jones, *Python Cookbook*, rozdz. „Files and I/O".
- R. Hettinger, *Generator Tricks for Systems Programmers* (PyCon 2008).

