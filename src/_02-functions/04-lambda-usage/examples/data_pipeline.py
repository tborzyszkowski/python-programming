"""Większy przykład: pipeline przetwarzania transakcji.

Cel: filtrowanie, mapowanie, agregacja i ranking.
"""

from functools import reduce


TRANSAKCJE = [
    {"id": 1, "kategoria": "sprzet", "kwota": 1200.0, "klient": "A"},
    {"id": 2, "kategoria": "ksiazki", "kwota": 80.0, "klient": "B"},
    {"id": 3, "kategoria": "sprzet", "kwota": 450.0, "klient": "A"},
    {"id": 4, "kategoria": "kurs", "kwota": 999.0, "klient": "C"},
    {"id": 5, "kategoria": "ksiazki", "kwota": 150.0, "klient": "B"},
]


def top_kwoty(transakcje: list[dict], min_kwota: float) -> list[dict]:
    return list(filter(lambda t: t["kwota"] >= min_kwota, transakcje))


def kwoty_brutto(transakcje: list[dict], vat: float = 0.23) -> list[float]:
    return list(map(lambda t: round(t["kwota"] * (1 + vat), 2), transakcje))


def suma_kwot(transakcje: list[dict]) -> float:
    return reduce(lambda acc, t: acc + t["kwota"], transakcje, 0.0)


def ranking_klientow(transakcje: list[dict]) -> list[tuple[str, float]]:
    """Zwraca ranking (klient, suma_kwot) malejąco po sumie."""
    klienci = sorted({t["klient"] for t in transakcje})
    sums = [(k, suma_kwot(list(filter(lambda t, k=k: t["klient"] == k, transakcje)))) for k in klienci]
    return sorted(sums, key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    high = top_kwoty(TRANSAKCJE, 500)
    print("Transakcje >= 500:", high)

    print("Kwoty brutto:", kwoty_brutto(high))
    print("Suma netto high:", suma_kwot(high))
    print("Ranking klientów:", ranking_klientow(TRANSAKCJE))

