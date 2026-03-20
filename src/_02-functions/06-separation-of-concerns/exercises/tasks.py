"""Zadania: Separation of Concerns i warstwowanie funkcji."""

from __future__ import annotations

from typing import Iterable


# MODEL LAYER

def parse_input_line(line: str) -> tuple[str, dict[str, float]]:
    """TODO:
    Oczekiwany format: 'Name, homework, project, exam'.
    Zwracaj (name, components_dict).
    W przypadku zlego formatu rzuc ValueError.
    """
    raise NotImplementedError


def validate_component_score(score: float) -> None:
    """TODO: Dopuszczalny zakres punktow to 0..100 (wlacznie)."""
    raise NotImplementedError


def calculate_final_score(components: dict[str, float], weights: dict[str, float]) -> float:
    """TODO:
    Oblicz wynik wazony i zaokraglij do 2 miejsc.
    Rzuc ValueError gdy brakuje komponentu lub suma wag != 1.0.
    """
    raise NotImplementedError


def decide_status(score: float, threshold: float = 50.0) -> str:
    """TODO: Zwracaj 'PASS' lub 'FAIL'."""
    raise NotImplementedError


# PRESENTATION LAYER

def render_console_report(name: str, score: float, status: str) -> str:
    """TODO: Zwroc komunikat: '<name>: final=<score>, status=<status>'."""
    raise NotImplementedError


# INTERACTION LAYER

def run_grade_pipeline(raw_line: str, weights: dict[str, float], threshold: float = 50.0) -> str:
    """TODO:
    Zloz warstwy: parse -> validate -> calculate -> decide -> render.
    """
    raise NotImplementedError


def batch_pipeline(lines: Iterable[str], weights: dict[str, float]) -> list[str]:
    """TODO:
    Przetworz wiele linii i dla blednych wpisow dodaj
    'ERROR[<index>]: <komunikat>'.
    """
    raise NotImplementedError

