"""Komponenty instancyjne vs klasowe/statyczne – rozszerzony przykład."""
from __future__ import annotations
import uuid


class Session:
    """Sesja użytkownika – ilustracja atrybutów klasowych vs instancyjnych."""

    # ── atrybuty KLASOWE (wspólne dla wszystkich instancji) ──
    active_count: int = 0
    MAX_SESSIONS: int = 100

    def __init__(self, user: str) -> None:
        if not Session.is_valid_username(user):
            raise ValueError(f"Nieprawidłowa nazwa użytkownika: {user!r}")
        if Session.active_count >= Session.MAX_SESSIONS:
            raise RuntimeError("Osiągnięto limit sesji")

        # ── atrybuty INSTANCYJNE (unikalne dla każdego obiektu) ──
        self._user = user
        self._session_id = Session.generate_id()

        Session.active_count += 1   # modyfikacja atrybutu klasowego

    def __repr__(self) -> str:
        return f"Session(user={self._user!r}, id={self._session_id!r})"

    def __del__(self) -> None:
        Session.active_count -= 1

    # ── właściwości ────────────────────────────────────────
    @property
    def user(self) -> str:
        return self._user

    @property
    def session_id(self) -> str:
        return self._session_id

    # ── metody instancyjne ─────────────────────────────────
    def rename(self, new_name: str) -> None:
        if not Session.is_valid_username(new_name):
            raise ValueError(f"Nieprawidłowa nazwa: {new_name!r}")
        self._user = new_name

    def logout(self) -> str:
        return f"Użytkownik {self._user} wylogowany"

    # ── metody KLASOWE (operacje na klasie, nie na instancji) ──
    @classmethod
    def active_sessions(cls) -> int:
        return cls.active_count

    @classmethod
    def create_guest(cls) -> Session:
        """Fabryka: tworzy sesję gościa."""
        return cls(f"guest_{Session.generate_id()[:4]}")

    # ── metody STATYCZNE (pomocnicze – nie potrzebują klasy ani instancji) ──
    @staticmethod
    def is_valid_username(name: str) -> bool:
        return len(name) >= 3 and name.replace("_", "").isalnum()

    @staticmethod
    def generate_id() -> str:
        return uuid.uuid4().hex[:8]


def main() -> None:
    print(f"Aktywne sesje: {Session.active_sessions()}")  # 0

    s1 = Session("jan_kowalski")
    s2 = Session("anna_nowak")
    print(f"Aktywne sesje: {Session.active_sessions()}")  # 2
    print(s1)
    print(s2)

    guest = Session.create_guest()
    print(f"Gość: {guest}")
    print(f"Aktywne sesje: {Session.active_sessions()}")  # 3

    # Usunięcie obiektu zmniejsza licznik
    del guest
    print(f"Po wylogowaniu gościa: {Session.active_sessions()}")  # 2

    # Metoda statyczna – można wywołać bez instancji
    print(Session.is_valid_username("ab"))   # False (za krótka)
    print(Session.is_valid_username("jan"))  # True


if __name__ == "__main__":
    main()
