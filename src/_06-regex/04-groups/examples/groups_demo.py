"""Demonstracja grup przechwytujacych, nazwanych i wstecznych odniesien.

Uruchomienie:
    python src/_06-regex/04-groups/examples/groups_demo.py
"""
import re


def sekcja(tytul: str) -> None:
    print(f"\n{'='*55}")
    print(f"  {tytul}")
    print(f"{'='*55}")


# ── 1. GRUPY NUMEROWANE ──────────────────────────────────────────
sekcja("1. Grupy numerowane ()")

DATA_RE = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
m = DATA_RE.search("Urodziny: 1990-05-20")
if m:
    print(f"  group(0): {m.group(0)!r}   (calość)")
    print(f"  group(1): {m.group(1)!r}   (rok)")
    print(f"  group(2): {m.group(2)!r}   (miesiac)")
    print(f"  group(3): {m.group(3)!r}   (dzien)")
    print(f"  groups(): {m.groups()}")

# ── 2. GRUPY NAZWANE ─────────────────────────────────────────────
sekcja("2. Grupy nazwane (?P<name>...)")

DATA_NAZWANA = re.compile(
    r'(?P<rok>\d{4})-(?P<miesiac>\d{2})-(?P<dzien>\d{2})'
)
m = DATA_NAZWANA.search("Konferencja: 2024-09-01")
if m:
    print(f"  group('rok'):     {m.group('rok')}")
    print(f"  group('miesiac'): {m.group('miesiac')}")
    print(f"  groupdict():      {m.groupdict()}")

# ── 3. GRUPY W findall ───────────────────────────────────────────
sekcja("3. Grupy w findall – lista krotek")

wynik = DATA_NAZWANA.findall("od 2024-01-01 do 2024-12-31")
print(f"  findall: {wynik}")

# ── 4. GRUPY NIEPRZECHWYTUJĄCE (?:...) ───────────────────────────
sekcja("4. Grupy nieprzechwytujace (?:...)")

URL_RE = re.compile(r'(?:https?|ftp)://(\S+)')
for url in ["https://python.org", "ftp://files.example.com", "mailto:x@y.com"]:
    m = URL_RE.search(url)
    group1 = m.group(1) if m else 'brak'
    print(f"  {url!r:35s} -> {group1!r}")

# ── 5. GRUPY W re.sub ────────────────────────────────────────────
sekcja("5. Grupy w re.sub – zmiana formatu dat")

wynik = DATA_NAZWANA.sub(r'\g<dzien>.\g<miesiac>.\g<rok>',
                         "Termin: 2024-11-30 i 2025-01-01")
print(f"  {wynik!r}")

# ── 6. WSTECZNE ODNIESIENIA \1 ───────────────────────────────────
sekcja("6. Wsteczne odniesienia \\1 – powtorzone slowa")

zdanie = "to to jest jest bardzo bardzo ciekawe"
powtorzenia = re.findall(r'\b(\w+)\s+\1\b', zdanie, re.IGNORECASE)
print(f"  Powtorzenia: {powtorzenia}")

# ── 7. PARSOWANIE ADRESU IP ──────────────────────────────────────
sekcja("7. Parsowanie adresu IP i portu")

CONN_RE = re.compile(
    r'(?P<host>[\w.\-]+):(?P<port>\d+)/(?P<db>\w+)'
)
for conn in ["localhost:5432/mydb", "db.example.com:3306/shop"]:
    m = CONN_RE.search(conn)
    if m:
        print(f"  {conn!r:30s} -> {m.groupdict()}")


