"""Systematyczny przeglad funkcji modulu re.

Uruchomienie:
    python src/_06-regex/03-re-module/examples/re_module_tour.py
"""
import re

TEKST = "Zamowienie #42 zlozono 2024-03-15. Kontakt: jan@example.com lub 600 100 200."
WZORZEC_LICZBA = r'\d+'
WZORZEC_DATA = r'\d{4}-\d{2}-\d{2}'
WZORZEC_EMAIL = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'


def sekcja(tytul: str) -> None:
    print(f"\n{'─'*55}")
    print(f"  {tytul}")
    print(f"{'─'*55}")


sekcja("re.match – szuka tylko na poczatku")
m = re.match(WZORZEC_LICZBA, TEKST)
print(f"  re.match(r'\\d+', tekst) -> {m}")  # None – zaczyna sie od 'Z'
m2 = re.match(r'Zamow\w+', TEKST)
print(f"  re.match(r'Zamow\\w+', tekst) -> {m2.group() if m2 else None}")

sekcja("re.search – pierwsze dopasowanie gdziekolwiek")
m = re.search(WZORZEC_LICZBA, TEKST)
print(f"  re.search(r'\\d+', tekst) -> {m.group()!r} @ {m.span()}")

sekcja("re.fullmatch – caly napis musi pasowac")
for s in ["2024-03-15", "24-3-15", "abc"]:
    m = re.fullmatch(WZORZEC_DATA, s)
    print(f"  re.fullmatch(data, {s!r}) -> {'pasuje' if m else 'nie pasuje'}")

sekcja("re.findall – lista wszystkich dopasowań")
liczby = re.findall(WZORZEC_LICZBA, TEKST)
print(f"  liczby: {liczby}")
emaile = re.findall(WZORZEC_EMAIL, TEKST)
print(f"  emaile: {emaile}")
# Z grupami – zwraca liste krotek
fragmenty = re.findall(r'(\d{4})-(\d{2})-(\d{2})', TEKST)
print(f"  daty (grupy): {fragmenty}")

sekcja("re.finditer – iterator po obiektach Match")
print("  Wszystkie liczby ze spanami:")
for m in re.finditer(WZORZEC_LICZBA, TEKST):
    print(f"    {m.group()!r:6s} @ {m.span()}")

sekcja("re.sub – zamiana")
wynik = re.sub(r'\d+', 'X', TEKST)
print(f"  cyfry -> X: {wynik!r}")
# Sub z funkcja
wynik2 = re.sub(r'\d+', lambda m: str(int(m.group()) * 10), "1 + 2 = 3")
print(f"  *10: {wynik2!r}")
tekst_spacje = "za   duzo    spacji"
wynik3 = re.sub(r'\s+', ' ', tekst_spacje)
print(f"  normalizacja spacji: {wynik3!r}")

sekcja("re.split – podzial")
wynik = re.split(r'[;,\s]+', "a,b; c  d")
print(f"  re.split: {wynik}")

sekcja("re.compile – kompilacja wzorca")
EMAIL_RE = re.compile(WZORZEC_EMAIL)
print(f"  findall: {EMAIL_RE.findall(TEKST)}")
print(f"  sub:     {EMAIL_RE.sub('[EMAIL]', TEKST)}")

sekcja("Obiekt Match – metody")
m = re.search(r'(\d{4})-(\d{2})-(\d{2})', TEKST)
if m:
    print(f"  group(0): {m.group(0)!r}  (cale dopasowanie)")
    print(f"  group(1): {m.group(1)!r}  (rok)")
    print(f"  group(2): {m.group(2)!r}  (miesiac)")
    print(f"  span():   {m.span()}")
    print(f"  start():  {m.start()}, end(): {m.end()}")

