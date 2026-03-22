"""Rozwiazania: modul vs skrypt."""


def classify_runtime(name_value: str) -> str:
    return "script" if name_value == "__main__" else "module"


def guarded_main(name_value: str) -> bool:
    return name_value == "__main__"

