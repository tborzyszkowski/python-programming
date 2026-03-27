from solutions_01 import Student, count_first_year


def test_count_first_year() -> None:
    students = [Student("A", 1), Student("B", 2), Student("C", 1)]
    assert count_first_year(students) == 2
