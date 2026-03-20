"""Porownanie podejscia monolitycznego i warstwowego."""

from layered_grade_app import process_one_line


def monolithic_grade_processor(raw_line: str) -> str:
    """Antywzorzec: jedna funkcja realizuje wiele concerns naraz."""
    parts = [p.strip() for p in raw_line.split(",")]
    if len(parts) != 5:
        raise ValueError("Niepoprawny format danych")

    name = parts[0]
    values = [float(value) for value in parts[1:]]
    if any(value < 0 or value > 100 for value in values):
        raise ValueError("Wynik poza zakresem")

    weights = [0.15, 0.15, 0.30, 0.40]
    score = round(sum(v * w for v, w in zip(values, weights)), 2)
    status = "PASS" if score >= 50 else "FAIL"
    return f"{name}: score={score:.2f}, status={status}"


if __name__ == "__main__":
    line = "Kasia, 70, 80, 90, 60"

    print("Monolit:")
    print(monolithic_grade_processor(line))

    print("\nWarstwy (SoC):")
    print(process_one_line(line))

