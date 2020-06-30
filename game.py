from card import Card
from grid import Grid
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict


class Game:


    def __init__(self):  
        self.grid = Grid()
        self.play_game() #Player turn
        


        #play game function - Loops

    def play_game(self):

        again = 'True'

        while again:
            self.grid.print_click()   #Print new Grid board
            again = self.move()
        
        print('End Turn')

    def move(self):

        #Look for Input
        
        move = input("Player Input Word: ")

        if move == 'Q':
            return False
        elif move in self.grid.c_dict:
            card = self.grid.c_dict[move]
            card.setClick('Y')
        else:
            print(f"ERROR: '{move}' NOT FOUND IN BOARD")

        return True

    #TODO: Set up the player inputs and loop them
    #Figure out how often and when we should be printing the grid (maybe a loop?)
    

        



    # """This is the player move."""

    # def __init__(self, turn: int = 1):
    #     self.p1_move()
    #     #self.p2_move()

    # def p1_move(self, move: str = input()):
    #     self.move = input("PLAYER 1: Please select a card: ")
    #     if self.move == 
    #     return self.move

#     def p2_move(self, move: str = input()):
#         self.move = input("PLAYER 2 Please select a card: ")
#         return self.move

#     def p1_endturn(self):
#         self._turn = 2
#         return self.turn

#     def p2_endturn(self):
#         self._turn = 1
#         return self.turn

#     def checkcard(self, word:str)

#         if word

# def main():

#     #While no team has gotten all their cards
#     while(win == 0):

#         if turn == 1:

#             p1_move()

#             p1_endturn()

#         else 

#             p2_move()
            
#             p2_endturn()



test = Game()
