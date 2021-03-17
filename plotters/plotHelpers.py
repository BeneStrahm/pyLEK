# ------------------------------------------------------------------------------
# Description:  Calculating the figure size of a plot
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2021-02-06
# Execution:    Import functions / collections (from helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import subprocess
import os
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


def savePdf_tex(fig, dir_fileName, **kwargs):
    """ Exporting a figure to .pdf_tex via command line interface
    :param fig: fig object to be saved 
    :param dir_fileName: string w/ Directory / Filename to save to,  
                         must be specified when savePlt is specified
    """
    import matplotlib.pyplot as plt
    # Save as.pdf
    fig.savefig("temp.pdf", format="pdf", **kwargs)

    # Shell command to be called
    incmd = ["inkscape", "temp.pdf", "-export-type=pdf",
             "-export-filename={}.pdf".format(dir_fileName),
             "-export-latex"]

    # Open shell to export
    subprocess.check_output(incmd)

    # Clean up .pdf
    os.remove("temp.pdf")

def fontChecker():
    import matplotlib.pyplot as plt

    # Retrieve active font
    font_family = plt.rcParams['font.family'][0]
    font_active = plt.rcParams["font." + font_family][0]

    # Rebuild font
    import matplotlib.font_manager as font_manager 

    # Get all available fonts on the computer
    avail_Fonts= [font.name for font in font_manager.fontManager.ttflist]

    # Check if Univers for UniS has been installed
    if not (font_active in avail_Fonts):

        # Try rebuilding fonts
        font_manager._rebuild()

        # Check again
        if not (font_active in avail_Fonts):
            print("In order to use \"" + font_active + "\" first install it. Default \"" + font_family + "\" font will be used.")


# ----------------------------------------------------------------------
# Tests / Example
# ----------------------------------------------------------------------


def sample():
    figSize = calcFigSize()
    print("Calculated figure size: " + figSize)

    fontChecker()


if __name__ == "__main__":
    sample()
