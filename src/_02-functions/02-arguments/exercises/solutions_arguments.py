"""Przykładowe rozwiązania: *args i **kwargs."""


def policz_statystyki(*args: float) -> dict:
    if not args:
        raise ValueError("Podaj co najmniej jedną liczbę")
    return {
        "min": min(args),
        "max": max(args),
        "suma": sum(args),
        "srednia": sum(args) / len(args),
    }


def zbuduj_url(base: str, **query) -> str:
    if not query:
        return base
    pairs = [f"{k}={v}" for k, v in query.items()]
    return f"{base}?{'&'.join(pairs)}"


def skaluj_wyniki(*args: int, mnoznik: int = 2) -> list[int]:
    return [x * mnoznik for x in args]


def polacz_konfiguracje(**kwargs) -> dict:
    cfg = {"debug": False, "timeout": 30, "retries": 3}
    cfg.update(kwargs)
    return cfg


def wywolaj_funkcje(func, *args, **kwargs):
    return func(*args, **kwargs)

