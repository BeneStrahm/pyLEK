# ------------------------------------------------------------------------------
# Description:  Helper functions for file/folder management
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2020-09-25
# Execution:    Import functions / collections (from pylek.helpers import util)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import os
import sys
import shutil
from typing import NamedTuple
import tkinter as tk
from tkinter import filedialog
from pyLEK.helpers.deprecated import *
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


def delFilesInFolder(fname):
    """Delete all files in a specified folder
    :param fname: string with name of folder
    """
    folder = fname
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def getPathOfFile():
    """Allows to drag&drop file on your script and read path of file, see 
    filemanager.sample_getPathOfFile for an example
    :rtype cwd: current working directory
    :rtype filepath: str w/ absolute path of file
    :rtype folderpath: str w/ absolute path of folder containing file
    """
    # Current working directory
    cwd = os.getcwd()

    try:
        # If file was dropped on script
        filePath = sys.argv[1]
        folderPath = os.path.dirname(filePath)
    except IndexError:
        # If no file was dropped on script
        print("IndexWarning: Drag&Drop file on script to read path. Returning \"None\" for filePath and folderPath")
        filePath = None
        folderPath = None

    return cwd, filePath, folderPath


@deprecated("use pyLEK.helper.filemanager.py scanFolder() instead")
def scanFolderForFiles(fname):
    pass


def scanFolder(fname):
    """Scans for all files and folders in a specified folder
    :param fname: string with name of folder
    :rtype dirpath: directory that was scanned
    :rtype dirnames: list w/ all folders in dirpath
    :rtype filenames: list w/ all files in dirpath
    """
    folder = fname
    # Walk through selected folder and scan for all files
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        f.extend(filenames)
        break
    return dirpath, dirnames, filenames


def folderDialog():
    """Opens dialog to choose a folder
    :rtype dirpath: str w/ path to folder
    """
    root = tk.Tk()
    root.withdraw()
    dirpath = filedialog.askdirectory()

    return dirpath


def fileDialog():
    """Opens dialog to choose a file
    :rtype filepath: str w/ path to file
    """
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()

    return filepath

# ------------------------------------------------------------------------------
# Samples
# ------------------------------------------------------------------------------


def sample_getPathOfFile():
    # In your script, import first
    from pyLEK.helpers import filemanager

    # Drag&Drop any file on filemanager.py to execute
    cwd, filePath, folderPath = filemanager.getPathOfFile()
    print('getcwd:      ' + cwd)
    print('filePath:    ' + str(filePath))
    print('folderPath:  ' + str(folderPath))
    input()


def sample_scanFolderForFiles():
    # In your script, import first
    from pyLEK.helpers import filemanager

    # As an example, get current working dir
    cwd = os.getcwd()

    # Execute the function
    dirpath, dirnames, filenames = filemanager.scanFolderForFiles(cwd)
    print('scanpath:   ' + dirpath)

    print('\nFound the following folders')
    for dirname in dirnames:
        print('dirnames:   ' + str(dirname))

    print('\nFound the following files')
    for filename in filenames:
        print('filename:   ' + str(filename))


def sample_folderDialog():
    # In your script, import first
    from pyLEK.helpers import filemanager

    # Execute the function
    dirpath = filemanager.folderDialog()
    print('Dirpath:   ' + dirpath)


if __name__ == "__main__":
    # sample_getPathOfFile()
    # sample_scanFolderForFiles()
    sample_folderDialog()
