"""Generuje pliki PNG z diagramów PlantUML (.puml) dla modułu _04-classes."""
from __future__ import annotations

import pathlib
import sys

import plantuml

BASE_DIR = pathlib.Path(__file__).parent
SERVER_URL = "http://www.plantuml.com/plantuml/png/"


def find_puml_files(base_dir: pathlib.Path) -> list[pathlib.Path]:
    return sorted(base_dir.rglob("*.puml"))


def generate_png(puml_path: pathlib.Path, renderer: plantuml.PlantUML) -> pathlib.Path:
    png_path = puml_path.with_suffix(".png")
    source = puml_path.read_text(encoding="utf-8")
    image_bytes = renderer.processes(source)
    if not image_bytes:
        raise RuntimeError(f"Brak danych PNG dla: {puml_path}")
    png_path.write_bytes(image_bytes)
    return png_path


def main() -> None:
    puml_files = find_puml_files(BASE_DIR)
    if not puml_files:
        print("Nie znaleziono plików .puml")
        return

    renderer = plantuml.PlantUML(url=SERVER_URL)
    errors: list[tuple[pathlib.Path, str]] = []

    for puml in puml_files:
        rel = puml.relative_to(BASE_DIR)
        try:
            png = generate_png(puml, renderer)
            print(f"[OK] {rel} -> {png.name}")
        except Exception as exc:  # pragma: no cover
            errors.append((rel, str(exc)))
            print(f"[ERR] {rel}: {exc}")

    print(f"Wynik: {len(puml_files) - len(errors)}/{len(puml_files)}")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
