"""Plik do uruchamiania przez python -m."""

from calc_module import add


if __name__ == "__main__":
    print("run_as_module says:", add(10, 5))

