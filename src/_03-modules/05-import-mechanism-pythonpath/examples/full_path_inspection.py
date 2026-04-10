"""Pełna inspekcja sys.path z opisami źródeł wpisów."""

from __future__ import annotations

import os
import sys
import sysconfig


def annotated_sys_path() -> list[dict[str, str]]:
    """Zwraca sys.path z adnotacjami o źródle każdego wpisu."""
    result = []
    stdlib_dir = sysconfig.get_path("stdlib")
    site_dir = sysconfig.get_path("purelib")

    for i, entry in enumerate(sys.path):
        if entry == "":
            source = "pusty string → bieżący katalog roboczy"
        elif stdlib_dir and entry.startswith(stdlib_dir):
            source = "biblioteka standardowa"
        elif site_dir and entry.startswith(site_dir):
            source = "site-packages (pip)"
        elif i == 0:
            source = "katalog uruchamianego skryptu"
        elif "PYTHONPATH" in os.environ.get("PYTHONPATH", "") and entry in os.environ.get("PYTHONPATH", "").split(os.pathsep):
            source = "PYTHONPATH"
        else:
            source = "inne (dystrybucja / .pth)"

        result.append({"index": str(i), "path": entry, "source": source})

    return result


def print_sys_path() -> None:
    """Wypisuje sys.path w czytelnym formacie."""
    print(f"Python {sys.version}")
    print(f"Katalog roboczy: {os.getcwd()}")
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', '<nie ustawiony>')}")
    print()
    print(f"{'Idx':<4} {'Źródło':<35} Ścieżka")
    print("-" * 90)
    for item in annotated_sys_path():
        print(f"{item['index']:<4} {item['source']:<35} {item['path']}")


if __name__ == "__main__":
    print_sys_path()

