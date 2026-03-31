"""Zadanie 08 – Dziedziczenie wielokrotne i MRO.

Uzupełnij klasę Event o metodę klasową source() zwracającą nazwę pierwszego mixinu w MRO.
Wskazówka: cls.mro() zwraca listę; pomiń samą klasę Event i klasę object.
"""


class LoggerMixin:
    pass


class TimestampMixin:
    pass


class Event(LoggerMixin, TimestampMixin):
    @classmethod
    def describe_chain(cls) -> list[str]:
        return [c.__name__ for c in cls.mro()]

    @classmethod
    def source(cls) -> str:
        """Zwróć nazwę pierwszej klasy bazowej (pierwszego mixinu) w MRO."""
        raise NotImplementedError

