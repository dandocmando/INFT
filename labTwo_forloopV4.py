"""
Boring stuff
Author: Dan
Date: 8/3/22
Creates a diamond.
"""


def diamondgenerator():
    line = float(input("Enter an odd integer: \n"))
    if (line % 2) == 0:  # Checks if line is an odd number
        print("Please enter an odd number!")
        diamondgenerator()  # if an odd number is entered the program will restart

    else:

        ast = "*"
        blank = " "
        line = line / 2  # half's the number (however not true division), the way the diamond is created fixes this
        # inaccuracy
        line = int(line)  # turns line from a float into an integer

        for i in range(line):  # first for loop, runs the loop for the val of line

            print(blank * (line - i) + ast + ast * i + ast * i)  # creates the first triangle of the diamond
            if i == line - 1:  # defines the middle point of the diamond, this prints the middle set of *
                print((blank * (line - (i + 1)) + ast + ast * (i + 1) + ast * (i + 1)))  # middle of the diamond

                for x in range(line)[::-1]:  # creates the last triangle, this for loop counts in reverse
                    print(blank * (line - x) + ast + ast * x + ast * x)  # creates the last triangle, completes the
                    # diamond


diamondgenerator()
