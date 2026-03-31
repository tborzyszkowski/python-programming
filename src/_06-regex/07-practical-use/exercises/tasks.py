"""Zadania: praktyczne zastosowania wyrazen regularnych."""
import re


def waliduj_email(s: str) -> bool:
    """Zwraca True, jesli napis ma format poprawnego adresu e-mail.

    Wymagania: czesc_lokalna@domena.tld
    - czesc_lokalna: litery, cyfry, . _ % + -
    - domena: litery, cyfry, . -
    - TLD: co najmniej 2 litery

    Przyklad:
        waliduj_email("jan@example.com")  -> True
        waliduj_email("brak_malpy")       -> False
        waliduj_email("x@.com")           -> False
    """
    raise NotImplementedError("Zaimplementuj waliduj_email")


def waliduj_pesel(s: str) -> bool:
    """Zwraca True, jesli napis jest poprawnym numerem PESEL.

    Wymagania:
    1. Dokladnie 11 cyfr.
    2. Suma kontrolna: sum(cyfra_i * waga_i) % 10 == 0
       wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

    Przyklad:
        waliduj_pesel("44051401458")  -> True
        waliduj_pesel("12345678901")  -> False (zla suma kontrolna)
        waliduj_pesel("1234")         -> False (za krotki)
    """
    raise NotImplementedError("Zaimplementuj waliduj_pesel")


def waliduj_url(s: str) -> bool:
    """Zwraca True, jesli napis jest poprawnym URL http/https.

    Wymagania:
    - Schemat: http:// lub https://
    - Domena: znaki alfanumeryczne i myslnik
    - Co najmniej jedno TLD: .com, .pl itp. (min. 2 litery)
    - Opcjonalna sciezka po /

    Przyklad:
        waliduj_url("https://python.org")          -> True
        waliduj_url("http://a.b.c/path?q=1")       -> True
        waliduj_url("ftp://zly.schemat.com")        -> False
        waliduj_url("https://")                    -> False
    """
    raise NotImplementedError("Zaimplementuj waliduj_url")


def parsuj_linie_logu(linia: str) -> dict | None:
    """Parsuje linie logu Apache Combined Log Format.

    Format:
        IP - user [czas] "METODA sciezka protokol" status rozmiar

    Zwraca slownik z kluczami:
        ip, uzytkownik, czas, metoda, sciezka, protokol, status (int), rozmiar (int)
    lub None, jesli linia nie pasuje do formatu.

    Przyklad:
        parsuj_linie_logu(
            '127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] '
            '"GET /index.html HTTP/1.1" 200 1234'
        )
        -> {'ip': '127.0.0.1', 'uzytkownik': 'frank', ..., 'status': 200, 'rozmiar': 1234}
    """
    raise NotImplementedError("Zaimplementuj parsuj_linie_logu")


def maskuj_dane_osobowe(tekst: str) -> str:
    """Zastepuje adresy e-mail przez '[REDACTED_EMAIL]'
    i numery telefonow (9 cyfr, ewentualnie z separatorami) przez '[REDACTED_PHONE]'.

    Przyklad:
        maskuj_dane_osobowe("Kontakt: jan@example.com tel. 600 100 200")
        -> "Kontakt: [REDACTED_EMAIL] tel. [REDACTED_PHONE]"
    """
    raise NotImplementedError("Zaimplementuj maskuj_dane_osobowe")

