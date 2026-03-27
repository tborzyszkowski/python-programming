class Vector2D:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __len__(self) -> int:
        return 2

    def __str__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    @property
    def magnitude_hint(self) -> float:
        return abs(self.x) + abs(self.y)
