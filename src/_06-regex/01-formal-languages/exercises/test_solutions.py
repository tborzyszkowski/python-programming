import pathlib
import sys

import pytest

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_formal import (
    czy_ciag_binarny,
    czy_zawiera_cyfre,
    licz_dopasowania,
    symuluj_dfa,
)


# --- czy_zawiera_cyfre ---

def test_czy_zawiera_cyfre_true():
    assert czy_zawiera_cyfre("abc3") is True
    assert czy_zawiera_cyfre("1") is True
    assert czy_zawiera_cyfre("x0y") is True


def test_czy_zawiera_cyfre_false():
    assert czy_zawiera_cyfre("abc") is False
    assert czy_zawiera_cyfre("") is False
    assert czy_zawiera_cyfre("!@#") is False


# --- czy_ciag_binarny ---

def test_czy_ciag_binarny_true():
    assert czy_ciag_binarny("0") is True
    assert czy_ciag_binarny("1") is True
    assert czy_ciag_binarny("1010") is True
    assert czy_ciag_binarny("0000") is True


def test_czy_ciag_binarny_false():
    assert czy_ciag_binarny("") is False
    assert czy_ciag_binarny("102") is False
    assert czy_ciag_binarny("abc") is False
    assert czy_ciag_binarny("2") is False


# --- symuluj_dfa ---

# DFA: akceptuje napisy zaczynajace sie od 'a'
_P = {
    ("q0", "a"): "q1",
    ("q1", "a"): "q1",
    ("q1", "b"): "q1",
}


def test_symuluj_dfa_akceptuje():
    assert symuluj_dfa(_P, "q0", {"q1"}, "ab") is True
    assert symuluj_dfa(_P, "q0", {"q1"}, "a") is True
    assert symuluj_dfa(_P, "q0", {"q1"}, "aab") is True


def test_symuluj_dfa_odrzuca():
    assert symuluj_dfa(_P, "q0", {"q1"}, "ba") is False
    assert symuluj_dfa(_P, "q0", {"q1"}, "") is False
    assert symuluj_dfa(_P, "q0", {"q1"}, "b") is False


def test_symuluj_dfa_konczy_na_ab():
    # DFA: akceptuje napisy konczace sie na 'ab'
    p2 = {
        ("q0", "a"): "q1", ("q0", "b"): "q0",
        ("q1", "a"): "q1", ("q1", "b"): "q2",
        ("q2", "a"): "q1", ("q2", "b"): "q0",
    }
    assert symuluj_dfa(p2, "q0", {"q2"}, "ab") is True
    assert symuluj_dfa(p2, "q0", {"q2"}, "aab") is True
    assert symuluj_dfa(p2, "q0", {"q2"}, "ba") is False
    assert symuluj_dfa(p2, "q0", {"q2"}, "a") is False


# --- licz_dopasowania ---

def test_licz_dopasowania_liczby():
    assert licz_dopasowania(r'\d+', 'abc 123 def 456') == 2
    assert licz_dopasowania(r'\d+', 'brak') == 0


def test_licz_dopasowania_slowa():
    assert licz_dopasowania(r'ab', 'ababab') == 3
    assert licz_dopasowania(r'ab', 'xyz') == 0


def test_licz_dopasowania_puste():
    assert licz_dopasowania(r'\d+', '') == 0

