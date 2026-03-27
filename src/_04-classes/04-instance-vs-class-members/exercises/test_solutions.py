from solutions_04 import Session


def test_reset_counter() -> None:
    Session("u1")
    Session("u2")
    assert Session.active_count == 2
    Session.reset_counter()
    assert Session.active_count == 0
