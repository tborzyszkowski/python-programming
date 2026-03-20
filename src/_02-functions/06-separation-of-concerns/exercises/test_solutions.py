import pathlib
import sys

import pytest

sys.path.append(str(pathlib.Path(__file__).parent))

from solutions_separation_of_concerns import (
    batch_pipeline,
    calculate_final_score,
    decide_status,
    parse_input_line,
    render_console_report,
    run_grade_pipeline,
    validate_component_score,
)


WEIGHTS = {
    "homework": 0.2,
    "project": 0.3,
    "exam": 0.5,
}


def test_parse_input_line():
    name, components = parse_input_line("Anna, 80, 90, 70")
    assert name == "Anna"
    assert components == {"homework": 80.0, "project": 90.0, "exam": 70.0}


def test_validate_component_score():
    validate_component_score(0)
    validate_component_score(100)
    with pytest.raises(ValueError):
        validate_component_score(-0.1)
    with pytest.raises(ValueError):
        validate_component_score(100.1)


def test_calculate_final_score_success():
    components = {"homework": 80.0, "project": 90.0, "exam": 70.0}
    assert calculate_final_score(components, WEIGHTS) == 78.0


def test_calculate_final_score_invalid_weights():
    components = {"homework": 80.0, "project": 90.0, "exam": 70.0}
    with pytest.raises(ValueError):
        calculate_final_score(components, {"homework": 0.4, "project": 0.4, "exam": 0.1})


def test_decide_status():
    assert decide_status(50.0) == "PASS"
    assert decide_status(49.99) == "FAIL"


def test_render_console_report():
    assert render_console_report("Jan", 78.0, "PASS") == "Jan: final=78.00, status=PASS"


def test_run_grade_pipeline():
    out = run_grade_pipeline("Jan, 80, 90, 70", WEIGHTS)
    assert out == "Jan: final=78.00, status=PASS"


def test_batch_pipeline_with_error():
    lines = [
        "Jan, 80, 90, 70",
        "Marta, 100, 100",  # invalid format
        "Ola, 10, 20, 30",
    ]
    out = batch_pipeline(lines, WEIGHTS)
    assert out[0] == "Jan: final=78.00, status=PASS"
    assert out[1].startswith("ERROR[2]:")
    assert out[2] == "Ola: final=23.00, status=FAIL"

