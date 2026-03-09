"""Mini pipeline raportowania ocen zgodny z SRP."""


def parse_student_line(line: str) -> tuple[str, list[float]]:
    """Format linii: 'Anna;80;90;70'"""
    parts = [p.strip() for p in line.split(";")]
    if len(parts) < 2:
        raise ValueError("Linia musi zawierac imie i co najmniej jeden wynik")
    name = parts[0]
    scores = [float(x) for x in parts[1:]]
    return name, scores


def validate_scores(scores: list[float]) -> None:
    for score in scores:
        if score < 0 or score > 100:
            raise ValueError(f"Wynik poza zakresem: {score}")


def compute_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("Brak wynikow")
    return round(sum(scores) / len(scores), 2)


def classify(avg: float) -> str:
    if avg >= 90:
        return "A"
    if avg >= 75:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 50:
        return "D"
    return "F"


def build_summary(name: str, avg: float, grade: str) -> str:
    return f"{name}: srednia={avg:.2f}, ocena={grade}"


def process_student_record(line: str) -> str:
    name, scores = parse_student_line(line)
    validate_scores(scores)
    avg = compute_average(scores)
    grade = classify(avg)
    return build_summary(name, avg, grade)


if __name__ == "__main__":
    data = [
        "Anna;80;90;70",
        "Jan;45;55;60",
        "Celina;98;95;100",
    ]

    for row in data:
        print(process_student_record(row))

