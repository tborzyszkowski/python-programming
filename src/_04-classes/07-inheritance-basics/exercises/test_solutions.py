from solutions_07 import Train


def test_train_move() -> None:
    assert Train().move() == "Pociąg jedzie po torach"
