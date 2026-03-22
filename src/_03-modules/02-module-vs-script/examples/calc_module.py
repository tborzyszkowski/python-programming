"""Przyklad modulu z opcjonalnym trybem skryptowym."""


def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


def main() -> None:
    print("2 + 3 =", add(2, 3))
    print("2 * 3 =", multiply(2, 3))


if __name__ == "__main__":
    main()

