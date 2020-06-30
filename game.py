from card import Card
from grid import Grid
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict

#TODO: Figure out how to end the game
#Figure out win conditions


class Game:


    def __init__(self):  
        self.grid = Grid()
        
        play = True
        while play:
            self.play_game(play) #Player turn
        


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
        else:
            print(f"ERROR: '{move}' NOT FOUND IN BOARD")

        return True
