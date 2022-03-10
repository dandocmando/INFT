"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

import time
import random

def main():
    print("This is a game of rock paper scissors!")
    time.sleep(0.5)
    print("You will say rock, paper or scissors and the computer will play against you.")
    time.sleep(0.5)
    print("The inputs are: R = Rock, S = Scissors, P = paper.")
    print("You get five rounds to win.\n")
    time.sleep(5)


    player = 0
    com = 0
    options = ['R','S','P']

    for x in range(5):
        print(x)
        print("Scissors!")
        time.sleep(0.5)
        print("Paper!")
        time.sleep(0.5)
        print("Rock!")
        time.sleep(0.5)
        n = input()
        compChoice = random.choice(options)

        if n == random.choice(options):
            print("You won!\n")
            player+=1
            time.sleep(2)
        if n == 'S' and compChoice == ''
        else:
            print("Computer won!\n")
            com+=1
            time.sleep(2)

        if x ==5:
            if player > com:
                print("Well Done, you beat the computer!")
            else:
                print("You lost to the computer!")

def whowins(player):
    # win conditions



    RS = "R"
    RP = "P"

    SP = "S"
    SR = "R"

    PR = "R"
    PS = "S"
    if player == RS:
        print("win")
    print(RS)


main()
whowins()