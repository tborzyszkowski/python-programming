"""Rozwiązania: moduł vs skrypt."""

import re


def classify_runtime(name_value: str) -> str:
    return "script" if name_value == "__main__" else "module"


def guarded_main(name_value: str) -> bool:
    return name_value == "__main__"


def has_side_effect(lines: list[str]) -> bool:
    for line in lines:
        if not line.startswith((" ", "\t")) and re.search(r"\b(print|input)\s*\(", line):
            return True
    return False


def extract_public_api(source_lines: list[str]) -> list[str]:
    result = []
    for line in source_lines:
        if line.startswith("def "):
            name = line[4:].split("(")[0].strip()
            result.append(name)
    return result
