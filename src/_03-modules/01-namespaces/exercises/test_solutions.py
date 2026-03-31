from solutions_namespaces import (
    find_in_legb,
    is_name_global,
    make_call_counter,
    merge_symbol_tables,
)


def test_find_in_legb_order():
    assert find_in_legb("L", "E", "G") == ("L", "E", "G")


def test_merge_symbol_tables_local_wins():
    assert merge_symbol_tables({"x": 2}, {"x": 1, "y": 3}) == {"x": 2, "y": 3}


def test_make_call_counter_increments():
    counter = make_call_counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3


def test_make_call_counter_independent():
    a = make_call_counter()
    b = make_call_counter()
    a()
    a()
    assert b() == 1  # niezalezny licznik


def test_is_name_global_found():
    assert is_name_global("VALUE", {"VALUE": 42, "x": 1}) is True


def test_is_name_global_not_found():
    assert is_name_global("y", {"VALUE": 42, "x": 1}) is False


