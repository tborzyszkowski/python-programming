class Session:
    active_count = 0

    def __init__(self, user: str) -> None:
        self.user = user
        Session.active_count += 1

    @classmethod
    def reset_counter(cls) -> None:
        cls.active_count = 0
