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
import seaborn as sns
import matplotlib.cm as cm
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


def plot3D_trisurf(x, y, z, *, xlabel=None, ylabel=None, zlabel=None, title=None, legend=None,
                   dir_fileName=None, colorbar=True, colorbar_loc='left',
                   xlim=[], ylim=[], zlim=[], xscale='linear', yscale='linear', zscale='linear',
                   style_dict={}, mpl='_3D', colormap='plasma',
                   savePlt=False, savePkl=False, showPlt=False, saveTex=False,
                   fig=None, ax=None):
    """Plotting Surface plots (x,y,z-plot) using triangulation on one figure in a uniform style
    :param x: list w/ data to plot, with shape [datapoints] - 1D-Data
    :param y: list w/ data to plot, with shape [datapoints] - 1D-Data
    :param y: list w/ data to plot, with shape [datapoints] - 1D-Data
    :param xlabel: string w/ labels for x axis
    :param ylabel: string w/ labels for y axis
    :param zlabel: string w/ labels for z axis
    :param title: string w/ plot title
    :param legend: list w/ legends [n]
    :param dir_fileName: string w/ Directory / Filename to save to,
                         must be specified when savePlt is specified
    :param xlim: list w/ limits  for x axis [xmin, xmax]
    :param ylim: list w/ limits  for y axis [ymin, ymax]
    :param zlim: list w/ limits  for z axis [zmin, zmax]
    :param xscale: string w/ scales acc. to matplotlib
    :param yscale: string w/ scales acc. to matplotlib
    :param style_dict: dict w/ settings to overwrite mplstyle-template
    :param mpl: string w/ name of the mplstyle-sheet
    :param colormap: Seaborn Colorpalette name
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

    # An empty figure with one axe
    if fig is None:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

    # Setting the title of the axe-object
    if not (title is None):
        ax.set_title(title)

    # Setting the x-axis / y-axis label of the axe-object
    if not (xlabel is None):
        ax.set_xlabel(xlabel)
    if not (ylabel is None):
        ax.set_ylabel(ylabel)
    if not (zlabel is None):
        ax.set_zlabel(zlabel)

    # Setting the x-axis / y-axis limits of the axe-object
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    if zlim:
        ax.set_ylim(ylim)

    # Setting the x-axis / y-axis scale of the axe-object
    if xscale:
        ax.set_xscale(xscale)
    if yscale:
        ax.set_yscale(yscale)
    if zscale:
        ax.set_zscale(yscale)

    # Create color / linestyles
    if colormap is None:
        cmap = sns.color_palette("plasma", as_cmap=True)  # Get a CMap
    else:
        cmap = sns.color_palette(colormap, as_cmap=True)  # Get a CMap

    # Trisurf-plot of the axe-object
    ax.plot_trisurf(x, y, z, label='label', edgecolor='none', linewidth=0,
                    antialiased=True, cmap=cmap)

    if colorbar:
        m = cm.ScalarMappable(cmap=cmap)
        fig.colorbar(m, ax=ax, location=colorbar_loc, shrink=0.5, )

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
    # only show plot with custom size
    # Example for DIN A4 Page with left and right margin of 2.5cm
    # figure size is always in inches (1 in = 2.54 cm)
    n_angles = 36
    n_radii = 8
    min_radius = 0.25
    radii = np.linspace(min_radius, 0.95, n_radii)

    angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi/n_angles

    # Map radius, angle pairs to x, y, z points.
    x = (radii*np.cos(angles)).flatten()
    y = (radii*np.sin(angles)).flatten()
    z = (np.cos(radii)*np.cos(angles*3.0)).flatten()

    xlabel = "Test X Axis"
    ylabel = "Test Y Axis"
    zlabel = "Test Y Axis"

    title = "Test Title"

    figSize = plotHelpers.calcFigSize()

    style_dict = {"figure.figsize": figSize, "lines.linewidth": 5, }

    # plot2D w/ all available options
    fig, ax = plot3D_trisurf(x, y, z, xlabel=xlabel, ylabel=ylabel, zlabel=zlabel, title=title, legend=None,
                             dir_fileName=None, colorbar=True, colorbar_loc='left',
                             xlim=[], ylim=[], zlim=[], xscale='linear', yscale='linear', zscale='linear',
                             style_dict=style_dict, mpl='_3D', colormap='crest',
                             savePlt=False, savePkl=False, showPlt=showPlt, saveTex=False,
                             fig=fig, ax=ax)

    return fig, ax


if __name__ == "__main__":
    sample_1()
