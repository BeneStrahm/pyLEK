# ------------------------------------------------------------------------------
# Description:  Helper functions for csv file handling
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2020-09-16
# Execution:    Import functions / collections (from pylek.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import pandas as pd
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


def writeToCsv(fname, array, writeMode='a'):
    """Writing lines to .txt files
    :param fname: str w/ name of .txt file to write to
    :param array: list/np.array w/ text content
    :param writeMode: str w/ how to open file ('a', 'w')
    """
    pd.DataFrame(array).to_csv(fname, mode=writeMode,
                               index=False, sep='\t', decimal=',')
