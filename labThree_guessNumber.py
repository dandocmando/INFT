"""
Boring stuff
Author: Dan
Date: 3/3/22
"""
import random


def main():
    n = int(input("Please enter a number between one and ten: \n"))
    correctNumber = random.randrange(0, 10)
    print(correctNumber)
    if correctNumber == n:
        print("You guessed the correct number!")
    else:
        print("That isn't the right number!")


main()
