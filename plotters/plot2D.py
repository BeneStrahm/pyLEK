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

import plotters.pythonHelperPlot2DStyle as pltstyle

# ----------------------------------------------------------------------
# Parameter List
# ----------------------------------------------------------------------
# variation
# - 'color'
# - 'linestyle'
#
# colorScheme
# - 'UniS'
# - 'Monochrome'
#
# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def plot2D(x,y, xlabel, ylabel, title, legend, dir_fileName=None, 
           xlim=[], ylim=[], xscale='linear', yscale='linear',
           style_dict={}, colorScheme='Monochrome', variation='color',
           fileFormat=None, transparent=True, usetex=False, alphaLines=1.0):

    """Plotting 2-D Lines (x,y-plot) on one figure in a uniform style

    :param x: list w/ data to plot, with shape [n_row, datapoints]
    :param y: list w/ data to plot, with shape [n_row, datapoints]
    :param xlabel: string w/ labels for x axis
    :param xlabel: string w/ labels for y axis
    :param title: string w/ plot title
    :param legend: list w/ legends [n]
    :param dir_fileName: string w/ Directory / Filename to save to,  
                         must be specified when fileFormat is specified
    :param xlim: list w/ limits  for x axis [xmin, xmax]
    :param ylim: list w/ limits  for y axis [ymin, ymax]
    :param xscale: string w/ scales acc. to matplotlib
    :param yscale: string w/ scales acc. to matplotlib
    :param style_dict: dict w/ settings to overwrite mplstyle-template
    :param colorScheme: string ('Monochrome', 'UniS')
    :param variation: string ('color', 'linestyle')
    :param fileFormat: list w/ strings ('svg', 'png', 'pdf', 'pkl', None)
    :param usetex: bool true if background should be transparent
    :param transparent: bool true to use Latex-text layout
    :param alphaLines: float w/ line thickness
    """

    # Modify plot styles 
    pltstyle.modifyPlotStyle(style_dict)

    # Get the plot styles
    pltstyle.retrievePlotStyle(style_dict)

    # Create color / linestyles
    customCycler = pltstyle.setLineStyle(colorScheme, variation)

    # Prepare Plots
    x = np.transpose(x)
    y = np.transpose(y)

    # Set to use Latex-text layout
    mpl.rc('text', usetex=usetex)

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
    ax.plot(x,y,label ='label', alpha=alphaLines) 

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
    
    # Save plot as pdf
    if not fileFormat == None:
        if "pdf" in fileFormat:
            plt.savefig(dir_fileName + ".pdf", format="pdf", transparent=transparent) 
        
        # Save plot as png
        elif "png" in fileFormat:
            plt.savefig(dir_fileName + ".png", format="png", transparent=transparent)  

        # Save plot as 
        elif "svg" in fileFormat:
            plt.savefig(dir_fileName + ".svg", format="svg", transparent=transparent)

        # Save plot with pickle
        elif "pkl" in fileFormat:
            pkl.dump(ax, open(dir_fileName + ".pickle", "wb"))
    
    # Show plot in interactive mode
    else:
        plt.show()
    
    # Clean up mplstyles
    pltstyle.cleanPlotStyle()

    # Clean up everything
    plt.clf()
    plt.close()
    

# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

def testPlot():
    x = np.linspace(0, 2 * np.pi, 50)
    offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    y = np.transpose([np.sin(x + phi) for phi in offsets])

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"

    title = "Test Title"

    legend = ["testdata1","testdata2","testdata3","testdata4"]

    dir_fileName = "Testfile.svg"

    # Test dictionary for parameters
    style_dict = {"lines.linewidth":1.5}

    plot2D([x], [y[:,0],y[:,1],y[:,2],y[:,3]], xlabel, ylabel, title, legend, dir_fileName, 
           style_dict=style_dict)

    plt.show()