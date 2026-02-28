class Person:
    person_count = 0
    def __init__(self, name, age, email, phone): #Take Details
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.person_count += 1

    def info(self): #Showing all Detais
        print(f'The Name is:{self.name}')
        print(f'The Age is:{self.age}')
        print(f'The Email is:{self.email}')
        print(f'The Phone is:{self.phone}')
    
    def upd_email(self): #Update Mail
        self.email = input('Enter Your Mail to Update: ')
        print(f'The Updated Mail:{self.email}')

    def upd_phone(self): #Update Phone
        self.phone = int(input('Enter the Number to Update: '))
        print(f'The Updated Phone Number is:{self.phone}')

    def upd_name(self): #Update Name
        self.name = input('Enter The Correct Name: ')
        print(f'The Correct Name:{self.name}')
