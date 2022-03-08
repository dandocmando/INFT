"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():

    myName = input("Enter your name:\n")
    print("Hi", myName, "!")
    myTime = eval(input("Enter the time you ran for in Minutes:\n"))
    myTimeSeconds =myTime*60
    print("You ran for", myTimeSeconds, " seconds.")
    myDistance = eval(input("Enter the distance you ran in kilometers\n"))
    myDistanceMiles = myDistance/1.61
    print("You ran:", round(myDistanceMiles, 2), "miles")
    myPaceSeconds = myTimeSeconds /myDistanceMiles
    print("Your pace is", myPaceSeconds, "seconds per mile, good job", myName,"!")







main()