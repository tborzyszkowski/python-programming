"""Biblioteka walidatorow opartych na wyrazeniach regularnych.

Uruchomienie:
    python src/_06-regex/07-practical-use/examples/data_validator.py
"""
import re

# ── Skompilowane wzorce ───────────────────────────────────────────

EMAIL_RE = re.compile(r"""
    ^
    [a-zA-Z0-9._%+\-]+   # czesc lokalna
    @
    [a-zA-Z0-9.\-]+      # domena
    \.
    [a-zA-Z]{2,}         # TLD
    $
""", re.VERBOSE)

URL_RE = re.compile(r"""
    ^
    https?://                              # schemat
    [a-zA-Z0-9]                           # pierwszy znak domeny
    (?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?  # srodek domeny
    (?:\.[a-zA-Z]{2,})+                   # etykiety TLD (np. .com, .org.pl)
    (/[^\s]*)?                            # opcjonalna sciezka
    $
""", re.VERBOSE)

TELEFON_RE = re.compile(r"""
    ^
    (?:\+48\s?)?    # opcjonalny prefix +48
    \d{3}           # 3 cyfry
    [\s\-]?         # opcjonalny separator
    \d{3}           # 3 cyfry
    [\s\-]?         # opcjonalny separator
    \d{3}           # 3 cyfry
    $
""", re.VERBOSE)

PESEL_WAGI = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]


def waliduj_email(s: str) -> bool:
    return bool(EMAIL_RE.fullmatch(s))


def waliduj_url(s: str) -> bool:
    return bool(URL_RE.fullmatch(s))


def waliduj_telefon(s: str) -> bool:
    return bool(TELEFON_RE.fullmatch(s))


def waliduj_pesel(s: str) -> bool:
    if not re.fullmatch(r'\d{11}', s):
        return False
    return sum(int(c) * w for c, w in zip(s, PESEL_WAGI)) % 10 == 0


def maskuj_dane(tekst: str) -> str:
    tekst = EMAIL_RE.sub('[EMAIL]', tekst)
    tekst = TELEFON_RE.sub('[TELEFON]', tekst)
    return tekst


# ── Demo ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Walidacja e-mail ===")
    for addr in ["jan@example.com", "a@b.pl", "bez_malpy", "x@.com"]:
        print(f"  {addr!r:25s}: {'OK' if waliduj_email(addr) else 'ZLE'}")

    print("\n=== Walidacja URL ===")
    for url in ["https://python.org", "http://a.b.c/path?q=1",
                "ftp://nie.ten", "https://.com"]:
        print(f"  {url!r:35s}: {'OK' if waliduj_url(url) else 'ZLE'}")

    print("\n=== Walidacja telefonu ===")
    for tel in ["600100200", "600 100 200", "+48600100200", "123", "+1 800 555 0100"]:
        print(f"  {tel!r:20s}: {'OK' if waliduj_telefon(tel) else 'ZLE'}")

    print("\n=== Walidacja PESEL ===")
    for pesel in ["44051401458", "90090515836", "12345678901", "1234"]:
        print(f"  {pesel!r:15s}: {'OK' if waliduj_pesel(pesel) else 'ZLE'}")

    print("\n=== Maskowanie danych osobowych ===")
    tekst = "Kontakt z jan@example.com tel. 600 100 200 w sprawie zamowienia."
    print(f"  Oryginał: {tekst}")
    print(f"  Maskowany: {maskuj_dane(tekst)}")

