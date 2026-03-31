"""Zadania: własne wyjątki."""


class InvalidAgeError(Exception):
    """Wiek jest spoza dozwolonego zakresu."""


def validate_age(age: int) -> int:
    """Zwróć wiek, jeśli jest z zakresu 1..130, inaczej zgłoś InvalidAgeError."""
    raise NotImplementedError

