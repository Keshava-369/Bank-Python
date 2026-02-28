class Account: 
    acc_count = 0
    def __init__(self,Person,acc_type='Saving Account'):
        self.Person = Person
        self.acc_type = acc_type
        self.balance = 0
        self.transaction = []

    def deposit(self,amount): #Deposit Amount
        self.balance += amount
        print(f'The Balance After Depositing:{self.balance}')
        self.transaction.append(amount)

    def withdraw(self,amount): #Withdraw Amount
        print(f'The Amount You Entered to Withdraw is:{amount}')
        self.balance -= amount
        print(f'The Amount Withdrawn Successfully \n The Balance:{self.balance}')

    def check_balnce(self): #Balance Enquiry
        print(f'The Leftover Balance in Your Account is:{self.balance}')

    def account_info(self): #Account Basic Details
        print(f'The Account Holder Name:{self.Person}')
        print(f'The Account Holder Account Type:{self.acc_type}')

    def transaction(self): #Total Transactions
        print(f'The Transactions are:{self.transaction}')
