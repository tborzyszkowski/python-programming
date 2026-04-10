import math
import pytest

from solutions_09 import Circle, Triangle, total_area, largest_shape


def test_triangle_area() -> None:
    assert Triangle(4.0, 3.0).area() == 6.0


def test_triangle_area_zero_base() -> None:
    assert Triangle(0, 5.0).area() == 0.0


def test_circle_area() -> None:
    c = Circle(1.0)
    assert c.area() == pytest.approx(math.pi)


def test_circle_area_larger() -> None:
    c = Circle(3.0)
    assert c.area() == pytest.approx(math.pi * 9)


def test_describe_triangle() -> None:
    t = Triangle(4.0, 3.0)
    assert t.describe() == "Triangle: area=6.00"


def test_describe_circle() -> None:
    c = Circle(1.0)
    assert c.describe() == f"Circle: area={math.pi:.2f}"


def test_total_area() -> None:
    shapes = [Triangle(4, 3), Circle(1)]
    expected = 6.0 + math.pi
    assert total_area(shapes) == pytest.approx(expected)


def test_total_area_empty() -> None:
    assert total_area([]) == 0.0


def test_largest_shape_triangle_wins() -> None:
    t = Triangle(10, 10)
    c = Circle(1)
    assert largest_shape([t, c]) is t


def test_largest_shape_circle_wins() -> None:
    t = Triangle(1, 1)
    c = Circle(10)
    assert largest_shape([t, c]) is c


