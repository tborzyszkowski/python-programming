"""Bezpieczna wersja zależności, która unika cyklicznego importu."""


def from_a(value: int) -> int:
    return value + 1


def from_b(value: int) -> int:
    return value * 2


def orchestrate(value: int) -> int:
    # Import lokalny bywa praktycznym obejściem w określonych sytuacjach.
    from circular_safe import from_a, from_b

    return from_b(from_a(value))


if __name__ == "__main__":
    print(orchestrate(10))

