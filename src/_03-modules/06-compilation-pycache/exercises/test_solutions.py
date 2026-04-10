from solutions_compilation import (
    pyc_filename,
    should_recompile,
    pycache_path,
    extract_module_name_from_pyc,
)


def test_pyc_filename():
    assert pyc_filename("demo", "cpython-313") == "demo.cpython-313.pyc"


def test_should_recompile():
    assert should_recompile(20, 10) is True
    assert should_recompile(10, 20) is False


def test_should_recompile_equal():
    assert should_recompile(10, 10) is False


def test_pycache_path_with_dir():
    assert pycache_path("src/utils.py", "cpython-313") == "src/__pycache__/utils.cpython-313.pyc"


def test_pycache_path_no_dir():
    assert pycache_path("main.py", "cpython-312") == "__pycache__/main.cpython-312.pyc"


def test_extract_module_name():
    assert extract_module_name_from_pyc("utils.cpython-313.pyc") == "utils"


def test_extract_module_name_underscore():
    assert extract_module_name_from_pyc("my_module.cpython-312.pyc") == "my_module"
