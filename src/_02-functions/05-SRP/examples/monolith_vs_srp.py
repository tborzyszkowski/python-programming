"""Porownanie podejscia monolitycznego i SRP dla przetwarzania ocen."""


def process_monolith(lines: list[str]) -> str:
    """Wersja anty-SRP: jedna funkcja robi wszystko."""
    parsed = []
    for line in lines:
        name, raw = line.split(",")
        score = float(raw.strip())
        if score < 0 or score > 100:
            raise ValueError(f"Niepoprawny wynik: {score}")
        parsed.append((name.strip(), score))

    avg = sum(score for _, score in parsed) / len(parsed)
    status = "zaliczono" if avg >= 50 else "niezaliczono"
    return f"Monolith: liczba={len(parsed)}, srednia={avg:.2f}, status={status}"


# --- SRP ---
def parse_line(line: str) -> tuple[str, float]:
    name, raw = line.split(",")
    return name.strip(), float(raw.strip())


def validate_score(score: float) -> None:
    if score < 0 or score > 100:
        raise ValueError(f"Niepoprawny wynik: {score}")


def compute_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("Brak wynikow")
    return sum(scores) / len(scores)


def classify(avg: float) -> str:
    return "zaliczono" if avg >= 50 else "niezaliczono"


def format_report(count: int, avg: float, status: str) -> str:
    return f"SRP: liczba={count}, srednia={avg:.2f}, status={status}"


def process_srp(lines: list[str]) -> str:
    parsed = [parse_line(line) for line in lines]
    for _, score in parsed:
        validate_score(score)
    scores = [score for _, score in parsed]
    avg = compute_average(scores)
    return format_report(len(parsed), avg, classify(avg))


if __name__ == "__main__":
    sample = ["Anna, 85", "Jan, 40", "Piotr, 65"]
    print(process_monolith(sample))
    print(process_srp(sample))

