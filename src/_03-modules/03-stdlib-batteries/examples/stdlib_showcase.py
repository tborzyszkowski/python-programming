"""Krotki przeglad wybranych modulow biblioteki standardowej."""

from collections import Counter
from itertools import combinations
from pathlib import Path
import json


def count_words(text: str) -> Counter:
    words = [w.lower() for w in text.split()]
    return Counter(words)


def choose_pairs(items: list[str]) -> list[tuple[str, str]]:
    return list(combinations(items, 2))


def to_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True)


def project_root_name() -> str:
    return Path(__file__).resolve().parents[4].name


if __name__ == "__main__":
    print(count_words("Python python modules"))
    print(choose_pairs(["A", "B", "C"]))
    print(to_json({"topic": "stdlib", "ok": True}))
    print(project_root_name())

