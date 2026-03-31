import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_groups import (
    parsuj_wersje,
    wyciagnij_date,
    wyciagnij_pary_klucz_wartosc,
    zamien_format_daty,
    znajdz_powtorzenia,
)


def test_wyciagnij_date():
    wynik = wyciagnij_date("Data: 2024-03-15")
    assert wynik == {'rok': '2024', 'miesiac': '03', 'dzien': '15'}


def test_wyciagnij_date_brak():
    assert wyciagnij_date("brak daty") is None


def test_zamien_format_daty():
    assert zamien_format_daty("Urodziny: 1990-05-20") == "Urodziny: 20.05.1990"
    assert zamien_format_daty("od 2024-01-01 do 2024-12-31") == "od 01.01.2024 do 31.12.2024"


def test_znajdz_powtorzenia():
    assert znajdz_powtorzenia("to to jest jest test") == ["to", "jest"]
    assert znajdz_powtorzenia("brak powtorzen") == []


def test_znajdz_powtorzenia_case_insensitive():
    assert znajdz_powtorzenia("The the cat") == ["The"]


def test_parsuj_wersje():
    assert parsuj_wersje("Python 3.12.0") == (3, 12, 0)
    assert parsuj_wersje("v1.0.0-rc1") == (1, 0, 0)


def test_parsuj_wersje_brak():
    assert parsuj_wersje("brak wersji") is None


def test_wyciagnij_pary_klucz_wartosc():
    wynik = wyciagnij_pary_klucz_wartosc("host=localhost port=5432 db=test")
    assert wynik == {'host': 'localhost', 'port': '5432', 'db': 'test'}


def test_wyciagnij_pary_klucz_wartosc_puste():
    assert wyciagnij_pary_klucz_wartosc("brak par") == {}

