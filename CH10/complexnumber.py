#complexnumber.py
"""Complex class with overloaded operators"""
class Complex:
    """Complex class that represents a complex number with real and imaginary parts"""
    def __init__(self, real, imaginary):
        """Initialize Complex class's attributes"""
        self.real = real
        self.imaginary = imaginary

    def __add__(self, right):               #Self = First (left) operand and right = second (right) operand). Only with methods that overload binary operators
        """Overrides the + operator with two Complex objects as arguments and returns a new Complex object"""
        return Complex(self.real + right.real, self.imaginary + right.imaginary)

    def __iadd__(self, right):                #Define how += operator adds two Complex objects
        """Overrides the += operator with two Complex objects as arguments and it modifies their left oprands (self object)"""
        self.real += right.real
        self.imaginary += right.imaginary
        return self

    def __repr__(self):
        """Returns a string representation of the Complex object"""
        return (f'({self.real} '  +
                ('+ ' if self.imaginary >= 0 else '- ') +
                f'{abs(self.imaginary)}i)')


