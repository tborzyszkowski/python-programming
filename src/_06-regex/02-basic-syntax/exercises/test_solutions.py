import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_syntax import (
    czy_data_iso,
    czy_tylko_litery,
    czy_poprawny_identyfikator,
    znajdz_liczby_calkowite,
    znajdz_slowa_na_wielka,
)


def test_czy_tylko_litery_true():
    assert czy_tylko_litery("Hello") is True
    assert czy_tylko_litery("Python") is True
    assert czy_tylko_litery("abc") is True


def test_czy_tylko_litery_false():
    assert czy_tylko_litery("Hello2") is False
    assert czy_tylko_litery("") is False
    assert czy_tylko_litery("hi there") is False
    assert czy_tylko_litery("abc!") is False


def test_znajdz_liczby_calkowite():
    assert znajdz_liczby_calkowite("cena 42 zl, ilosc: 3") == ["42", "3"]
    assert znajdz_liczby_calkowite("brak") == []
    assert znajdz_liczby_calkowite("100 200 300") == ["100", "200", "300"]


def test_czy_data_iso_true():
    assert czy_data_iso("2024-01-15") is True
    assert czy_data_iso("1999-12-31") is True


def test_czy_data_iso_false():
    assert czy_data_iso("24-1-5") is False
    assert czy_data_iso("2024/01/15") is False
    assert czy_data_iso("2024-1-5") is False
    assert czy_data_iso("") is False


def test_znajdz_slowa_na_wielka():
    wynik = znajdz_slowa_na_wielka("Pan Jan jedzie do Krakowa")
    assert wynik == ["Pan", "Jan", "Krakowa"]


def test_znajdz_slowa_na_wielka_puste():
    assert znajdz_slowa_na_wielka("brak wielkich") == []


def test_czy_poprawny_identyfikator_true():
    assert czy_poprawny_identyfikator("my_var") is True
    assert czy_poprawny_identyfikator("_priv") is True
    assert czy_poprawny_identyfikator("CamelCase") is True
    assert czy_poprawny_identyfikator("x1") is True


def test_czy_poprawny_identyfikator_false():
    assert czy_poprawny_identyfikator("2bad") is False
    assert czy_poprawny_identyfikator("good-name") is False
    assert czy_poprawny_identyfikator("") is False
    assert czy_poprawny_identyfikator("a b") is False

