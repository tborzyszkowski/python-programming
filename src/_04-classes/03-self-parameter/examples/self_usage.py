"""Rola parametru self – rozszerzony przykład."""
from __future__ import annotations


class Counter:
    """Licznik kroków z konfigurowalnymkrokiem i limitem."""

    def __init__(self, start: int = 0, step: int = 1, limit: int | None = None) -> None:
        self._value = start
        self._step = step
        self._limit = limit

    # ── reprezentacja ──────────────────────────────────────
    def __str__(self) -> str:
        return f"Counter(value={self._value}, step={self._step})"

    def __repr__(self) -> str:
        return f"Counter(start={self._value!r}, step={self._step!r}, limit={self._limit!r})"

    # ── właściwości ────────────────────────────────────────
    @property
    def value(self) -> int:
        return self._value

    # ── metody instancyjne (self = konkretny obiekt) ───────
    def increment(self) -> int:
        """Zwiększ licznik o krok. Respektuje limit."""
        if self._limit is not None and self._value + self._step > self._limit:
            raise OverflowError(f"Przekroczono limit {self._limit}")
        self._value += self._step
        return self._value

    def decrement(self) -> int:
        """Zmniejsz licznik o krok."""
        self._value -= self._step
        return self._value

    def reset(self) -> None:
        """Zeruj licznik."""
        self._value = 0

    # ── metoda łańcuchowa (builder pattern) ────────────────
    def by(self, step: int) -> Counter:
        """Zwraca nowy licznik z innym krokiem (niemutujące)."""
        return Counter(start=self._value, step=step, limit=self._limit)


def demonstrate_self() -> None:
    """Pokaż, że self to referencja do konkretnej instancji."""
    c1 = Counter(start=0, step=1)
    c2 = Counter(start=100, step=5)

    print("c1:", c1)
    print("c2:", c2)

    # Wywołanie metody na c1 nie wpływa na c2
    c1.increment()
    c1.increment()
    print("Po dwóch increment() na c1:")
    print("  c1:", c1)   # value=2
    print("  c2:", c2)   # value=100 – niezmienione

    # Ekwiwalent jawnego przekazania self
    Counter.increment(c2)   # to samo co c2.increment()
    print("Po Counter.increment(c2):", c2)

    # Licznik z limitem
    limited = Counter(start=8, step=1, limit=10)
    limited.increment()
    limited.increment()
    try:
        limited.increment()  # przekroczyłby limit
    except OverflowError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    demonstrate_self()
