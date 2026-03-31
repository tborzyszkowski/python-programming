"""Demonstracja flag modulu re.

Uruchomienie:
    python src/_06-regex/05-flags/examples/flags_demo.py
"""
import re

WIELOLINIOWY = """\
# Konfiguracja serwera
host = localhost
port = 5432
DEBUG = True
debug_level = 3
"""


def sekcja(tytul: str) -> None:
    print(f"\n{'='*55}")
    print(f"  {tytul}")
    print(f"{'='*55}")


# ── 1. re.IGNORECASE ─────────────────────────────────────────────
sekcja("1. re.IGNORECASE (re.I)")

tekst = "Python PYTHON python PyThOn"
print(f"  Bez flagi: {re.findall(r'python', tekst)}")
print(f"  re.I:      {re.findall(r'python', tekst, re.I)}")

# ── 2. re.MULTILINE ──────────────────────────────────────────────
sekcja("2. re.MULTILINE (re.M) – ^ i $ dla kazdej linii")

print(f"  Bez re.M – poczatek linii: {re.findall(r'^\w+', WIELOLINIOWY)}")
print(f"  re.M    – poczatek linii: {re.findall(r'^\w+', WIELOLINIOWY, re.M)}")
print(f"  Bez re.M – koniec linii:  {re.findall(r'\w+$', WIELOLINIOWY)}")
print(f"  re.M    – koniec linii:  {re.findall(r'\w+$', WIELOLINIOWY, re.M)}")

# ── 3. re.DOTALL ─────────────────────────────────────────────────
sekcja("3. re.DOTALL (re.S) – . pasuje tez do \\n")

html = "<p>\nAkapit\nz nowa linia\n</p>"
print(f"  Bez re.S: {re.search(r'<p>.*</p>', html)}")
m = re.search(r'<p>(.*)</p>', html, re.S)
content = m.group(1) if m else None
print(f"  re.S:     {content!r}")

# ── 4. re.VERBOSE ────────────────────────────────────────────────
sekcja("4. re.VERBOSE (re.X) – czytelne wzorce")

# Bez VERBOSE:
DATA_ZWYKLA = re.compile(r'(?P<rok>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})')

# Z VERBOSE – ten sam wzorzec, o wiele czytelniejszy:
DATA_VERBOSE = re.compile(r"""
    (?P<rok>  \d{4})   # czterocyfrowy rok
    -                  # separator
    (?P<m>    \d{2})   # dwucyfrowy miesiac (01-12)
    -                  # separator
    (?P<d>    \d{2})   # dwucyfrowy dzien (01-31)
""", re.VERBOSE)

for s in ["2024-03-15", "nie-data"]:
    m1 = DATA_ZWYKLA.search(s)
    m2 = DATA_VERBOSE.search(s)
    r1 = m1.groupdict() if m1 else None
    r2 = m2.groupdict() if m2 else None
    print(f"  {s!r:15s} zwykla={r1}  verbose={r2}  zgodne={r1==r2}")

# ── 5. LACZENIE FLAG ─────────────────────────────────────────────
sekcja("5. Laczenie flag re.I | re.M")

tekst2 = "Debug: on\nDEBUG: OFF\ndebug: yes"
print(f"  re.I|re.M – wartosci debug: {re.findall(r'^debug:\s*(\w+)', tekst2, re.I | re.M)}")

# ── 6. FLAGI INLINE ──────────────────────────────────────────────
sekcja("6. Flagi inline (?flags)")

print(f"  (?i)python: {re.findall(r'(?i)python', 'Python PYTHON')}")
print(f"  (?im)^\\w+:  {re.findall(r'(?im)^\w+', 'A\nB\nC')}")


