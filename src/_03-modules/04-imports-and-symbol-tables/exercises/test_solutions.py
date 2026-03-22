from solutions_imports import import_style_result, symbol_lifetime


def test_import_style_result():
    assert import_style_result(81) == 9


def test_symbol_lifetime():
    assert symbol_lifetime() == (True, True)

