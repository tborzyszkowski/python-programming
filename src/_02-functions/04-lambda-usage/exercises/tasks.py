"""Zadania: praktyczne użycie lambda w przetwarzaniu danych."""


def sortuj_produkty(produkty: list[dict], klucz: str) -> list[dict]:
    """Zwróć nową listę produktów posortowaną po zadanym kluczu."""
    raise NotImplementedError("Zaimplementuj sortuj_produkty")


def filtruj_transakcje(transakcje: list[dict], prog: float) -> list[dict]:
    """Zwróć transakcje o kwocie >= prog."""
    raise NotImplementedError("Zaimplementuj filtruj_transakcje")


def mapuj_kwoty_brutto(transakcje: list[dict], vat: float = 0.23) -> list[float]:
    """Zwróć listę kwot brutto: netto * (1 + vat), zaokrąglone do 2 miejsc."""
    raise NotImplementedError("Zaimplementuj mapuj_kwoty_brutto")


def agreguj_kwoty(transakcje: list[dict]) -> float:
    """Zwróć sumę pól 'kwota' ze wszystkich transakcji."""
    raise NotImplementedError("Zaimplementuj agreguj_kwoty")


def ranking_studentow(studenci: list[dict]) -> list[str]:
    """Zwróć listę imion studentów posortowaną malejąco po średniej."""
    raise NotImplementedError("Zaimplementuj ranking_studentow")

