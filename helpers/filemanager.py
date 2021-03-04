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

def sample_getPathOfFile():
    # In your script, import first
    from pyLEK.helpers import filemanager

    # Drag&Drop any file on filemanager.py to execute
    cwd, filePath, folderPath = filemanager.getPathOfFile()
    print('getcwd:      ' + cwd)
    print('filePath:    ' + str(filePath))
    print('folderPath:  ' + str(folderPath))
    input()

if __name__ == "__main__":
    sample_getPathOfFile()
