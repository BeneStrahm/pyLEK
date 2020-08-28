# ------------------------------------------------------------------------------
# Description:  Helper functions for matlab
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2020-08-26
# Execution:    Import functions / collections (from helpers.util import func)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------                                                          

import scipy.io

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# DEPRECATED, USE hdf5storage MODULE - LOADMAT
def loadMat(filename):
    """Loading matlab matrices
    :param filename: string with name of .mat file read from
    :rtype mat: list  with content of .mat file
    :rtype keys: list of all keys of .mat file
    """
    # load .mat file
    mat = scipy.io.loadmat(filename)

    # get all keys of .mat file
    keys = []
    for item in mat:
        keys.append(item)

    return mat, keys