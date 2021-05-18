# ------------------------------------------------------------------------------
# Description:  Helper functions to create animations
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2021-04-16
# Execution:    Executing from command line (py filename.py)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import os
from pick import pick
from pyLEK.helpers import filemanager
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


def getFiles(*, inFolder=None):
    if inFolder == None:
        inFolder = filemanager.folderDialog(title="Choose the folder containing the files to be converted")

    # Select as current wkdir
    os.chdir(inFolder)

    # Walk through selected folder and scan for all files
    dirpath, dirnames, filenames = filemanager.scanFolderForFiles(os.getcwd())

    return inFolder, filenames


def pngToMp4(*, inFolder=None):
    # Get folder & list of files
    inFolder, filenames = getFiles(inFolder=inFolder)

    # Animation name = name of selected folder
    outFile = os.path.split(inFolder)[-1]

    # Time step between frames
    fps = int(input("Enter Frames per second [FPS]: "))

    # Create animation and save as *.mp4
    import imageio
    with imageio.get_writer(outFile + '.mp4', mode='I', fps=fps) as writer:
        for filename in filenames:

            # Select only *.png files
            if filename.endswith(".png"):
                print(filename)
                image = imageio.imread(filename)
                writer.append_data(image)

    print('.. were converted to \"' + outFile + '.mp4\" in path \"' + inFolder + '\"')


def pngToGif(*, inFolder=None):
    # Get folder & list of files
    inFolder, filenames = getFiles(inFolder=inFolder)

    # Animation name = name of selected folder
    outFile = os.path.split(inFolder)[-1]

    # Time step between frames
    dT = float(input("Enter time between Frames in seconds [dT]: "))
    # Create animation and save as *.mp4
    import imageio
    with imageio.get_writer(outFile + '.gif', mode='I', duration=dT) as writer:
        for filename in filenames:

            # Select only *.png files
            if filename.endswith(".png"):
                print(filename)
                image = imageio.imread(filename)
                writer.append_data(image)

    print('.. were converted to \"' + outFile + '.gif\" in path \"' + inFolder + '\"')

if __name__ == "__main__":
    # Opens user dialog to select functions from predefined list
    title = 'Please choose conversion option'
    options = ['pngToMp4', 'pngToGif']
    option, index = pick(options, title)

    {
        'pngToMp4':  pngToMp4,
        'pngToGif':  pngToGif,
    }.get(option)()

