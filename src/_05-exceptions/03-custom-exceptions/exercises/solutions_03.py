"""Rozwiązania: własne wyjątki."""


class InvalidAgeError(Exception):
    """Wiek jest spoza dozwolonego zakresu."""


def validate_age(age: int) -> int:
    if age < 1 or age > 130:
        raise InvalidAgeError(f"Niepoprawny wiek: {age}")
    return age

