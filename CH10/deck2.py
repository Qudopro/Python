#deck2.py
"""Deck class represents a deck of Cards"""
import random
from carddataclass import Card

class DeckOfCards:
    NUMBER_OF_CARDS = 52            #Constant number of Cards

    def __init__(self):
        """Initialize a Deck of Cards"""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(
                Card(Card.FACES[count%13],                        #Always returns a value 1-12 (%13 because of there's 13 elements in FACES)
                     Card.SUITS[count//13]                        #Always returns a value 0-3
                     )
            )

    def shuffle(self):
        """Shuffle the deck"""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Return one Card"""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None


    def __str__(self):
        """Return a string representation of the deck in four columns"""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'                 #Call to __format__ method with format specifier <19
            if(index + 1) % 4 == 0:
                s += '\n'

        return s
