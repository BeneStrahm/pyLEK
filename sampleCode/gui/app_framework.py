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
# e.g: https://www.ilek.uni-stuttgart.de/
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
# Contains all imported modules / functions
# PyQt5 gui
from PyQt5 import QtWidgets, uic
from pyLEK.sampleCode.gui.mainwindow import Ui_MainWindow

# python modules
import sys
import numpy as np

# pyLEK/helpers
from pyLEK.sampleCode.foo.bar import someCode
import pyLEK.plotters.plot2D as plt

# ------------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------------


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # Here we declare that the MainWindow class inherits from
        # QtWidgets.QMainWindow, Ui_MainWindow
        super().__init__(*args, **kwargs)

        # Initialize gui
        self.gui = Ui_MainWindow()

        # Setup gui
        self.gui.setupUi(self)

        # 1. Example: Connect input widgets
        self.gui.lineEdit_edit.textChanged.connect(self.lineEditDisplayText)

        # 2. Example: Connect input widgets
        self.gui.spinBox_edit.valueChanged.connect(self.spinBoxDisplayText)

        # Example: Pressing run button and execute script
        self.gui.pushButton_run.clicked.connect(self.runTest)

        # Example: Create a plot
        self.gui.pushButton_plot.clicked.connect(self.plotData)

    def plotData(self):
        # Left canvas
        # -----------
        # Clear
        self.gui.MplWidget_left.canvas.ax.clear()
        self.gui.MplWidget_left.canvas.ax.cla()

        # Plotting: Pass the MplWidget.canvas.fig / ..ax object to the sample plot defined
        # in plot2D.py. The sample plot then calls the plot2D-function, which modifies and returns the
        # MplWidget.canvas.fig / ..ax object

        self.gui.MplWidget_left.canvas.fig, self.gui.MplWidget_left.canvas.ax = plt.sample_1(
            showPlt=False, fig=self.gui.MplWidget_left.canvas.fig, ax=self.gui.MplWidget_left.canvas.ax)

        # In order to set up your own plot, use the following scheme
        # self.gui.MplWidget_left.canvas.fig, self.gui.MplWidget_left.canvas.ax = plt.plot2D(
        #     x, y, *keyargs, fig=self.gui.MplWidget_left.canvas.fig, ax=self.gui.MplWidget_left.canvas.ax)

        # Update
        self.gui.MplWidget_left.canvas.draw()

        # Right canvas
        # ------------
        # Clear
        self.gui.MplWidget_right.canvas.ax.clear()
        self.gui.MplWidget_right.canvas.ax.cla()

        # Plotting
        self.gui.MplWidget_right.canvas.fig, self.gui.MplWidget_right.canvas.ax = plt.sample_2(
            showPlt=False, fig=self.gui.MplWidget_right.canvas.fig, ax=self.gui.MplWidget_right.canvas.ax)
        
        # In order to save the plot, recall the plot function but without passing fig, ax
        # Like this, the plot style will be according to the desired .mplstyle
        # In case of the example: 
        plt.sample_2(showPlt=False, fig=None, ax=None)

        # For your own plot:
        # plt.plot2D(x, y, *keyargs, savefig=True, fig=None, ax=None)

        # Internal note: An alternative would be to "copy" and "recreate" the ax object in the 
        # plot function.
        # See https://stackoverflow.com/questions/6309472/matplotlib-can-i-create-axessubplot-objects-then-add-them-to-a-figure-instance

        # Update
        self.gui.MplWidget_right.canvas.draw()

    def runTest(self):
        # Calls the function printSomeText()
        someCode.printSomeText(
            "You could run you own script by modifying \"def runTest(self):\"")

    def lineEditDisplayText(self):
        lineEditText = self.gui.lineEdit_edit.text()
        self.gui.lineEdit_display.setText("You wrote: " + lineEditText)

    def spinBoxDisplayText(self):
        spinBoxValue = self.gui.spinBox_edit.value()
        spinBoxValue = spinBoxValue * 2
        self.gui.spinBox_display.setValue(spinBoxValue)


def start():
    """Starting the application
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
