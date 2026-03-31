"""Zaawansowane wzorce: leniwe kwantyfikatory, lookahead/lookbehind, backtracking.

Uruchomienie:
    python src/_06-regex/06-advanced-patterns/examples/advanced_patterns.py
"""
import re
import timeit


def sekcja(tytul: str) -> None:
    print(f"\n{'='*55}")
    print(f"  {tytul}")
    print(f"{'='*55}")


# ── 1. CHCIWY vs LENIWY ──────────────────────────────────────────
sekcja("1. Chciwy vs leniwy kwantyfikator")

html = "<b>pogrubiony</b> i <i>kursywa</i>"
print(f"  Chciwy  <.*>  : {re.findall(r'<.*>', html)}")
print(f"  Leniwy  <.*?> : {re.findall(r'<.*?>', html)}")

# ── 2. LOOKAHEAD POZYTYWNY (?=...) ───────────────────────────────
sekcja("2. Lookahead pozytywny (?=...)")

ceny = "Laptop 4200 zl, Mysz 80 zl, Klawiatura 250 EUR"
# Cyfry poprzedzające " zl"
wynik = re.findall(r'\d+(?=\s?zl)', ceny)
print(f"  Liczby przed 'zl': {wynik}")

# ── 3. LOOKAHEAD NEGATYWNY (?!...) ───────────────────────────────
sekcja("3. Lookahead negatywny (?!...)")

# Slowa NIE poprzedzone przez "nie "
zdanie = "Python jest dobry, nie jest slow"
wynik = re.findall(r'\b(?!nie\b)\w+', zdanie)
print(f"  Slowa (bez 'nie'): {wynik}")

# ── 4. LOOKBEHIND POZYTYWNY (?<=...) ─────────────────────────────
sekcja("4. Lookbehind pozytywny (?<=...)")

przelew = "PLN 1500 EUR 200 PLN 300"
wynik = re.findall(r'(?<=PLN )\d+', przelew)
print(f"  Kwoty PLN: {wynik}")

# ── 5. LOOKBEHIND NEGATYWNY (?<!...) ─────────────────────────────
sekcja("5. Lookbehind negatywny (?<!...)")

tekst = "abc 3xyz def 5abc"
# Slowa niezaczynajace sie od cyfry
wynik = re.findall(r'(?<!\d)\b[a-z]+\b', tekst)
print(f"  Slowa nie po cyfrze: {wynik}")

# ── 6. WALIDACJA HASLA z LOOKAHEAD ───────────────────────────────
sekcja("6. Walidacja hasla – wielokrotny lookahead")

HASLO_RE = re.compile(r"""
    (?=.*[A-Z])    # co najmniej 1 wielka litera
    (?=.*[a-z])    # co najmniej 1 mala litera
    (?=.*\d)       # co najmniej 1 cyfra
    .{8,}          # co najmniej 8 znakow
""", re.VERBOSE)

for haslo in ["abc", "Abc1defg", "ABCDEFG1", "Abc12def"]:
    wynik = "OK" if HASLO_RE.fullmatch(haslo) else "ZLE"
    print(f"  {haslo!r:15s}: {wynik}")

# ── 7. CATASTROPHIC BACKTRACKING – demo ──────────────────────────
sekcja("7. Backtracking – porownanie bezpiecznych wzorcow")

bezpieczny = re.compile(r'\d+(\.\d+)?$')      # OK
niebezpieczny_przyklad = re.compile(r'\d+$')  # rowniez OK, dla demonstracji

test = "123456789"
t1 = timeit.timeit(lambda: bezpieczny.match(test), number=100_000)
print(f"  \\d+(\\.\\d+)?$  na {test!r}: {t1*1000:.2f} ms / 100k")

# ── 8. re.escape ─────────────────────────────────────────────────
sekcja("8. re.escape – bezpieczne wyszukiwanie tekstu uzytkownika")

user_input = "3.14 (pi)"
safe = re.escape(user_input)
print(f"  Wejscie: {user_input!r}")
print(f"  re.escape: {safe!r}")
wynik = re.findall(safe, "wynosi 3.14 (pi) przyblizenie")
print(f"  Dopasowania: {wynik}")

