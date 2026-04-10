from solutions_01 import Student, count_first_year, students_by_year, most_common_year


def test_count_first_year() -> None:
    students = [Student("A", 1), Student("B", 2), Student("C", 1)]
    assert count_first_year(students) == 2


def test_count_first_year_empty() -> None:
    assert count_first_year([]) == 0


def test_students_by_year_sorted() -> None:
    students = [Student("Ewa", 1), Student("Adam", 1), Student("Ola", 2)]
    assert students_by_year(students, 1) == ["Adam", "Ewa"]


def test_students_by_year_none() -> None:
    students = [Student("Ewa", 1)]
    assert students_by_year(students, 3) == []


def test_most_common_year() -> None:
    students = [Student("A", 1), Student("B", 2), Student("C", 1)]
    assert most_common_year(students) == 1


def test_most_common_year_tie() -> None:
    students = [Student("A", 2), Student("B", 1)]
    # remis: zwróć najniższy numer roku
    assert most_common_year(students) == 1

