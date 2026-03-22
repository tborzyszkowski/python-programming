from solutions_advanced_imports import detect_circular_hint, exported_by_star


def test_detect_circular_hint_true():
    msg = "ImportError: cannot import name X from partially initialized module"
    assert detect_circular_hint(msg) is True


def test_exported_by_star():
    assert exported_by_star(["a", "b"], "b") is True
    assert exported_by_star(["a", "b"], "c") is False

