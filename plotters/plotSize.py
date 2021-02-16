# ------------------------------------------------------------------------------
# Description:  Calculating the figure size of a plot
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2021-02-06
# Execution:    Import functions / collections (from helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

# ----------------------------------------------------------------------
# Imported functions
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def calcFigSize(numberOfFigures=1, aspectRatio=3/2, pageWidth=21,
                leftmargin=2.5, rightmargin=2.5, spacing=0.0):
    """Size of one/multiple figures on a defined page width
    :param numberOfFigures: int w/ number of figures [cm]
    :param aspectRatio: int w/ aspect ratio of the figure
    :param pageWidth: int w/ total page margin [cm]
    :param leftmargin: int w/ left margin [cm]
    :param rightmargin: int w/ right margin [cm]
    :param spacing: int w/ spacing between the figures [cm]
    :rtype figSize: str to be inserted into style_dict
    """

    figWidth = (pageWidth-leftmargin-rightmargin) / numberOfFigures - spacing
    figHeight = figWidth * aspectRatio ** -1

    # Convert to inches
    figWidth, figHeight = figWidth / 2.54, figHeight / 2.54

    # Format as str to insert in style_dict
    figSize = str(figWidth) + ", " + str(figHeight)

    return figSize

# ----------------------------------------------------------------------
# Tests / Example
# ----------------------------------------------------------------------


def sample():
    figSize = calcFigSize()
    print("Calculated figure size: " + figSize)


if __name__ == "__main__":
    sample()
