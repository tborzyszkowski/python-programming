# Moduł 07 – HTMLParser w Pythonie 3

Niniejszy moduł omawia moduł `html.parser` z biblioteki standardowej Pythona 3 – strumieniowy analizator HTML oparty na modelu zdarzeń. Poznamy sposób działania parsera, rozszerzanie go przez dziedziczenie, obsługę wywołań zwrotnych, a także praktyczne zastosowania (ekstrakcja linków, zliczanie tagów). Na koniec omówimy ograniczenia `HTMLParser` i porównamy go z alternatywami.

Każdy temat umieszczony jest w osobnym podkatalogu zawierającym:
- `README.md` – wyczerpujące omówienie koncepcji, fragmenty kodu, diagramy i referencje
- `diagrams/` – pliki PlantUML (`.puml`) ilustrujące omawiane zagadnienia
- `examples/` – uruchamialne skrypty Python 3
- `exercises/` – zadania do samodzielnego rozwiązania, przykładowe rozwiązania i testy

## Spis treści

| Katalog | Temat | Kluczowe zagadnienia |
|---|---|---|
| [01-streaming-parser-events/](01-streaming-parser-events/README.md) | Analizator strumieniowy i zdarzenia | `HTMLParser`, `feed()`, model SAX-like, tokenizacja HTML |
| [02-subclassing/](02-subclassing/README.md) | Rozszerzanie parsera | Dziedziczenie po `HTMLParser`, wzorzec Template Method, `__init__`, `reset` |
| [03-event-handling/](03-event-handling/README.md) | Obsługa zdarzeń i wywołania zwrotne | `handle_starttag`, `handle_endtag`, `handle_data`, `handle_comment`, `handle_decl` |
| [04-link-extraction/](04-link-extraction/README.md) | Ekstrakcja linków (szczegółowo) | Wyciąganie `href`/`src`, normalizacja URL, filtrowanie, kompletny przykład |
| [05-tag-counting/](05-tag-counting/README.md) | Zliczanie tagów | Histogram tagów, `collections.Counter`, głębokość zagnieżdżenia |
| [06-limitations-and-alternatives/](06-limitations-and-alternatives/README.md) | Ograniczenia i alternatywy | Malformed HTML, brak DOM/CSS, BeautifulSoup, lxml, porównanie |

## Wymagania

```
Python >= 3.10
pytest >= 7.4
plantuml          # do wizualizacji diagramów .puml (pip install plantuml)
```

> `html.parser` jest częścią biblioteki standardowej – **nie wymaga instalacji zewnętrznych pakietów**.
> Temat 06 (alternatywy) korzysta opcjonalnie z `beautifulsoup4` i `lxml`.

## Uruchamianie przykładów i testów

```bash
# Przykłady
python src/_07-html-parser/01-streaming-parser-events/examples/streaming_demo.py
python src/_07-html-parser/02-subclassing/examples/custom_parser.py
python src/_07-html-parser/03-event-handling/examples/callbacks_demo.py
python src/_07-html-parser/04-link-extraction/examples/link_extractor.py
python src/_07-html-parser/05-tag-counting/examples/tag_counter.py
python src/_07-html-parser/06-limitations-and-alternatives/examples/alternatives_demo.py

# Testy (wszystkie)
python -m pytest src/_07-html-parser/ -v

# Testy pojedynczego tematu
python -m pytest src/_07-html-parser/01-streaming-parser-events/exercises/test_solutions.py -v
python -m pytest src/_07-html-parser/02-subclassing/exercises/test_solutions.py -v
python -m pytest src/_07-html-parser/03-event-handling/exercises/test_solutions.py -v
python -m pytest src/_07-html-parser/04-link-extraction/exercises/test_solutions.py -v
python -m pytest src/_07-html-parser/05-tag-counting/exercises/test_solutions.py -v
python -m pytest src/_07-html-parser/06-limitations-and-alternatives/exercises/test_solutions.py -v
```

## Zadania do samodzielnego rozwiązania

| Temat | Zakres zadań |
|---|---|
| **01-streaming-parser-events** | zliczanie zdarzeń, wykrywanie zamknięcia tagów, karmienie fragmentami |
| **02-subclassing** | klasa zbierająca nagłówki, ekstraktor atrybutów `src` z `<img>` |
| **03-event-handling** | ekstrakcja komentarzy, zbieranie tekstu, mapowanie atrybutów |
| **04-link-extraction** | wyciąganie linków `<a>`, filtrowanie URL zewnętrznych, ekstrakcja z `<img>` |
| **05-tag-counting** | histogram tagów, najczęstszy tag, maksymalna głębokość zagnieżdżenia |
| **06-limitations-and-alternatives** | naprawa malformed HTML, porównanie z BeautifulSoup |

## Diagramy PlantUML

| Diagram | Opis | Plik |
|---|---|---|
| **Przepływ zdarzeń** | Sekwencja: `feed()` → tokenizer → callbacks | `01-streaming-parser-events/diagrams/streaming_events.puml` |
| **Hierarchia klas** | Diagram klas: `HTMLParser` ← podklasa użytkownika | `02-subclassing/diagrams/subclass_hierarchy.puml` |
| **Dispatch callbacków** | Aktywność: typ tokenu → odpowiedni callback | `03-event-handling/diagrams/callback_dispatch.puml` |
| **Przepływ ekstrakcji** | Flowchart ekstrakcji linków z HTML | `04-link-extraction/diagrams/link_extraction_flow.puml` |
| **Zliczanie tagów** | Przepływ budowania histogramu tagów | `05-tag-counting/diagrams/tag_counter_flow.puml` |
| **Porównanie parserów** | Tabela: HTMLParser vs BS4 vs lxml | `06-limitations-and-alternatives/diagrams/comparison_table.puml` |

