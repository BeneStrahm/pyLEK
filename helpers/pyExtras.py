# ------------------------------------------------------------------------------
# Description:  Helper functions in python
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2020-08-26
# Execution:    Import functions / collections (from pylek.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

def getKeyList(dict: dict):
    """Get keys of a dictionary
    :param dict: Dictonary to read from
    :rtype keys: List of keys in the dictionary
    """
    return dict.keys()


def getValueList(dict: dict):
    """Get values of a dictionary
    :param dict: Dictonary to read from
    :rtype values: List of values in the dictionary
    """
    return dict.values()


def getKeyValueList(dict: dict):
    """Get keys and values of a dictionary
    :param dict: Dictonary to read from
    :rtype keys: List of keys in the dictionary
    :rtype values: List of values in the dictionary
    """
    return dict.keys(), dict.values()
