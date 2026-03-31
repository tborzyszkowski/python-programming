from __future__ import annotations


def divide(a: float, b: float) -> float:
    return a / b


def safe_division_message(a: float, b: float) -> str:
    result = None
    try:
        result = divide(a, b)
    except ZeroDivisionError:
        return "Błąd: dzielenie przez zero"
    else:
        return f"Wynik: {result}"
    finally:
        _ = "Tu zwykle zamykamy zasób, np. plik lub połączenie."


def main() -> None:
    print(safe_division_message(10, 2))
    print(safe_division_message(10, 0))


if __name__ == "__main__":
    main()

