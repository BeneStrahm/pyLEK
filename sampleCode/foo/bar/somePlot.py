# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  ** Add here short description **
# Author:       ** Add here author's e-mail adress **
# Created:      ** Add here the date of creation **
# Execution:    Import functions / collections (from helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Sources
# ------------------------------------------------------------------------------ 
# Literature / Website ressources
# e.g: https://www.ilek.uni-stuttgart.de/
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------                                                          
# Contains all imported modules / functions
from pyLEK.plotters import plot2D
import numpy as np
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# Example
def plotSomething(): 
    """plots some figure with custom mplStyle
    """

    # FIRST PLOT
    # only show plot with custom size and linewidth, add a vertical line
    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    y = [np.sin(x + phi) for phi in offsets]

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"

    title = "Using my own .mplstyle"

    # plot2D w/ all available options
    fig, ax = plot2D.plot2D([x, x, x, x], y, xlabel=xlabel, ylabel=ylabel, title=title,
                     mpl='_myStyle', showPlt=True,)

    return fig, ax