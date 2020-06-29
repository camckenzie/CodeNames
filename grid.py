from card import Card
#from move import Move
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict


class Grid:
    

    """This is the grid."""


    def __init__(self):
        self.cards = []

        self.choices = ['Red', 'Blue', 'Black', 'Neutral']
        self.choice_limit: Dict[str, int] = {'Red': 8, 'Blue': 7, 'Black': 1, 'Neutral': 9}
        self.choice_count: Dict[str, int] = {'Red': 0, 'Blue': 0, 'Black': 0, 'Neutral': 0}
        #Keep track of cards revealed here:
        
        #self.player_count: Dict[str, int] = {'Red': 0, 'Blue': 0, 'Black': 0, 'Neutral': 0}

        self.initialize_grid()
        #self.print_text()
        self.print_team()
        self.print_click()

    def initialize_grid(self):
        for i in range(25):
            text = words.pop(randint(0, 25-i))
            team = choice(self.choices)
            new_card = Card(text, team)

            self.choice_count[team] += 1
            self.cards.append(new_card)

            if self.choice_limit[team] == self.choice_count[team]:
                self.choices.remove(team)

    
    # def print_text(self):
        
    #     x = PrettyTable()
    #     x.field_names = ["column1", "column2", "column3", "column4","column5"]
    #     array = []

    #     for idx, card in enumerate(self.cards):
    #         array.append(card.getText()) #ADD THE CARD NUMBER HERE

    #         if len(array) == 5:
    #             x.add_row(array)
    #             array = []

    #     print(x)


    def print_team(self):

        y = PrettyTable()
        y.field_names = ["column1", "column2", "column3", "column4","column5"]
        t_array = []

        for idx, card in enumerate(self.cards):
            t_array.append(card.getTeam())

            if len(t_array) == 5:
                y.add_row(t_array)
                t_array = []

        print(y)

    def print_click(self):

        z = PrettyTable()
        z.field_names = ["column1", "column2", "column3", "column4","column5"]
        c_array = []

        for idx, card in enumerate(self.cards):

            if card.getClick() == 'Y':
                c_array.append(f'{card.getText()} ({card.getTeam()})')

            elif card.getClick() == 'N':
                c_array.append(card.getText())

            if len(c_array) == 5:
                z.add_row(c_array)
                c_array = []

        print(z)    


test = Grid()
#test.print_text()
#test.print_team()

