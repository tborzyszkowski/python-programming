"""Zadania: mechanizm importu."""


def classify_spec_origin(origin: str | None) -> str:
    """Zwróć not-found/built-in/file."""
    raise NotImplementedError


def is_visible_on_path(path_entries: list[str], module_dir: str) -> bool:
    """Sprawdź, czy katalog modułu jest widoczny na sys.path."""
    raise NotImplementedError


def diagnose_import_error(module_name: str, sys_path: list[str], sys_modules: dict) -> str:
    """Zdiagnozuj przyczynę problemu z importem.

    Zwróć jedną z wartości:
    - 'cached' — jeśli moduł jest w sys_modules (już załadowany),
    - 'found' — jeśli katalog zawierający moduł jest w sys_path
                (sprawdź, czy module_name + '.py' lub module_name jako katalog
                 jest „pokryty" przez jakikolwiek wpis w sys_path;
                 uproszczenie: sprawdź, czy jakikolwiek wpis sys_path kończy się
                 na katalogu nadrzędnym modułu; tu wystarczy sprawdzić,
                 czy module_name jest kluczem w sys_modules lub
                 czy jakikolwiek wpis path zawiera 'site-packages'),
    - 'not-found' — w przeciwnym razie.

    Uproszczony model:
        - jeśli module_name w sys_modules → 'cached'
        - jeśli jakikolwiek wpis w sys_path zawiera 'site-packages' → 'found'
        - w przeciwnym razie → 'not-found'
    """
    raise NotImplementedError

