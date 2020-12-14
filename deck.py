import random as rando
from copy import deepcopy

# Sorry is represented by 0
class Deck(object):
    def __init__(self):
        self.fullCards = {
    0 : 4,
    1 : 5,
    2 : 4,
    3 : 4,
    4 : 4,
    5 : 4,
    7 : 4,
    8 : 4,
    10 : 4,
    11 : 4,
    12 : 4,
}
        self.cards = {
    0 : 4,
    1 : 5,
    2 : 4,
    3 : 4,
    4 : 4,
    5 : 4,
    7 : 4,
    8 : 4,
    10 : 4,
    11 : 4,
    12 : 4,
}
        self.numCards = 45

    def drawCard(self):
        thereAreCards = False
        # iterate through card types
        for i in self.cards.keys():
            if self.cards[i] != 0:
                thereAreCards = True
        # if there are no cards, restock the deck
        if not thereAreCards:
            self.cards = deepcopy(self.fullCards)
        
        # pick a card value
        pickedCard = rando.choice(list(self.cards.keys()))
        # while there are no cards of selected value,
        while self.cards[pickedCard] == 0:
            # keep picking card values
            pickedCard = rando.choice(list(self.cards.keys()))
        # value with cards has been selected, remove a card from the value
        self.cards[pickedCard] -= 1
        if self.cards[pickedCard] < 0:
            self.cards[pickedCard] = 0
        return pickedCard
