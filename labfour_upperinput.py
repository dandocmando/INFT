"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():
    uppercase = 0
    user_in = input()
    for x in range(len(user_in)):
        if user_in[x] == user_in[x].upper():
            uppercase = 1

    if uppercase == 1:
        print("has uppercase")
    else:
        print("no uppercase")






main()