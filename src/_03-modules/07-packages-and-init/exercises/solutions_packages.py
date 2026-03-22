"""Rozwiazania: pakiety i __init__.py."""


def package_public_api(all_list: list[str]) -> tuple[str, ...]:
    return tuple(all_list)


def is_namespace_package(has_init_file: bool) -> bool:
    return not has_init_file

