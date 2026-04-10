"""Zadania: zarządzanie zależnościami."""


def choose_env_tool(needs_data_science: bool) -> str:
    """Zwróć sugerowane narzędzie: venv albo conda."""
    raise NotImplementedError


def normalize_requirement(entry: str) -> str:
    """Uprość zapis dependency do postaci lowercase bez spacji."""
    raise NotImplementedError


def parse_requirements(text: str) -> list[str]:
    """Parsuj tekst requirements.txt — zwróć listę nazw pakietów (bez wersji).

    Ignoruj puste linie i komentarze (zaczynające się od #).
    Z wpisu 'requests>=2.28.0' wyciągnij 'requests'.
    Z wpisu 'Flask' wyciągnij 'flask' (lowercase).

    Przykład:
        parse_requirements("requests>=2.28\\n# komentarz\\nFlask\\n")
        ->  ["requests", "flask"]
    """
    raise NotImplementedError


def find_missing(installed: set[str], required: set[str]) -> set[str]:
    """Znajdź pakiety wymagane, ale niezainstalowane.

    Porównanie powinno być case-insensitive.

    Przykład:
        find_missing({"requests", "flask"}, {"requests", "pytest"})  ->  {"pytest"}
    """
    raise NotImplementedError

