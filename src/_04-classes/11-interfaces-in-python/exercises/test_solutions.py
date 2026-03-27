from solutions_11 import BlikProcessor


def test_blik_processor() -> None:
    assert BlikProcessor().pay(12.5) == "blik:12.50"
