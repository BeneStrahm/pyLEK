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


def plot2D(x, y, *, xlabel=None, ylabel=None, title=None, legend=None,
           dir_fileName=None, vLines=None, vTexts=None,  hLines=None, hTexts=None,
           xlim=[], ylim=[], xscale='linear', yscale='linear',
           style_dict={}, mpl='_2D', colorScheme='Monochrome', variation='color', customCycler=None,
           savePlt=False, savePkl=False, showPlt=False, saveTex=False,
           fig=None, ax=None,annotate=[]):
    """Plotting 2-D Lines (x,y-plot) on one figure in a uniform style
    :param x: list w/ data to plot, with shape [n_row, datapoints]
    :param y: list w/ data to plot, with shape [n_row, datapoints]
    :param xlabel: string w/ labels for x axis
    :param xlabel: string w/ labels for y axis
    :param title: string w/ plot title
    :param legend: list w/ legends [n]
    :param dir_fileName: string w/ Directory / Filename to save to,  
                         must be specified when savePlt is specified
    :param vLines: list w/ floats on where to add vertical line
    :param vTexts: list w/ strings for the vertical lines 
    :param hLines: list w/ floats on where to add horizontal line
    :param hTexts: list w/ strings for the horizontal lines 
    :param xlim: list w/ limits  for x axis [xmin, xmax]
    :param ylim: list w/ limits  for y axis [ymin, ymax]
    :param xscale: string w/ scales acc. to matplotlib
    :param yscale: string w/ scales acc. to matplotlib
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
    x = np.transpose(x)
    y = np.transpose(y)

    # An empty figure with one axe
    if fig is None:
        fig, ax = plt.subplots()

    # Setting the title of the axe-object
    if not (title is None):
        ax.set_title(title)

    # Setting the x-axis / y-axis label of the axe-object
    if not (xlabel is None):
        ax.set_xlabel(xlabel)
    if not (ylabel is None):
        ax.set_ylabel(ylabel)

    # Setting the x-axis / y-axis limits of the axe-object
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    # Setting the x-axis / y-axis scale of the axe-object
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    #Anmerkungen für Punkte im Plot
    if annotate:
        for a in annotate:
            ax.annotate(a[0],a[1])
        
    # Create color / linestyles
    if customCycler is None:
        customCycler = colorCycler.createCycler(colorScheme, variation)

    # Setting the cycler
    ax.set_prop_cycle(customCycler)

    # 2D - Plot of the axe-object
    ax.plot(x, y, label='label')

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

    # Add horizontal line
    if hLines:
        for hLine in hLines:
            # Add vertical line to ax
            ax.axhline(hLine, linestyle="--", linewidth=1.0, marker="None", color='black',
                       zorder=max(len(x), len(y))+1)

    if hTexts:
        for hLine, hText in zip(hLines, hTexts):
            # Add Text to lines
            ax.text(0.02 * (ax.get_xlim()[1] - ax.get_xlim()[0]) + ax.get_xlim()[0], hLine,
                    hText, rotation=0, rotation_mode='anchor',
                    horizontalalignment='left', verticalalignment='bottom',
                    fontsize='x-small')
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
    mplStyle.cleanPlotStyle(mplPath)

    # Clean up everything
    if fig is None:
        plt.clf()
        plt.close()

    return fig, ax

# ----------------------------------------------------------------------
# Tests / Example
# ----------------------------------------------------------------------


def sample_1(*, showPlt=True, fig=None, ax=None):
    # FIRST PLOT
    # only show plot with custom size and linewidth, add a vertical line
    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    y = [np.sin(x + phi) for phi in offsets]

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"

    title = "Test Title"

    vLines = [np.mean(x)]
    vTexts = ['test description']

    hLines = [np.std(y)]
    hTexts = ['test description']

    figSize = plotHelpers.calcFigSize()

    style_dict = {"lines.linewidth": 5, "figure.figsize": figSize}

    # plot2D w/ all available options
    fig, ax = plot2D([x, x, x, x], y, xlabel=xlabel, ylabel=ylabel, title=title, legend=None,
                     dir_fileName=None, vLines=vLines, vTexts=vTexts, hLines=hLines, hTexts=hTexts,
                     xlim=[], ylim=[], xscale='linear', yscale='linear',
                     style_dict=style_dict, mpl='_2D', colorScheme='UniS', variation='color', customCycler=None,
                     savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                     fig=fig, ax=ax)

    return fig, ax


def sample_2(*, showPlt=True, fig=None, ax=None):
    # SECOND PLOT
    # save in this folder as .pdf  and show plot
    # plot without a line but only with different markers
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 8, endpoint=False)
    y = [np.sin(x + phi) for phi in offsets]

    style_dict = {"lines.linewidth": 0,
                  "savefig.format": "pdf"}

    legend = ["testdata1", "testdata2", "testdata3", "testdata4",
              "testdata5", "testdata6", "testdata7", "testdata8"]

    # Change to current file location
    os.chdir(os.path.dirname(sys.argv[0]))

    dir_fileName = "plot_as_pdf_example"
    # plot2D w/ only specified options, save as .pdf
    fig, ax = plot2D([x, x, x, x, x, x, x, x], y, legend=legend,
                     dir_fileName=dir_fileName,
                     style_dict=style_dict, variation='marker',
                     showPlt=showPlt, savePlt=True,
                     fig=fig, ax=ax)

    return fig, ax


def sample_3(*, showPlt=True, fig=None, ax=None):
    # THIRD PLOT
    # save in this folder as .pdf_tex for latex and show plot
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    y = [np.sin(x + phi) for phi in offsets]

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"

    title = "LaTeX (.pdf\_tex) example \n legend w/ LaTeX Code to be compiled"

    legend = [r"\$\sin x\$", r"\$\sin x + \frac{\pi}{2}\$",
              r"\footnotesize{testdata3}", r"\bfseries{testdata4}"]

    figSize = plotHelpers.calcFigSize()

    style_dict = {"lines.linewidth": 2, "figure.figsize": figSize}

    # Change to current file location
    os.chdir(os.path.dirname(sys.argv[0]))

    dir_fileName = "plot_as_pdftex_example"
    # plot2D w/ only specified options, save as .pdf_tex
    fig, ax = plot2D([x, x, x, x], y, xlabel=xlabel, ylabel=ylabel, title=title,
                     legend=legend, dir_fileName=dir_fileName,
                     style_dict=style_dict, variation='color',
                     showPlt=showPlt, saveTex=True,
                     fig=fig, ax=ax)

    return fig, ax


def sample_4(*, showPlt=True, fig=None, ax=None):
    # FOURTH PLOT
    # Use seaborn color scheme & show plot
    # For searborn color schemes see:
    # https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f

    # Any other (custom) color scheme can be used by creating a cycler
    # See also: https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html

    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    y = [np.sin(x + phi) for phi in offsets]

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"

    title = "Seaborn Color Scheme \"OrRd_r\""

    figSize = plotHelpers.calcFigSize()

    style_dict = {"lines.linewidth": 5, "figure.figsize": figSize}

    # Creating a custom cycler with predefined searborn color scheme
    import seaborn as sns
    from cycler import cycler

    N_colors = 5            # Number of colors
    paletteName = "OrRd_r"  # Name of seaborn color palette

    # Create the color palette ...
    customColorPalette = sns.color_palette(
        palette=paletteName, as_cmap=True)(np.linspace(0, 1, N_colors))

    # ... and create a cycler from it
    customCycler = cycler(color=customColorPalette)

    # plot2D w/ only specified options, save as .pdf_tex
    fig, ax = plot2D([x, x, x, x], y, xlabel=xlabel, ylabel=ylabel, title=title,
                     style_dict=style_dict, customCycler=customCycler,
                     showPlt=showPlt,
                     fig=fig, ax=ax)

    return fig, ax


if __name__ == "__main__":
    sample_1()
    sample_2()
    sample_3()
    sample_4()
