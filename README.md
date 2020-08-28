# ILEK-py-helpers

# I. Template
When adding new functions always respect the following template and the style guideline. Otherwise you're file will be removed. Keep the functions simple, short and comment when necessary.

    # ------------------------------------------------------------------------------
    # Description:  ** Add here short description **
    # Author:       ** Add here author's e-mail adress **
    # Created:      ** Add here the date of creation **
    # Execution:    Import functions / collections (from helpers.util import func)
    # ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------
    # Libraries
    # ------------------------------------------------------------------------------                                                          

    # Example
    import scipy.io

    # ------------------------------------------------------------------------------
    # Functions
    # ------------------------------------------------------------------------------

    # Example
    def getList(dict): 
        """Get keys of a dictionary				# Description of function
        :param dict: Dictonary to read from			# Type & description of input
        :rtype keys: List of keys in the dictionary		# Type & description of return
        """
        return dict.keys() 					# Actual Function statements

# II. Style guideline:
https://www.python.org/dev/peps/pep-0008/

# III. Import modules / usage
1. Add the path of this folder to PYTHONPATH  (Umgebungsvariable -> Nutzervariablen). Now you don't have to add the full path for import statements.
https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages

2. import modules, z.B: from helper import pyExtras

