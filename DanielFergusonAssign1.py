"""
Boring stuff
Author: Daniel Ferguson
Auth ID: 3374690
Date: Start -> 09/3/22 Upload -> 31/3/22
Task: INFT1004 Assignment 1: Spending Spree
This is version 5, if you would like to view previous versions I can supply them.
You DO NOT need to write defs into the console, just run the entire program.
Only used one class to pass variables :)
"""
import sys
import time


class SpendingSpree:
    def __init__(self):  # def init is a special def, it's always run on class initiation
        self.gc_items_lst = []  # init variables so that other defs can use them
        self.gc_cost_lst = []
        self.temp_max = 0
        self.loop_count = 0
        self.gc_name = ""
        self.gc_max_spend = 0
        self.gc_max_items = 0
        self.username = ""
        self.default_time = 0.3

    def intro(self):
        print("Hello, I am Delilah, your personal gift card management system.")
        time.sleep(self.default_time)
        self.username = input("What is your name?\n")  # asks for users name for later use.
        print("Please enter the specifications of your gift card:\n")

        # all inputs are for the gift card specifications.
        gc_name = input("Gift card name:")
        gc_max_spend = float(input("Gift card maximum spending:"))
        gc_max_items = int(input("Maximum number of items allowed to purchase:"))
        self.gc_name = gc_name  # sends local values back to init to they can be used by other defs
        self.gc_max_items = gc_max_items  # not technically necessary, could just assign above values .self
        self.gc_max_spend = gc_max_spend  # this shows the movement of var data better, so I have left it.

        print("\n")
        # prints out the previously input details
        time.sleep(self.default_time)
        print("These are your gift card details:\n" + "\nGift card name: " + gc_name)
        time.sleep(self.default_time)
        print("Gift card maximum spending allowed: " + str(gc_max_spend))
        time.sleep(self.default_time)
        print("Gift card maximum number of items allowed to purchase: " + str(gc_max_items) + "\n")

    def loop(self):
        temp_max = self.temp_max  # pulls variable values from init def
        gc_max_items = self.gc_max_items
        gc_max_spend = self.gc_max_spend
        gc_cost_lst = self.gc_cost_lst
        gc_items_lst = self.gc_items_lst
        loop_count = self.loop_count
        # no str into int input exception handling has been implemented, as isn't mentioned in marking guidelines.
        # loop will repeat until loop_count is greater than gc_max_items or temp_max is higher than gc_max_spend
        while loop_count < gc_max_items and temp_max < gc_max_spend:
            cost = float(input("Purchase price: "))  # takes user input into cost variable
            temp_max = temp_max + cost  # stores the temporary total cost

            if temp_max <= gc_max_spend:  # checks if temp max is lower or equal to max spend
                gc_cost = cost  # assigns gc_cost the value of cost
                gc_cost_lst.append(gc_cost)  # appends gc_cost value into gc_cost_lst

                gc_items_desc = input("Purchase description: ")  # takes user input for item description
                gc_items_lst.append(gc_items_desc)  # appends input desc into items lst
                loop_count = loop_count + 1  # increments loop count

            else:
                time.sleep(self.default_time)
                print("The gift card doesn't have enough funds to process this purchase, please try again.\n")

                # resets temp_max back to the last accepted spending amount by settings its value to gc_cost_lst
                temp_max = sum(gc_cost_lst)

            time.sleep(self.default_time)
            print("\nGift card used so far: $" + str(temp_max) + " out of $" + str(gc_max_spend) + "\n")
            self.loop_count = loop_count  # loop is modified after assignment so self.loop needs to be updated

    def list(self):
        gc_cost_lst = self.gc_cost_lst  # serves same purpose as previous def :)
        gc_items_lst = self.gc_items_lst
        loop_count = self.loop_count
        gc_name = self.gc_name
        gc_max_spend = self.gc_max_spend
        username = self.username

        # nests Cost and Items into sublists so that Cost var can be manipulated using sorted function
        # use prints on the below lists after manipulation to gain greater understanding of what is happening :)
        gc_list_nested = [list(t) for t in zip(gc_cost_lst, gc_items_lst)]
        # uses nested list to sort nested items based on cost, because desc is nested it follows cost movement
        gc_list_sorted = sorted(gc_list_nested, key=lambda l: l[0], reverse=True)

        print("Gift card expended, your purchases are listed below, they are ordered from most to least expensive.\n")
        for x in range(loop_count):  # prints the list of transactions ordered highest cost to lowest :)
            print("Cost: $" + str(gc_list_sorted[x][0]) + ", item description: " + str(gc_list_sorted[x][1]))
            time.sleep(self.default_time)  # exceeds requirement to print most expensive item.

        gc_num_item_purchased = len(gc_list_sorted)  # counts number of nested list items for average computation
        gc_average_cost = sum(gc_cost_lst) / gc_num_item_purchased  # average cost with sum of lst / num of purchases

        time.sleep(self.default_time)
        print("\nGift card used: " + str(gc_name) + ", spending limit: $" + str(gc_max_spend))
        time.sleep(self.default_time)
        print("The number of items purchased was: " + str(gc_num_item_purchased))
        time.sleep(self.default_time)
        print("The average cost was: $" + str(round(gc_average_cost, 2)) + "\n")  # rounds avg cost -> 2 dec places
        time.sleep(self.default_time)
        print(username + ", would you like to try another card or exit the program?")
        time.sleep(self.default_time)
        retry = input("Enter R to retry, enter E to exit the program: ")

        if retry == "R":
            print("\n")
            spending_spree_ob_nest = SpendingSpree()  # creates object based on spendingspree class
            spending_spree_ob_nest.intro()  # runs the required defs inside object
            spending_spree_ob_nest.loop()
            spending_spree_ob_nest.list()

        elif retry == "E":
            print("Have a nice day!")
            sys.exit()  # ends the .py

        else:
            print("You failed to correctly enter a choice so I decided to exit the program for you :)")
            sys.exit()


spending_Spree_ob = SpendingSpree()
spending_Spree_ob.intro()
spending_Spree_ob.loop()
spending_Spree_ob.list()
