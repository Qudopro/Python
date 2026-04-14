#accountdoctest.py
import doctest
from decimal import Decimal
"""Account class definition"""
class Account:
    """Account class for demonstrating doctest"""
    def __init__(self, name, balance):
        """Initialize an Account object.
        >>> account = Account('John Green', Decimal('50.00'))
        >>> account.name
        'John Green'
        >>> account.balance
        Decimal('50.00')

        The balance argument must be greater than or equal to 0
        >>> account2 = Account('John Green', Decimal('-50.00'))
        Traceback (most recent call last):
        ...
        ValueError: Insufficient balance. Balance cannot be negative.
        """
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

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)