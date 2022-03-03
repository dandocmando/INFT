"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():
    username = input("Enter your name please:\n")
    firstNum = int(input("Please enter the first number:\n"))
    secNum = int(input("Please enter the second number:\n"))

    numTotal = firstNum+secNum
    print("The total of the two numbers is ", str(numTotal))

    numAvg = (firstNum+secNum)/2
    print("The average of the two numbers is", str(numAvg))




main()