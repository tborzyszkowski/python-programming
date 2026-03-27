class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia")
        self.balance += amount


if __name__ == "__main__":
    account = BankAccount("Jan", 100.0)
    account.deposit(20.0)
    print(account.balance)
