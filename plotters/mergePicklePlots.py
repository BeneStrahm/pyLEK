#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:   Merge Plots which were saved as .pickle
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2019-03-06
# Execution:    Import functions / collections (from pyLek.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Sources
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import pickle as pkl
import matplotlib.pyplot as plt
from pyLEK.plotters import plot2D
from pyLEK.plotters import plotHelpers
import os
import sys
import numpy as np
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# 1) Create plots with the plotters using the option savePkl = True

# ------------------------------------------------------------------------------
# Note: You wont need this part of the script in your setup, it just serves
# to create the sample .pickle plots

def samplePlots(*, showPlt=False):
    # Dataset x-Axis
    x = np.linspace(0, 2 * np.pi, 50)

    # Change to current file location
    os.chdir(os.path.dirname(sys.argv[0]))

    # FIRST PLOT
    # ----------
    y = np.sin(x)
    title = "First Plot"

    dir_fileName = "plot_as_pickle_01"

    # plot2D w/ only specified options, save as .pickle
    plot2D.plot2D(x, y, title=title, dir_fileName=dir_fileName,
                  savePkl=True, showPlt=showPlt)

    # SECOND PLOT
    # -----------
    y = np.cos(x)
    title = "Second Plot"

    dir_fileName = "plot_as_pickle_02"

    # plot2D w/ only specified options, save as .pickle
    plot2D.plot2D(x, y, title=title, dir_fileName=dir_fileName,
                  savePkl=True, showPlt=showPlt)

    # THIRD PLOT
    # ----------
    y = np.cos(2*x)
    title = "Third Plot"

    dir_fileName = "plot_as_pickle_03"

    # plot2D w/ only specified options, save as .pickle
    plot2D.plot2D(x, y, title=title, dir_fileName=dir_fileName,
                  savePkl=True, showPlt=showPlt)


# 2) Copy all plots you want to combine into a folder
# ------------------------------------------------------------------------------
# Done already

# 3) Copy mergePicklePlots.py into the folder and customize the following to your needs
# ------------------------------------------------------------------------------

def getDataFromPickle(ax):
    line = ax.lines[0]
    x = line.get_xdata()
    y = line.get_ydata()
    legend = ax.get_title()

    return x, y, legend


def parsePlots():
    # Specify the file name
    # fname = str(input("Specify File Name: "))
    fname1 = "plot_as_pickle_01"
    fname2 = "plot_as_pickle_02"
    fname3 = "plot_as_pickle_03"

    # Change to current file location
    os.chdir(os.path.dirname(sys.argv[0]))

    # Load the ax-objects
    ax1 = pkl.load(open(fname1 + '.pickle', 'rb'))
    ax2 = pkl.load(open(fname2 + '.pickle', 'rb'))
    ax3 = pkl.load(open(fname3 + '.pickle', 'rb'))

    # Get data from the ax-objects
    x1, y1, legend1 = getDataFromPickle(ax1)
    x2, y2, legend2 = getDataFromPickle(ax2)
    x3, y3, legend3 = getDataFromPickle(ax3)

    # Clean up
    plt.close('all')

    # Merged data for plotting
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    legend = [legend1, legend2, legend3]

    return x, y, legend

# 4) Use again the plotters to plot the figures loaded with mergePicklePlots.py
# ------------------------------------------------------------------------------

def replotMerged(x, y, legend):
    plot2D.plot2D(x, y, title="Merged Plots",
                  legend=legend, ylim=[-1, 1], showPlt=True)

# Execution routine:
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    # 1) Create plots with the plotters using the option savePkl = True
    samplePlots()

    # 2) Copy all plots you want to combine into a folder
    pass

    # 3) Copy mergePicklePlots.py into the folder and customize the following to your needs
    x, y, legend = parsePlots()

    # 4) Use again the plotters to plot the figures loaded with mergePicklePlots.py
    replotMerged(x, y, legend)
