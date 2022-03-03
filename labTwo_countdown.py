"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():

    bla = int(input("What number would you like to countdown from?\n"))
    x = bla

    for i in range(bla)[::-1]:

        while x > 0:
            print(x)

        if i == 1:
            print("Blast off!")
        x=x-1






main()