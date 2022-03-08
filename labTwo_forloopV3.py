"""
Boring stuff
Author: Dan
Date: 8/3/22
Creates a diamond.
"""

def genAsterLines():
    line = int(input("Enter an integer: \n"))
    ast = "*"
    blank = " "

    for i in range(line):

        print(blank*(line-i)+ast+ast*i+ast*i)
        if i == line-1:
            print((blank*(line-(i+1))+ast+ast*(i+1)+ast*(i+1)))

            for x in range(line)[::-1]:
                print(blank * (line - x) + ast + ast * x + ast * x)


genAsterLines()
