"""Rozwiązania: pycache i pyc."""

import posixpath


def pyc_filename(module_name: str, tag: str) -> str:
    return f"{module_name}.{tag}.pyc"


def should_recompile(source_mtime: int, pyc_mtime: int) -> bool:
    return source_mtime > pyc_mtime


def pycache_path(source_path: str, tag: str) -> str:
    # Normalizuj na unix-style
    source_path = source_path.replace("\\", "/")
    if "/" in source_path:
        directory, filename = source_path.rsplit("/", 1)
        base = directory + "/__pycache__"
    else:
        base = "__pycache__"
        filename = source_path
    module_name = filename.rsplit(".", 1)[0]
    return f"{base}/{module_name}.{tag}.pyc"


def extract_module_name_from_pyc(pyc_name: str) -> str:
    # "utils.cpython-313.pyc" -> split by "." -> ["utils", "cpython-313", "pyc"]
    return pyc_name.split(".")[0]
