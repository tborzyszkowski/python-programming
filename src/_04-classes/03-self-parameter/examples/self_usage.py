class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> int:
        self.value += 1
        return self.value


if __name__ == "__main__":
    counter = Counter()
    print(counter.increment())
