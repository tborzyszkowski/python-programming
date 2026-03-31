from __future__ import annotations

from pathlib import Path

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_char(char: str, shift: int) -> str:
    lower = char.lower()
    if lower not in ALPHABET:
        return char
    index = ALPHABET.index(lower)
    shifted = ALPHABET[(index + shift) % len(ALPHABET)]
    return shifted.upper() if char.isupper() else shifted


def caesar_transform(text: str, shift: int) -> str:
    return "".join(shift_char(ch, shift) for ch in text)


def encrypt_text_file(input_path: Path, output_path: Path, shift: int) -> None:
    with input_path.open("r", encoding="utf-8") as src:
        content = src.read()
    encrypted = caesar_transform(content, shift)
    with output_path.open("w", encoding="utf-8") as dst:
        dst.write(encrypted)


def copy_binary_file(input_path: Path, output_path: Path) -> None:
    with input_path.open("rb") as src:
        data = src.read()
    with output_path.open("wb") as dst:
        dst.write(data)


def main() -> None:
    base = Path(__file__).parent
    plain = base / "plain.txt"
    encrypted = base / "encrypted.txt"
    decrypted = base / "decrypted.txt"

    plain.write_text("Python 3 Exceptions", encoding="utf-8")
    encrypt_text_file(plain, encrypted, 3)
    encrypt_text_file(encrypted, decrypted, -3)

    print("Plain:", plain.read_text(encoding="utf-8"))
    print("Encrypted:", encrypted.read_text(encoding="utf-8"))
    print("Decrypted:", decrypted.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()

