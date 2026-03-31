from __future__ import annotations


def demo_value_error() -> str:
    try:
        int("abc")
    except ValueError as exc:
        return f"ValueError: {exc}"
    return "OK"


def demo_zero_division_error() -> str:
    try:
        _ = 10 / 0
    except ZeroDivisionError as exc:
        return f"ZeroDivisionError: {exc}"
    return "OK"


def demo_key_error() -> str:
    data = {"name": "Ada"}
    try:
        _ = data["age"]
    except KeyError as exc:
        return f"KeyError: {exc}"
    return "OK"


def main() -> None:
    print(demo_value_error())
    print(demo_zero_division_error())
    print(demo_key_error())


if __name__ == "__main__":
    main()

