from solutions_packages import is_namespace_package, package_public_api


def test_package_public_api():
    assert package_public_api(["a", "b"]) == ("a", "b")


def test_is_namespace_package():
    assert is_namespace_package(False) is True
    assert is_namespace_package(True) is False

