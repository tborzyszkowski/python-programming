from solutions_12 import build_discount


def test_build_discount_vip() -> None:
    strategy = build_discount("vip")
    assert round(strategy.apply(100.0), 2) == 70.0
