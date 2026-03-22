"""Większy przykład: mini narzędzia dla dziekanatu.

Pokazuje projektowanie funkcji z docstringami, walidacją i typowaniem.
"""


def waliduj_oceny(oceny: list[float]) -> None:
    """Sprawdza, czy oceny są w skali 2.0-5.0."""
    if not oceny:
        raise ValueError("Lista ocen nie może być pusta")
    for ocena in oceny:
        if ocena < 2.0 or ocena > 5.0:
            raise ValueError(f"Niepoprawna ocena: {ocena}")


def policz_srednia_wazona(oceny: list[float], ects: list[int]) -> float:
    """Liczy średnią ważoną ocen wg punktów ECTS."""
    if len(oceny) != len(ects):
        raise ValueError("Listy oceny i ects muszą mieć ten sam rozmiar")
    waliduj_oceny(oceny)
    if any(e <= 0 for e in ects):
        raise ValueError("ECTS muszą być dodatnie")

    licznik = sum(o * e for o, e in zip(oceny, ects))
    mianownik = sum(ects)
    return round(licznik / mianownik, 2)


def klasyfikuj_stypendium(srednia: float, prog: float = 4.5) -> str:
    """Zwraca decyzję stypendialną na podstawie średniej."""
    return "Przyznane" if srednia >= prog else "Brak"


def raport_studenta(imie: str, oceny: list[float], ects: list[int]) -> str:
    """Buduje raport podsumowujący wyniki studenta."""
    srednia = policz_srednia_wazona(oceny, ects)
    decyzja = klasyfikuj_stypendium(srednia)
    return (
        f"Student: {imie}\n"
        f"Średnia ważona: {srednia}\n"
        f"Stypendium: {decyzja}"
    )


if __name__ == "__main__":
    print(raport_studenta("Anna", [5.0, 4.5, 4.0, 5.0], [6, 5, 4, 3]))
    print(raport_studenta("Zdziś", [3.0, 3.0, 4.0, 2.0], [6, 5, 4, 3]))

