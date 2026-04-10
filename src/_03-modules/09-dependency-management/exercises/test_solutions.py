from solutions_dependencies import (
    choose_env_tool,
    normalize_requirement,
    parse_requirements,
    find_missing,
)


def test_choose_env_tool():
    assert choose_env_tool(True) == "conda"
    assert choose_env_tool(False) == "venv"


def test_normalize_requirement():
    assert normalize_requirement(" PyTest >= 7.4 ") == "pytest>=7.4"


def test_parse_requirements_basic():
    text = "requests>=2.28\n# komentarz\nFlask\n"
    assert parse_requirements(text) == ["requests", "flask"]


def test_parse_requirements_empty_lines():
    text = "\n\nrequests\n\n"
    assert parse_requirements(text) == ["requests"]


def test_parse_requirements_version_operators():
    text = "django>=4.0,<5.0\nnumpy==1.25\n"
    assert parse_requirements(text) == ["django", "numpy"]


def test_parse_requirements_comments_only():
    text = "# to jest komentarz\n# i kolejny"
    assert parse_requirements(text) == []


def test_find_missing_some():
    assert find_missing({"requests", "flask"}, {"requests", "pytest"}) == {"pytest"}


def test_find_missing_none():
    assert find_missing({"requests", "flask"}, {"requests", "flask"}) == set()


def test_find_missing_case_insensitive():
    assert find_missing({"Requests"}, {"requests"}) == set()


def test_find_missing_all():
    assert find_missing(set(), {"pytest", "flask"}) == {"pytest", "flask"}
