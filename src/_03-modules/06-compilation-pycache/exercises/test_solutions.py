from solutions_compilation import pyc_filename, should_recompile


def test_pyc_filename():
    assert pyc_filename("demo", "cpython-313") == "demo.cpython-313.pyc"


def test_should_recompile():
    assert should_recompile(20, 10) is True
    assert should_recompile(10, 20) is False

