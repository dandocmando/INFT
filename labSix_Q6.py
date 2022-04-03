"""
Boring stuff
Author: Dan
Date: 3/3/22
"""


def main():
    fileObh = open('ChambersDefinitions.txt', "r")
    words = fileObh.read().splitlines()
    fileObh.close()

    zip_switch = iter(words)
    stripped_dict = dict((a[0], b) for a, b in zip(zip_switch, zip_switch))
    print(stripped_dict)





# def_dict = {k: row[0] for row in words for k in row[1:]}
# print(def_dict)


main()
