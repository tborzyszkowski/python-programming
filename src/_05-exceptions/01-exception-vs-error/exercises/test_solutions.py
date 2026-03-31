import pytest

from solutions_01 import parse_positive_int


def test_parse_positive_int_ok():
    assert parse_positive_int("12") == 12


def test_parse_positive_int_non_positive():
    with pytest.raises(ValueError):
        parse_positive_int("0")

