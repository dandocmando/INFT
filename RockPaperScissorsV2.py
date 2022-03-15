"""
Boring stuff
Author: Dan
Date: 10/3/22
"""

import random
import time


class rockPaperScissors():
    def __init__(self, playerScore, compScore, playerName, outcomes=['R', 'P', 'S']):
        rockPaperScissors.playerScore = playerScore
        rockPaperScissors.compScore = compScore
        rockPaperScissors.playerName = playerName
        rockPaperScissors.outcomes = outcomes

    def introduction(self):
        print("This is a game of rock paper scissors!")
        #time.sleep(0.5)
        print("You will say rock, paper or scissors and the computer will play against you.")
        #time.sleep(0.5)
        print("The inputs are: R = Rock, S = Scissors, P = paper.")
        print("You get five rounds to win.\n")
        #time.sleep(5)


class computer():
    def __init__(self):
        self.outcomes = rockPaperScissors.outcomes
        #self.player = rockPaperScissors.playerName


    def compChoice(self):
        # print(self.outcomes)
        compChoice = random.choice(self.outcomes)
        print(compChoice)

class player():
    def __init__(self):
        self.player = rockPaperScissors.playerName
        self.playerScore = rockPaperScissors.playerScore

    def playerChoice(self):
        print("Guess either: R, P, S")
        plChoice = input()



playerName = "testinput"

# class initialisation and execution
init_rockPaperScissors = rockPaperScissors(0, 0, playerName)  # initialises the rockpaperscissors class inputs name
init_rockPaperScissors.introduction()  # executes the introduction def in rock++etc class

compObject = computer()  # initialises the computer class as compObject
compObject.compChoice()  # executes the compChoice def in computer class

initPlayer = player()
initPlayer.playerChoice()

