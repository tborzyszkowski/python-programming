"""Przykladowe rozwiazania zadan SRP."""


def parse_student_line(line: str) -> tuple[str, list[float]]:
    parts = [p.strip() for p in line.split(";")]
    if len(parts) < 2:
        raise ValueError("Linia musi zawierac imie i co najmniej jeden wynik")
    name = parts[0]
    scores = [float(x) for x in parts[1:]]
    return name, scores


def validate_score(score: float) -> None:
    if score < 0 or score > 100:
        raise ValueError(f"Niepoprawny wynik: {score}")


def compute_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("Brak wynikow")
    return round(sum(scores) / len(scores), 2)


def classify_result(avg: float) -> str:
    if avg >= 90:
        return "A"
    if avg >= 75:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 50:
        return "D"
    return "F"


def build_summary(name: str, avg: float, cls: str) -> str:
    return f"{name}: srednia={avg:.2f}, ocena={cls}"


def process_student_record(line: str) -> str:
    name, scores = parse_student_line(line)
    for score in scores:
        validate_score(score)
    avg = compute_average(scores)
    cls = classify_result(avg)
    return build_summary(name, avg, cls)

