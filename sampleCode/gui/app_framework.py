# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  ** Add here short description **
# Author:       ** Add here author's e-mail adress **
# Created:      ** Add here the date of creation **
# Execution:    Import functions / collections (from helpers import util)
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
from PyQt5 import QtWidgets, uic
import sys

from matplotlib.axes import Axes

from sampleCode.gui.mainwindow import Ui_MainWindow 

from sampleCode.foo.bar import someCode

import plotters.plot2D as plt

import numpy as np

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
        # Testdata
        x = np.linspace(0, 2 * np.pi, 50)
        offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
        y = [np.sin(x + phi) for phi in offsets]

        xlabel = "Test X Axis"
        ylabel = "Test Y Axis"

        title = "Test Title"

        vLines = [np.mean(x)]
        vTexts = ['test description']

        legend = ["testdata1", "testdata2", "testdata3", "testdata4"]

        style_dict = {"lines.linewidth": 5 }

        # Clear 
        self.gui.MplWidget.canvas.ax.clear()
        self.gui.MplWidget.canvas.ax.cla()

        # Plot
        self.gui.MplWidget.canvas.fig, self.gui.MplWidget.canvas.ax = plt.plot2D([x, x, x, x], y, xlabel, ylabel, title, legend, dir_fileName=None,
                vLines=vLines, vTexts=vTexts,
                xlim=[], ylim=[], xscale='linear', yscale='linear',
                style_dict=style_dict, mpl='default', colorScheme='UniS', variation='color',
                savePlt=False, savePkl=False, showPlt=False,
                ax=self.gui.MplWidget.canvas.ax, fig=self.gui.MplWidget.canvas.fig)
    
        # Update 
        self.gui.MplWidget.canvas.draw()

    def runTest(self): 
        # Calls the function printSomeText()
        someCode.printSomeText("You could run you own script by modifying \"def runTest(self):\"")

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
