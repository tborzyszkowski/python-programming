"""
Wzorcowe rozwiązania – Sposoby uruchamiania kodu w Pythonie
===========================================================
"""
import sys
import types
import pathlib
import importlib


def info_o_module(nazwa_modulu: str) -> dict:
    modul = importlib.import_module(nazwa_modulu)
    publiczne = [a for a in dir(modul) if not a.startswith("_")]
    return {
        "nazwa":    modul.__name__,
        "plik":     getattr(modul, "__file__", None),
        "pakiet":   getattr(modul, "__package__", "") or "",
        "atrybuty": len(publiczne),
    }


def lazy_import(nazwa_modulu: str):
    if nazwa_modulu in sys.modules:
        return sys.modules[nazwa_modulu]
    return importlib.import_module(nazwa_modulu)


def uruchom_kod_jako_modul(kod: str, nazwa: str = "__dynamic__") -> dict:
    m = types.ModuleType(nazwa)
    exec(compile(kod, nazwa, "exec"), m.__dict__)
    return m.__dict__


def znajdz_modul_w_sys_path(nazwa_pliku: str) -> str | None:
    for katalog in sys.path:
        sciezka = pathlib.Path(katalog) / nazwa_pliku
        if sciezka.is_file():
            return str(sciezka)
    return None


def lista_modulow_z_prefiksem(prefiks: str) -> list[str]:
    return sorted(
        name for name, mod in sys.modules.items()
        if name.startswith(prefiks) and mod is not None
    )


if __name__ == "__main__":
    print("info_o_module('math'):", info_o_module("math"))
    import os
    print("lazy_import('os') is os:", lazy_import("os") is os)
    ns = uruchom_kod_jako_modul("x = 6 * 7\ndef double(n): return n * 2")
    print("uruchom_kod_jako_modul: x =", ns.get("x"))
    print("znajdz_modul_w_sys_path('os.py'):", znajdz_modul_w_sys_path("os.py"))
    print("lista_modulow_z_prefiksem('sys'):", lista_modulow_z_prefiksem("sys"))

