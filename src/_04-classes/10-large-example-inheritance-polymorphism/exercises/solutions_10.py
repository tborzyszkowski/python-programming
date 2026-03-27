class WeightedPolicy:
    def __init__(self, w1: float, w2: float) -> None:
        self.w1 = w1
        self.w2 = w2

    def final_score(self, points: list[float]) -> float:
        return points[0] * self.w1 + points[1] * self.w2
