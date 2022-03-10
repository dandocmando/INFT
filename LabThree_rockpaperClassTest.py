"""
Boring stuff
Author: Dan
Date: 3/3/22
"""
import time
import random


class rockPaperScissors(object):

    def __init__(self, playerScore, compScore, playerName, outcomes=["R", "P", "S"]):
        rockPaperScissors.playerScore = playerScore
        rockPaperScissors.compScore = compScore
        rockPaperScissors.playerName = playerName
        self.outcomes = outcomes

    def introduction(self):
        print("Hello " + self.playerName)
        print("This is a game of rock paper scissors!")
        # time.sleep(0.5)
        print("You will say rock, paper or scissors and the computer will play against you.")
        # time.sleep(0.5)
        print("The inputs are: R = Rock, S = Scissors, P = paper.")
        print("You get five rounds to win.\n")
        # time.sleep(5)


class computer(object):
    def compChoice(self, compChoice):
        compChoice.outcomes = compChoice
        print(compChoice)


playerName = input("enter name\n")

objectTest = rockPaperScissors(0, 0, playerName)
comp = computer(objectTest)



