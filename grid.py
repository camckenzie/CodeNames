from card import Card
from random import randint
from word import words
from prettytable import PrettyTable

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
        
        x = PrettyTable()
        x.field_names = ["column1", "column2", "column3", "column4","column5"]
        array = []
        for idx, card in enumerate(self.cards):
            array.append(card.getText())
            if len(array) == 5:

                x.add_row(array)
                array = []

            #print(idx,card.getText())

            #x.add_row(['Yu Lin','Chris','Shanaya','Zu'])

        print(x)

test = Grid()
test.display_grid()

