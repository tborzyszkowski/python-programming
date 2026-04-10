"""Zadania: pycache i pyc."""


def pyc_filename(module_name: str, tag: str) -> str:
    """Zbuduj nazwę jak dla module.cpython-313.pyc."""
    raise NotImplementedError


def should_recompile(source_mtime: int, pyc_mtime: int) -> bool:
    """Zwróć True, gdy źródło jest nowsze od cache."""
    raise NotImplementedError


def pycache_path(source_path: str, tag: str) -> str:
    """Zbuduj pełną ścieżkę do pliku .pyc w katalogu __pycache__.

    Wejście: ścieżka do pliku źródłowego (np. 'src/utils.py') i tag (np. 'cpython-313').
    Wynik: ścieżka do .pyc (np. 'src/__pycache__/utils.cpython-313.pyc').

    Użyj separatora '/' (unix-style).

    Przykład:
        pycache_path("src/utils.py", "cpython-313")  ->  "src/__pycache__/utils.cpython-313.pyc"
        pycache_path("main.py", "cpython-312")  ->  "__pycache__/main.cpython-312.pyc"
    """
    raise NotImplementedError


def extract_module_name_from_pyc(pyc_name: str) -> str:
    """Wyciągnij nazwę modułu z nazwy pliku .pyc.

    Przykład:
        extract_module_name_from_pyc("utils.cpython-313.pyc")  ->  "utils"
        extract_module_name_from_pyc("my_module.cpython-312.pyc")  ->  "my_module"
    """
    raise NotImplementedError

