"""
Boring stuff
Author: Dan
Date: 3/3/22
"""


def main():
    print("This program will countdown to 0")

    for i in range(5)[::-1]:  # Counts down from 5 to zero
        print(i + 1)

        if i == 0:  # if the loop is finished this will be true
            print("Blast off!")


main()
