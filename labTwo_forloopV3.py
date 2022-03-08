"""
Boring stuff
Author: Dan
Date: 8/3/22
Creates a diamond.
"""


def diamondgenerator():
    line = float(input("Enter an integer: \n"))
    ast = "*"
    blank = " "
    line = line / 2

    for i in range(int(line)):

        print(blank * (int(line) - i) + ast + ast * i + ast * i)
        if i == int(line) - 1:
            print((blank * (int(line) - (i + 1)) + ast + ast * (i + 1) + ast * (i + 1)))

            for x in range(int(line))[::-1]:
                print(blank * (int(line) - x) + ast + ast * x + ast * x)


diamondgenerator()
