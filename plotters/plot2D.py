# ------------------------------------------------------------------------------
# Description:  Plotting 2-D Lines on one figure
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from helpers.util import func)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------  

import matplotlib.pyplot as plt
import matplotlib as mpl
import pickle as pkl
import numpy as np

# ----------------------------------------------------------------------
# Imported functions
# ----------------------------------------------------------------------

import plotters.plotStyle.colorCycler as colorCycler
import plotters.plotStyle.mplStyle as mplStyle

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def plot2D(x, y, xlabel, ylabel, title, legend, dir_fileName=None,
           vLines = None, vTexts = None,  
           xlim=[], ylim=[], xscale='linear', yscale='linear',
           style_dict={}, mpl='default', colorScheme='Monochrome', variation='color',
           savePlt=False, savePkl=False, showPlt=False):

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
    :param xlim: list w/ limits  for x axis [xmin, xmax]
    :param ylim: list w/ limits  for y axis [ymin, ymax]
    :param xscale: string w/ scales acc. to matplotlib
    :param yscale: string w/ scales acc. to matplotlib
    :param style_dict: dict w/ settings to overwrite mplstyle-template
    :param mpl: string w/ name of the mplstyle-sheet
    :param colorScheme: string ('Monochrome', 'UniS')
    :param variation: string ('color', 'linestyle')
    :param savePkl: bool true to save plot 
    :param savePkl: bool true to save as .pickle
    :param showPlt: bool true show plot in interactive mode
    """

    # Modify plot styles 
    mplStyle.modifyPlotStyle(style_dict, mpl)

    # Get the plot styles
    mplStyle.retrievePlotStyle(style_dict, mpl)

    # Create color / linestyles
    customCycler = colorCycler.createCycler(colorScheme, variation)

    # Prepare Plots
    x = np.transpose(x)
    y = np.transpose(y)

    # An empty figure with one axe 
    fig, ax = plt.subplots()  

    # Setting the title of the axe-object             
    ax.set_title(title)            

    # Setting the x-axis / y-axis label of the axe-object             
    ax.set_xlabel(xlabel)    
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

    # 2D - Plot of the axe-object  
    ax.plot(x,y,label ='label') 

    # Correctly ordering legend entries by replacing labels with entries 
    # from the legend list. If this is not done there is not order in
    # the legend see: https://matplotlib.org/users/legend_guide.html
    handles, labels = ax.get_legend_handles_labels()

    for j, element in enumerate(legend, start=0):
        labels[j] = element

    # Setting the legend
    leg = ax.legend(labels)  

    # Set line thickness / transparency of the legend to standart
    for line in leg.get_lines():
        line.set_linewidth(1.5)
        line.set_alpha(1.0)
    
    # Add vertical line
    if vLines:
        for vLine in vLines:
            # Add vertical line to ax
            ax.axvline(vLine, linestyle="--", linewidth=1.0, marker="None", color='black', \
                       zorder=len(labels)+1)

    if vTexts:
        for vLine, vText in zip(vLines, vTexts):
            # Add Text to lines
                ax.text(vLine, 0.98 * (ax.get_ylim()[1] - ax.get_ylim()[0]) + ax.get_ylim()[0], \
                    vText, rotation=90, rotation_mode='anchor', \
                    horizontalalignment='right',verticalalignment='bottom', \
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
    
    # Show plot in interactive mode
    if showPlt == True:
        plt.show()
    
    # Clean up mplstyles
    mplStyle.cleanPlotStyle(mpl)

    # Clean up everything
    plt.clf()
    plt.close()
    

# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

def sample():
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    y = [np.sin(x + phi) for phi in offsets]

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"

    title = "Test Title"

    vLines = [np.mean(x)]
    vTexts = ['test description']

    legend = ["testdata1","testdata2","testdata3","testdata4"]

    # Test dictionary for parameters
    style_dict = {"lines.linewidth":5, "savefig.format":"pdf"}

    dir_fileName = "test"

    plot2D([x, x, x, x] , y, xlabel, ylabel, title, legend, dir_fileName=dir_fileName,
           vLines = vLines, vTexts = vTexts,  
           xlim=[], ylim=[], xscale='linear', yscale='linear',
           style_dict=style_dict, mpl='default', colorScheme='Monochrome', variation='color',
           savePlt=False, savePkl=False, showPlt=True)

if __name__ == "__main__":
    sample()