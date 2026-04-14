#salariedcommissionemploye.py
"""SalariedCommissionEmployee derived from CommissionEmployee"""
from commissionemployee import CommissionEmployee
from decimal import Decimal

class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who gets paid a salary plus commission based on gross sales"""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary):
        """Initialize SalariedCommissionEmployee's attributes"""
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)          #Call __init__ base case.
        self.base_salary = base_salary              #Validate via property

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, salary):
        """Set base salary or raise ValueError if invalid"""
        if salary <= Decimal('0.00'):
            raise ValueError('Salary must be greater than or equal to zero')

        self._base_salary = salary

    def earnings(self):
        """Calculate earnings."""
        return super().earnings() + self.base_salary

    def __repr__(self):
        """Return string representation of SalariedCommissionEmployee"""
        return ('Salaried' + super().__repr__() +
                f'base_salary: {self.base_salary:.2f}'
                )

