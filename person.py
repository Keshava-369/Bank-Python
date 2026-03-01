class Person:
    _person_count = 0
    def __init__(self, name, age, email, phone): #Take Details
        self.name = name
        self.age = age
        self.__email = email
        self.__phone = phone

        Person._person_count += 1
        

    
    def info(self): #Showing all Detais
        print(f'The Name is:{self.name}')
        print(f'The Age is:{self.age}')
        print(f'The Email is:{self.__email}') 
        print(f'The Phone is:{self.__phone}')
    
    def upd_email(self): #Update Mail
        self.__email = input('Enter Your Mail to Update: ')
        print(f'The Updated Mail:{self.__email}')

    def upd_phone(self): #Update Phone
        self.__phone = int(input('Enter the Number to Update: '))
        print(f'The Updated Phone Number is:{self.__phone}')

    def upd_name(self): #Update Name
        self.name = input('Enter The Correct Name: ')
        print(f'The Correct Name:{self.name}')

    @classmethod
    def person_count(cls): #Count of Person
        print(f'The Number of Persons are:{cls._person_count}')
        
    def remove_person(self): #Remove Person
        self.name = None
        self.age = None
        self.__email = None
        self.__phone = None
        Person._person_count -= 1
        print('The Person Removed Successfully')
