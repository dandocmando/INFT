"""
Boring stuff
Author: Dan
Date: 10/3/22
"""

import random
import time


class RockPaperScissors:
    def __init__(self, playerName):
        self.playerScore = 0
        self.compScore = 0
        self.playerName = playerName
        self.outcomes = ['R', 'P', 'S']

    def introduction(self):
        print("This is a game of rock paper scissors!")
        # time.sleep(0.5)
        print("You will say rock, paper or scissors and the computer will play against you.")
        # time.sleep(0.5)
        print("The inputs are: R = Rock, S = Scissors, P = paper.")
        print("You get five rounds to win.\n")
        # time.sleep(5)

    def comp_vs_user(self):
        print("nnn")

    def comp_choice(self):

        # print(random.choice(list(self.outcomes)))
        return random.choice(list(self.outcomes))

    def user_choice(self):
        enter_legal_choice = False
        while not enter_legal_choice:
            print("Guess either: R, P, S")
            player_choice = input()

            if player_choice not in self.outcomes:
                print("You didn't input R, P or S. Please try again.")

            else:
                enter_legal_choice = True

            comp_choice = self.comp_choice()
            print("test")


# playerName = "testinput"

# class initialisation and execution
init_rockPaperScissors = RockPaperScissors("Dan")  # initialises the rockpaperscissors class inputs name
init_rockPaperScissors.introduction()  # executes the introduction def in rock++etc class
init_rockPaperScissors.comp_choice()
init_rockPaperScissors.user_choice()
