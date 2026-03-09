import pathlib
import sys

import pytest

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_srp import (
    build_summary,
    classify_result,
    compute_average,
    parse_student_line,
    process_student_record,
    validate_score,
)


def test_parse_student_line():
    name, scores = parse_student_line("Anna;80;90;70")
    assert name == "Anna"
    assert scores == [80.0, 90.0, 70.0]


def test_validate_score():
    validate_score(0)
    validate_score(100)
    with pytest.raises(ValueError):
        validate_score(-1)
    with pytest.raises(ValueError):
        validate_score(101)


def test_compute_average():
    assert compute_average([80, 90, 70]) == 80.0
    with pytest.raises(ValueError):
        compute_average([])


def test_classify_result():
    assert classify_result(95) == "A"
    assert classify_result(80) == "B"
    assert classify_result(61) == "C"
    assert classify_result(50) == "D"
    assert classify_result(10) == "F"


def test_build_summary():
    assert build_summary("Anna", 80.0, "B") == "Anna: srednia=80.00, ocena=B"


def test_process_student_record():
    out = process_student_record("Jan;45;55;60")
    assert out == "Jan: srednia=53.33, ocena=D"

