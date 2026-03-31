from __future__ import annotations


class RegistrationError(Exception):
    """Bazowy wyjątek dla domeny rejestracji studentów."""


class InvalidStudentIdError(RegistrationError):
    """Identyfikator ma niepoprawny format."""


class DuplicateStudentError(RegistrationError):
    """Student o tym identyfikatorze już istnieje."""


def register_student(student_id: str, existing_ids: set[str]) -> str:
    if not student_id.startswith("s") or not student_id[1:].isdigit():
        raise InvalidStudentIdError(f"Niepoprawny identyfikator: {student_id}")
    if student_id in existing_ids:
        raise DuplicateStudentError(f"Duplikat identyfikatora: {student_id}")
    existing_ids.add(student_id)
    return student_id


def main() -> None:
    ids = {"s100"}
    for value in ["x12", "s100", "s101"]:
        try:
            print("Dodano:", register_student(value, ids))
        except RegistrationError as exc:
            print("Błąd domenowy:", exc)


if __name__ == "__main__":
    main()

