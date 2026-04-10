"""Demonstracja efektów ubocznych importu vs strażnika __name__."""


# ── Wersja 1: moduł z efektami ubocznymi ──────────────────────────

_log: list[str] = []


def dodaj_do_logu(msg: str) -> None:
    """Dodaje komunikat do logu."""
    _log.append(msg)


def pobierz_log() -> list[str]:
    """Zwraca kopię logu."""
    return list(_log)


# Ten kod wykona się przy KAŻDYM imporcie — efekt uboczny!
# W dobrym stylu powinien być chroniony strażnikiem if __name__ == "__main__".
# Zostawiamy go celowo, aby pokazać problem.

dodaj_do_logu("moduł załadowany")
print(f"[side_effect_demo] __name__ = {__name__!r}")


# ── Wersja 2: strażnik — kod uruchamia się TYLKO przy bezpośrednim uruchomieniu

if __name__ == "__main__":
    dodaj_do_logu("uruchomiony jako skrypt")
    print(f"Log: {pobierz_log()}")
    print("Demonstracja: uruchom 'import side_effect_demo' z innego pliku")
    print("i sprawdź, że log zawiera 'moduł załadowany', ale NIE 'uruchomiony jako skrypt'.")

