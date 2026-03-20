"""Przykladowe rozwiazania zadan z Separation of Concerns."""

from __future__ import annotations

from typing import Iterable


def parse_input_line(line: str) -> tuple[str, dict[str, float]]:
    parts = [part.strip() for part in line.split(",")]
    if len(parts) != 4:
        raise ValueError("Oczekiwano: Name, homework, project, exam")

    name = parts[0]
    components = {
        "homework": float(parts[1]),
        "project": float(parts[2]),
        "exam": float(parts[3]),
    }
    return name, components


def validate_component_score(score: float) -> None:
    if score < 0 or score > 100:
        raise ValueError(f"Wynik poza zakresem 0..100: {score}")


def calculate_final_score(components: dict[str, float], weights: dict[str, float]) -> float:
    missing = set(weights) - set(components)
    if missing:
        missing_names = ", ".join(sorted(missing))
        raise ValueError(f"Brak komponentow: {missing_names}")

    weight_sum = sum(weights.values())
    if abs(weight_sum - 1.0) > 1e-9:
        raise ValueError("Suma wag musi byc rowna 1.0")

    final_score = sum(components[name] * weights[name] for name in weights)
    return round(final_score, 2)


def decide_status(score: float, threshold: float = 50.0) -> str:
    return "PASS" if score >= threshold else "FAIL"


def render_console_report(name: str, score: float, status: str) -> str:
    return f"{name}: final={score:.2f}, status={status}"


def run_grade_pipeline(raw_line: str, weights: dict[str, float], threshold: float = 50.0) -> str:
    name, components = parse_input_line(raw_line)
    for value in components.values():
        validate_component_score(value)

    final_score = calculate_final_score(components, weights)
    status = decide_status(final_score, threshold)
    return render_console_report(name, final_score, status)


def batch_pipeline(lines: Iterable[str], weights: dict[str, float]) -> list[str]:
    output: list[str] = []
    for index, line in enumerate(lines, start=1):
        try:
            output.append(run_grade_pipeline(line, weights))
        except ValueError as exc:
            output.append(f"ERROR[{index}]: {exc}")
    return output

