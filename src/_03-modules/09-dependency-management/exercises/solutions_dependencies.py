"""Rozwiązania: zarządzanie zależnościami."""

import re


def choose_env_tool(needs_data_science: bool) -> str:
    return "conda" if needs_data_science else "venv"


def normalize_requirement(entry: str) -> str:
    return entry.strip().lower().replace(" ", "")


def parse_requirements(text: str) -> list[str]:
    result = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Wyciągnij nazwę pakietu (przed operatorem wersji)
        name = re.split(r"[><=!~;@\[]", line)[0].strip().lower()
        if name:
            result.append(name)
    return result


def find_missing(installed: set[str], required: set[str]) -> set[str]:
    installed_lower = {pkg.lower() for pkg in installed}
    return {pkg for pkg in required if pkg.lower() not in installed_lower}
