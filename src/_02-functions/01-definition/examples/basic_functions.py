"""
Demonstracja podstaw definiowania funkcji w Pythonie 3.
"""


def powitaj(imie: str, wiek: int = 18) -> str:
    """Zwraca spersonalizowane powitanie.

    Args:
        imie (str): Imię osoby do powitania.
        wiek (int, opcjonalny): Wiek osoby. Domyślnie 18.

    Returns:
        str: Sformatowany ciąg powitalny.
    """
    return f"Witaj, {imie}! Masz {wiek} lat."


def oblicz_pole_trojkata(a: float, h: float) -> float:
    """Oblicza pole trójkąta.

    Args:
        a (float): Długość podstawy.
        h (float): Wysokość.

    Returns:
        float: Pole trójkąta.
    """
    return 0.5 * a * h


def nic_nie_rob():
    """Funkcja pusta (placeholder)."""
    pass


if __name__ == "__main__":
    print("-" * 30)
    # Wywołanie z argumentami pozycyjnymi
    witaj = powitaj("Anna", 25)
    print(witaj)

    # Wywołanie z argumentem domyślnym
    witaj_domyslnie = powitaj("Bartek")
    print(witaj_domyslnie)

    # Wywołanie z argumentami nazwanymi (keyword arguments)
    witaj_kw = powitaj(wiek=30, imie="Celina")
    print(witaj_kw)

    print("-" * 30)
    pole = oblicz_pole_trojkata(10, 5)
    print(f"Pole trójkąta (a=10, h=5): {pole}")

    print("-" * 30)
    print(f"Dokumentacja funkcji `powitaj`:\n{powitaj.__doc__}")

