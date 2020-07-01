from card import Card
from grid import Grid
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict, List

#TODO: 
#Figure out win conditions, how to end the game
#Remove duplicate code in p1/p2 move
# Scoring - Count for number of Red/Blue words that have been clicked 

class Game:


    def __init__(self):  
        self.grid = Grid()
        self.current_score: Dict[str, int] = {'Red': 0, 'Blue': 0}
        #self.score()
        play = True
        while play:
            self.play_game(play) #Player turn
            #self.score() 
        


        #play game function - Loops

    def play_game(self, play: bool=True):


        p1 = 'True'
        p2 = 'True'

        print('PLAYER 1 TURN')
        while p1:
            self.grid.print_click()   #Print new Grid board
            p1 = self.move()
            print(f'SCORE: {self.current_score}')

            if self.current_score['Blue'] == self.grid.choice_count['Blue']:
                 play = False
                 return play 
        print('Player 1 End Turn')
        
        print('PLAYER 2 TURN')
        while p2:
            self.grid.print_click()   #Print new Grid board
            p2 = self.move()
            print(f'SCORE: {self.current_score}')

            if self.current_score['Red'] == self.grid.choice_count['Red']:
                 play = False
                 return play 
        print('Player 2 End Turn')

        play = False
        return play

    def move(self):

        #Look for Input
        
        #self.current_score: Dict[str, int] = {'Red': 0, 'Blue': 0} #Current Score
        move = input("Select a word: ")

        if move == 'Q':
            return False
        elif move in self.grid.c_dict:
            card = self.grid.c_dict[move]
            card.setClick('Y')

            if card._team == 'Red' or card._team == 'Blue':
                self.current_score[card._team] +=1

                if self.current_score[card._team] == self.grid.choice_count[card._team]:
                    print(f'{card._team} WINS!')
 
                    

        else:
            print(f"ERROR: '{move}' NOT FOUND IN BOARD")

        return True

    def score(self):

        #Calculates current score
        #self.choice_limit: Dict[str, int] = {'Red': 8, 'Blue': 7} #Final Score
        self.current_score: Dict[str, int] = {'Red': 0, 'Blue': 0} #Current Score
        
        for team in self.grid.c_dict.values():
            if team._click == 'Y' and (team._team == 'Red' or team._team == 'Blue'):
                self.current_score[team._team] +=1
        
        print(f'SCORE: {self.current_score}')

        # self.choice_count[team] += 1
        # self.c_dict[new_card.getText()] = Card(text, team)

        # if self.choice_limit[team] == self.choice_count[team]:
        #     self.choices.remove(team)
        

test = Game()