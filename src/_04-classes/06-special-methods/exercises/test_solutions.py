from solutions_06 import Vector2D


def test_repr_contains_coordinates() -> None:
    obj = Vector2D(1.5, -2.0)
    assert "1.5" in repr(obj)
    assert "-2.0" in repr(obj)
