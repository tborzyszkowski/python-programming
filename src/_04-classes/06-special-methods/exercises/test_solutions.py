import math
from solutions_06 import Vector2D


def test_repr_contains_coordinates() -> None:
    obj = Vector2D(1.5, -2.0)
    assert "1.5" in repr(obj)
    assert "-2.0" in repr(obj)


def test_repr_eval_roundtrip() -> None:
    v = Vector2D(3, 4)
    assert eval(repr(v)) == v


def test_eq_equal() -> None:
    assert Vector2D(1, 2) == Vector2D(1, 2)


def test_eq_not_equal() -> None:
    assert Vector2D(1, 2) != Vector2D(3, 4)


def test_eq_different_type() -> None:
    assert Vector2D(1, 2) != "not a vector"


def test_add() -> None:
    result = Vector2D(1, 2) + Vector2D(3, 4)
    assert result == Vector2D(4, 6)


def test_neg() -> None:
    result = -Vector2D(3, -4)
    assert result == Vector2D(-3, 4)


def test_magnitude_345() -> None:
    assert Vector2D(3, 4).magnitude == 5.0


def test_magnitude_zero() -> None:
    assert Vector2D(0, 0).magnitude == 0.0


def test_magnitude_unit() -> None:
    assert abs(Vector2D(1, 0).magnitude - 1.0) < 1e-9
