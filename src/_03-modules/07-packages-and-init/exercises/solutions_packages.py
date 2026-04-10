"""Rozwiązania: pakiety i __init__.py."""


def package_public_api(all_list: list[str]) -> tuple[str, ...]:
    return tuple(all_list)


def is_namespace_package(has_init_file: bool) -> bool:
    return not has_init_file


def build_init_content(public_names: list[str], module_name: str) -> str:
    names_str = ", ".join(public_names)
    all_str = ", ".join(f'"{n}"' for n in public_names)
    return f"from .{module_name} import {names_str}\n\n__all__ = [{all_str}]\n"


def resolve_import_path(package_parts: list[str], module_name: str) -> str:
    parts = package_parts + [module_name]
    return ".".join(parts)
