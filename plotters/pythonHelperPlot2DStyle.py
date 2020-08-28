# ----------------------------------------------------------------------
# Description:  Setting up plot styles for plot2D.py
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from helpers.util import func)
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np                      # only used for testplot
from cycler import cycler
import os

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def retrievePlotStyle(style_dict):
    # Retrieving the current plot settings
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    if bool(style_dict):
        plt.style.use(scriptDir + '/mplstyles/plot2Dtemp.mplstyle')
    else:
        plt.style.use(scriptDir + '/mplstyles/plot2Ddefault.mplstyle')

def modifyPlotStyle(style_dict):
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    # Modify the plot settings
    # mplstyle-format:  key : val # optional comment

    # Read in the file and replace lines by key - values pair
    filedata = []
    with open(scriptDir + '/mplstyles/plot2Ddefault.mplstyle', 'r') as file :
        for line in file:
            skipline = False
            for key, value in style_dict.items():
                if key in line:
                    filedata.append(str(key) + ' : ' + str(value) + '\n')
                    skipline = True
            if skipline == False:
                filedata.append(line)    

    # Write the file out again
    with open(scriptDir + '/mplstyles/plot2Dtemp.mplstyle', 'w') as file:
        for line in filedata:
            file.write(line)

def cleanPlotStyle():
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    # delete temporary mplstyles
    os.remove(scriptDir + '/mplstyles/plot2Dtemp.mplstyle') 


def setLineStyle(colorScheme, variation):
    # Containing n - colors
    colorList = []
    if colorScheme == 'Monochrome':     
        colorList.append('#000000')     # black,            RGB 0,0,0
        colorList.append('#d6d6d6')     # light grey,       RGB 214,214,214 
        colorList.append('#333333')     # dark grey,        RGB 91,91,91 
        colorList.append('#adadad')     # med. light grey,  RGB 173,173,173
    
    elif colorScheme == 'UniS':     
        colorList.append('#323232')     # Anthrazit,        RGB 62,68,76
        colorList.append('#004191')     # Mittelblau,       RGB 0,81,158
        colorList.append('#00BEFF')     # Hellblau,         RGB 0,190,255

    else:
        print("Undefined color Scheme!")

    # Containing m - linestyles
    linestyleList = []
    linestyleList.append('solid')
    linestyleList.append('dashed')
    linestyleList.append('dotted')
    linestyleList.append('dashdot')

    # Creating n * m - styles, 1st varying colors, 2nd varying linestyles
    if variation == 'color':
        customCycler = (cycler(linestyle = linestyleList) * cycler(color = colorList))

    # Creating m * n - styles, 1st varying linestyles, 2nd varying colors
    elif variation == 'linestyle':
        customCycler = (cycler(color = colorList) * cycler(linestyle = linestyleList))

    else:
        print("Undefined color Scheme!")
    
    return customCycler

# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

def testPlot():
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    yy = np.transpose([np.sin(x + phi) for phi in offsets])

    # Test dictionary for parameters
    style_dict = {"lines.linewidth":2.5}

    # Modify plot styles 
    modifyPlotStyle(style_dict)

    # Get the plot styles
    retrievePlotStyle(style_dict)

    # Create color / linestyles
    customCycler = setLineStyle(colorScheme='TUM', variation='color')

    fig, ax = plt.subplots()                # An empty figure with one axe
    ax.set_title('Test Plot')               # Setting the title of the axe-object
    ax.set_prop_cycle(customCycler)         # Setting the cycler
    ax.plot(yy)                             # 2D - Plot of the axe-object    
    
    plt.show()

    # Clean up mplstyles
    cleanPlotStyle()


