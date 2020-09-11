# ----------------------------------------------------------------------
# Description:  Retrieving, modifying and cleaning default.mplStyle
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from helpers.util import func)
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------

import matplotlib.pyplot as plt
import os

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def retrievePlotStyle(style_dict):
    # Retrieving the current plot settings
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    if bool(style_dict):
        plt.style.use(scriptDir + '/temp.mplstyle')
    else:
        plt.style.use(scriptDir + '/default.mplstyle')

def modifyPlotStyle(style_dict):
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    # Modify the plot settings
    # mplstyle-format:  key : val # optional comment

    # Read in the file and replace lines by key - values pair
    filedata = []
    with open(scriptDir + '/default.mplstyle', 'r') as file :
        for line in file:
            skipline = False
            for key, value in style_dict.items():
                if key in line:
                    filedata.append(str(key) + ' : ' + str(value) + '\n')
                    skipline = True
            if skipline == False:
                filedata.append(line)    

    # Write the file out again
    with open(scriptDir + '/temp.mplstyle', 'w') as file:
        for line in filedata:
            file.write(line)

def cleanPlotStyle():
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    # delete temporary mplstyles
    os.remove(scriptDir + '/temp.mplstyle') 