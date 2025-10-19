import collections

# Define a named tuple to represent a playing card
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    
    # __getitem__ makes the deck iterable and supports indexing and slicing
    def __getitem__(self, position):
            return self._cards[position]
    

beer_card = Card('7', 'diamonds')

print(beer_card)

print("--------------------------------")


deck = FrenchDeck()

#the deck of goes from 0 to 51  2 of spaded to Ace of hearts
print(len(deck))
print(deck[0])
print(deck[-1])
#This should print the 10th card in the deck which is the Queen of Spades
print(deck[10])


print("--------------------------------")

from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))


print("--------------------------------")

#slicing the deck
print(deck[:3])  # First three cards
print(deck[12::13])  # All the aces


print("--------------------------------")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank) # Get the index of the rank
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high): # Sort the deck using the spades_high function
    print(card)
print("--------------------------------")