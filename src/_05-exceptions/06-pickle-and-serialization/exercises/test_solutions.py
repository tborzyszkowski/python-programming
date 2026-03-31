from pathlib import Path

from solutions_06 import clone_with_pickle, save_and_load


def test_clone_with_pickle_creates_independent_copy():
    original = {"group": [1, 2, 3]}
    cloned = clone_with_pickle(original)
    cloned["group"].append(4)
    assert original == {"group": [1, 2, 3]}


def test_save_and_load_roundtrip(tmp_path: Path):
    payload = {"name": "Python", "year": 1991}
    path = tmp_path / "payload.pkl"
    loaded = save_and_load(payload, path)
    assert loaded == payload

