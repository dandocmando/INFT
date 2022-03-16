"""
Boring stuff
Author: Daniel Ferguson
Date: 10/3/22
Task: INFT1004 Assignment 1: Spending Spree
This is version 3, previous versions weren't compact enough.
"""

def main():

    gcItemsLst = []  # init variables
    gcCostLst = []
    gcMaxItems = 3
    gcMaxSpend = 1000
    tempMax = 0
    tempLoop = 0

    while tempLoop < gcMaxItems:
        cost = int(input("gc item cost"))
        tempMax=tempMax + cost
        #print(tempMax)

        if tempMax < gcMaxSpend:
            gcCost = cost
            gcCostLst.append(gcCost)

            gcItems = input("item")
            gcItemsLst.append(gcItems)
            tempLoop=tempLoop+1
            #print(tempLoop)
            #print(sum(gcCostLst))

        else:
            print("The gift card doesn't have enough funds to process this purchase, please try again.")
            print(tempLoop)
            tempMax=sum(gcCostLst)
            #print(tempMax)

        print("Gift card used so far: $"+str(tempMax)+" out of $"+str(gcMaxSpend))




    #gcCombinedLst = [item for sublist in zip(gcCostLst, gcItemsLst) for item in sublist]  # uses list comprehension to create a zip object, combines the list in sequential order.
    gclisttest = [list(t) for t in zip(gcCostLst, gcItemsLst)]  # nests Cost and Items into sublists so that Cost can be manipulated using sorted function
    gclistSorted = sorted(gclisttest, key=lambda x: x[0], reverse=True)  # uses sorted to sort list based on cost



    #print(gcCombinedLst)
    print(gclistSorted)

    for x in range(gcMaxItems):  # deprecated
        print("Cost: $"+str(gclistSorted[x][0])+", item description: "+str(gclistSorted[x][1]))
    gcNumItemPurchased = len(gclistSorted)
    print(gcNumItemPurchased)




main()
