from dataclasses import dataclass


@dataclass
class Student:
    name: str
    year: int


def describe_student(student: Student) -> str:
    return f"{student.name} (rok {student.year})"


if __name__ == "__main__":
    print(describe_student(Student("Jan", 1)))
