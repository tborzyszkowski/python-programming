from solutions_10 import WeightedPolicy


def test_weighted_policy() -> None:
    policy = WeightedPolicy(0.4, 0.6)
    assert policy.final_score([3.0, 5.0]) == 4.2
