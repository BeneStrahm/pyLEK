# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  Handling w/ kwargs
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      07.07.2022
# Execution:    Import functions / collections (from pyLek.helpers import util)
# Status:       Finished
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


def checkFloatKwarg(key: str, kwargs: dict, a=float('-inf'), b=float('inf')):
    """
    Checks if key is in kwargs, is float and optional if a <= val <= b
    :param key: key to search for in kwargs
    :param kwargs: dictionary to search
    :param a: lower bound for float, defaults to float('-inf')
    :param b: upper bound for float, defaults to float('inf')
    :return: value of key in kwargs
    :rtype: float
    """
    if kwargs.get(key) != None:
        val = kwargs.get(key)
        try:
            inp = float(val)
            if b >= inp >= a:
                pass
            else:
                print('Ungültige Angabe für \'' + key +
                      '\', bitte versuchen Sie es noch einmal')
                sys.exit(1)
        except ValueError:
            print('Das ist keine Zahl, bitte versuchen Sie es noch einmal')
            sys.exit(1)
        return inp
