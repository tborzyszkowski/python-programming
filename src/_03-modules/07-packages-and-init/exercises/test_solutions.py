from solutions_packages import (
    is_namespace_package,
    package_public_api,
    build_init_content,
    resolve_import_path,
)


def test_package_public_api():
    assert package_public_api(["a", "b"]) == ("a", "b")


def test_is_namespace_package():
    assert is_namespace_package(False) is True
    assert is_namespace_package(True) is False


def test_build_init_content():
    result = build_init_content(["add", "mean"], "math_ops")
    assert result == 'from .math_ops import add, mean\n\n__all__ = ["add", "mean"]\n'


def test_build_init_content_single():
    result = build_init_content(["hello"], "greetings")
    assert result == 'from .greetings import hello\n\n__all__ = ["hello"]\n'


def test_resolve_import_path_nested():
    assert resolve_import_path(["school", "core"], "grade_model") == "school.core.grade_model"


def test_resolve_import_path_flat():
    assert resolve_import_path([], "utils") == "utils"


def test_resolve_import_path_single():
    assert resolve_import_path(["pkg"], "mod") == "pkg.mod"
