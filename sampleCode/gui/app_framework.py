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
        # In the class MplWidget pyLEK-plotters are imported. Therefore all objects
        # of the class MplWidget can use the pyLEK-plotters methods
        # Class MplWidget
        # -> Object MplWidget_left
        # -> Object MplWidget_right

        # See also mplwidget.py for more information

        # Using the pyLEK-plotter functions

        # Left canvas
        # -----------
        # Calling plotPieCharts w/ all available options, execute sample plot
        self.gui.MplWidget_left.plot2D(None, None, xlabel=None, ylabel=None, title=None, legend=None,
               dir_fileName=None, vLines=None, vTexts=None,  hLines=None, hTexts=None,
               xlim=[], ylim=[], xscale='linear', yscale='linear',
               style_dict={}, mpl='default', colorScheme='Monochrome', variation='color', customCycler=None,
               savePlt=False, savePkl=False, showPlt=False, saveTex=False)

        # Right canvas
        # ------------
        # Calling plotPieChart w\ options, execute sample plot
        self.gui.MplWidget_right.plotPieChart(None)

        # Calling plotBarChart w\ options, execute sample plot
        # self.gui.MplWidget_right.plotBarChart(None)

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
