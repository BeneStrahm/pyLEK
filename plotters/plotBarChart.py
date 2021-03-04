# ------------------------------------------------------------------------------
# Description:  Plotting bar charts on one figure
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2021-02-27
# Execution:    Import functions / collections (from pyLEK.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
import matplotlib.ticker as mtick

# ----------------------------------------------------------------------
# Imported functions
# ----------------------------------------------------------------------

import pyLEK.plotters.plotStyle.colorCycler as colorCycler
import pyLEK.plotters.plotStyle.mplStyle as mplStyle
import pyLEK.plotters.plotHelpers as plotHelpers

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def plotBarChart(y, *, xlabel=None, ylabel=None, title=None, legend=None,
                 xticks=None, xticklabels=None, xticksrotation=None,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='stacked', annotations=None, annotations_position='above',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None,  hLines=None, hTexts=None,
                 xlim=[], ylim=[], xscale='linear', yscale='linear',
                 style_dict={}, mpl='barchart', colorScheme='Monochrome', variation='color',
                 savePlt=False, savePkl=False, showPlt=False, saveTex=False,
                 fig=None, ax=None):
    """Plotting bar charts on one figure in a uniform style
    :param y: np.array w/ data to plot, with shape [n_datasets, datapoints]
    :param xlabel: string w/ labels for x axis
    :param xlabel: string w/ labels for y axis
    :param title: string w/ plot title
    :param legend: list w/ legends [n_datasets]
    :param xticks: list w/ position of ticks [n_ticks]
    :param xticklabels: list w/ ticks [n_ticks]
    :param xticksrotation: int w/ rotation of ticks
    :param yticks: llist w/ position of ticks [n_ticks]
    :param yticklabels: list w/ ticks [n_ticks]
    :param yticksrotation: int w/ rotation of ticks
    :param barChart: string ('stacked', 'grouped')
    :param annotations: string ('%', 'individual','sum') or None
    :param annotations_position: string ('above', 'center', 'right')
    :param orientation: string ('horizontal', 'vertical')
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

    # Create color / linestyles
    customCycler = colorCycler.createCycler(colorScheme, variation)

    # Prepare Plots
    x = np.arange(len(y[0]))

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

    # Setting the cycler
    ax.set_prop_cycle(customCycler)

    # Bar width (1=no space between bars)
    bar_width = 0.8

    # Stacked Bar Chart - Plot of the axe-object
    if barChart == 'stacked':
        #
        bars_set = []
        bottom = np.zeros(len(y[0]))
        for yi in y:
            if orientation == 'vertical':
                bars_set.append(ax.bar(x, yi, bottom=bottom, width=bar_width,
                                       label='label', edgecolor='white', linewidth=0.5))
            elif orientation == 'horizontal':
                bars_set.append(ax.barh(x, yi, left=bottom, height=bar_width,
                                        label='label', edgecolor='white', linewidth=0.5))

            bottom = bottom + yi

    elif barChart == 'stacked100%':
        #
        bars_set = []
        bottom = np.zeros(len(y[0]))
        for yi in y:
            yi_rel = yi / np.sum(y, axis=0)
            if orientation == 'vertical':
                bars_set.append(ax.bar(x, yi_rel, bottom=bottom, width=bar_width,
                                       label='label', edgecolor='white', linewidth=0.5))
            elif orientation == 'horizontal':
                bars_set.append(ax.barh(x, yi_rel, left=bottom, height=bar_width,
                                        label='label', edgecolor='white', linewidth=0.5))
            bottom = bottom + yi_rel

        # Set labels to %
        if orientation == 'vertical':
            if yticklabels is None:
                ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
        elif orientation == 'horizontal':
            if xticklabels is None:
                ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))

    elif barChart == 'grouped':
        bars_set = []
        bottom = np.zeros(len(y[0]))
        for i, yi in enumerate(y):
            x_pos = x-bar_width/2 + bar_width/len(y) * i
            if orientation == 'vertical':
                y_pos = x-bar_width/2 + bar_width/len(y) * i
                bars_set.append(ax.bar(x_pos, yi, width=bar_width/len(y),
                                       label='label', edgecolor='white', linewidth=0.5))
            elif orientation == 'horizontal':
                x_pos = x-bar_width/2 + bar_width/len(y) * i
                bars_set.append(ax.barh(x_pos, yi, left=bottom, height=bar_width/len(y),
                                        label='label', edgecolor='white', linewidth=0.5))

    # Add text annotations to the top of the bars.
    if not (annotations is None):

        # Get maximal size of y-axis for text alignment
        ymax = ax.get_ylim()[1]
        xmax = ax.get_xlim()[1]

        # Loop overs datasets
        for i, bars in enumerate(bars_set):

            # Loop over bars in each dataset
            for j, bar in enumerate(bars):

                # Position of text and grab the color of bars so the text gets the same color
                if annotations_position == 'above':
                    x_pos = bar.get_x() + bar.get_width() / 2
                    y_pos = bar.get_y() + bar.get_height() + 0.0175 * ymax
                    bar_color = bars[0].get_facecolor()
                    va = 'center'
                    ha = 'center'
                elif annotations_position == 'right':
                    x_pos = bar.get_x() + bar.get_width() + 0.005 * xmax
                    y_pos = bar.get_y() + bar.get_height() / 2
                    bar_color = bars[0].get_facecolor()
                    va = 'center_baseline'
                    ha = 'left'
                elif annotations_position == 'center':
                    x_pos = bar.get_x() + bar.get_width() / 2
                    y_pos = bar.get_y() + bar.get_height() / 2
                    bar_color = 'white'
                    va = 'center'
                    ha = 'center'
                else:
                    print('Unknown option for annotation position')


                # Get the text
                if annotations == 'individual':
                    # Get each individual value
                    bar_text = "{:.0f}".format(y[i][j])

                    # Add the text
                    ax.text(x_pos, y_pos, bar_text, fontsize='x-small', va=va,
                            ha=ha, color=bar_color)

                elif annotations == 'sum':
                    # Only sum for last bar_set
                    if i == len(bars_set)-1:
                        # Calculate the sum of all bars at each bar
                        bar_text = "$\Sigma$=" + \
                            "{:.0f}".format(np.sum(y, 0)[j])

                        # Add the text
                        ax.text(x_pos, y_pos, bar_text, fontsize='x-small', va=va,
                                ha=ha, color=bar_color)

                elif annotations == '%':
                    # Get max for xtick
                    # bar_text =
                    # Calc relative for each bar
                    bar_text = "{:.0%}".format(y[i][j] / np.sum(y, 0)[j])

                    # Add the text
                    ax.text(x_pos, y_pos, bar_text, fontsize='x-small', va=va,
                            ha=ha, color=bar_color)

                else:
                    print('Unknown option for annotation type')
    else:
        print('Unknown option for bar chart type')

    # Setting the x-ticks / y-ticks label of the axe-object
    if not (xticks is None):                # Position
        ax.set_xticks(xticks)

    if not (xticklabels is None):           # Label
        ax.set_xticklabels(xticklabels)

    if not (xticksrotation is None):        # Textrotation
        for label in ax.get_xticklabels():
            label.set_ha("center")
            label.set_rotation(xticksrotation)

    if not (yticks is None):                # Position
        ax.set_yticks(yticks)

    if not (yticklabels is None):           # Label
        ax.set_yticklabels(yticklabels)

    if not (yticksrotation is None):        # Textrotation
        for label in ax.get_yticklabels():
            label.set_ha("center")
            label.set_rotation(yticksrotation)

    # Correctly ordering legend entries by replacing labels with entries
    # from the legend list. If this is not done there is not order in
    # the legend see: https://matplotlib.org/users/legend_guide.html
    if not (legend is None):
        handles, labels = ax.get_legend_handles_labels()

        for j, element in enumerate(legend, start=0):
            labels[j] = element

        # Setting the legend
        if "legend.loc" in style_dict:
            # Multiple columns for legend if placed below or above ax
            above_below = ['upper left', 'upper right', 'upper center',
                           'lower left', 'lower right', 'lower center']
            if style_dict["legend.loc"] in above_below:
                leg = fig.legend(labels, ncol=len(y))
            else:
                leg = fig.legend(labels)

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
    mplStyle.cleanPlotStyle(mpl)

    # Clean up everything
    if fig is None:
        plt.clf()
        plt.close()

    return fig, ax

# ----------------------------------------------------------------------
# Tests / Example
# ----------------------------------------------------------------------


def sample_stacked(*, showPlt=True, fig=None, ax=None):
    # Data: https://www.skyscrapercenter.com/year-in-review/2019
    completions_200_plus = np.array(
        [71, 83, 70, 73, 103, 117, 134, 142, 146, 126, 102])
    completions_300_plus = np.array(
        [9,  9,  8,  9, 11, 15,  9, 15, 18, 26, 21])
    completions_400_plus = np.array(
        [4,  2,  2,  0,  1,  2,  1,  2,  3,  6,  4])

    # When using stacked charts, the data is offset automatically !
    # In this example:
    # All buildings 400+ m are included in the buildings 300+ m
    # For the stacked bar chart, the data has to be divided in
    # all buildings 400+ and all buildings 300-400 m !
    #
    # See also the following three plots where the annotation
    # changes for explanation
    #
    # See also this code L120ff
    y = [completions_400_plus, completions_300_plus -
         completions_400_plus, completions_200_plus-completions_300_plus]

    xlabel = "Year"
    ylabel = "Number of Completions"

    # Custom tick annotations
    # Position of the labels
    xticks = np.arange(len(y[0]))
    # Labels
    xticklabels = ["2010", "2011", "2012", "2013", "2014",
                   "2015", "2016", "2017", "2018", "2029", "2020"]
    # Label Orientation
    xticksrotation = 45

    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    figSize = plotHelpers.calcFigSize()

    style_dict = {"figure.figsize": figSize, "axes.titlepad": 12,
                  "legend.loc": "lower center", "figure.subplot.top": 0.85, "figure.subplot.bottom": 0.2}

    # 1. Plot
    legend = ['# of 400+ m completions',
              '# of 300+ m completions', '# of 200+ m completions']
    title = "Completions Timeline (stacked bar chart w/ summation)"
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks, xticklabels=xticklabels, xticksrotation=xticksrotation,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='stacked', annotations='sum', annotations_position='above',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=[], xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 2. Plot
    legend = ['% of 400+ m completions',
              '% of 300-400 m completions', '% of 200-300 m completions']
    title = "Completions Timeline (stacked bar chart w/ ratio)"
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks, xticklabels=xticklabels, xticksrotation=xticksrotation,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='stacked', annotations='%', annotations_position='above',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=[], xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 3. Plot
    legend = ['# of 400+ m completions',
              '# of 300-400 m completions', '# of 200-300 m completions']
    xticks_mod = xticks[::2]
    xticklabels_mod = xticklabels[::2]
    xticksrotation_mod = 0
    title = "Completions Timeline (stacked bar chart w/ respective number) \n [modified ticks] "
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks_mod, xticklabels=xticklabels_mod, xticksrotation=xticksrotation_mod,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='stacked', annotations='individual', annotations_position='above',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=[], xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 4. Plot
    legend = ['% of 400+ m completions',
              '% of 300-400 m completions', '% of 200-300 m completions']
    style_dict = {"figure.figsize": figSize, "axes.titlepad": 12, "axes.spines.top": "True",
                  "legend.loc": "lower center", "figure.subplot.top": 0.85, "figure.subplot.bottom": 0.2}
    ylim = [0, 1]
    title = "Completions Timeline (stacked bar chart [100%] w/ ratio)"
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks, xticklabels=xticklabels, xticksrotation=xticksrotation,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='stacked100%', annotations='%', annotations_position='center',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=ylim, xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 5. Plot
    legend = ['# of 400+ m completions',
              '# of 300-400 m completions', '# of 200-300 m completions']
    title = "Completions Timeline (stacked bar chart [100%] w/ respective number)"
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks, xticklabels=xticklabels, xticksrotation=xticksrotation,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='stacked100%', annotations='individual', annotations_position='center',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=ylim, xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 5. Plot / Switch to horizontal
    legend = ['# of 400+ m completions',
              '# of 300-400 m completions', '# of 200-300 m completions']
    title = "Completions Timeline (horizontal stacked bar chart [100%] w/ respective number)"
    style_dict = {"figure.figsize": figSize, "axes.titlepad": 12, "axes.spines.right": "True",
                  "legend.loc": "lower center", "figure.subplot.top": 0.85, "figure.subplot.bottom": 0.2}

    # plot w/ all available options
    fig, ax = plotBarChart(y, xlabel=ylabel, ylabel=xlabel, title=title, legend=legend,
                           xticks=None, xticklabels=None, xticksrotation=None,
                           yticks=xticks, yticklabels=xticklabels, yticksrotation=None,
                           barChart='stacked100%', annotations='individual', annotations_position='right',
                           orientation='horizontal',
                           dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                           xlim=ylim, ylim=[], xscale='linear', yscale='linear',
                           style_dict=style_dict, mpl='barchart_horizontal', colorScheme='UniS', variation='color',
                           savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                           fig=fig, ax=ax)

    return fig, ax


def sample_grouped(*, showPlt=True, fig=None, ax=None):
    # Data: https://www.skyscrapercenter.com/year-in-review/2019
    completions_200_plus = np.array(
        [71, 83, 70, 73, 103, 117, 134, 142, 146, 126, 102])
    completions_300_plus = np.array(
        [9,  9,  8,  9, 11, 15,  9, 15, 18, 26, 21])
    completions_400_plus = np.array(
        [4,  2,  2,  0,  1,  2,  1,  2,  3,  6,  4])

    # When using stacked charts, the data is offset automatically !
    # In this example:
    # All buildings 400+ m are included in the buildings 300+ m
    # For the stacked bar chart, the data has to be divided in
    # all buildings 400+ and all buildings 300-400 m !
    #
    # See also the following three plots where the annotation
    # changes for explanation
    #
    # See also this code L120ff
    y = [completions_400_plus, completions_300_plus -
         completions_400_plus, completions_200_plus-completions_300_plus]

    xlabel = "Year"
    ylabel = "Number of Completions"

    # Custom tick annotations
    # Position of the labels
    xticks = np.arange(len(y[0]))
    # Labels
    xticklabels = ["2010", "2011", "2012", "2013", "2014",
                   "2015", "2016", "2017", "2018", "2029", "2020"]
    # Label Orientation
    xticksrotation = 45

    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    figSize = plotHelpers.calcFigSize()

    style_dict = {"figure.figsize": figSize, "axes.titlepad": 12,
                  "legend.loc": "lower center", "figure.subplot.top": 0.85, "figure.subplot.bottom": 0.2}

    # 1. Plot
    legend = ['% of 400+ m completions',
              '% of 300-400 m completions', '% of 200-300 m completions']
    title = "Completions Timeline (grouped bar chart w/ ratio)"
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks, xticklabels=xticklabels, xticksrotation=xticksrotation,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='grouped', annotations='%', annotations_position='above',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=[], xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 2. Plot
    legend = ['# of 400+ m completions',
              '# of 300-400 m completions', '# of 200-300 m completions']
    title = "Completions Timeline (grouped bar chart w/ respective number) \n [modified ticks] "
    # plot w/ all available options
    plotBarChart(y, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend,
                 xticks=xticks, xticklabels=xticklabels, xticksrotation=xticksrotation,
                 yticks=None, yticklabels=None, yticksrotation=None,
                 barChart='grouped', annotations='individual', annotations_position='above',
                 orientation='vertical',
                 dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                 xlim=[], ylim=[], xscale='linear', yscale='linear',
                 style_dict=style_dict, mpl='barchart_vertical', colorScheme='UniS', variation='color',
                 savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                 fig=None, ax=None)

    # 3. Plot / Switch to horizontal
    legend = ['# of 400+ m completions',
              '# of 300-400 m completions', '# of 200-300 m completions']
    title = "Completions Timeline (horizontal grouped bar chart w/ respective number) \n [modified ticks] "
    # plot w/ all available options
    fix, ax = plotBarChart(y, xlabel=ylabel, ylabel=xlabel, title=title, legend=legend,
                           xticks=None, xticklabels=None, xticksrotation=None,
                           yticks=xticks, yticklabels=xticklabels, yticksrotation=None,
                           barChart='grouped', annotations='individual', annotations_position='right',
                           orientation='horizontal',
                           dir_fileName=None, vLines=None, vTexts=None, hLines=None, hTexts=None,
                           xlim=[], ylim=[], xscale='linear', yscale='linear',
                           style_dict=style_dict, mpl='barchart_horizontal', colorScheme='UniS', variation='color',
                           savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                           fig=fig, ax=ax)

    return fig, ax


if __name__ == "__main__":
    sample_stacked()
    sample_grouped()
