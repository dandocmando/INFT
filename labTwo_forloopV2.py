"""
Boring stuff
Author: Dan
Date: 3/3/22
"""
numOfLines = ""


def genAsterLines(numOfLines):
    line = int(input("Enter an integer (0~10): \n"))
    ast = "*"
    blank = " "


    for i in range(line):
        # print(blank*i,ast)

        print(blank*(line-i)+ast+ast*i+ast*i)
        if i == line-1:
            print((ast*i)*2+ast*(i-1))

            for x in range(line)[::-1]:
                print(blank * (line - x) + ast + ast * x + ast * x)



genAsterLines(numOfLines)
