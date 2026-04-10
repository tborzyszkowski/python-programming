class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Brak środków")
        self.balance -= amount


def safe_transfer(src: BankAccount, dst: BankAccount, amount: float) -> None:
    src.withdraw(amount)
    dst.deposit(amount)


def total_balance(accounts: list[BankAccount]) -> float:
    return sum(acc.balance for acc in accounts)
