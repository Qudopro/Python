#wellpaidduck.py
from decimal import Decimal

class WellPaidDuck:
    def __repr__(self):
        return 'I am well-paid duck'

    def earnings(self):
        return Decimal('1_000_000.00')