from solutions_stdlib import all_pairs, histogram


def test_histogram():
    assert histogram(["a", "a", "b"]) == {"a": 2, "b": 1}


def test_all_pairs():
    assert all_pairs([1, 2, 3]) == [(1, 2), (1, 3), (2, 3)]

