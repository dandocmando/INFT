"""
Boring stuff
Author: Dan
Date: 31/3/22
Functionality complete
"""

import random
import time


class RockPaperScissors:
    def __init__(self, playerName):
        self.player_choice = None
        self.playerScore = 0
        self.compScore = 0
        self.playerName = playerName
        self.outcomes = ['R', 'P', 'S']

    def introduction(self):
        print("This is a game of rock paper scissors!")
        time.sleep(0.5)
        print("You will say rock, paper or scissors and the computer will play against you.")
        time.sleep(0.5)
        print("The inputs are: R = Rock, S = Scissors, P = paper.")
        print("You get five rounds to win.\n")
        time.sleep(2)

    def comp_choice(self):
        return random.choice(list(self.outcomes))

    def user_choice(self):
        enter_legal_choice = False
        while not enter_legal_choice:
            print("Guess either: R, P, S")
            self.player_choice = input()

            if self.player_choice not in self.outcomes:
                print("You didn't input R, P or S. Please try again.")

            else:
                enter_legal_choice = True

    def main_game(self):

        for i in range(5):
            print("This is round: "+str(i+1)+" out of 5.")
            comp_choice = self.comp_choice()
            #print("comp: " + comp_choice)  # used for debugging
            self.user_choice()
            if comp_choice == self.player_choice:
                print("Its a draw! Both you and the computer guessed the same answer.")

            elif self.player_choice == "R" and comp_choice == "P":
                print("Computer wins! You chose: " + self.player_choice + " computer chose: " + comp_choice)
                self.compScore += 1

            elif self.player_choice == "R" and comp_choice == "S":
                print("You win! You chose: " + self.player_choice + " computer chose: " + comp_choice)
                self.playerScore += 1

            elif self.player_choice == "P" and comp_choice == "R":
                print("You win! You chose: " + self.player_choice + " computer chose: " + comp_choice)
                self.playerScore += 1

            elif self.player_choice == "P" and comp_choice == "S":
                print("Computer wins! You chose: " + self.player_choice + " computer chose: " + comp_choice)
                self.compScore += 1

            elif self.player_choice == "S" and comp_choice == "R":
                print("Computer wins! You chose: " + self.player_choice + " computer chose: " + comp_choice)
                self.compScore += 1

            elif self.player_choice == "S" and comp_choice == "P":
                print("You win! You chose: " + self.player_choice + " computer chose: " + comp_choice)
                self.playerScore += 1

        if self.playerScore > self.compScore:
            print(str(self.playerName)+" wins by "+str(self.playerScore-self.compScore)+" points!")

        elif self.compScore > self.playerScore:
            print("Computer wins by"+str(self.compScore-self.playerScore)+" points!")

        elif self.playerScore == self.compScore:
            print("Its a tie!")

        else:
            print("Nobody won go away loser!")


# class initialisation and execution
init_rockPaperScissors = RockPaperScissors("Dan")  # initialises the rockpaperscissors class inputs name
init_rockPaperScissors.introduction()  # executes the introduction def in rock++etc class
init_rockPaperScissors.main_game()  # starts the main game
