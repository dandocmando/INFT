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

    def compChoice(self):
        # print(self.outcomes)
        compChoice = random.choice(self.outcomes)
       # return compChoice


    def playerChoice(self, playerScore):
        print("Guess either: R, P, S")
        choice = input()
        return playerScore


    def playerVComp(self):
        print("nnn")
        # if self.playerGuess == self.compGuess:
        # print("equal")

        print(self.playerGuess)


#playerName = "testinput"

# class initialisation and execution
init_rockPaperScissors = RockPaperScissors("Dan")  # initialises the rockpaperscissors class inputs name
init_rockPaperScissors.introduction()  # executes the introduction def in rock++etc class


