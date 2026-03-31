from solutions_05 import caesar_transform


def test_caesar_transform_encrypts_text():
    assert caesar_transform("abc XYZ", 3) == "def ABC"


def test_caesar_transform_decrypts_text():
    encrypted = caesar_transform("Python", 5)
    assert caesar_transform(encrypted, -5) == "Python"

