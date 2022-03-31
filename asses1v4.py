"""
Boring stuff
Author: Daniel Ferguson
Date: 10/3/22
Task: INFT1004 Assignment 1: Spending Spree
This is version 4, combination of methods used in v2 and v3, prior to v5 introduction of classes.
First fully functioning version.
"""
import sys


def main():
    print("Hello, I am Delilah, your personal gift card management system.")
    username = input("What is your name?\n")  # asks for users name for later use.

    print("Please enter the specifications of your gift card:\n")

    # all inputs are for the gift card specifications.
    gc_name = input("Gift card name:")
    gc_max_spend = int(input("Gift card maximum spending:"))
    gc_max_items = int(input("Maximum number of items allowed to purchase:"))
    print("\n")

    # prints out the previously input details
    print("These are your gift card details:\n" + "\nGift card name: " + gc_name)
    print("Gift card maximum spending allowed: " + str(gc_max_spend))
    print("Gift card maximum number of items allowed to purchase: " + str(gc_max_items) + "\n")

    gc_items_lst = []  # init variables
    gc_cost_lst = []
    # gc_max_items = 3  # used for testing
    # gc_max_spend = 1000  # used for testing
    temp_max = 0
    loop_count = 0

    # loop will repeat until loop_count is greater than gc_max_items or temp_max is higher than gc_max_spend
    while loop_count < gc_max_items and temp_max < gc_max_spend:
        cost = int(input("Purchase price: "))  # takes user input into cost variable
        temp_max = temp_max + cost  # stores the temporary total cost

        if temp_max <= gc_max_spend:  # checks if temp max is lower or equal to max spend
            gc_cost = cost  # assigns gc_cost the value of cost
            gc_cost_lst.append(gc_cost)  # appends gc_cost value into gc_cost_lst

            gc_items_desc = input("Purchase description: ")  # takes user input for item description
            gc_items_lst.append(gc_items_desc)
            loop_count = loop_count + 1

        else:
            print("The gift card doesn't have enough funds to process this purchase, please try again.\n")

            # resets temp_max back to the last accepted spending amount by adding the current total of gc_cost_lst
            temp_max = sum(gc_cost_lst)

        print("\nGift card used so far: $" + str(temp_max) + " out of $" + str(gc_max_spend) + "\n")

    # nests Cost and Items into sublists so that Cost can be manipulated using sorted function
    gc_list_nested = [list(t) for t in zip(gc_cost_lst, gc_items_lst)]
    gc_list_sorted = sorted(gc_list_nested, key=lambda l: l[0], reverse=True)  # uses sorted to sort list based on cost

    print("Gift card completely used!\n")

    for x in range(loop_count):  # prints the list of transactions ordered highest cost to lowest :)
        print("Cost: $" + str(gc_list_sorted[x][0]) + ", item description: " + str(gc_list_sorted[x][1]))

    gc_num_item_purchased = len(gc_list_sorted)
    gc_average_cost = sum(gc_cost_lst) / gc_num_item_purchased

    # print(round(gc_average_cost, 2))
    # print(gc_num_item_purchased)
    print("\nGift card used: "+str(gc_name)+", spending limit: "+str(gc_max_spend))
    print("The number of items purchased was: " + str(gc_num_item_purchased))
    print("The average cost was: " + str(round(gc_average_cost, 2))+"\n")

    print("Would you like to try another card or exit the program?")
    retry = input("Enter R to retry, enter E to exit the program: ")
    if retry == "R":
        print("\n")
        main()

    elif retry == "E":
        print("Have a nice day!")
        sys.exit()

    else:
        print("You failed to correctly enter a choice so I decided to exit the program for you.")
        sys.exit()


main()
