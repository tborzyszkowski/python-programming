from __future__ import annotations

import pickle
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Student:
    name: str
    year: int


@dataclass
class Course:
    title: str
    students: list[Student]


def save_course(course: Course, path: Path) -> None:
    with path.open("wb") as handle:
        pickle.dump(course, handle)


def load_course(path: Path) -> Course:
    with path.open("rb") as handle:
        return pickle.load(handle)


def main() -> None:
    base = Path(__file__).parent
    path = base / "course.pkl"

    original = Course("Python 101", [Student("Ala", 1), Student("Olek", 1)])
    save_course(original, path)
    loaded = load_course(path)

    original.students[0].name = "Zmienione"

    print("Original:", original)
    print("Loaded:", loaded)
    print("To samo id?", id(original) == id(loaded))


if __name__ == "__main__":
    main()

