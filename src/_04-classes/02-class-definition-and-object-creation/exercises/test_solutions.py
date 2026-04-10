import pytest
from solutions_02 import BankAccount, safe_transfer, total_balance


def test_deposit() -> None:
    acc = BankAccount("Jan", 100.0)
    acc.deposit(50.0)
    assert acc.balance == 150.0


def test_deposit_negative_raises() -> None:
    acc = BankAccount("Jan", 100.0)
    with pytest.raises(ValueError):
        acc.deposit(-10.0)


def test_withdraw() -> None:
    acc = BankAccount("Jan", 100.0)
    acc.withdraw(30.0)
    assert acc.balance == 70.0


def test_withdraw_insufficient_raises() -> None:
    acc = BankAccount("Jan", 50.0)
    with pytest.raises(ValueError):
        acc.withdraw(100.0)


def test_safe_transfer() -> None:
    src = BankAccount("A", 100.0)
    dst = BankAccount("B", 0.0)
    safe_transfer(src, dst, 40.0)
    assert src.balance == 60.0
    assert dst.balance == 40.0


def test_safe_transfer_insufficient_raises() -> None:
    src = BankAccount("A", 10.0)
    dst = BankAccount("B", 0.0)
    with pytest.raises(ValueError):
        safe_transfer(src, dst, 100.0)
    # dst nie powinno się zmienić
    assert dst.balance == 0.0


def test_total_balance() -> None:
    accounts = [BankAccount("A", 100), BankAccount("B", 200), BankAccount("C", 50)]
    assert total_balance(accounts) == 350.0


def test_total_balance_empty() -> None:
    assert total_balance([]) == 0.0
