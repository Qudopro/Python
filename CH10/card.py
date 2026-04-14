#card.py
"""Card class that represents a playing card and its image file name"""
class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10','Jack','Queen','King']
    SUITS = ['hearts','diamonds','clubs','spades']


    def __init__(self, face, suit):
        """Initialize a Card with a face and suit"""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the face of the card"""
        return self._face

    @property
    def suit(self):
        """Return the suit of the card"""
        return self._suit

    @property
    def image_name(self):               #Create image_name property dynamically
        """Return the Card's image file name"""
        return str(self).replace(' ','_') + '.png'          #Getting the Card object's string representation with underscores and filename extension

    def __repr__(self):
        """Return a string representation of the card"""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return a string representation of the card"""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation of the card"""
        return f'{str(self):{format}}'          #format = Format string used to format the object. We use the format parameter's value as the format specifier: {format}

