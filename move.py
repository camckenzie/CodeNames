from card import Card
from grid import Grid
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict


class Move:
    

    """This is the player move."""

    def __init__(self, turn: int = 1):
        self.p1_move()
        self.p2_move()

    def p1_move(self, move: str = input()):
        self.move = input("PLAYER 1: Please select a card: ")
        return self.move

    def p2_move(self, move: str = input()):
        self.move = input("PLAYER 2 Please select a card: ")
        return self.move

    def p1_endturn(self):
        self._turn = 2
        return self.turn

    def p2_endturn(self):
        self._turn = 1
        return self.turn

    def checkcard(self, word:str)

        if word

def main():

    #While no team has gotten all their cards
    while(win == 0):

        if turn == 1:

            p1_move()

            p1_endturn()

        else 

            p2_move()
            
            p2_endturn()




