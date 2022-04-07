"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

import random


def main():
    lower_bound = int(input("Enter lower bounds: "))
    upper_bound = int(input("Enter upper bounds: "))
    ran_num = random.randint(lower_bound, upper_bound)
    print(ran_num)
    is_correct = False
    while not is_correct:
        num = int(input("Enter a number:"))
        if num == 999:
            is_correct = True
        elif num == ran_num:
            print("YOu guessed the correct number!")
            is_correct = True
        elif num != ran_num:
            print("Your guess was " + str(abs(num - ran_num))+" away from the correct number.")


main()
