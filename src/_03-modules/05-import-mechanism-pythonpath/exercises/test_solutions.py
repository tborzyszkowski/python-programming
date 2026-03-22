from solutions_import_mechanism import classify_spec_origin, is_visible_on_path


def test_classify_spec_origin():
    assert classify_spec_origin(None) == "not-found"
    assert classify_spec_origin("built-in") == "built-in"
    assert classify_spec_origin("C:/x.py") == "file"


def test_is_visible_on_path():
    entries = ["C:/work", "C:/work/src"]
    assert is_visible_on_path(entries, "C:/work/src") is True

