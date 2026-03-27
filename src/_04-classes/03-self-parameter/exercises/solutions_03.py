class Counter:
    def __init__(self) -> None:
        self.value = 0

    def add_many(self, n: int) -> int:
        self.value += n
        return self.value
