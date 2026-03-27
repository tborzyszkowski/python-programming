from solutions_08 import Event


def test_source_returns_first_mixin() -> None:
    assert Event.source() == "LoggerMixin"
