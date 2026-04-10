"""Proste porównanie listy zależności."""


def compare_specs(requirements: set[str], pyproject: set[str]) -> dict[str, set[str]]:
    return {
        "only_requirements": requirements - pyproject,
        "only_pyproject": pyproject - requirements,
        "common": requirements & pyproject,
    }


if __name__ == "__main__":
    req = {"pytest", "plantuml"}
    pyproj = {"pytest", "mypy"}
    print(compare_specs(req, pyproj))

