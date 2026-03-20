"""Przyklad warstwowej aplikacji opartej na funkcjach (SoC + SRP)."""

from __future__ import annotations

from typing import Dict, Iterable, Tuple


DEFAULT_WEIGHTS: Dict[str, float] = {
    "quiz1": 0.15,
    "quiz2": 0.15,
    "project": 0.30,
    "exam": 0.40,
}


# ==================== MODEL LAYER ====================

def parse_user_line(raw_line: str) -> tuple[str, dict[str, float]]:
    """Parse line in format: 'Name, q1, q2, project, exam'."""
    parts = [part.strip() for part in raw_line.split(",")]
    if len(parts) != 5:
        raise ValueError("Oczekiwano formatu: Name, q1, q2, project, exam")

    name = parts[0]
    components = {
        "quiz1": float(parts[1]),
        "quiz2": float(parts[2]),
        "project": float(parts[3]),
        "exam": float(parts[4]),
    }
    return name, components


def validate_components(components: dict[str, float]) -> None:
    """Validate each score in inclusive range 0..100."""
    for key, value in components.items():
        if value < 0 or value > 100:
            raise ValueError(f"Wynik poza zakresem 0..100: {key}={value}")


def compute_weighted_score(components: dict[str, float], weights: dict[str, float]) -> float:
    """Compute weighted score from component dictionary and weights."""
    missing = set(weights) - set(components)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Brak komponentow: {missing_list}")

    weight_sum = sum(weights.values())
    if abs(weight_sum - 1.0) > 1e-9:
        raise ValueError("Suma wag musi byc rowna 1.0")

    score = sum(components[name] * weights[name] for name in weights)
    return round(score, 2)


def classify_score(score: float, threshold: float = 50.0) -> str:
    """Return PASS for scores >= threshold, otherwise FAIL."""
    return "PASS" if score >= threshold else "FAIL"


def build_result(name: str, score: float, status: str) -> dict[str, object]:
    """Return normalized result object for presentation layer."""
    return {"name": name, "score": score, "status": status}


# ================= PRESENTATION LAYER =================

def build_presentable_report(result: dict[str, object]) -> str:
    """Render text report without changing domain result semantics."""
    name = str(result["name"])
    score = float(result["score"])
    status = str(result["status"])
    return f"{name}: score={score:.2f}, status={status}"


# ================= INTERACTION LAYER =================

def process_one_line(raw_line: str, weights: dict[str, float] | None = None) -> str:
    """Orchestrate layers for a single user input line."""
    local_weights = weights or DEFAULT_WEIGHTS
    name, components = parse_user_line(raw_line)
    validate_components(components)
    score = compute_weighted_score(components, local_weights)
    status = classify_score(score)
    result = build_result(name, score, status)
    return build_presentable_report(result)


def process_batch(lines: Iterable[str]) -> list[str]:
    """Process many lines and keep information about failed entries."""
    output: list[str] = []
    for index, line in enumerate(lines, start=1):
        try:
            output.append(process_one_line(line))
        except ValueError as exc:
            output.append(f"ERROR[{index}]: {exc}")
    return output


if __name__ == "__main__":
    sample_lines = [
        "Anna, 80, 90, 75, 88",
        "Jan, 40, 55, 60, 45",
        "Marta, 100, 98, 95, 97",
        "Ola, 20, 30, 40",  # invalid line for demo
    ]

    for row in process_batch(sample_lines):
        print(row)

