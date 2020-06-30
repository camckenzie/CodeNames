from card import Card
from grid import Grid
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict, List

#TODO: Figure out how to end the game
#Figure out win conditions
# Scoring - Count for number of Red/Blue words that have been clicked 

class Game:


    def __init__(self):  
        self.grid = Grid()
        
        self.score()
        # play = True
        # while play:
        #     self.play_game(play) #Player turn
        


        #play game function - Loops

    def play_game(self, play: bool=True):

        p1 = 'True'
        p2 = 'True'

        print('PLAYER 1 TURN')
        while p1:
            self.grid.print_click()   #Print new Grid board
            p1 = self.move()
        print('Player 1 End Turn')
        
        print('PLAYER 2 TURN')
        while p2:
            self.grid.print_click()   #Print new Grid board
            p2 = self.move()
        print('Player 2 End Turn')


    def move(self):

        #Look for Input
        
        move = input("Select a word: ")

        if move == 'Q':
            return False
        elif move in self.grid.c_dict:
            card = self.grid.c_dict[move]
            card.setClick('Y')
            #print(self.grid.c_dict)
        else:
            print(f"ERROR: '{move}' NOT FOUND IN BOARD")

        return True

    def score(self):

        #Calculates current score
        self.choice_limit: Dict[str, int] = {'Red': 8, 'Blue': 7} #Final Score
        self.choice_count: Dict[str, int] = {'Red': 0, 'Blue': 0} #Current Score
        
        # Count total number of Blue cards that are clicked
        #self.c_dict[text] = Card

        blue_score = 0
        for team in self.grid.c_dict.values():
            if team._team == 'Red' or team._team == 'Blue':
                self.choice_count[team._team] +=1
        
        print(self.choice_count)
        
        # Count total number of Red cards that are clicked


        # self.choice_count[team] += 1
        # self.c_dict[new_card.getText()] = Card(text, team)

        # if self.choice_limit[team] == self.choice_count[team]:
        #     self.choices.remove(team)
        

test = Game()