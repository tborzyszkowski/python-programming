"""Dziedziczenie wielokrotne i MRO – rozszerzony przykład."""
from __future__ import annotations
from datetime import datetime


# ─────────────────────────────────────────────────────────
#  Interfejsy zdolności (mixiny)
# ─────────────────────────────────────────────────────────

class Flyable:
    def fly(self) -> str:
        return f"{type(self).__name__} leci"

    def altitude(self) -> float:
        return 0.0


class Swimmable:
    def swim(self) -> str:
        return f"{type(self).__name__} płynie"


class Walkable:
    def walk(self) -> str:
        return f"{type(self).__name__} chodzi"


# ─────────────────────────────────────────────────────────
#  Mixiny pomocnicze
# ─────────────────────────────────────────────────────────

class LoggerMixin:
    """Dodaje historię zdarzeń do dowolnej klasy."""

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        self._log: list[str] = []

    def log(self, msg: str) -> None:
        self._log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

    def get_log(self) -> list[str]:
        return list(self._log)


class TimestampMixin:
    """Dodaje znacznik czasu utworzenia."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        self._created_at = datetime.now()

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def age_seconds(self) -> float:
        return (datetime.now() - self._created_at).total_seconds()


# ─────────────────────────────────────────────────────────
#  Klasy z dziedziczeniem wielokrotnym
# ─────────────────────────────────────────────────────────

class Duck(LoggerMixin, Flyable, Swimmable, Walkable):
    """Kaczka potrafi latać, pływać i chodzić."""

    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name

    def __str__(self) -> str:
        return f"Duck({self._name!r})"

    def describe(self) -> str:
        actions = [self.fly(), self.swim(), self.walk()]
        for a in actions:
            self.log(a)
        return " | ".join(actions)


class LoggedEvent(LoggerMixin, TimestampMixin):
    """Zdarzenie z logiem i znacznikiem czasu."""

    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name

    def __str__(self) -> str:
        return f"Event({self._name!r}, created={self._created_at.strftime('%H:%M:%S')})"

    def fire(self) -> None:
        self.log(f"Zdarzenie {self._name!r} wywołane")


def main() -> None:
    # Duck
    donald = Duck("Donald")
    print(donald.describe())
    print("Log Donalda:", donald.get_log())

    print("\nMRO klasy Duck:")
    for cls in Duck.__mro__:
        print(f"  {cls.__name__}")

    # LoggedEvent
    ev = LoggedEvent("click")
    ev.fire()
    ev.fire()
    print(f"\n{ev}")
    print("Log zdarzenia:", ev.get_log())

    print("\nMRO klasy LoggedEvent:")
    for cls in LoggedEvent.__mro__:
        print(f"  {cls.__name__}")


if __name__ == "__main__":
    main()
