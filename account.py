class Account:
    def __init__(self, person,balance=0):
        self.balance = balance
        self.person = person

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True  # Deposit Done
        return False  # Deposit fail

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True  # Withdrawal Done
        return False  # Withdrawal fail

    def display_balance(self): #Display Balance
        print(f"Current balance: ${self.get_balance()}")
        
    def disp_info(self):
        print(f'The Holder, Balance{self.person,self.balance}')
