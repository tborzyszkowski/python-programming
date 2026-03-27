from solutions_02 import BankAccount, safe_transfer


def test_safe_transfer() -> None:
    src = BankAccount("A", 100.0)
    dst = BankAccount("B", 0.0)
    safe_transfer(src, dst, 40.0)
    assert src.balance == 60.0
    assert dst.balance == 40.0
