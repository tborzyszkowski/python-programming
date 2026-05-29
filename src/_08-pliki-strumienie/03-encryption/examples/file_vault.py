"""Sejf plików z szyfrowaniem Fernet i weryfikacją SHA-256.

Uruchomienie:
    python src/_08-pliki-strumienie/03-encryption/examples/file_vault.py
"""
from __future__ import annotations

import hashlib
import shutil
import tempfile
from pathlib import Path

try:
    from cryptography.fernet import Fernet
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False


class FileVault:
    """Zaszyfrowany sejf plików.

    Każdy plik jest szyfrowany Fernetem i przechowywany wraz
    z SHA-256 oryginału do weryfikacji integralności.
    """

    def __init__(self, katalog: Path, klucz: bytes) -> None:
        if not HAS_CRYPTO:
            raise ImportError("pip install cryptography")
        self.katalog = katalog
        self.katalog.mkdir(parents=True, exist_ok=True)
        self.fernet = Fernet(klucz)

    def add(self, plik: Path) -> None:
        """Dodaje plik do sejfu (szyfruje in-place do katalogu sejfu)."""
        dane = plik.read_bytes()
        sha  = hashlib.sha256(dane).hexdigest()
        zaszyfrowane = self.fernet.encrypt(dane)
        (self.katalog / plik.name).write_bytes(zaszyfrowane)
        (self.katalog / f"{plik.name}.sha256").write_text(sha, encoding="utf-8")
        print(f"  [+] Dodano: {plik.name}  (SHA-256: {sha[:16]}...)")

    def get(self, nazwa: str, cel: Path) -> None:
        """Wyciąga i deszyfruje plik z sejfu, weryfikując SHA-256."""
        enc  = (self.katalog / nazwa).read_bytes()
        dane = self.fernet.decrypt(enc)
        sha_oczek = (self.katalog / f"{nazwa}.sha256").read_text(encoding="utf-8").strip()
        sha_aktual = hashlib.sha256(dane).hexdigest()
        if sha_aktual != sha_oczek:
            raise ValueError(f"Integralność naruszona! {sha_aktual} != {sha_oczek}")
        cel.write_bytes(dane)
        print(f"  [-] Wyciągnięto: {nazwa} → {cel}")

    def list(self) -> list[str]:
        """Zwraca listę plików w sejfie (bez .sha256)."""
        return sorted(
            p.name for p in self.katalog.iterdir()
            if not p.name.endswith(".sha256")
        )


def main() -> None:
    if not HAS_CRYPTO:
        print("Zainstaluj: pip install cryptography")
        return

    tmp = Path(tempfile.mkdtemp(prefix="vault_"))
    try:
        vault_dir = tmp / "vault"
        klucz = Fernet.generate_key()
        vault = FileVault(vault_dir, klucz)

        # Tworzymy kilka plików testowych
        f1 = tmp / "raport.txt"
        f2 = tmp / "hasla.csv"
        f1.write_text("Tajny raport Q1 2024\nZysk: 1 000 000 PLN\n", encoding="utf-8")
        f2.write_text("login,haslo\nadmin,sekret123\n", encoding="utf-8")

        print("\n=== Dodawanie plików do sejfu ===")
        vault.add(f1)
        vault.add(f2)

        print(f"\nPliki w sejfie: {vault.list()}")

        print("\n=== Wyciąganie pliku ===")
        out = tmp / "raport_odszyfrowany.txt"
        vault.get("raport.txt", out)
        print(f"Zawartość: {out.read_text(encoding='utf-8')!r}")

        print("\n=== Próba wyciągnięcia z błędnym kluczem ===")
        zly_klucz = Fernet.generate_key()
        zly_vault = FileVault(vault_dir, zly_klucz)
        try:
            zly_vault.get("raport.txt", tmp / "nie_powstanie.txt")
        except Exception as e:
            print(f"  Oczekiwany błąd: {type(e).__name__}")

    finally:
        shutil.rmtree(tmp)
        print(f"\n[OK] Katalog tymczasowy usunięty: {tmp}")


if __name__ == "__main__":
    main()

