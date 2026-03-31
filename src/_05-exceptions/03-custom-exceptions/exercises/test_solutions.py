import pytest

from solutions_03 import InvalidAgeError, validate_age


def test_validate_age_ok():
    assert validate_age(20) == 20


def test_validate_age_raises_custom_exception():
    with pytest.raises(InvalidAgeError):
        validate_age(0)

