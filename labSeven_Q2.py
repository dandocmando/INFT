import numpy as np
import pandas as pd


def editCSV():
    df = pd.read_csv('someNumbers.csv', header=None)  # reads someNumbers.csv into df var

    data_frame = pd.DataFrame(df)  # creates a panda dataframe with the contents of the someNumbers.csv file
    lst = data_frame.to_numpy().flatten()  # creates a  flattened list in numpty from the panda dataframe
    array = np.array(lst).reshape(5, 4)  # creates a numpty array from the list and reshapes it to 5 high 4 deep

    # noinspection PyTypeChecker
    pd.DataFrame(array).to_csv('rearrangedArray.csv', index=None, header=None)  # exports the array into a dataframe then csv

    print(array)


editCSV()
