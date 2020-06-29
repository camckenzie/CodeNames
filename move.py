from card import Card
from grid import Grid
from random import randint, choice
from word import words
from prettytable import PrettyTable
from typing import Dict


class Move:
    

    """This is the player move."""

    def __init__(self):
        self.p1_move()
        self.p2_move()

    def p1_move(self, move: str = input()):
        self.move = input("PLAYER 1: Please select a card: ")
        return self.move

    def p2_move(self, move: str = input()):
        self.move = input("PLAYER 2 Please select a card: ")
        return self.move


