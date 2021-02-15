# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  ** Add here short description **
# Author:       ** Add here author's e-mail adress **
# Created:      ** Add here the date of creation **
# Execution:    Executing from command line (py filename.py)
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
# e.g: import scipy.io
from sampleCode.foo.bar import someCode

from sampleCode.gui import app_framework
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# Example


# main() should contain code that you want to run when the file is executed
def main():
    # Calls the function printSomeText()
    someCode.printSomeText("Hello World")

    # To start gui, uncomment following line
    app_framework.start()


if __name__ == "__main__":                          # Calling main()-function when script is excecuted
    # See also https://realpython.com/python-main-function/
    main()