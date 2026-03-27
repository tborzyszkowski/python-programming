from solutions_03 import Counter


def test_add_many() -> None:
    counter = Counter()
    assert counter.add_many(3) == 3
    assert counter.add_many(4) == 7
