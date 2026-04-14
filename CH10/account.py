#account.py
from decimal import Decimal
"""Account class definition"""
class Account:
    """Account class for maintaining a bank account balance."""
    def __init__(self, name, balance):
        """Initialize an Account object."""

        #if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Insufficient balance. Balance cannot be negative.')

        #Create attributes dynamically
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""
        if(amount < Decimal('0.00')):
            raise ValueError('Insufficient balance. Balance cannot be negative.')

        self.balance += amount


