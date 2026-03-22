"""Zadania: pakiety i __init__.py."""


def package_public_api(all_list: list[str]) -> tuple[str, ...]:
    """Zamien liste __all__ na niemutowalna krotke."""
    raise NotImplementedError


def is_namespace_package(has_init_file: bool) -> bool:
    """Zwroc True gdy katalog moze byc namespace package."""
    raise NotImplementedError

