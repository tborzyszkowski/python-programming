"""Rozwiazania: namespaces."""


def find_in_legb(local_value: str, enclosing_value: str, global_value: str) -> tuple[str, str, str]:
    enclosed = enclosing_value

    def inner() -> tuple[str, str, str]:
        local = local_value
        return local, enclosed, global_value

    return inner()


def merge_symbol_tables(local_table: dict, global_table: dict) -> dict:
    merged = dict(global_table)
    merged.update(local_table)
    return merged

