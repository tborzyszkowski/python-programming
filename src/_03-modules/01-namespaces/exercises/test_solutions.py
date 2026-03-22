from solutions_namespaces import find_in_legb, merge_symbol_tables


def test_find_in_legb_order():
    assert find_in_legb("L", "E", "G") == ("L", "E", "G")


def test_merge_symbol_tables_local_wins():
    assert merge_symbol_tables({"x": 2}, {"x": 1, "y": 3}) == {"x": 2, "y": 3}

