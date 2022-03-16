"""
Boring stuff
Author: Daniel Ferguson
Date: 10/3/22
Task: INFT1004 Assignment 1 Spending Spree
"""
import time


# build gift card config
def main():
    print("Hello, I am Delilah, your personal gift card management system.")
    username = input("What is your name?\n")  # asks for users name for later use.

    print("Please enter the specifications of your gift card:\n")

    # all inputs are for the gift card specifications.
    gcName = input("Gift card name:")
    gcMaxSpending = int(input("Gift card maximum spending:"))
    gcMaxItems = int(input("Maximum number of items allowed to purchase:"))
    print("\n")

    # prints out the previously input details
    print(
        "These are your gift card details.\n" + "\nGift card name: " + gcName + "\nGift card maximum spending allowed: " + str(
            gcMaxSpending))
    print("Gift card maximum number of items allowed to purchase: " + str(gcMaxItems) + "\n")

    gcItemsLst = []  # creates the initial variable i will be turning into a nested list
    gcCostRunningTotal = []
    retrys = 0

    # repeat until number of uses / $ expended
    for i in range(gcMaxItems):  # iterates loop for the num of times gc can purchase items (specified previously)

        gcItemsLst.append([int(input("cost"))])  # first step of the nested list, asks for item cost

        gcItemsLst[i].append(input("description"))  # nests the item description with item cost
        # print(gcItemsLst[0 + i])

        gcCostRunningTotalFlat = [item for sublist in gcItemsLst for item in sublist]  # uses python list comprehension to
        # flatten list so that the next function can calculate the running cost

        gcCostRunningTotal = sum(filter(lambda i: isinstance(i, int), gcCostRunningTotalFlat))  # takes flattened list
        # and filters out the ints and adds them up so that we can check if the next item will be over the amount

        print(gcCostRunningTotal)
        if gcCostRunningTotal > gcMaxSpending:
            print("too much spending nigga")
            retrys += 1

    print(gcItemsLst)

    print(gcCostRunningTotalFlat)
    print(gcCostRunningTotal)

    # lst = list(map(int, arr.split(' ')))
    # lstLen = len(gcItemsLst)
    # gcCostRunningTotal = [sum(gcItemsLst[0:z:1]) for z in range(0, lstLen + 1)]
    # print(gcCostRunningTotal)

    # print(lst)


# print(sorted(lst))
# print(lst[1][1])

# print organised list of expendeture

# 95% w key

main()
