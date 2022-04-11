import numpy as np


def sortedArray():
    number_lines = [line.strip() for line in open('../INFT_Assess2/someNumbers.csv')]
    numbers_L = [line.split(',') for line in number_lines]
    xSeries = np.arange(1, 11)
    ySeries1 = []
    ySeries2 = []
    for n in numbers_L[0]:
        ySeries1.append(float(n))
    for n in numbers_L[1]:
        ySeries2.append(float(n))

    ySeries1 = np.sort(ySeries1, axis=None)
    ySeries2 = np.sort(ySeries2, axis=None)


sortedArray()
