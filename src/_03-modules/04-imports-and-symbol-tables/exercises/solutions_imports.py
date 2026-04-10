"""Rozwiązania: importy i tablice symboli."""

import builtins
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


def detect_builtin_shadowing(names: list[str]) -> list[str]:
    builtin_names = set(dir(builtins))
    return [n for n in names if n in builtin_names]


def categorize_name_origin(name: str, local_ns: dict, global_ns: dict) -> str:
    if name in local_ns:
        return "local"
    if name in global_ns:
        return "global"
    return "builtin-or-missing"

