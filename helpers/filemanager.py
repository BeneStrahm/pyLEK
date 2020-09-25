# ------------------------------------------------------------------------------
# Description:  Helper functions for file/folder management
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      2020-09-25
# Execution:    Import functions / collections (from helpers.util import func)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------                                                          
import os, shutil
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