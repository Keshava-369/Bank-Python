class Account:
    _acc_count = 0
    _acc_num = 0

    def __init__(self, Person, acc_type='Saving Account'):
        self.Person = Person
        self.acc_type = acc_type
        self.__balance = 0
        self.transactions = []
        Account._acc_count += 1
        Account._acc_num += 1

    def deposit(self, amount):
        self.__balance += amount
        print(f'The Balance After Depositing:{self.__balance}')
        self.transactions.append(amount)

    def show_transactions(self):
        print(f'The Transactions are:{self.transactions}')


    def withdraw(self,amount): #Withdraw Amount
        print(f'The Amount You Entered to Withdraw is:{amount}')
        self.__balance -= amount
        print(f'The Amount Withdrawn Successfully \n The Balance:{self.__balance}')

    def check_balance(self): #Balance Enquiry
        print(f'The Leftover Balance in Your Account is:{self.__balance}')

    def account_info(self): #Account Basic Details
        print(f'The Account Holder Name:{self.Person}')
        print(f'The Account Holder Account Type:{self.acc_type}')
        
    @classmethod
    def account_number(cls):
        print(f'The Account Number is:{1000+cls._acc_num}')

    @classmethod
    def acc_count(cls):
        print(f'The Number of Accounts are:{cls._acc_count}')
