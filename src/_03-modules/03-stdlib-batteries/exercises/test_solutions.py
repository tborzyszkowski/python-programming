from solutions_stdlib import all_pairs, histogram, days_between, file_extension


def test_histogram():
    assert histogram(["a", "a", "b"]) == {"a": 2, "b": 1}


def test_histogram_empty():
    assert histogram([]) == {}


def test_all_pairs():
    assert all_pairs([1, 2, 3]) == [(1, 2), (1, 3), (2, 3)]


def test_all_pairs_empty():
    assert all_pairs([]) == []


def test_days_between_positive():
    assert days_between("2026-01-01", "2026-01-10") == 9


def test_days_between_reversed():
    assert days_between("2026-03-15", "2026-03-10") == 5


def test_days_between_same():
    assert days_between("2026-06-01", "2026-06-01") == 0


def test_file_extension_txt():
    assert file_extension("/home/user/raport.txt") == ".txt"


def test_file_extension_csv():
    assert file_extension("dane.csv") == ".csv"


def test_file_extension_none():
    assert file_extension("README") == ""
