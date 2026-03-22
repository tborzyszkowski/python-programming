"""Uruchomienie przykladow pakietowych."""

from basic_pkg import add, mean
from school.core.grade_model import final_grade
from school.ui.renderer import render_grade


def main() -> None:
    print("add:", add(2, 5))
    print("mean:", mean([3, 4, 5]))
    grade = final_grade([4, 5, 5, 3])
    print(render_grade("Ala", grade))


if __name__ == "__main__":
    main()

