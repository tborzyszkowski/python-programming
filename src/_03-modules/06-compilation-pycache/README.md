# 06 - Kompilacja modułów, `__pycache__`, `.pyc`

## Cel

Pokazać, co Python kompiluje podczas importu, czym jest bytecode, jaki jest sens plików `.pyc` i jak kontrolować proces kompilacji.

## Kluczowe fakty

- Python kompiluje kod źródłowy `.py` do **bytecode** — niskopoziomowych instrukcji dla maszyny wirtualnej CPython.
- Bytecode trafia do cache: katalog `__pycache__/`.
- Nazwa pliku `.pyc` zawiera tag wersji interpretera, np. `module.cpython-313.pyc`.
- Cache przyspiesza kolejne importy, ale **nie zmienia logiki programu**.

## Co to znaczy „kompilacja" w Pythonie?

Python **nie kompiluje** domyślnie do kodu maszynowego jak C/C++. Proces wygląda tak:

```
Kod źródłowy (.py)
    │
    ▼
Kompilator Pythona (wbudowany)
    │
    ▼
Bytecode (.pyc) ← instrukcje dla maszyny wirtualnej CPython
    │
    ▼
Maszyna wirtualna CPython (interpreter bytecode)
    │
    ▼
Wynik działania programu
```

To model podobny do Javy (kod źródłowy → bytecode → JVM), ale z ważną różnicą: **kompilacja odbywa się automatycznie** i transparentnie — programista nie musi wywoływać kompilera.

### Czym jest bytecode?

Bytecode to **ciąg instrukcji**, które maszyna wirtualna CPython wykonuje krok po kroku. Każda instrukcja ma kod operacji (opcode) i opcjonalny argument.

Możemy obejrzeć bytecode za pomocą modułu `dis` (disassembler):

```python
import dis

def dodaj(a, b):
    return a + b

dis.dis(dodaj)
```

Wynik:

```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

Interpretacja:
- `LOAD_FAST 0 (a)` — załaduj argument `a` na stos,
- `LOAD_FAST 1 (b)` — załaduj argument `b` na stos,
- `BINARY_ADD` — zdejmij dwa elementy ze stosu, dodaj, wynik na stos,
- `RETURN_VALUE` — zwróć element ze szczytu stosu.

**Dlaczego to ważne?** Bytecode wyjaśnia, jak Python wykonuje kod wewnętrznie. Rozumienie tego mechanizmu pomaga debugować problemy z wydajnością i rozumieć semantykę języka.

### Bardziej rozbudowany przykład `dis`

```python
import dis

def silnia(n):
    if n <= 1:
        return 1
    return n * silnia(n - 1)

dis.dis(silnia)
```

Wynik pokazuje instrukcje warunkowe (`POP_JUMP_IF_FALSE`), wywołania rekurencyjne (`CALL_FUNCTION`) i operacje arytmetyczne.

## Katalog `__pycache__`

Gdy Python importuje moduł, automatycznie kompiluje go do bytecode i zapisuje w podkatalogu `__pycache__`:

```
moj_projekt/
    utils.py
    __pycache__/
        utils.cpython-312.pyc    ← bytecode dla Python 3.12
        utils.cpython-313.pyc    ← bytecode dla Python 3.13
```

### Dlaczego tag wersji w nazwie?

Nazwa pliku `utils.cpython-312.pyc` zawiera tag implementacji i wersji. Dzięki temu:
- różne wersje Pythona mogą współistnieć w tym samym katalogu,
- aktualizacja Pythona automatycznie powoduje nową kompilację,
- nie trzeba ręcznie czyścić cache.

### Kiedy Python rekompiluje `.pyc`?

Python porównuje **datę modyfikacji** (mtime) pliku źródłowego `.py` z datą zapisaną w nagłówku pliku `.pyc`:

```
Czy .pyc istnieje?
    │
    ├─ NIE → kompiluj .py → zapisz .pyc
    │
    └─ TAK → porównaj mtime źródła z mtime zapisanym w .pyc
              │
              ├─ źródło nowsze → rekompiluj
              └─ źródło nie nowsze → użyj .pyc z cache
```

Od Pythona 3.7 dostępny jest też tryb walidacji oparty na **hashu** źródła (zamiast mtime), kontrolowany przez opcję `--check-hash-based-pycs`.

## Sterowanie kompilacją

### `python -B` — wyłączenie zapisu `.pyc`

```bash
python -B main.py
```

Lub przez zmienną środowiskową:

```bash
export PYTHONDONTWRITEBYTECODE=1
python main.py
```

Przydatne, gdy:
- nie chcesz zaśmiecać dysku (np. jednorazowe skrypty),
- testujesz na systemie plików tylko do odczytu.

### `compileall` — kompilacja całego katalogu

```bash
python -m compileall src/
```

Kompiluje rekursywnie wszystkie pliki `.py` w katalogu `src/` do `.pyc`. Przydatne:
- przy wdrażaniu aplikacji (przyspieszenie pierwszego importu),
- do weryfikacji poprawności składniowej wielu plików naraz.

### `py_compile` — kompilacja pojedynczego pliku

```python
import py_compile

py_compile.compile("moj_modul.py", doraise=True)
# Tworzy __pycache__/moj_modul.cpython-3XX.pyc
```

## Krok po kroku na kodzie

Plik: `examples/compile_demo.py`

```python
def compile_file(path: str) -> pathlib.Path:
    source = pathlib.Path(path)
    py_compile.compile(str(source), cfile=None, doraise=True)
    cache_dir = source.parent / "__pycache__"
    candidates = sorted(cache_dir.glob(f"{source.stem}*.pyc"))
    if not candidates:
        raise FileNotFoundError("Nie znaleziono pliku .pyc")
    return candidates[-1]
```

Interpretacja:
- funkcja wymusza kompilację,
- potem znajduje wygenerowany plik `.pyc`,
- można od razu zobaczyć, jak Python nazywa cache.

Plik: `examples/cache_info.py` — pokazuje, jak listować wszystkie `.pyc` w katalogu.

## Mini-lab: obserwacja cache bytecode

### Cele
- sprawdzić, kiedy Python odświeża `.pyc`,
- odróżnić kod źródłowy od cache,
- zrozumieć wpływ wersji interpretera na nazwę pliku `.pyc`.

### Kroki
1. Uruchom `examples/compile_demo.py`.
2. Odszukaj wygenerowany plik w `__pycache__/`.
3. Zmień jedną linię kodu źródłowego i uruchom ponownie.
4. Porównaj datę modyfikacji pliku `.pyc`.
5. Uruchom `examples/cache_info.py` i wypisz wszystkie pliki cache.
6. Użyj `dis.dis()` na prostej funkcji, aby zobaczyć bytecode.

### Oczekiwany efekt
- Student rozumie, że usunięcie `__pycache__` nie psuje programu, tylko wymusza ponowne wygenerowanie cache.

### Rozszerzenie
- Porównaj nazwę `.pyc` na dwóch różnych wersjach Pythona.
- Użyj `python -m compileall .` i sprawdź, co się stanie.

## Powiązane zadania

- `exercises/tasks.py` — budowanie nazwy `.pyc` i decyzja o rekompilacji,
- `exercises/solutions_compilation.py` — rozwiązania,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- przekonanie, że usunięcie `__pycache__` psuje kod (nie psuje — Python odtworzy cache),
- kopiowanie `.pyc` między różnymi wersjami interpretera (nie zadziała — inny tag),
- mylenie bytecode z kodem maszynowym (bytecode nie jest natywny, wymaga VM),
- ignorowanie `.pyc` w `.gitignore` (powinny być ignorowane w repozytorium).

> **Wskazówka:** dodaj `__pycache__/` i `*.pyc` do pliku `.gitignore` w każdym projekcie.

## Pytania kontrolne

1. Dlaczego plik `.pyc` zawiera tag wersji Pythona?
2. Co się stanie po usunięciu `__pycache__/`?
3. Czy `.pyc` zmienia wynik działania programu?
4. Co pokazuje `dis.dis()` i do czego się przydaje?
5. Kiedy warto użyć `python -B`?
6. Jak skompilować cały katalog do bytecode?

## Literatura

- https://docs.python.org/3/library/py_compile.html
- https://docs.python.org/3/library/compileall.html
- https://docs.python.org/3/library/dis.html
- https://docs.python.org/3/reference/import.html
- PEP 3147 — PYC Repository Directories: https://peps.python.org/pep-3147/
