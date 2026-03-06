"""
Skrypt generujacy pliki PNG z diagramow PlantUML (.puml).
Uzywa publicznego serwera plantuml.com przez biblioteke `plantuml`.

Uruchomienie:
    python generate_diagrams.py

Wymagania:
    pip install plantuml
"""
import sys
import io
import pathlib
import plantuml

# Wymuszamy UTF-8 na stdout/stderr (Windows cp1250 nie obsluguje wielu znakow)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


PUML_SERVER = "http://www.plantuml.com/plantuml/png/"
BASE_DIR = pathlib.Path(__file__).parent


def find_puml_files(base: pathlib.Path) -> list[pathlib.Path]:
    return sorted(base.rglob("*.puml"))


def generate_png(puml_path: pathlib.Path, pl: plantuml.PlantUML) -> pathlib.Path:
    """Wysyła plik .puml do serwera i zapisuje wynikowy .png obok niego."""
    png_path = puml_path.with_suffix(".png")
    source = puml_path.read_text(encoding="utf-8")
    png_data = pl.processes(source)
    if not png_data:
        raise RuntimeError(f"Serwer zwrócił puste dane dla: {puml_path.name}")
    png_path.write_bytes(png_data)
    return png_path


def main() -> None:
    puml_files = find_puml_files(BASE_DIR)
    if not puml_files:
        print("Nie znaleziono plikow .puml.")
        sys.exit(0)

    print(f"Znaleziono {len(puml_files)} plik(ow) .puml\n")
    pl = plantuml.PlantUML(url=PUML_SERVER)

    errors: list[tuple[pathlib.Path, str]] = []
    for puml_path in puml_files:
        rel = puml_path.relative_to(BASE_DIR)
        try:
            png_path = generate_png(puml_path, pl)
            size_kb = png_path.stat().st_size / 1024
            print(f"  [OK]  {rel}  ->  {png_path.name}  ({size_kb:.1f} KB)")
        except Exception as exc:
            print(f"  [!!]  {rel}  ->  BLAD: {exc}")
            errors.append((puml_path, str(exc)))

    print(f"\n{'='*55}")
    ok = len(puml_files) - len(errors)
    print(f"Wynik: {ok}/{len(puml_files)} wygenerowanych pomyślnie.")
    if errors:
        print("\nNieudane:")
        for p, msg in errors:
            print(f"  {p.relative_to(BASE_DIR)}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()

