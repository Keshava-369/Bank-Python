"""
Module for validating person data including email and phone number.
"""

import re

class Person:
    """
    A class to represent a person's data.
    """
    def __init__(self, name: str, email: str, phone: str) -> None:
        """
        Initialize a new Person instance.

        :param name: Name of the person.
        :param email: Email address of the person.
        :param phone: Phone number of the person.
        """
        self.name = name
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)

    @staticmethod
    def validate_email(email: str) -> str:
        """
        Validate the provided email address.

        :param email: Email address to validate.
        :return: Validated email address.
        :raises ValueError: If the email address is invalid.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            raise ValueError('Invalid email address')
        return email

    @staticmethod
    def validate_phone(phone: str) -> str:
        """
        Validate the provided phone number.

        :param phone: Phone number to validate.
        :return: Validated phone number.
        :raises ValueError: If the phone number is invalid.
        """
        pattern = r'^[+]?[0-9]{10,15}$'
        if not re.match(pattern, phone):
            raise ValueError('Invalid phone number')
        return phone

    def __repr__(self) -> str:
        """
        Return a string representation of the Person instance.
        """
        return f'Person(name={self.name}, email={self.email}, phone={self.phone})'

    def __str__(self) -> str:
        """
        Return a human-readable string for the Person instance.
        """
        return f'{self.name} can be contacted at {self.email} or {self.phone}'
