def main():
    gcItemsLst = []
    gcCostLst = []
    gcMaxItems = 3
    gcMaxSpend = 1000
    tempMax = 0
    tempLoop = 0

    while tempLoop < gcMaxItems:
        cost = int(input("test input"))
        tempMax=tempMax + cost
        print(tempMax)

        if tempMax < gcMaxSpend:

            gcCost = cost
            gcCostLst.append(gcCost)

            gcItems = input("item")
            gcItemsLst.append(gcItems)
            tempLoop=tempLoop+1
            print(tempLoop)
            print(sum(gcCostLst))
        else:
            #tempLoop=tempLoop+1
            print(tempLoop)
            tempMax=sum(gcCostLst)






    for x in range(gcMaxItems):
        #gcCostLst.insert(x + 1, gcItemsLst[x+1])
        print(str(gcCostLst[x])+str(gcItemsLst[x]))

    # print(gcItemsLst)
    #print(gcCostLst)


main()
