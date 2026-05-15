# 06 - `pickle` i serializacja

## Cel

Zrozumieć, czym jest serializacja, jak działa `pickle` i jak bezpiecznie zapisywać i odczytywać obiekty Python z obiektami zagnieżdżonymi.

## Teoria

### Czym jest serializacja?

**Serializacja** (ang. *serialization*, też *marshalling* lub *pickling*) to zamiana obiektu
istniejącego w pamięci na ciąg bajtów (lub tekst), który można:
- zapisać na dysku,
- przesłać przez sieć,
- przechować w bazie danych.

**Deserializacja** to operacja odwrotna: odtworzenie obiektu z bajtów.

Bez serializacji obiekt istnieje tylko w trakcie działania programu. Serializacja
umożliwia **trwałość danych** (ang. *persistence*).

### Przykłady zastosowań

| Zastosowanie | Technologia |
|---|---|
| Szybkie zapisanie stanu (checkpointing) | `pickle` |
| Wymiana danych z innymi systemami | `json`, `xml` |
| Modele ML / cache obliczeń | `pickle`, `joblib` |
| Komunikacja sieciowa między Pythonami | `pickle` |

### Moduł `pickle`

`pickle` jest wbudowany w bibliotekę standardową. Potrafi serializować niemal
każdy obiekt Pythona: instancje klas, słowniki, listy, zagnieżdżone struktury.

```python
import pickle

data = {"name": "Python", "year": 1991}

# Serializacja do bajtów (w pamięci)
payload: bytes = pickle.dumps(data)
print(type(payload))        # <class 'bytes'>

# Deserializacja
restored = pickle.loads(payload)
print(restored == data)     # True
print(restored is data)     # False — to nowy obiekt!
```

```python
from pathlib import Path

# Serializacja do pliku
with Path("data.pkl").open("wb") as f:
    pickle.dump(data, f)

# Deserializacja z pliku
with Path("data.pkl").open("rb") as f:
    loaded = pickle.load(f)
```

### Serializacja obiektów zagnieżdżonych

Diagram: `diagrams/topic_06.png`

![Serializacja pickle](diagrams/topic_06.png)

Plik: `examples/pickle_demo.py`

```python
from dataclasses import dataclass
import pickle
from pathlib import Path


@dataclass
class Student:
    name: str
    year: int


@dataclass
class Course:
    title: str
    students: list[Student]


def save_course(course: Course, path: Path) -> None:
    with path.open("wb") as handle:
        pickle.dump(course, handle)


def load_course(path: Path) -> Course:
    with path.open("rb") as handle:
        return pickle.load(handle)
```

Po załadowaniu cała struktura (kurs + lista studentów) jest **niezależną kopią**:

```python
original = Course("Python 101", [Student("Ala", 1)])
save_course(original, Path("course.pkl"))
loaded = load_course(Path("course.pkl"))

original.students[0].name = "Zmienione"
print(loaded.students[0].name)   # "Ala" — kopia niezależna!
```

### Relacja do kopii głębokiej

`pickle.dumps` + `pickle.loads` w pamięci daje efekt identyczny z `copy.deepcopy`:

```python
import copy, pickle

obj = {"a": [1, 2, 3]}
by_deepcopy = copy.deepcopy(obj)
by_pickle   = pickle.loads(pickle.dumps(obj))

obj["a"].append(4)
print(by_deepcopy)   # {"a": [1, 2, 3]}
print(by_pickle)     # {"a": [1, 2, 3]}
```

`pickle` jest jednak wolniejszy dla operacji czysto pamięciowych — `copy.deepcopy` jest tu wydajniejszy.
`pickle` stosuj gdy potrzebujesz trwałości lub przesyłania przez sieć.

### Ostrzeżenie bezpieczeństwa

> **Nigdy nie deserializuj danych `pickle` z nieufnych źródeł.**
>
> `pickle.loads(bytes)` może wykonać **dowolny kod Python** zawarty w danych.
> Atakujący może spreparować bajty, które instalują złośliwe oprogramowanie.
> Dla danych z sieci lub od użytkownika używaj `json` lub dedykowanych bibliotek (np. `msgspec`, `pydantic`).

### Alternatywy

| Format | Czytelny | Przenośny | Bezpieczny | Obsługuje dowolne obiekty |
|---|---|---|---|---|
| `pickle` | Nie | Tylko Python | Nie | Tak |
| `json` | Tak | Tak | Tak | Tylko typy podstawowe |
| `csv` | Tak | Tak | Tak | Tylko tabele |
| `xml` | Tak | Tak | Tak (z walidacją) | Hierarchiczne |
| `msgpack` | Nie | Tak | Tak | Typy podstawowe + ext |
| `msgspec` / `pydantic` | Nie (bin) / Tak | Tak | Tak | Ze schemą |
| `shelve` | Nie | Tylko Python | Nie | Tak (dict-like) |

Poniżej każdy format jest omówiony z przykładem: co powstaje (jak wyglądają dane) i jak go uzyskać.

---

#### `pickle` — binarny, tylko Python

`pickle` produkuje bajty nieczytelne dla człowieka, zrozumiałe wyłącznie dla Pythona.
Protokół 5 (Python ≥ 3.8) to obecnie domyślny najwyższy protokół.

```python
import pickle

data = {"name": "Python", "year": 1991, "tags": ["oop", "scripting"]}

# Serializacja
raw: bytes = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(raw[:30])
# b'\x80\x05\x95;\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94...'

# Deserializacja
restored = pickle.loads(raw)
print(restored)
# {'name': 'Python', 'year': 1991, 'tags': ['oop', 'scripting']}
```

Zapis i odczyt pliku:

```python
from pathlib import Path

path = Path("data.pkl")

with path.open("wb") as f:        # tryb BINARNY — obowiązkowo!
    pickle.dump(data, f)

with path.open("rb") as f:
    loaded = pickle.load(f)

print(loaded == data)   # True
```

Zawartość pliku `data.pkl` (zapis hex — całkowicie nieczytelna dla człowieka):

```
80 05 95 3b 00 00 00 00  00 00 00 7d 94 28 8c 04
6e 61 6d 65 94 8c 06 50  79 74 68 6f 6e 94 8c 04
...
```

> **Kiedy używać?** Szybkie checkpointing stanu, modele ML (`joblib`), kolejki zadań
> (Celery), cache wyników – gdy dane są **wewnętrzne** i nie trafiają do zewnętrznych systemów.

---

#### `json` — tekstowy, przenośny, bezpieczny

JSON (JavaScript Object Notation) jest standardem wymiany danych czytelnym dla człowieka.
Obsługuje tylko: dicts, lists, strings, int, float, bool, None.

```python
import json

data = {"name": "Python", "year": 1991, "tags": ["oop", "scripting"]}

# Serializacja do łańcucha
text: str = json.dumps(data, ensure_ascii=False, indent=2)
print(text)
```

Wynik — czytelny i przenośny:

```json
{
  "name": "Python",
  "year": 1991,
  "tags": [
    "oop",
    "scripting"
  ]
}
```

Zapis i odczyt pliku:

```python
from pathlib import Path

path = Path("data.json")

with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with path.open("r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)  # {'name': 'Python', 'year': 1991, 'tags': ['oop', 'scripting']}
```

Serializacja obiektów niestandardowych — potrzebny `default`:

```python
from dataclasses import dataclass, asdict
import json

@dataclass
class Student:
    name: str
    year: int

s = Student("Ala", 1)

# Sposób 1: ręczna konwersja na dict
text = json.dumps(asdict(s))
print(text)  # {"name": "Ala", "year": 1}

# Sposób 2: klasa JSONEncoder
class StudentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {"name": obj.name, "year": obj.year}
        return super().default(obj)

text2 = json.dumps(s, cls=StudentEncoder)
print(text2)  # {"name": "Ala", "year": 1}
```

> **Kiedy używać?** REST API, pliki konfiguracyjne, wymiana danych z innymi językami,
> wszędzie tam gdzie czytelność i przenośność są ważniejsze niż kompletność typów.

---

#### `csv` — tabelaryczny, powszechnie wspierany

CSV (Comma-Separated Values) nadaje się wyłącznie do danych tabelarycznych (lista wierszy o stałych kolumnach).

```python
import csv
from io import StringIO

# Dane: lista słowników (tabela)
students = [
    {"name": "Ala",   "year": 1, "grade": 4.5},
    {"name": "Bartek","year": 2, "grade": 5.0},
    {"name": "Celina","year": 1, "grade": 3.5},
]

# Serializacja do łańcucha (podgląd)
buf = StringIO()
writer = csv.DictWriter(buf, fieldnames=["name", "year", "grade"])
writer.writeheader()
writer.writerows(students)
print(buf.getvalue())
```

Wynik — czytelny w Excelu i Notepaddzie:

```
name,year,grade
Ala,1,4.5
Bartek,2,5.0
Celina,1,3.5
```

Zapis i odczyt pliku:

```python
from pathlib import Path

path = Path("students.csv")

# Zapis
with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "year", "grade"])
    writer.writeheader()
    writer.writerows(students)

# Odczyt
with path.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    loaded = list(reader)

# UWAGA: wszystkie wartości wracają jako str!
print(loaded[0])  # {'name': 'Ala', 'year': '1', 'grade': '4.5'}
print(float(loaded[0]["grade"]))  # 4.5  — ręczna konwersja
```

> **Kiedy używać?** Eksport do Excela / arkuszy kalkulacyjnych, proste logi, dane
> dla innych programów, raporty. Nie nadaje się do zagnieżdżonych struktur ani kolekcji obiektów.

---

#### `xml` — hierarchiczny, przenośny, z walidacją (DTD/XSD)

XML (Extensible Markup Language) jest werbozyjny, ale obsługuje hierarchię i walidację schematów.
Biblioteka standardowa: `xml.etree.ElementTree`.

```python
import xml.etree.ElementTree as ET

# Budowanie drzewa XML
root = ET.Element("course", title="Python 101")
for s in [("Ala", 1), ("Bartek", 2)]:
    student = ET.SubElement(root, "student")
    student.set("name", s[0])
    student.set("year", str(s[1]))

tree = ET.ElementTree(root)

# Podgląd jako tekst
ET.indent(tree, space="  ")         # Python ≥ 3.9
ET.dump(root)
```

Wynik:

```xml
<course title="Python 101">
  <student name="Ala" year="1" />
  <student name="Bartek" year="2" />
</course>
```

Zapis i odczyt pliku:

```python
from pathlib import Path

path = Path("course.xml")

tree.write(str(path), encoding="unicode", xml_declaration=True)

# Odczyt
tree2 = ET.parse(str(path))
root2 = tree2.getroot()
for s in root2.findall("student"):
    print(s.get("name"), s.get("year"))
# Ala 1
# Bartek 2
```

> **Kiedy używać?** Integracje korporacyjne (SOAP, Office Open XML), pliki konfiguracyjne
> z walidacją, formaty dokumentów (SVG, XHTML). Unikaj gdy JSON wystarczy — XML jest dużo bardziej gadatliwy.

---

#### `msgpack` — binarny, szybki, przenośny (wielojęzykowy)

MessagePack to binarny format podobny do JSON, ale kilkakrotnie mniejszy i szybszy.
Wymaga instalacji: `pip install msgpack`.

```python
import msgpack

data = {"name": "Python", "year": 1991, "tags": ["oop", "scripting"]}

# Serializacja
raw: bytes = msgpack.packb(data, use_bin_type=True)
print(raw)
# b'\x83\xa4name\xa6Python\xa4year\xcd\x07\xc7\xa4tags\x92\xa3oop\xa9scripting'
print(f"JSON: {len(str(data))} znaków, msgpack: {len(raw)} bajtów")

# Deserializacja
restored = msgpack.unpackb(raw, raw=False)
print(restored)  # {'name': 'Python', 'year': 1991, 'tags': ['oop', 'scripting']}
```

Zapis i odczyt pliku:

```python
from pathlib import Path

path = Path("data.msgpack")

with path.open("wb") as f:
    msgpack.pack(data, f, use_bin_type=True)

with path.open("rb") as f:
    loaded = msgpack.unpack(f, raw=False)

print(loaded)
```

> **Kiedy używać?** Komunikacja sieciowa wymagająca małego rozmiaru i dużej prędkości,
> kolejki wiadomości (np. Redis, Kafka z serializacją binarną), systemy wbudowane.
> Obsługuje C, Java, Go, Rust i wiele innych.

---

#### `msgspec` / `pydantic` — serializacja ze schemą, walidacja typów

`msgspec` (Python ≥ 3.8, `pip install msgspec`) to bardzo szybka biblioteka do
serializacji ze schemą, wspierająca JSON i MessagePack. Automatycznie waliduje typy.

```python
import msgspec
from msgspec import Struct

class Student(Struct):
    name: str
    year: int

class Course(Struct):
    title: str
    students: list[Student]

course = Course("Python 101", [Student("Ala", 1), Student("Bartek", 2)])

# Serializacja do JSON (bajty UTF-8)
json_bytes: bytes = msgspec.json.encode(course)
print(json_bytes)
# b'{"title":"Python 101","students":[{"name":"Ala","year":1},{"name":"Bartek","year":2}]}'

# Serializacja do MessagePack
mp_bytes: bytes = msgspec.msgpack.encode(course)
print(f"JSON: {len(json_bytes)} B, MsgPack: {len(mp_bytes)} B")

# Deserializacja z walidacją
loaded: Course = msgspec.json.decode(json_bytes, type=Course)
print(loaded.students[0].name)  # Ala

# Błąd walidacji:
try:
    msgspec.json.decode(b'{"title": 42, "students": []}', type=Course)
except msgspec.ValidationError as e:
    print(e)
# Expected `str`, got `int` - at `$.title`
```

Analogiczny przykład z `pydantic` (`pip install pydantic`):

```python
from pydantic import BaseModel
import json

class StudentModel(BaseModel):
    name: str
    year: int

class CourseModel(BaseModel):
    title: str
    students: list[StudentModel]

course = CourseModel(title="Python 101", students=[StudentModel(name="Ala", year=1)])

# Serializacja do JSON
text: str = course.model_dump_json(indent=2)
print(text)
# {
#   "title": "Python 101",
#   "students": [
#     {
#       "name": "Ala",
#       "year": 1
#     }
#   ]
# }

# Deserializacja z walidacją
loaded = CourseModel.model_validate_json(text)
print(loaded.students[0].name)  # Ala
```

> **Kiedy używać?** Aplikacje webowe, REST API (FastAPI używa pydantic wewnętrznie),
> mikrousługi wymagające rygorystycznej walidacji, wszędzie gdzie definicja schematu
> jest konieczna.

---

#### `shelve` — słownik trwały, oparty na `pickle`

`shelve` z biblioteki standardowej oferuje interfejs słownikowy (`dict`-like) do
trwałego przechowywania obiektów Pythona na dysku. Wewnętrznie używa `pickle` + `dbm`.

```python
import shelve

# Zapis
with shelve.open("baza") as db:
    db["kurs1"] = {"title": "Python 101", "ects": 4}
    db["kurs2"] = {"title": "Algorytmy",  "ects": 6}

# Odczyt — jak słownik
with shelve.open("baza") as db:
    print(db["kurs1"])          # {'title': 'Python 101', 'ects': 4}
    print(list(db.keys()))      # ['kurs1', 'kurs2']

# Na dysku powstaną pliki: baza.dir, baza.bak, baza.dat (lub baza.db)
```

> **Kiedy używać?** Proste aplikacje wymagające trwałego słownika bez pełnej bazy danych.
> Unikaj w środowiskach wieloprocesowych i tam, gdzie potrzebna jest przenośność (formaty `dbm` różnią się między systemami).

---

#### Porównanie rozmiarów — ta sama struktura danych

Poniższy eksperyment pokazuje, ile miejsca zajmują różne formaty dla tego samego obiektu:

```python
import pickle, json, csv, io
# pip install msgpack msgspec
import msgpack, msgspec
from msgspec import Struct

students_data = [{"name": f"Student_{i}", "year": i % 4 + 1, "grade": 3.5 + (i % 4) * 0.5}
                 for i in range(100)]

# pickle
pkl = pickle.dumps(students_data, protocol=pickle.HIGHEST_PROTOCOL)

# json
jsn = json.dumps(students_data, ensure_ascii=False).encode()

# msgpack
msp = msgpack.packb(students_data, use_bin_type=True)

# csv
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=["name", "year", "grade"])
w.writeheader(); w.writerows(students_data)
csv_b = buf.getvalue().encode()

print(f"pickle  : {len(pkl):5} B")
print(f"json    : {len(jsn):5} B")
print(f"msgpack : {len(msp):5} B")
print(f"csv     : {len(csv_b):5} B")
```

Przykładowy wynik (100 studentów):

```
pickle  :  3821 B
json    :  5812 B
msgpack :  2647 B
csv     :  2701 B
```

> MessagePack jest zazwyczaj 30–50 % mniejszy od JSON i porównywalny z CSV dla danych tabelarycznych.
> `pickle` ma narzut metadanych klas Pythona, ale dla złożonych obiektów bywa najkompaktniejszy.

## Mini-lab (krok po kroku)

1. Uruchom `examples/pickle_demo.py` i zaobserwuj, że `original` i `loaded` są niezależne.
2. Dodaj pole `ects: int` do `Course` i zserializuj ponownie.
3. Zapisz listę 3 kursów do jednego pliku `.pkl` i odczytaj ją.
4. Porównaj czas `copy.deepcopy(obj)` vs `pickle.loads(pickle.dumps(obj))` dla dużej listy.

### Oczekiwany efekt mini-labu

- Student rozumie różnicę między obiektem oryginalnym a zdeserializowanym.
- Student wie, kiedy `pickle`, a kiedy `json` lub `copy.deepcopy`.

## Zadanie do samodzielnego rozwiązania

- szablon: `exercises/tasks.py`
- przykładowe rozwiązanie: `exercises/solutions_06.py`
- testy: `exercises/test_solutions.py`

Zadania:
1. `clone_with_pickle(obj)` — zwróć niezależną kopię obiektu przez `pickle`.
2. `save_and_load(obj, path)` — zapisz do pliku i odczytaj.

## Pytania egzaminacyjne

1. Dlaczego `pickle` bywa porównywany do kopii głębokiej?
2. Jakie ryzyko bezpieczeństwa wiąże się z `pickle.loads`?
3. Kiedy lepiej wybrać `json` zamiast `pickle`?
4. Czy `pickle` zachowuje relacje referencyjne między zagnieżdżonymi obiektami?
5. Dlaczego pliki `.pkl` muszą być otwierane w trybie binarnym (`"wb"`, `"rb"`)?

## Literatura

- https://docs.python.org/3/library/pickle.html — dokumentacja modułu `pickle`
- https://docs.python.org/3/library/copy.html — `copy.deepcopy`
- https://docs.python.org/3/library/json.html — wbudowany moduł `json`
- https://docs.python.org/3/library/csv.html — wbudowany moduł `csv`
- https://docs.python.org/3/library/xml.etree.elementtree.html — `xml.etree.ElementTree`
- https://docs.python.org/3/library/shelve.html — wbudowany moduł `shelve`
- https://msgpack.org/ — specyfikacja MessagePack (format wielojęzykowy)
- https://pypi.org/project/msgpack/ — biblioteka `msgpack` dla Pythona
- https://jcristharif.com/msgspec/ — `msgspec`: szybka serializacja ze schemą
- https://docs.pydantic.dev/ — `pydantic`: walidacja danych i serializacja ze schemą
- M. Lutz, *Learning Python*, rozdz. „Persistence and Databases"
- L. Ramalho, *Fluent Python*, rozdz. „Object Serialization"
