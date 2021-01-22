# ----------------------------------------------------------------------
# Description:  Retrieving, modifying and cleaning default.mplStyle
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from helpers import util)
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------

import matplotlib.pyplot as plt
import os

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def retrievePlotStyle(style_dict, mpl):
    # Retrieving the current plot settings
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    if bool(style_dict):
        plt.style.use(scriptDir + '/' + mpl + '_temp.mplstyle')
    else:
        plt.style.use(scriptDir + '/' + mpl + '.mplstyle')


def modifyPlotStyle(style_dict, mpl):
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    # Modify the plot settings
    # mplstyle-format:  key : val # optional comment

    # Read in the file and replace lines by key - values pair
    filedata = []
    with open(scriptDir + '/' + mpl + '.mplstyle', 'r') as file:
        for line in file:
            skipline = False
            for key, value in style_dict.items():
                # key + ":" is necessary, otherwise eg. lines.marker and lines.markerfacecolor
                # are both replaced when only lines.marker should be modified
                if (key+":") in line:
                    filedata.append(str(key) + ' : ' + str(value) + '\n')
                    skipline = True
            if skipline == False:
                filedata.append(line)

    # Write the file out again
    with open(scriptDir + '/' + mpl + '_temp.mplstyle', 'w') as file:
        for line in filedata:
            file.write(line)


def cleanPlotStyle(mpl):
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    # delete temporary mplstyles
    os.remove(scriptDir + '/' + mpl + '_temp.mplstyle')
