"""
Moduł demonstracyjny – przykładowe funkcje do importu.

Uruchomienie bezpośrednie:
    python -m run_as_module    (z katalogu examples/)

Import:
    from run_as_module import powitaj, oblicz_bmi
"""


def powitaj(imie: str) -> str:
    """Zwraca powitanie dla podanego imienia."""
    return f"Witaj, {imie}! Uruchomiono jako moduł."


def oblicz_bmi(masa_kg: float, wzrost_m: float) -> float:
    """Oblicza wskaźnik masy ciała (BMI).

    Args:
        masa_kg: masa ciała w kilogramach
        wzrost_m: wzrost w metrach

    Returns:
        Wartość BMI zaokrąglona do 2 miejsc po przecinku.
    """
    if wzrost_m <= 0:
        raise ValueError("Wzrost musi być większy od zera.")
    return round(masa_kg / wzrost_m ** 2, 2)


if __name__ == "__main__":
    print(powitaj("Użytkownik"))
    bmi = oblicz_bmi(70, 1.75)
    print(f"BMI (70 kg, 1.75 m) = {bmi}")

