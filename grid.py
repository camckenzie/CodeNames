from card import Card
from random import randint
from word import words
from prettytable import PrettyTable

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
        print()
        for card in self.cards:
            print(card.getText())

    
    # def info(self) -> List[str]:
        
    #     #return []
    
    # def grid_table(self) -> None:

    #     pt: PrettyTable = PrettyTable(field_names='1', '2', '3', '4', '5')

    #     for card in self.cards:
    #         pt.add_column('test',card.getText())
    #     print('GRID THING')

test = Grid()
test.display_grid()

#test.grid_table()

