from solutions_dependencies import choose_env_tool, normalize_requirement


def test_choose_env_tool():
    assert choose_env_tool(True) == "conda"
    assert choose_env_tool(False) == "venv"


def test_normalize_requirement():
    assert normalize_requirement(" PyTest >= 7.4 ") == "pytest>=7.4"

