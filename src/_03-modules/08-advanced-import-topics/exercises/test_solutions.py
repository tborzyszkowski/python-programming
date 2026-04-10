from solutions_advanced_imports import (
    detect_circular_hint,
    exported_by_star,
    validate_plugin_name,
    suggest_fix_for_circular,
)


def test_detect_circular_hint_true():
    msg = "ImportError: cannot import name X from partially initialized module"
    assert detect_circular_hint(msg) is True


def test_detect_circular_hint_false():
    msg = "ImportError: No module named xyz"
    assert detect_circular_hint(msg) is False


def test_detect_circular_hint_keyword():
    assert detect_circular_hint("circular import detected") is True


def test_exported_by_star():
    assert exported_by_star(["a", "b"], "b") is True
    assert exported_by_star(["a", "b"], "c") is False


def test_validate_plugin_name_allowed():
    assert validate_plugin_name("math_plugin", {"math_plugin", "text_plugin"}) is True


def test_validate_plugin_name_denied():
    assert validate_plugin_name("evil_module", {"math_plugin", "text_plugin"}) is False


def test_validate_plugin_name_case_sensitive():
    assert validate_plugin_name("Math_Plugin", {"math_plugin"}) is False


def test_suggest_fix_alphabetical():
    assert suggest_fix_for_circular("orders", "inventory") == "inventory_orders_common"


def test_suggest_fix_case_insensitive():
    assert suggest_fix_for_circular("B", "A") == "a_b_common"


def test_suggest_fix_same_order():
    assert suggest_fix_for_circular("alpha", "beta") == "alpha_beta_common"

