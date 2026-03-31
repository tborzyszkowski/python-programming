import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_practical import (
    maskuj_dane_osobowe,
    parsuj_linie_logu,
    waliduj_email,
    waliduj_pesel,
    waliduj_url,
)

# ── waliduj_email ──────────────────────────────────────────────────

def test_waliduj_email_true():
    assert waliduj_email("jan@example.com") is True
    assert waliduj_email("a.b+c@sub.domain.pl") is True


def test_waliduj_email_false():
    assert waliduj_email("brak_malpy") is False
    assert waliduj_email("x@.com") is False
    assert waliduj_email("@domain.com") is False
    assert waliduj_email("") is False


# ── waliduj_pesel ─────────────────────────────────────────────────

def test_waliduj_pesel_true():
    assert waliduj_pesel("44051401458") is True
    assert waliduj_pesel("90090515836") is True


def test_waliduj_pesel_false_suma():
    assert waliduj_pesel("12345678901") is False


def test_waliduj_pesel_false_format():
    assert waliduj_pesel("1234") is False
    assert waliduj_pesel("abcdefghijk") is False


# ── waliduj_url ───────────────────────────────────────────────────

def test_waliduj_url_true():
    assert waliduj_url("https://python.org") is True
    assert waliduj_url("http://a.b.c/path?q=1") is True
    assert waliduj_url("https://sub.example.co.uk/") is True


def test_waliduj_url_false():
    assert waliduj_url("ftp://zly.schemat.com") is False
    assert waliduj_url("https://") is False
    assert waliduj_url("brak schematu") is False


# ── parsuj_linie_logu ─────────────────────────────────────────────

_LINIA = (
    '127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] '
    '"GET /index.html HTTP/1.1" 200 1234'
)


def test_parsuj_linie_logu_ok():
    wynik = parsuj_linie_logu(_LINIA)
    assert wynik is not None
    assert wynik["ip"] == "127.0.0.1"
    assert wynik["uzytkownik"] == "frank"
    assert wynik["metoda"] == "GET"
    assert wynik["sciezka"] == "/index.html"
    assert wynik["status"] == 200
    assert wynik["rozmiar"] == 1234


def test_parsuj_linie_logu_rozmiar_dash():
    linia = '10.0.0.1 - - [01/Jan/2025:00:00:01 +0000] "DELETE /r HTTP/2" 204 -'
    wynik = parsuj_linie_logu(linia)
    assert wynik is not None
    assert wynik["rozmiar"] == 0


def test_parsuj_linie_logu_blad():
    assert parsuj_linie_logu("USZKODZONA LINIA") is None


# ── maskuj_dane_osobowe ───────────────────────────────────────────

def test_maskuj_dane_osobowe_email():
    wynik = maskuj_dane_osobowe("Kontakt: jan@example.com w sprawie")
    assert "[REDACTED_EMAIL]" in wynik
    assert "jan@example.com" not in wynik


def test_maskuj_dane_osobowe_telefon():
    wynik = maskuj_dane_osobowe("Zadzwon: 600 100 200 lub 601100200")
    assert "[REDACTED_PHONE]" in wynik
    assert "600 100 200" not in wynik


def test_maskuj_dane_osobowe_bez_danych():
    tekst = "Zwykly tekst bez danych osobowych."
    assert maskuj_dane_osobowe(tekst) == tekst

