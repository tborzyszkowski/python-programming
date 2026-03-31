"""Systematyczny przeglad podstawowej skladni wyrazen regularnych.

Uruchomienie:
    python src/_06-regex/02-basic-syntax/examples/syntax_explorer.py
"""
import re

TEKST = "Pan Jan Kowalski (ur. 1985-03-22) zaplacil 1 200,50 zl za 3 ksiazki."


def sekcja(tytul: str) -> None:
    print(f"\n{'='*50}")
    print(f"  {tytul}")
    print(f"{'='*50}")
    print(f"Tekst: {TEKST!r}\n")


# 1. SUROWE STRINGI
sekcja("1. Surowe stringi r\"...\"")
# Bez r"" trzeba podwajac ukosniki
print(f"  r'\\d+':  {re.findall(r'\\d+', TEKST)}")
print(f"  '\\\\d+': {re.findall('\\d+', TEKST)}  (rownowaznie)")

# 2. KLASY ZNAKOW
sekcja("2. Klasy znakow")
print(f"  \\d  (cyfry):            {re.findall(r'\\d', TEKST)}")
print(f"  \\d+ (liczby):           {re.findall(r'\\d+', TEKST)}")
print(f"  \\w+ (slowa):            {re.findall(r'\\w+', TEKST)[:5]} ...")
print(f"  \\s  (biale znaki):      {re.findall(r'\\s', TEKST)[:4]} ...")
print(f"  [A-Z] (wielkie litery): {re.findall(r'[A-Z]', TEKST)}")
print(f"  [aeiou] (samogloski):   {re.findall(r'[aeiou]', TEKST)}")

# 3. KOTWICE
sekcja("3. Kotwice")
print(f"  ^Pan:   {re.findall(r'^Pan', TEKST)}")
print(f"  zl.$:   {re.findall(r'zl\\.$', TEKST)}")
print(f"  \\bJan\\b: {re.findall(r'\\bJan\\b', TEKST)}")
print(f"  \\bzl\\b:  {re.findall(r'\\bzl\\b', TEKST)}")

# 4. KWANTYFIKATORY
sekcja("4. Kwantyfikatory")
print(f"  \\d{{4}}   (dokladnie 4 cyfry): {re.findall(r'\\d{{4}}', TEKST)}")
print(f"  \\d{{1,3}} (1-3 cyfry):        {re.findall(r'\\d{{1,3}}', TEKST)}")
print(f"  colou?r:                       {re.findall(r'colou?r', 'color colour colouur')}")

# 5. KLASA ZNAKOW Z ZAKRESEM
sekcja("5. Zakresy i negacje")
print(f"  [A-Z][a-z]+ (slowa z wielka): {re.findall(r'[A-Z][a-z]+', TEKST)}")
print(f"  [^\\w\\s]+ (nie-alfanum):       {re.findall(r'[^\\w\\s]+', TEKST)}")

# 6. ALTERNACJA
sekcja("6. Alternacja |")
pan_pani = "Pan Marek i Pani Anna"
print(f"  Pan|Pani: {re.findall(r'Pan|Pani', pan_pani)}")
print(f"  Pani|Pan: {re.findall(r'Pani|Pan', pan_pani)}  (kolejnosc ma znaczenie!)")

# 7. METAZNAKI DOSŁOWNIE
sekcja("7. Metaznaki dosłownie")
ceny = "Cena: 3.99 zl lub 2.50 zl"
print(f"  3\\.99:          {re.findall(r'3\\.99', ceny)}")
print(f"  re.escape('.'): {re.escape('.')!r}")
print(f"  \\d+\\.\\d{{2}}:   {re.findall(r'\\d+\\.\\d{{2}}', ceny)}")

