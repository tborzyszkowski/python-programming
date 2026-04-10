from solutions_imports import (
    import_style_result,
    symbol_lifetime,
    detect_builtin_shadowing,
    categorize_name_origin,
)


def test_import_style_result():
    assert import_style_result(81) == 9


def test_symbol_lifetime():
    assert symbol_lifetime() == (True, True)


def test_detect_builtin_shadowing_found():
    assert detect_builtin_shadowing(["list", "x", "sum", "my_var"]) == ["list", "sum"]


def test_detect_builtin_shadowing_none():
    assert detect_builtin_shadowing(["my_func", "custom_var"]) == []


def test_detect_builtin_shadowing_all():
    assert detect_builtin_shadowing(["len", "print"]) == ["len", "print"]


def test_categorize_local():
    assert categorize_name_origin("x", {"x": 1}, {"y": 2}) == "local"


def test_categorize_global():
    assert categorize_name_origin("y", {"x": 1}, {"y": 2}) == "global"


def test_categorize_missing():
    assert categorize_name_origin("z", {"x": 1}, {"y": 2}) == "builtin-or-missing"


def test_categorize_local_wins():
    # jeśli nazwa jest i w local i w global, wygrywa local
    assert categorize_name_origin("x", {"x": 1}, {"x": 2}) == "local"
