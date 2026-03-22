"""Rozwiazania: importy i tablice symboli."""

import math


def import_style_result(value: float) -> float:
    return math.sqrt(value)


def symbol_lifetime() -> tuple[bool, bool]:
    global marker
    marker = "module"

    def inner() -> bool:
        local_value = 123
        return "local_value" in locals()

    local_seen = inner()
    global_seen = "marker" in globals()
    return local_seen, global_seen

