class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True  # Deposit successful
        return False  # Deposit failed

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True  # Withdrawal successful
        return False  # Withdrawal failed

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f"Current balance: ${self.get_balance()}")