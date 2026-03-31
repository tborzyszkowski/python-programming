from __future__ import annotations

from pathlib import Path


def read_first_line(path: Path) -> str:
    with path.open("r", encoding="utf-8") as handle:
        return handle.readline().strip()


def safe_read_first_line(path: Path) -> str:
    try:
        return read_first_line(path)
    except FileNotFoundError:
        return f"Brak pliku: {path}"


def main() -> None:
    existing = Path(__file__)
    missing = existing.with_name("nie_ma_mnie.txt")
    print(safe_read_first_line(existing))
    print(safe_read_first_line(missing))


if __name__ == "__main__":
    main()

