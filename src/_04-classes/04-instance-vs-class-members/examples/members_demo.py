class Session:
    active_count = 0

    def __init__(self, user: str) -> None:
        self.user = user
        Session.active_count += 1

    @classmethod
    def active_sessions(cls) -> int:
        return cls.active_count

    @staticmethod
    def is_valid_username(name: str) -> bool:
        return len(name) >= 3
