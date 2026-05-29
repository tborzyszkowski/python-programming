from __future__ import annotations

from pathlib import Path


def read_first_line(path: Path) -> str:
    with path.open("r", encoding="utf-8") as handle:
        return handle.readline().strip()


def safe_read_first_line(path: Path) -> str:
    result = ""
    try:
        result = read_first_line(path)
    except FileNotFoundError:
        result = f"Brak pliku: {path}"
    return result

def zerodiv(a, b):
    """Division that overrides the ZeroDivisionError."""
    try:
        return a / b
    except ZeroDivisionError:
        if b == 0.:
            if a == 0.:
                return float('NaN')
            else:
                return float('Inf')

def main() -> None:
    existing = Path(__file__)
    missing = existing.with_name("nie_ma_mnie.txt")
    # print(safe_read_first_line(existing))
    # print(safe_read_first_line(missing))
    # print(zerodiv(1.0, 0.0))
    # print(zerodiv(-1.0, 0.0))
    # print(zerodiv(0.0, 0.0))
    # x = zerodiv(1.0, 0.0) + 1
    # print(x)
    x = 1 / 0

if __name__ == "__main__":
    main()

