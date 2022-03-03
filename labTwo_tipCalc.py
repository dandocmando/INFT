"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():

    mealCost = int(input("How much did your meal cost?\n"))
    tipinPerc = int(input("What would you like to tip? (in %)\n"))/100
    tipCost = mealCost*tipinPerc
    totalCost = mealCost+tipCost
    print("The tip for this meal will cost: $"+str(tipCost))
    print("The meal will cost: $"+str(totalCost))





main()