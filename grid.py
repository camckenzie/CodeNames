from card import Card
from random import randint
from word import words

print('something')
class Grid:
    

    """This is the grid."""


    def __init__(self):
        self.cards = []
        self.initialize_grid()

    def initialize_grid(self):
        for i in range(25):
            text = words.pop(randint(0, 25-i))
            new_card = Card(text)
            self.cards.append(new_card)
    
    def display_grid(self):
        for card in self.cards:
            print(card.getText())

test = Grid()
test.display_grid()

