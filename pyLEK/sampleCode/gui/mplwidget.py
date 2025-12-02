# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  Framework for custom application
# Author:       ** Add here author's e-mail adress **
# Created:      ** Add here the date of creation **
# Execution:    Import functions / collections (from pyLEK.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Sources
# ------------------------------------------------------------------------------
# Literature / Website ressources
# https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5/44029435#44029435
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
# Contains all imported modules / functions

from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib

# pyLEK/helpers
import plotters.plot2D as plot2D
import plotters.plotBarChart as plotBarChart
import plotters.plotPieChart as plotPieChart

# ------------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------------

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure


class MplCanvas(Canvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(tight_layout=True)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

# Matplotlib widget left


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.toolbar = NavigationToolbar(self.canvas, self) # Create corresponding mpl toolbar
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.toolbar)
        self.setLayout(self.vbl)

    # Using the pyLEK-plotter functions
    def plot2D(self, x, y, *, xlabel=None, ylabel=None, title=None, legend=None,
               dir_fileName=None, vLines=None, vTexts=None,  hLines=None, hTexts=None,
               xlim=[], ylim=[], xscale='linear', yscale='linear',
               style_dict={}, mpl='_2D', colorScheme='Monochrome', variation='color', customCycler=None,
               savePlt=False, savePkl=False, showPlt=False, saveTex=False):
        # Clear
        self.canvas.ax.clear()
        self.canvas.ax.cla()

        # Plotting: Pass the canvas.fig / ..ax object to the sample plot defined
        # in plot2D.py. The sample plot then calls the plot2D-function, which modifies and returns the
        # MplWidget.canvas.fig / ..ax object

        self.canvas.fig, self.canvas.ax = plot2D.sample_2(
            showPlt=False, fig=self.canvas.fig, ax=self.canvas.ax)

        # In order to set up your own plot, use the following scheme
        # self.canvas.fig, self.canvas.ax = plot2D.plot2D(
        #     x, y, *keyargs, fig=self.canvas.fig, ax=self.canvas.ax)

        # Update the canvas
        self.canvas.draw()

        # In order to save the plot, recall the plot function but without passing fig, ax
        # Like this, the plot style will be according to the desired .mplstyle

        # For demonstration plot2D.sample_2() will be used. Here savePlt is set to True
        # The plot will be saved in pyLEK\sampleCode\plot_as_pdf_example.pdf

        plot2D.sample_2(showPlt=False, fig=None, ax=None)

        # For your own plot:
        # if savePlt == True:
        #     plot2D.plot2D(x, y, *keyargs, dir_fileName='Your_file_name', savePlt=True, fig=None, ax=None)

        # Internal note: An alternative would be to "copy" and "recreate" the ax object in the
        # plot function.
        # See https://stackoverflow.com/questions/6309472/matplotlib-can-i-create-axessubplot-objects-then-add-them-to-a-figure-instance

    def plotBarChart(self, y, *, xlabel=None, ylabel=None, title=None, legend=None,
                     xticks=None, xticklabels=None, xticksrotation=None,
                     yticks=None, yticklabels=None, yticksrotation=None,
                     barChart='stacked', annotations=None, annotations_position='above',
                     orientation='vertical',
                     dir_fileName=None, vLines=None, vTexts=None,  hLines=None, hTexts=None,
                     xlim=[], ylim=[], xscale='linear', yscale='linear',
                     style_dict={}, mpl='_barchart_v', colorScheme='Monochrome', variation='color', customCycler=None,
                     savePlt=False, savePkl=False, showPlt=False, saveTex=False):
        # Clear
        self.canvas.ax.clear()
        self.canvas.ax.cla()

        # Plotting: Pass the canvas.fig / ..ax object to the sample plot defined
        # in plotBarChart.py. The sample plot then calls the plotBarChart-function, which modifies and returns the
        # MplWidget.canvas.fig / ..ax object

        self.canvas.fig, self.canvas.ax = plotBarChart.sample_grouped(
            showPlt=False, fig=self.canvas.fig, ax=self.canvas.ax)

        # In order to set up your own plot, use the following scheme
        # self.canvas.fig, self.canvas.ax = plotBarChart.plotBarChart(
        #     y, *keyargs, fig=self.canvas.fig, ax=self.canvas.ax)

        # Update the canvas
        self.canvas.draw()

        # In order to save the plot, recall the plot function but without passing fig, ax
        # Like this, the plot style will be according to the desired .mplstyle

        # For your own plot:
        # if savePlt == True:
        #     plotBarChart.plotBarChart(y, *keyargs, dir_fileName='Your_file_name', savePlt=True, fig=None, ax=None)

        # Internal note: An alternative would be to "copy" and "recreate" the ax object in the
        # plot function.
        # See https://stackoverflow.com/questions/6309472/matplotlib-can-i-create-axessubplot-objects-then-add-them-to-a-figure-instance

    def plotPieChart(self, y, *, xlabel=None, ylabel=None, title=None, legend=None,
                     xticks=None, xticklabels=None, xticksrotation=None,
                     yticks=None, yticklabels=None, yticksrotation=None,
                     barChart='stacked', annotations=None, annotations_position='above',
                     orientation='vertical',
                     dir_fileName=None, vLines=None, vTexts=None,  hLines=None, hTexts=None,
                     xlim=[], ylim=[], xscale='linear', yscale='linear',
                     style_dict={}, mpl='_piechart', colorScheme='Monochrome', variation='color', customCycler=None,
                     savePlt=False, savePkl=False, showPlt=False, saveTex=False):
        # Clear
        self.canvas.ax.clear()
        self.canvas.ax.cla()

        # Plotting: Pass the canvas.fig / ..ax object to the sample plot defined
        # in plotBarChart.py. The sample plot then calls the plotBarChart-function, which modifies and returns the
        # MplWidget.canvas.fig / ..ax object

        self.canvas.fig, self.canvas.ax = plotPieChart.sample1(
            showPlt=False, fig=self.canvas.fig, ax=self.canvas.ax)

        # In order to set up your own plot, use the following scheme
        # self.canvas.fig, self.canvas.ax = plotPieChart.plotPieChart(
        #     y, *keyargs, fig=self.canvas.fig, ax=self.canvas.ax)

        # Update the canvas
        self.canvas.draw()

        # In order to save the plot, recall the plot function but without passing fig, ax
        # Like this, the plot style will be according to the desired .mplstyle

        # For your own plot:
        # if savePlt == True:
        #     plotPieChart.plotPieChart(y, *keyargs, dir_fileName='Your_file_name', savePlt=True, fig=None, ax=None)

        # Internal note: An alternative would be to "copy" and "recreate" the ax object in the
        # plot function.
        # See https://stackoverflow.com/questions/6309472/matplotlib-can-i-create-axessubplot-objects-then-add-them-to-a-figure-instance
