# ------------------------------------------------------------------------------
# Description:  Plotting bar charts on one figure
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2021-02-27
# Execution:    Import functions / collections (from pyLEK.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

from colorsys import yiq_to_rgb
import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
import matplotlib.ticker as mtick
import seaborn as sns

# ----------------------------------------------------------------------
# Imported functions
# ----------------------------------------------------------------------

import pyLEK.plotters.plotStyle.colorCycler as colorCycler
import pyLEK.plotters.plotStyle.mplStyle as mplStyle
import pyLEK.plotters.plotHelpers as plotHelpers

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def plotPieChart(y, *, title=None, outerLabels=None, innerLabels=None,
                 dir_fileName=None, pieWidth=0.4, pieRadius=1.2, innerPalette='light',
                 outerLabelDistance=1.2, innerLabelDistance=1.2, autopct='%1.0f%%',
                 style_dict={}, mpl='piechart', colorScheme='Monochrome', variation='color', customCycler=None,
                 savePlt=False, savePkl=False, showPlt=False, saveTex=False,
                 fig=None, ax=None):
    """Plotting bar charts on one figure in a uniform style
    :param y: list w/ data to plot, with shape [n_outer_pies, n_inner_pies]
              not each row needs to have the same shape
    :param title: string w/ plot title
    :param outerLabels: list w/ labels [n_outer_pies]
    :param innerLabels: list w/ labels [n_inner_pies]
    :param dir_fileName: string w/ Directory / Filename to save to,  
                         must be specified when savePlt is specified
    :param pieWidth: float w/ width of the pies
    :param pieRadius: float w/ outer radius of the outer pie
    :param innerPalette: string ('light', 'dark')
    :param outerLabelDistance: float or None, relative distance of pie labels.
                               If None, label are not drawn, but are shown in legend
    :param innerLabelDistance: float or None, relative distance of pie labels.
                               If None, label are not drawn, but are shown in legend
    :param autopct: None or str or callable,If not None, is a string or function used to 
                    label the wedges with their numeric value.
    :param style_dict: dict w/ settings to overwrite mplstyle-template
    :param mpl: string w/ name of the mplstyle-sheet
    :param colorScheme: string ('Monochrome', 'UniS')
    :param variation: string ('color', 'linestyle')
    :param customCycler: cycler, instead of colorScheme & variation cycler can be passed 
    :param savePlt: bool true to save plot, file format acc. to mpl-style
    :param savePkl: bool true to save as .pickle
    :param saveTex: bool true to save as .pdf_tex
    :param showPlt: bool true show plot in interactive mode
    :param fig: fig object to be overwritten 
    :param ax: ax object to be overwritten 
    :rtype fig: modified fig object
    :rtype ax: modified ax object
    """

    # Modify plot styles
    mplStyle.modifyPlotStyle(style_dict, mpl)

    # Get the plot styles
    mplStyle.retrievePlotStyle(style_dict, mpl)

    # Prepare Plots
    if isinstance(y[0], list):
        # Resort lists in np array, fill up with zeros
        dataArr = np.zeros([len(y), len(max(y, key=lambda y: len(y)))])
        for i, j in enumerate(y):
            dataArr[i][0:len(j)] = j

        # Creating inner circle
        # 1.) Flatten array
        innerData = dataArr.flatten()

        # 2.) Remove Zeros
        innerData = innerData[innerData != 0]

    elif isinstance(y[0], (int, float)):
        # Resort lists in np array
        dataArr = np.zeros([len(y), 1])
        for i, j in enumerate(y):
            dataArr[i] = j

    # Creating outter circle
    # 1.) Sum over axis
    outerData = dataArr.sum(axis=1)

    # An empty figure with one axe
    if fig is None:
        fig, ax = plt.subplots()

    # Setting the title of the axe-object
    if not (title is None):
        ax.set_title(title)

    # Create color / linestyles
    if customCycler is None:
        customCycler = colorCycler.createCycler(colorScheme, variation)

    # Setting the cycler
    ax.set_prop_cycle(customCycler)

    # Determine size of pies
    innerRadius = pieRadius-pieWidth

    # Determine position of autopct
    outerPos = (pieRadius - pieWidth / 2) / pieRadius
    innerPos = (innerRadius - pieWidth / 2) / innerRadius

    # Plot the outer pie
    mplTuple = ax.pie(outerData,
                      labels=outerLabels,
                      radius=pieRadius,
                      autopct=autopct,        # Enabling autolabeling data
                      pctdistance=outerPos,      # Autolabel position
                      labeldistance=outerLabelDistance,
                      rotatelabels=False,
                      wedgeprops=dict(
                          width=pieWidth, edgecolor='w', alpha=0.7),
                      textprops=dict(fontsize='small', ha='center', va='center'))
    wedges = mplTuple[0]

    if isinstance(y[0], list):
        # Facecolors of outer wedges
        outerFC = []
        for wedge in wedges:
            # Get facecolor
            color = wedge.get_fc()

            # Translate them into colormaps
            if innerPalette == 'light':
                cmap = sns.light_palette(color, as_cmap=True)
            elif innerPalette == 'dark':
                cmap = sns.dark_palette(color, as_cmap=True)
            else:
                cmap = sns.light_palette(color, as_cmap=True)
                print("Invalid Option for innerPalette: Continuing with light scheme")

            outerFC.append(cmap)

        # Determine facecolors of inner wedges
        innerFC = []
        for i, cmap in enumerate(outerFC):
            # N = Length of each row in y + 2
            # (Exclude first and last color)
            N = len(y[i]) + 2
            # Array of linear interpolated face colors
            # fcs.shape = [nColors * RGBA]
            fcs = cmap(np.linspace(1, 0.0, N)[1:-1])

            # RGBA-array
            # fc.shape = [RGBA]
            for fc in fcs:
                innerFC.append(fc)

        # Plot inner pie
        mplTuple = ax.pie(innerData,
                          colors=innerFC,
                          labels=innerLabels,
                          radius=pieRadius-pieWidth,
                          autopct=autopct,          # Enabling autolabeling data
                          pctdistance=innerPos,    # Autolabel position
                          labeldistance=innerLabelDistance,
                          rotatelabels=True,
                          wedgeprops=dict(
                              width=pieWidth, edgecolor='w', alpha=0.7),
                          textprops=dict(fontsize='small', ha='center', va='center'))

    wedges = mplTuple[0]

    if (outerLabelDistance is None) or (innerLabelDistance is None):
        # Remove inner labels from legend
        if not (innerLabelDistance is None):
            handles, labels = ax.get_legend_handles_labels()
            N = len(y)
            Handles = handles[:N]
            labels = labels[:N]
            pass

        # Remove outer labels from legend
        elif not (outerLabelDistance is None):
            handles, labels = ax.get_legend_handles_labels()
            N = len(y)
            handles = handles[N:]
            labels = labels[N:]

        else:
            handles, labels = ax.get_legend_handles_labels()

        # Setting the legend
        if "legend.loc" in style_dict:
            # Multiple columns for legend if placed below or above ax
            above_below = ['upper left', 'upper right', 'upper center',
                           'lower left', 'lower right', 'lower center']
            if style_dict["legend.loc"] in above_below:
                leg = fig.legend(handles, labels, ncol=len(y))
        else:
            leg = fig.legend(handles, labels)

    # Save plot
    if savePlt == True:
        try:
            plt.savefig(dir_fileName)
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
    mplStyle.cleanPlotStyle(mpl)

    # Clean up everything
    if fig is None:
        plt.clf()
        plt.close()

    return fig, ax

# ----------------------------------------------------------------------
# Tests / Example
# ----------------------------------------------------------------------


def sample1(*, showPlt=True, fig=None, ax=None):
    # Data:
    y = [11, 12, 25]

    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    figSize = plotHelpers.calcFigSize(aspectRatio=1)

    style_dict = {"figure.figsize": figSize,  "legend.loc": "lower center"}

    # 1. Plot
    title = "Simple Pie Chart"
    outerLabels = ['Group A', 'Group B', 'Group C']

    # plot w/ all available options
    plotPieChart(y, title=title, outerLabels=outerLabels, innerLabels=None,
                 dir_fileName=None, pieWidth=0.8, pieRadius=1.2, innerPalette='light',
                 outerLabelDistance=1.2, innerLabelDistance=1.2, autopct='%1.0f%%',
                 style_dict=style_dict, mpl='piechart', colorScheme='UniS', variation='color', customCycler=None,
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    return fig, ax


def sample2(*, showPlt=True, fig=None, ax=None):
    # Data:
    y = [[5, 6], [4, 3, 5], [7, 3, 4, 5, 6]]

    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    figSize = plotHelpers.calcFigSize(aspectRatio=1)

    style_dict = {"figure.figsize": figSize, "axes.titlepad": 12,
                  "legend.loc": "lower center", "figure.subplot.top": 0.85, "figure.subplot.bottom": 0.2}

    # Coloring
    # --------
    # Creating a custom cycler with predefined searborn color scheme
    import seaborn as sns
    from cycler import cycler

    N_colors = 5            # Number of colors
    paletteName = "BuPu_r"    # Name of seaborn color palette

    # Create the color palette ...
    customColorPalette = sns.color_palette(
        palette=paletteName, as_cmap=True)(np.linspace(0, 1, N_colors))

    # ... and create a cycler from it
    customCycler = cycler(color=customColorPalette)

    # 2. Plot
    title = "Pie Chart w/ inner and outer pie"
    outerLabels = ['Group A', 'Group B', 'Group C']
    innerLabels = ['A.1', 'A.2', 'B.1', 'B.2',
                   'B.3', 'C.1', 'C.2', 'C.3', 'C.4', 'C.5']

    # Labeling
    # --------
    # None passes labels to the legend
    outerLabelDistance = None

    # Determine size of pies
    pieWidth = 0.4
    pieRadius = 1.2
    innerRadius = pieRadius-pieWidth

    # Determine position of inner labels, centered on pies
    innerLabelDistance = (innerRadius - pieWidth / 2) / innerRadius

    # plot w/ all available options
    plotPieChart(y, title=title, outerLabels=outerLabels, innerLabels=innerLabels,
                 pieWidth=pieWidth, pieRadius=pieRadius,
                 outerLabelDistance=outerLabelDistance, innerLabelDistance=innerLabelDistance, autopct=None,
                 style_dict=style_dict, customCycler=customCycler,
                 showPlt=showPlt, savePlt=False,
                 fig=None, ax=None)

    return fig, ax


def sample3(*, showPlt=True, fig=None, ax=None):
    # Data:
    y = [11, 12, 25]

    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    figSize = plotHelpers.calcFigSize(aspectRatio=1)

    # 3. Plot
    title = "Pie Chart \n w/ Custom \n Labeling"
    outerLabels = ['Concrete', 'Steel', 'Mixed']

    # Example to use custom annotation function
    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d} kg)".format(pct, absolute)

    # Center the title
    style_dict = {"figure.figsize": figSize, "legend.loc": "lower center", 
                  'axes.titley': 0.39, 'ax.titlesize': 'xxx-small'}

    # plot w/ all available options
    plotPieChart(y, title=title, outerLabels=outerLabels,
                 pieWidth=0.6, pieRadius=1.2,
                 outerLabelDistance=None, autopct=lambda pct: func(pct, y),
                 style_dict=style_dict, colorScheme='UniS',
                 savePlt=False, showPlt=showPlt,
                 fig=None, ax=None)

    return fig, ax


if __name__ == "__main__":
    sample1()
    sample2()
    sample3()
