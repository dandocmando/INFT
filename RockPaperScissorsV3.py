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
        # time.sleep(0.5)
        print("You will say rock, paper or scissors and the computer will play against you.")
        # time.sleep(0.5)
        print("The inputs are: R = Rock, S = Scissors, P = paper.")
        print("You get five rounds to win.\n")
        # time.sleep(5)


class computer(rockPaperScissors):
    def __init__(self):
        self.outcomes = rockPaperScissors.outcomes
        self.player = rockPaperScissors.playerName

    def compChoice(self):
        # print(self.outcomes)
        compChoice = random.choice(self.outcomes)
       # return compChoice


class player(rockPaperScissors):
    def __init__(self, compScore, playerScore):

        rockPaperScissors.__init__(self, compScore, playerScore)



    def playerChoice(self, playerScore):
        print("Guess either: R, P, S")
        choice = input()
        return playerScore


class WinLose(rockPaperScissors):
    def __init__(self):
        self.playerGuess = player.playerChoice
        compGuess = computer.compChoice

    def __str__(self):
        print("test")
        return self.playerGuess

    def playerVComp(self):
        print("nnn")
        # if self.playerGuess == self.compGuess:
        # print("equal")

        print(self.playerGuess)


playerName = "testinput"

# class initialisation and execution
init_rockPaperScissors = rockPaperScissors(0, 0, playerName)  # initialises the rockpaperscissors class inputs name
init_rockPaperScissors.introduction()  # executes the introduction def in rock++etc class

compObject = computer()  # initialises the computer class as compObject
compObject.compChoice()  # executes the compChoice def in computer class

initPlayer = player()
initPlayer.playerChoice()

init_winlose = WinLose()
init_winlose.playerVComp()
