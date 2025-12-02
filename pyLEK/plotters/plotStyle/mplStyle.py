# ----------------------------------------------------------------------
# Description:  Retrieving, modifying and cleaning default.mplStyle
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2018-12-06
# Execution:    Import functions / collections (from helpers import util)
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------

import matplotlib.pyplot as plt
import os
from pyLEK.helpers import filemanager

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def findPlotStyle(mpl):
    import __main__
    import pathlib
    import os
    import sys

    # 1) Look in pyLEK for choosen mpstyle
    try:
        # Get path of this file (..pyLEK/plotStyle)
        thisDir = os.path.dirname(os.path.realpath(__file__))

        # Search in the folder of this file (..pyLEK/plotStyle)
        mplStyles, mplPaths = filemanager.scanSubdirsForFilesWithExtension(
            thisDir, ".mplstyle")

        if mpl + ".mplstyle" in mplStyles:
            i = mplStyles.index(mpl + ".mplstyle")
            mplPath = mplPaths[i]
            mplPath = os.path.splitext(mplPath)[0]
            print('Using pyLEK-default .mplstyle: ' + mplPath)
            return mplPath
    except Exception:
        # ignore and continue searching other locations
        pass

    # 2) Look in path of __main__ file for choosen mpstyle
    try:
        main_file = getattr(__main__, "__file__", None)
        if main_file:
            mainFolder = str(pathlib.Path(main_file).parent.resolve())

            # Search in the folder and subfolders of __main__
            mplStyles, mplPaths = filemanager.scanSubdirsForFilesWithExtension(
                mainFolder, ".mplstyle")

            if mpl + ".mplstyle" in mplStyles:
                i = mplStyles.index(mpl + ".mplstyle")
                mplPath = mplPaths[i]
                mplPath = os.path.splitext(mplPath)[0]
                print('Using custom .mplstyle: ' + mplPath)
                return mplPath
    except Exception:
        pass

    # 3) Look in PYTHONPATH for choosen mpstyle
    pythonPath = os.environ.get('PYTHONPATH', '')
    if pythonPath:
        for path in pythonPath.split(os.pathsep):
            try:
                # Search in the folder and subfolders of PYTHONPATH
                mplStyles, mplPaths = filemanager.scanSubdirsForFilesWithExtension(
                    path, ".mplstyle")

                if mpl + ".mplstyle" in mplStyles:
                    i = mplStyles.index(mpl + ".mplstyle")
                    mplPath = mplPaths[i]
                    mplPath = os.path.splitext(mplPath)[0]
                    print('Using PYTHONPATH .mplstyle: ' + mplPath)
                    return mplPath
            except Exception:
                continue

    # 4) Look in installed site-packages or sys.path for choosen mpstyle
    try:
        import site
        try:
            sitePaths = site.getsitepackages()
        except Exception:
            sitePaths = []

        # include sys.path as a fallback search space
        search_paths = list(sitePaths) + list(sys.path)

        for sitePath in search_paths:
            try:
                # Search in the folder and subfolders of site-packages / sys.path entries
                mplStyles, mplPaths = filemanager.scanSubdirsForFilesWithExtension(
                    sitePath, ".mplstyle")

                if mpl + ".mplstyle" in mplStyles:
                    i = mplStyles.index(mpl + ".mplstyle")
                    mplPath = mplPaths[i]
                    mplPath = os.path.splitext(mplPath)[0]
                    print('Using site-packages .mplstyle: ' + mplPath)
                    return mplPath
            except Exception:
                continue
    except Exception:
        pass

    raise FileNotFoundError(
        f".mplstyle '{mpl}.mplstyle' not found. Please specify a valid .mplstyle")


def retrievePlotStyle(style_dict, mplpath):
    # Retrieving the current plot settings
    if bool(style_dict):
        plt.style.use(mplpath + '_temp.mplstyle')
    else:
        plt.style.use(mplpath + '.mplstyle')


def modifyPlotStyle(style_dict, mplpath):
    # Modify the plot settings
    # mplstyle-format:  key : val # optional comment

    # Read in the file and replace lines by key - values pair
    filedata = []
    with open(mplpath + '.mplstyle', 'r') as file:
        for line in file:
            skipline = False
            for key, value in style_dict.items():
                # key + ":" is necessary, otherwise eg. lines.marker and lines.markerfacecolor
                # are both replaced when only lines.marker should be modified
                if (key+":") in line:
                    filedata.append(str(key) + ' : ' + str(value) + '\n')
                    skipline = True
            if skipline == False:
                filedata.append(line)

    # Write the file out again
    with open(mplpath + '_temp.mplstyle', 'w') as file:
        for line in filedata:
            file.write(line)


def cleanPlotStyle(mplpath):
    # delete temporary mplstyles
    os.remove(mplpath + '_temp.mplstyle')
