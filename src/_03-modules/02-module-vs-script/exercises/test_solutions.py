from solutions_module_vs_script import classify_runtime, guarded_main


def test_classify_script():
    assert classify_runtime("__main__") == "script"


def test_classify_module():
    assert classify_runtime("math") == "module"


def test_guarded_main():
    assert guarded_main("__main__") is True
    assert guarded_main("pkg.mod") is False

