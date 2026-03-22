"""Rozwiazania: zaawansowane importy."""


def detect_circular_hint(message: str) -> bool:
    lowered = message.lower()
    return "partially initialized module" in lowered or "circular" in lowered


def exported_by_star(all_list: list[str], symbol: str) -> bool:
    return symbol in set(all_list)

