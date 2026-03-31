"""Rozwiązania: obsługa plików i szyfr Cezara."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def _shift_char(char: str, shift: int) -> str:
    lower = char.lower()
    if lower not in ALPHABET:
        return char
    idx = ALPHABET.index(lower)
    shifted = ALPHABET[(idx + shift) % len(ALPHABET)]
    return shifted.upper() if char.isupper() else shifted


def caesar_transform(text: str, shift: int) -> str:
    return "".join(_shift_char(ch, shift) for ch in text)

