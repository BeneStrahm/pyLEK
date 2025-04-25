# ------------------------------------------------------------------------------
# Description:  Plotting 2-D Lines on one figure
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from pyLEK.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pickle as pkl
import numpy as np
import os
import sys

# ----------------------------------------------------------------------
# Imported functions
# ----------------------------------------------------------------------

import pyLEK.plotters.plotStyle.colorCycler as colorCycler
import pyLEK.plotters.plotStyle.mplStyle as mplStyle
import pyLEK.plotters.plotHelpers as plotHelpers

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def plot1D(x, *, s=None, c=None, xlabel=None, ylabel=None, title=None, legend=None,
           dir_fileName=None, vLines=None, vTexts=None,
           xlim=[], ylim=[-0.5, 0.5], xticks=True, xscale='linear',  xlabelformat='%.1f',
           style_dict={}, mpl='_1D', colorScheme='Monochrome', variation='color', customCycler=None,
           savePlt=False, savePkl=False, showPlt=False, saveTex=False,
           fig=None, ax=None, annotate=[]):
    """Plotting 2-D Lines (x,y-plot) on one figure in a uniform style
    :param x: list w/ data to plot, with shape [n_row, datapoints]
    :param s: list w/ size of markers to plot, with shape [datapoints] 
    :param c: list w/ color of markers to plot, with shape [datapoints]
    :param xlabel: string w/ labels for x axis
    :param ylabel: string w/ labels for y axis
    :param title: string w/ plot title
    :param legend: list w/ legends [n]
    :param dir_fileName: string w/ Directory / Filename to save to,  
                         must be specified when savePlt is specified
    :param vLines: list w/ floats on where to add vertical line
    :param vTexts: list w/ strings for the vertical lines 
    :param xlim: list w/ limits  for x axis [xmin, xmax]
    :param ylim: list w/ limits  for y axis [ymin, ymax]
    :param xticks: bool true to annotate ticks based on data and limits
    :param xscale: string w/ scales acc. to matplotlib
    :param xlabelformat: string w/ format for x axis labels
    :param style_dict: dict w/ settings to overwrite mplstyle-template
    :param mpl: string w/ name of the mplstyle-sheet
    :param colorScheme: string ('Monochrome', 'UniS')
    :param variation: string ('color', 'linestyle')
    :param customCycler: cycler, instead of colorScheme & variation cycler can be passed 
    :param savePĺt: bool true to save plot 
    :param savePkl: bool true to save as .pickle
    :param saveTex: bool true to save as .pdf_tex
    :param showPlt: bool true show plot in interactive mode
    :param fig: fig object to be overwritten 
    :param ax: ax object to be overwritten 
    :rtype fig: modified fig object
    :rtype ax: modified ax object
    """

    # Find plot styles
    mplPath = mplStyle.findPlotStyle(mpl)

    # Modify plot styles
    mplStyle.modifyPlotStyle(style_dict, mplPath)

    # Get the plot styles
    mplStyle.retrievePlotStyle(style_dict, mplPath)

    # Check font
    plotHelpers.fontChecker()

    # Prepare Plots
    y = np.zeros(len(x), )

    # An empty figure with one axe
    if fig is None:
        fig, ax = plt.subplots()

    # Setting the title of the axe-object
    if not (title is None):
        ax.set_title(title)

    # Setting the x-axis / y-axis label of the axe-object
    if not (xlabel is None):
        ax.set_xlabel(xlabel, loc='right', )

    if not (ylabel) is None:
        ax.set_ylabel(ylabel, rotation=0, va='center', ha='right', labelpad=12)

    # Setting the x-axis / y-axis limits of the axe-object
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    # Setting position spines in data coordinate
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))

    # Setting the x-axis / y-axis scale of the axe-object
    if xscale:
        ax.set_xscale(xscale)

    # Setting the x-axis / y-axis label format of the axe-object
    if xlabelformat:
        ax.xaxis.set_major_formatter(FormatStrFormatter(xlabelformat))

    # Anmerkungen für Punkte im Plot
    if annotate:
        for a in annotate:
            ax.annotate(a[0], a[1])

    # Add vertical line / arrow on spine
    if True and xlim:
        ax.plot(1.00, 0, ">k", transform=ax.get_yaxis_transform(),
                clip_on=False, fillstyle='full', markeredgewidth=1, markersize=4)
        ax.plot(xlim[0], 0, "|k",
                clip_on=False, fillstyle='full', markeredgewidth=1, markersize=8, )
        ax.plot(xlim[1], 0, "|k",
                clip_on=False, fillstyle='full', markeredgewidth=1, markersize=8, )

    # Create color / linestyles
    if customCycler is None:
        customCycler = colorCycler.createCycler(colorScheme, variation)

    # Setting the cycler
    ax.set_prop_cycle(customCycler)

    # 2D - Plot of the axe-object
    if c and s:
        ax.scatter(x, y, c=c, s=s, clip_on=False, zorder=3)

    elif s:
        ax.scatter(x, y, s=s, clip_on=False, zorder=3)

    elif c:
        ax.scatter(x, y, c=c, clip_on=False, zorder=3)

    else:
        ax.scatter(x, y, clip_on=False, zorder=3)

    # Correctly ordering legend entries by replacing labels with entries
    # from the legend list. If this is not done there is not order in
    # the legend see: https://matplotlib.org/users/legend_guide.html
    if not (legend is None):
        handles, labels = ax.get_legend_handles_labels()

        for j, element in enumerate(legend, start=0):
            labels[j] = element

        # Setting the legend
        leg = ax.legend(labels)

        # Set line thickness / transparency of the legend to standart
        for line in leg.get_lines():
            line.set_linewidth(1.5)
            # Do not set for only marker plots
            if "lines.linewidth" in style_dict:
                if style_dict["lines.linewidth"] == 0:
                    line.set_linewidth(0)
            line.set_alpha(1.0)

    if xticks:
        # Set ticks based on data and limits
        xmin, xmax = ax.get_xlim()

        # Major ticks - Bottom spine
        ax.set_xticks([xmin, xmax], [xmin, xmax], minor=False)
        # Minor ticks - Top spine
        ax.set_xticks(x, x, minor=True)

        ax.xaxis.set_major_formatter(FormatStrFormatter(xlabelformat))
        ax.xaxis.set_minor_formatter(FormatStrFormatter(xlabelformat))

        # Reset limits
        ax.set_xlim([xmin, .075 * (xmax-xmin) + xmax], )

    # Add vertical line
    if vLines:
        for vLine in vLines:
            # Add vertical line to ax
            ax.axvline(vLine, linestyle="--", linewidth=1.0, marker="None", color='black',
                       zorder=max(len(x), len(y))+1)

    if vTexts:
        for vLine, vText in zip(vLines, vTexts):
            # Add Text to lines
            ax.text(vLine, 0.98 * (ax.get_ylim()[1] - ax.get_ylim()[0]) + ax.get_ylim()[0],
                    vText, rotation=90, rotation_mode='anchor',
                    horizontalalignment='right', verticalalignment='bottom',
                    fontsize='x-small')

    # Save plot
    if savePlt == True:
        try:
            plt.savefig(dir_fileName)
            plt.savefig(dir_fileName + ".png")
        except ValueError:
            print("Error saving plot: To save plot specify a file name")

    # Save plot with pickle
    if savePkl == True:
        try:
            pkl.dump(ax, open(dir_fileName + ".pickle", "wb"))
        except TypeError:
            print("Error dumping pickle: To dump pickle specify a file name")

    # Save plot as pdf_tex
    if saveTex == True:
        try:
            plotHelpers.savePdf_tex(fig, dir_fileName)
        except TypeError:
            print("Error saving .pdf_tex: To save pdf_tex specify a file name")

    # Show plot in interactive mode
    if showPlt == True:
        plt.show()

    # Clean up mplstyles
    mplStyle.cleanPlotStyle(mplPath)

    # Clean up everything
    if fig is None:
        plt.clf()
        plt.close()

    return fig, ax

# ----------------------------------------------------------------------
# Tests / Example
# ----------------------------------------------------------------------


def sample_2(*, showPlt=True, fig=None, ax=None):
    x = [0.7, 1.3, 1.5, 1.8]
    xlim = [0, 2]
    fig, ax = plot1D(x, showPlt=showPlt, xlim=xlim,
                     xlabel='x', ylabel='$f_{1,k}$', fig=fig, ax=ax)

    return fig, ax


if __name__ == "__main__":
    sample_2()
