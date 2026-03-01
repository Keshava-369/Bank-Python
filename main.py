import person as p
import account as acc
import tranasctions as t

class person_info: #Person Class with Import of Person Module
    def __init__(self, person_instance): 
        self.person = person_instance

    def info(self):
        self.person.info()

    def upd_mail(self):
        self.person.upd_email()

    def upd_phone(self):
        self.person.upd_phone()

    def upd_name(self):
        self.person.upd_name()

class account: #Account Class with Import of Account Module
    def __init__(self, account_instance):
        self.account = account_instance

    def acc_info(self): #Account Information
        self.account.account_info()

    def acc_number(self): #account number
        self.account.account_number()

    def deposit(self, amount): #deposit 
        self.account.deposit(amount)

    def withdraw(self, amount): #withdraw
        self.account.withdraw(amount)

    def balance(self): 
        self.account.check_balance()

    def transactions(self): #list all Transactions meant only deposited
        self.account.show_transactions()

current_account = None

while True:
    user_choice = int(input('\n1.Create Person \n2.Create Account \n3.Deposit \n4.Withdraw \n5.Balance Enquiry \n6.Show Transactions \n7.Update Mail \n8.Update Phone \n9.Update Name \n10.Person Count  \n11.Exit \nEnter Your Choice: '))

    if user_choice == 1:
        p.Person(input('Enter Your Name: '), int(input('Enter Your Age: ')), input('Enter Your Email: '), int(input('Enter Your Phone Number: ')))

    elif user_choice == 2:
        name = input('Enter The Account Holder Name: ')
        acc_type = input('Enter The Account Type: ')
        current_account = acc.Account(name, acc_type)
        account(current_account).acc_info()

    elif user_choice in [3, 4, 5, 6]:
        if current_account is None:
            print("Please create an account first!")
            continue
        
        acc = account(current_account)
        if user_choice == 3: acc.deposit(float(input('Enter Amount: ')))
        elif user_choice == 4: acc.withdraw(float(input('Enter Amount: ')))
        elif user_choice == 5: acc.balance()
        elif user_choice == 6: acc.transactions()
        elif user_choice == 7: p.Person.upd_email()
        elif user_choice == 8: p.Person.upd_phone()
        elif user_choice == 9: p.Person.upd_name()
        elif user_choice == 10: p.Person.person_count()
    elif user_choice == 11: break
    else: print('Invalid Choice')
