"""Zadania: zarzadzanie zaleznosciami."""


def choose_env_tool(needs_data_science: bool) -> str:
    """Zwroc sugerowane narzedzie: venv albo conda."""
    raise NotImplementedError


def normalize_requirement(entry: str) -> str:
    """Uprosc zapis dependency do postaci lowercase bez spacji."""
    raise NotImplementedError

