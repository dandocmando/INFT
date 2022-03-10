"""
Boring stuff
Author: Dan
Date: 3/3/22
"""
import bisect


def main():
    mark = int(input("Please enter your score as a percentage: \n"))
    marksAvailable = 'FEDCBA'
    score = marksAvailable[bisect.bisect([50, 60, 70, 80, 90], mark)]
    print(score)


main()
