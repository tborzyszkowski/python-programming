# Moduł 09 – Django: Tworzenie aplikacji webowych w Pythonie

Moduł poświęcony budowie aplikacji webowych z użyciem frameworka **Django 4/5** w Pythonie 3.
Zaczynamy od podstaw – czym jest framework webowy i wzorzec MVT – a kończymy pełną,
działającą aplikacją CRUD z dwoma powiązanymi tabelami bazy SQLite.

---

## Cele dydaktyczne

Po przerobieniu modułu student powinien:

- rozumieć architekturę MVT (Model-View-Template) i odróżniać ją od MVC,
- instalować Django i tworzyć projekt oraz aplikację (`startproject`, `startapp`),
- definiować modele Django i wykonywać migracje bazy danych,
- pisać widoki funkcyjne i oparte na klasach (CBV),
- tworzyć szablony HTML z dziedziczeniem (`{% extends %}`, `{% block %}`),
- budować formularze Django i walidować dane wejściowe,
- implementować pełny CRUD (Create, Read, Update, Delete) bez użycia panelu admina,
- rozumieć relację jeden-do-wielu (ForeignKey) i wykorzystywać ją w aplikacji,
- konfigurować URL-e i łączyć je z widokami,
- przechowywać dane w bazie SQLite,
- pisać testy jednostkowe dla widoków i modeli Django.

---

## Struktura każdego tematu

```
NN-nazwa/
├── README.md          # teoria, mini-lab, pytania, literatura
├── diagrams/          # pliki .puml i .png
└── examples/          # uruchamialny kod Python / szablony HTML
```

Temat `06-complete-app` zawiera dodatkowo pełny projekt Django:

```
06-complete-app/
├── README.md
├── diagrams/
└── bookshelf/         # gotowy projekt Django (python manage.py runserver)
    ├── manage.py
    ├── requirements.txt
    ├── bookshelf/     # konfiguracja projektu
    └── catalog/       # aplikacja z modelami Author i Book
```

---

## Spis tematów

| #  | Katalog | Temat |
|----|---------|-------|
| 1  | [01-introduction-and-setup](01-introduction-and-setup/README.md) | Wprowadzenie do Django – MVT, instalacja, pierwszy projekt |
| 2  | [02-models-and-orm](02-models-and-orm/README.md) | Modele i ORM – definicja, migracje, zapytania |
| 3  | [03-views-and-urls](03-views-and-urls/README.md) | Widoki i URL-e – routing, widoki funkcyjne i klasowe |
| 4  | [04-templates](04-templates/README.md) | Szablony HTML – język szablonów, dziedziczenie |
| 5  | [05-forms-and-crud](05-forms-and-crud/README.md) | Formularze i CRUD – walidacja, Create/Update/Delete |
| 6  | [06-complete-app](06-complete-app/README.md) | Kompletna aplikacja – Półka z Książkami (Author ↔ Book) |

---

## Uruchamianie kompletnej aplikacji

```bash
cd src/_09-Django/06-complete-app/bookshelf
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data.json   # opcjonalne dane testowe
python manage.py runserver
# Otwórz http://127.0.0.1:8000/
```

## Uruchamianie testów

```bash
cd src/_09-Django/06-complete-app/bookshelf
pip install pytest pytest-django
pytest
```

---

## Wymagania

```
django>=4.2
```

Instalacja:

```bash
pip install django
# lub (w środowisku wirtualnym modułu):
pip install -r src/_09-Django/06-complete-app/bookshelf/requirements.txt
```

---

## Literatura przekrojowa

- Oficjalna dokumentacja Django: <https://docs.djangoproject.com/en/stable/>
- Django Tutorial (oficjalny): <https://docs.djangoproject.com/en/stable/intro/tutorial01/>
- W. S. Vincent, *Django for Beginners*, LearnDjango.com, 2023
- A. Holovaty & J. Kaplan-Moss, *The Definitive Guide to Django* (Django Book): <https://djangobook.com/>
- Two Scoops of Django – D. Greenfeld & A. Greenfeld: <https://www.feldroy.com/books/two-scoops-of-django-3-x>
- Real Python – Django tutorials: <https://realpython.com/tutorials/django/>
- MDN Web Docs – Django Web Framework (Python): <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django>
- Classy Class-Based Views: <https://ccbv.co.uk/>

