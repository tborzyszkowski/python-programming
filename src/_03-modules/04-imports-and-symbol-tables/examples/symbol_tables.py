"""Demonstracja globals(), locals() i builtins."""


def inspect_tables() -> dict[str, bool]:
    local_name = "inside"
    _ = local_name
    return {
        "local_name_in_locals": "local_name" in locals(),
        "inspect_tables_in_globals": "inspect_tables" in globals(),
        "len_in_globals": "len" in globals(),
    }


if __name__ == "__main__":
    print(inspect_tables())

