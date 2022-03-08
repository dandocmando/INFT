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
       #print(blank*i,ast)


        print(blank*i,ast*i)
        if i == line-1:

            print(ast*i+ast)

            for x in range(line)[::-1]:
                print(ast*x)

genAsterLines(numOfLines)