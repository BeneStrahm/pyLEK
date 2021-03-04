# ----------------------------------------------------------------------
# Description:  Setting up a color cycler
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from helpers import util)
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------

from cycler import cycler

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def createCycler(colorScheme, variation):
    # Containing n - colors
    colorList = []
    if colorScheme == 'Monochrome':
        colorList.append('#000000')     # black,            RGB 0,0,0
        colorList.append('#d6d6d6')     # light grey,       RGB 214,214,214
        colorList.append('#838383')     # dark grey,        RGB 131,131,131
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

    # Containing o - markers
    markerList = []
    markerList.append('1')
    markerList.append('x')
    markerList.append('v')
    markerList.append('+')

    # Creating n * m - styles, 1st varying colors, 2nd varying linestyles
    if variation == 'color':
        customCycler = cycler(linestyle=linestyleList) * \
            cycler(color=colorList)

    # Creating m * n - styles, 1st varying linestyles, 2nd varying colors
    elif variation == 'linestyle':
        customCycler = cycler(color=colorList) * \
            cycler(linestyle=linestyleList)

    # Creating m * o - styles, 1st varying linestyles, 2nd varying colors
    elif variation == 'marker':
        customCycler = cycler(color=colorList) * \
            cycler(marker=markerList) 

    else:
        print("Undefined color Scheme!")

    return customCycler


def test():
    customCycler = createCycler('Monochrome', 'linestyle')
    print(customCycler)
