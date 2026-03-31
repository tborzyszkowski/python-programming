from solutions_04 import safe_ratio


def test_safe_ratio_ok():
    assert safe_ratio("9", "3") == 3.0


def test_safe_ratio_invalid_value():
    assert safe_ratio("x", "3") is None


def test_safe_ratio_division_by_zero():
    assert safe_ratio("9", "0") is None

