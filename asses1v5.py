"""
Boring stuff
Author: Daniel Ferguson
Date: 10/3/22
Task: INFT1004 Assignment 1: Spending Spree
This is version 4.
Only used one class to pass variables :)
"""
import sys


class SpendingSpree:
    def __init__(self):
        self.gc_items_lst = []  # init variables in init so that other defs can use them
        self.gc_cost_lst = []
        self.temp_max = 0
        self.loop_count = 0
        self.gc_name = ""
        self.gc_max_spend = 0
        self.gc_max_items = 0
        self.username = ""

    def intro(self):
        print("Hello, I am Delilah, your personal gift card management system.")
        self.username = input("What is your name?\n")  # asks for users name for later use.
        print("Please enter the specifications of your gift card:\n")

        # all inputs are for the gift card specifications.
        gc_name = input("Gift card name:")
        gc_max_spend = int(input("Gift card maximum spending:"))
        gc_max_items = int(input("Maximum number of items allowed to purchase:"))
        self.gc_name = gc_name  # sends local values back to init to they can be used by other defs
        self.gc_max_items = gc_max_items
        self.gc_max_spend = gc_max_spend

        print("\n")
        # prints out the previously input details
        print("These are your gift card details:\n" + "\nGift card name: " + gc_name)
        print("Gift card maximum spending allowed: " + str(gc_max_spend))
        print("Gift card maximum number of items allowed to purchase: " + str(gc_max_items) + "\n")

    def loop(self):
        temp_max = self.temp_max  # pulls variable values from Rock init def
        gc_max_items = self.gc_max_items
        gc_max_spend = self.gc_max_spend
        gc_cost_lst = self.gc_cost_lst
        gc_items_lst = self.gc_items_lst
        loop_count = self.loop_count

        # loop will repeat until loop_count is greater than gc_max_items or temp_max is higher than gc_max_spend
        while loop_count < gc_max_items and temp_max < gc_max_spend:
            cost = int(input("Purchase price: "))  # takes user input into cost variable
            temp_max = temp_max + cost  # stores the temporary total cost

            if temp_max <= gc_max_spend:  # checks if temp max is lower or equal to max spend
                gc_cost = cost  # assigns gc_cost the value of cost
                gc_cost_lst.append(gc_cost)  # appends gc_cost value into gc_cost_lst

                gc_items_desc = input("Purchase description: ")  # takes user input for item description
                gc_items_lst.append(gc_items_desc)  # appends input desc into items lst
                loop_count = loop_count + 1  # increments loop count

            else:
                print("The gift card doesn't have enough funds to process this purchase, please try again.\n")

                # resets temp_max back to the last accepted spending amount by adding the current total of gc_cost_lst
                temp_max = sum(gc_cost_lst)

            print("\nGift card used so far: $" + str(temp_max) + " out of $" + str(gc_max_spend) + "\n")
            self.loop_count = loop_count  # loop is modified after assignment so self.loop needs to be updated

    def list(self):
        # brings def init variables into the list variables
        gc_cost_lst = self.gc_cost_lst
        gc_items_lst = self.gc_items_lst
        loop_count = self.loop_count
        gc_name = self.gc_name
        gc_max_spend = self.gc_max_spend
        username = self.username

        # nests Cost and Items into sublists so that Cost can be manipulated using sorted function
        gc_list_nested = [list(t) for t in zip(gc_cost_lst, gc_items_lst)]
        # uses nested list to sort nested items based on cost
        gc_list_sorted = sorted(gc_list_nested, key=lambda l: l[0], reverse=True)

        print("Gift card completely used!\n")
        for x in range(loop_count):  # prints the list of transactions ordered highest cost to lowest :)
            print("Cost: $" + str(gc_list_sorted[x][0]) + ", item description: " + str(gc_list_sorted[x][1]))

        gc_num_item_purchased = len(gc_list_sorted)  # counts number of nested list items for average computation
        gc_average_cost = sum(gc_cost_lst) / gc_num_item_purchased  # average cost with sum of lst / num of purchases

        print("\nGift card used: " + str(gc_name) + ", spending limit: " + str(gc_max_spend))
        print("The number of items purchased was: " + str(gc_num_item_purchased))
        print("The average cost was: " + str(round(gc_average_cost, 2)) + "\n")

        print(username + ", would you like to try another card or exit the program?")
        retry = input("Enter R to retry, enter E to exit the program: ")
        if retry == "R":
            print("\n")
            game_ob_nest = SpendingSpree()  # creates object based on spendingspree class
            game_ob_nest.intro()  # runs the required defs inside object
            game_ob_nest.loop()
            game_ob_nest.list()

        elif retry == "E":
            print("Have a nice day!")
            sys.exit()

        else:
            print("You failed to correctly enter a choice so I decided to exit the program for you.")
            sys.exit()


game_ob = SpendingSpree()
game_ob.intro()
game_ob.loop()
game_ob.list()
