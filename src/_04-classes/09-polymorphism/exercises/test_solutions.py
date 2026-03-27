from solutions_09 import Triangle


def test_triangle_area() -> None:
    assert Triangle(4.0, 3.0).area() == 6.0
