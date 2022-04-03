"""
Boring stuff
Author: Dan
Date: 3/3/22
"""


def main():
    # add stuff
    prodPrices = {}

    done = False
    while not done:
        new_product = input("Enter a new product: ")
        if new_product == "done":
            done = True

        else:
            # new_product = input("Enter a new product: ")
            new_price = input("Enter a new price: ")
            new_product_dict = {new_product: new_price}
            prodPrices.update(new_product_dict)
    for key in prodPrices:
        print(key, ':', prodPrices[key] + " AUD/KG")

    indiv_prices = input("Would you like to check an individual price? (y or n)")
    if indiv_prices == "y":
        indiv_prod = input("enter the exact name of item you would like to check?")
        if indiv_prod in prodPrices:
            print("Price of " + indiv_prod + " is $" + prodPrices[indiv_prod] + " AUD\KG")
        else:
            print("Item doesn't exist")


main()
