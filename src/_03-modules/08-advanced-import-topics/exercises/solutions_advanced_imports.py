"""Rozwiązania: zaawansowane importy."""


def detect_circular_hint(message: str) -> bool:
    lowered = message.lower()
    return "partially initialized module" in lowered or "circular" in lowered


def exported_by_star(all_list: list[str], symbol: str) -> bool:
    return symbol in set(all_list)


def validate_plugin_name(name: str, allowed: set[str]) -> bool:
    return name in allowed


def suggest_fix_for_circular(module_a: str, module_b: str) -> str:
    names = sorted([module_a.lower(), module_b.lower()])
    return f"{names[0]}_{names[1]}_common"

