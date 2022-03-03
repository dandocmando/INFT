"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():

    myTimeSeconds = 42*60
    print("This is how many seconds there are in 42 minutes: "+str(myTimeSeconds)+" seconds.")

    kmPerMile = 1.61
    myDistanceMiles = 10/kmPerMile
    print("This is how many miles are there in 10 kilometres: "+str(round(myDistanceMiles, 2))+ " miles.")

    timeInMinutes = 42 #turn 10km in 42 mins
    kmTraveled = 10
    kmph = 10/42*60 #km into one minute
    kmps = kmph/60/60
    #print(kmps)
    print("This is your average pace in kmps: "+str(round(kmps,5)))




main()