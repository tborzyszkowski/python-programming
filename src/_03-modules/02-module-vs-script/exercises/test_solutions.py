from solutions_module_vs_script import classify_runtime, guarded_main, has_side_effect, extract_public_api


def test_classify_script():
    assert classify_runtime("__main__") == "script"


def test_classify_module():
    assert classify_runtime("math") == "module"


def test_guarded_main():
    assert guarded_main("__main__") is True
    assert guarded_main("pkg.mod") is False


def test_has_side_effect_print():
    assert has_side_effect(["import os", "print('hello')"]) is True


def test_has_side_effect_indented():
    assert has_side_effect(["import os", "    print('hello')"]) is False


def test_has_side_effect_none():
    assert has_side_effect(["def f(): pass", "x = 1"]) is False


def test_has_side_effect_input():
    assert has_side_effect(["name = input('?')"]) is True


def test_extract_public_api_basic():
    lines = ["def add(a, b):", "    return a + b", "def mul(a, b):", "    return a * b"]
    assert extract_public_api(lines) == ["add", "mul"]


def test_extract_public_api_nested():
    lines = ["def outer():", "    def inner():", "        pass"]
    assert extract_public_api(lines) == ["outer"]


def test_extract_public_api_empty():
    assert extract_public_api(["x = 1", "y = 2"]) == []

