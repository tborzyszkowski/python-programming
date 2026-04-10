"""Porównanie import i from-import."""

import math
from math import sqrt


def using_import(x: float) -> float:
    return math.sqrt(x)


def using_from_import(x: float) -> float:
    return sqrt(x)


if __name__ == "__main__":
    print(using_import(49))
    print(using_from_import(49))

