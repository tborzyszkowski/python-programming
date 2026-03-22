"""Przyklady przestrzeni nazw i reguly LEGB."""

VALUE = "global-value"


def legb_demo() -> tuple[str, str, str]:
    value = "enclosing-value"

    def inner() -> tuple[str, str, str]:
        value = "local-value"
        return value, VALUE, str(len([1, 2, 3]))

    return inner()


def snapshot_symbol_tables() -> tuple[list[str], list[str]]:
    local_names = sorted(list(locals().keys()))
    global_names = sorted(name for name in globals().keys() if name.isupper())
    return local_names, global_names


if __name__ == "__main__":
    print("LEGB:", legb_demo())
    print("tables:", snapshot_symbol_tables())

