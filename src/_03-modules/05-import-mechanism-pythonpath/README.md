# 05 - Mechanizm importowania i PYTHONPATH

## Cel

Wyjaśnić, jak interpreter odnajduje moduł i pakiet, jaką rolę mają `sys.path`, katalog roboczy i zmienna `PYTHONPATH`. Pokazać narzędzia diagnostyczne i typowe anty-wzorce.

## Jak Python szuka modułu?

Gdy interpreter napotka instrukcję `import modul`, wykonuje następujące kroki:

### Krok 1: Sprawdzenie cache (`sys.modules`)

Python utrzymuje słownik `sys.modules`, który przechowuje wszystkie **już załadowane** moduły:

```python
import sys
print("json" in sys.modules)   # False — jeszcze nie ładowaliśmy
import json
print("json" in sys.modules)   # True — teraz jest w cache
print(sys.modules["json"])     # <module 'json' from '...'>
```

Jeśli moduł jest w cache, import jest **natychmiastowy** — Python nie szuka pliku ponownie. To wyjaśnia, dlaczego wielokrotne `import json` w różnych plikach projektu nie powoduje wielokrotnego ładowania.

### Krok 2: Wyszukiwanie specyfikacji (finders)

Jeśli modułu nie ma w cache, Python odpytuje **findery** z listy `sys.meta_path`:

```python
import sys
print(sys.meta_path)
# [<class '_frozen_importlib.BuiltinImporter'>,    ← moduły wbudowane (np. sys, builtins)
#  <class '_frozen_importlib.FrozenImporter'>,      ← moduły „zamrożone"
#  <class '_frozen_importlib_external.PathFinder'>]  ← szukanie na ścieżkach (sys.path)
```

Każdy finder implementuje metodę `find_spec(name, path)`. Pierwszy finder, który zwróci specyfikację (`ModuleSpec`), wygrywa.

### Krok 3: Przeszukiwanie ścieżek (`sys.path`)

`PathFinder` (trzeci z finderów) przeszukuje katalogi z `sys.path`:

```python
import sys
for i, entry in enumerate(sys.path):
    print(f"[{i}] {entry}")
```

Typowy wynik:

```
[0] /home/user/projekt          ← katalog uruchamianego skryptu (lub pusty string dla REPL)
[1] /usr/lib/python3.12         ← biblioteka standardowa
[2] /usr/lib/python3.12/lib-dynload  ← rozszerzenia C
[3] /home/user/projekt/.venv/lib/python3.12/site-packages  ← pakiety zainstalowane pip
```

**Kolejność ma znaczenie!** Python szuka od indeksu 0 w górę i zatrzymuje się przy pierwszym znalezieniu.

### Krok 4: Brak specyfikacji → `ModuleNotFoundError`

Jeśli żaden finder nie znalazł modułu, Python zgłasza wyjątek:

```python
import nieistniejacy_modul
# ModuleNotFoundError: No module named 'nieistniejacy_modul'
```

### Pełny schemat (podsumowanie)

```
import modul
    │
    ├─ modul w sys.modules? ──── TAK → zwróć z cache (natychmiastowo)
    │
    └─ NIE → odpytaj sys.meta_path
              │
              ├─ BuiltinImporter → moduł wbudowany? → TAK → załaduj
              ├─ FrozenImporter  → moduł zamrożony? → TAK → załaduj
              └─ PathFinder      → szukaj w sys.path
                                   │
                                   ├─ znaleziono .py/.pyc → załaduj, dodaj do sys.modules
                                   └─ nie znaleziono → ModuleNotFoundError
```

Diagram: `diagrams/import_resolution.png`

![Import resolution](diagrams/import_resolution.png)

## Skąd biorą się wpisy w `sys.path`?

| Źródło | Opis |
|---|---|
| Katalog skryptu | Jeśli uruchamiasz `python /home/user/app/main.py`, to `/home/user/app` jest pierwszym wpisem. |
| Pusty string `""` | Oznacza bieżący katalog roboczy (przy uruchomieniu z REPL lub `python -c`). |
| `PYTHONPATH` | Zmienna środowiskowa — katalogi oddzielone dwukropkiem (Linux) lub średnikiem (Windows). |
| Standardowe ścieżki | Dodane automatycznie: stdlib, `lib-dynload`, `site-packages`. |
| Plik `.pth` | Pliki w `site-packages` mogą dodawać ścieżki do `sys.path`. |

## Zmienna `PYTHONPATH`

`PYTHONPATH` rozszerza listę miejsc, gdzie Python szuka modułów:

```bash
# Linux / macOS:
export PYTHONPATH="/home/user/moje_moduly:/home/user/inny_projekt"
python main.py

# Windows (PowerShell):
$env:PYTHONPATH = "C:\moje_moduly;C:\inny_projekt"
python main.py
```

Wpisy z `PYTHONPATH` są dodawane do `sys.path` **po** katalogu skryptu, ale **przed** ścieżkami standardowymi.

## `importlib.reload()` — przeładowanie modułu

Ponieważ Python cache'uje moduły w `sys.modules`, zmiana pliku `.py` **nie jest widoczna** bez restartu interpretera. W trybie interaktywnym (REPL) można wymusić przeładowanie:

```python
import importlib
import moj_modul

# ... edytujemy moj_modul.py ...

importlib.reload(moj_modul)   # wymusza ponowne załadowanie z dysku
```

**Ograniczenia `reload()`:**
- nie przeładowuje zależności modułu,
- obiekty utworzone przed przeładowaniem nadal korzystają ze starej wersji klas,
- nie jest przeznaczony do użycia w kodzie produkcyjnym.

## Anty-wzorzec: ręczne `sys.path.insert()`

Częsty błąd w kodzie studenckim:

```python
import sys
sys.path.insert(0, "/home/user/moje_moduly")   # ANTY-WZORZEC!
import moj_modul
```

**Dlaczego to źle:**
- ścieżka jest zakodowana na sztywno — nie zadziała na innym komputerze,
- zmienia kolejność wyszukiwania — może przesłonić moduły standardowe,
- nie jest powtarzalne — wymaga modyfikacji kodu zamiast konfiguracji środowiska.

**Lepsze alternatywy:**
- użyj `PYTHONPATH`,
- zainstaluj pakiet w trybie editable: `pip install -e .`,
- skonfiguruj `pyproject.toml` i zainstaluj projekt.

## Krok po kroku na kodzie

Plik: `examples/path_inspector.py`

```python
def read_environment() -> dict[str, str]:
    return {
        "PYTHONPATH": os.environ.get("PYTHONPATH", "<not-set>"),
        "first_sys_path": sys.path[0] if sys.path else "<empty>",
    }
```

Interpretacja:
- `PYTHONPATH` rozszerza miejsca, gdzie Python szuka modułów,
- `sys.path[0]` zwykle wskazuje katalog uruchamianego skryptu.

Plik: `examples/find_module.py`

```python
def find_module_origin(module_name: str) -> str | None:
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        return None
    return spec.origin
```

To wygodny sposób sprawdzenia, skąd faktycznie ładuje się moduł (plik, built-in, brak).

```python
print(find_module_origin("json"))     # /usr/lib/python3.12/json/__init__.py
print(find_module_origin("sys"))      # built-in (zwróci None lub 'built-in')
print(find_module_origin("xyz_brak")) # None — moduł nie istnieje
```

## Mini-lab: diagnoza `ModuleNotFoundError`

### Cele
- opanować procedurę diagnostyczną,
- rozróżniać problem ścieżki od problemu kodu,
- utrwalić rolę `sys.path`.

### Kroki
1. Uruchom `examples/path_inspector.py` i zapisz wynik.
2. Uruchom ten sam plik z innego katalogu roboczego.
3. Porównaj `first_sys_path`.
4. Użyj `examples/find_module.py` dla modułu istniejącego i nieistniejącego.
5. Opisz, kiedy pojawi się `None` i co to oznacza.

### Oczekiwany efekt
- Student potrafi metodycznie wyjaśnić źródło błędu importu.

### Rozszerzenie
- Tymczasowo ustaw `PYTHONPATH` na własny katalog i sprawdź, jak zmienia się wynik wyszukiwania.

## Diagnostyka `ModuleNotFoundError` — procedura krok po kroku

Gdy pojawi się błąd `ModuleNotFoundError: No module named 'xyz'`:

1. **Sprawdź katalog roboczy:** `print(os.getcwd())` — czy jesteś tam, gdzie myślisz?
2. **Wypisz `sys.path`:** — czy katalog z modułem jest na liście?
3. **Sprawdź `PYTHONPATH`:** `print(os.environ.get("PYTHONPATH"))` — czy jest ustawiony poprawnie?
4. **Użyj `find_spec`:** `importlib.util.find_spec("xyz")` — czy Python w ogóle widzi moduł?
5. **Sprawdź aktywne środowisko:** `which python` (Linux) / `Get-Command python` (PowerShell) — czy używasz właściwego interpretera?
6. **Dopiero potem** modyfikuj strukturę pakietu lub importy.

## Powiązane zadania

- `exercises/tasks.py` — klasyfikacja pochodzenia modułu i widoczności ścieżek,
- `exercises/solutions_import_mechanism.py` — rozwiązania,
- `exercises/test_solutions.py` — testy.

## Typowe pułapki

- ręczne dopisywanie niepoprawnych ścieżek do `sys.path` (zakodowane na sztywno),
- zależność od konkretnego IDE bez rozumienia katalogu startowego,
- mylenie `PYTHONPATH` z instalacją pakietu przez `pip`,
- zapominanie o aktywacji `venv` — `pip install` trafia do globalnego interpretera,
- tworzenie pliku o nazwie kolidującej z modułem stdlib (np. `json.py`, `random.py`).

## Pytania kontrolne

1. Co daje cache `sys.modules`?
2. Kiedy `find_spec` zwróci `None`?
3. Czym różni się widoczność modułu od poprawności samego kodu modułu?
4. Jakie są elementy `sys.path` i skąd się biorą?
5. Dlaczego ręczne `sys.path.insert()` to anty-wzorzec?
6. Kiedy przydaje się `importlib.reload()`?

## Literatura

- https://docs.python.org/3/reference/import.html
- https://docs.python.org/3/library/sys.html#sys.path
- https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
- https://docs.python.org/3/library/importlib.html#importlib.reload
