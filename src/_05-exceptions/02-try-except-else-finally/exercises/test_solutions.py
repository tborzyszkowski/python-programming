from solutions_02 import to_float_or_none


def test_to_float_or_none_parses_number():
    assert to_float_or_none("3.5") == 3.5


def test_to_float_or_none_invalid_returns_none():
    assert to_float_or_none("x3") is None

