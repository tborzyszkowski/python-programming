"""Rozwiązania: pickle i serializacja."""

import pickle
from pathlib import Path


def clone_with_pickle(obj):
    payload = pickle.dumps(obj)
    return pickle.loads(payload)


def save_and_load(obj, path: Path):
    with path.open("wb") as handle:
        pickle.dump(obj, handle)
    with path.open("rb") as handle:
        return pickle.load(handle)

