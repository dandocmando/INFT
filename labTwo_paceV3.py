"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

myName = ""
myDistance = ""
myTime = ""


def main(myName, myDistance, myTime):
    myName = input("Enter your name:\n")
    # print("\n")
    myTime = eval(input("Enter the time you ran for in Minutes: \n"))

    myTimeSeconds = myTime * 60
    myDistance = eval(input("Enter the distance you ran in kilometers: \n"))

    myDistanceMiles = myDistance / 1.61

    print("You ran:", round(myDistanceMiles, 2), "miles")
    print("You ran for", myTimeSeconds, " seconds.")

    myPaceSeconds = myTimeSeconds / myDistanceMiles
    print("Your pace is", round(myPaceSeconds, 2), "seconds per mile, good job", myName, "!")


main(myName, myDistance, myTime)
