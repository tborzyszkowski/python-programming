"""Rozwiazania: zarzadzanie zaleznosciami."""


def choose_env_tool(needs_data_science: bool) -> str:
    return "conda" if needs_data_science else "venv"


def normalize_requirement(entry: str) -> str:
    return entry.strip().lower().replace(" ", "")

