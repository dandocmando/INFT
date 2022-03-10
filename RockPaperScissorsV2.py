"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

import random
import time


class rockPaperScissors():
    def __init__(self, playerScore, compScore, playerName, outcomes=['R', 'P', 'S']):
        rockPaperScissors.playerScore = playerScore
        rockPaperScissors.compScore = compScore
        rockPaperScissors.playerName = playerName
        rockPaperScissors.outcomes = outcomes


class computer():
    def __init__(self):
        self.outcomes = rockPaperScissors.outcomes
        self.player = rockPaperScissors.playerName

    def compChoice(self):
        print(self.outcomes)
        compChoice = random.choice(self.outcomes)
        print(compChoice)


playerName = "testinput"
initialise_rockPaperScissors = rockPaperScissors(0, 0, playerName)
compObject = computer()
compObject.compChoice()
