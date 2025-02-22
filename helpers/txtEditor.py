# ------------------------------------------------------------------------------
# Description:  Helper functions for txt file handling
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2020-09-16
# Execution:    Import functions / collections (from pylek.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import csv
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


def writeToTxt(fname, txtline, writeMode='a'):
    """Writing lines to .txt files
    :param fname: str w/ name of .txt file to write to
    :param txtline: str w/ text content
    :param writeMode: str w/ how to open file ('a', 'w')
    """
    with open(fname, writeMode, newline='\n') as txt:
        txt_writer = csv.writer(txt, delimiter='\t',
                                quotechar='"', quoting=csv.QUOTE_NONE)
        txt_writer.writerow([txtline])
