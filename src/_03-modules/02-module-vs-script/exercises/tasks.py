"""Zadania: modul vs skrypt."""


def classify_runtime(name_value: str) -> str:
    """Zwroc 'script' dla __main__, w przeciwnym razie 'module'."""
    raise NotImplementedError


def guarded_main(name_value: str) -> bool:
    """Zwroc True tylko gdy kod powinien wejsc do main()."""
    raise NotImplementedError

