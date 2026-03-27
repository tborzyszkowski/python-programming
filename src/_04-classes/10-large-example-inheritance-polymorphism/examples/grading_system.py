class GradePolicy:
    def final_score(self, points: list[float]) -> float:
        raise NotImplementedError


class MeanPolicy(GradePolicy):
    def final_score(self, points: list[float]) -> float:
        return sum(points) / len(points)


class BestOfTwoPolicy(GradePolicy):
    def final_score(self, points: list[float]) -> float:
        top = sorted(points, reverse=True)[:2]
        return sum(top) / len(top)


class Course:
    def __init__(self, name: str, policy: GradePolicy) -> None:
        self.name = name
        self.policy = policy

    def evaluate(self, points: list[float]) -> float:
        return self.policy.final_score(points)
