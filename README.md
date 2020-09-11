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
        """Get keys of a dictionary				        # Description of function

        :param dict: Dictonary to read from			    # Type & description of input
        :rtype keys: List of keys in the dictionary	    # Type & description of return
        """
        return dict.keys() 					            # Actual Function statements

# II. Style guideline:
https://www.python.org/dev/peps/pep-0008/

# III. Import modules / usage
1. Add the path of this folder to PYTHONPATH  (Umgebungsvariable -> Nutzervariablen). Now you don't have to add the full path for import statements.
https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages

2. import modules, z.B: from helper import pyExtras

# IV. Linked Repositories (Submodules)
The repository is using linked repositories created by third-party authors. In order to setup these submodules check out https://git-scm.com/book/en/v2/Git-Tools-Submodules

## a) robbievanleeuwen/feastruct
Structural finite element analysis, the pythonic way, see https://github.com/robbievanleeuwen/feastruct/

In order to use the module:

1. Open "cmd" as Administrator
2. With "cd" navigate to your local GitHub-Folder (e.g. C:\Users\Username\GitHub\ILEK-py-helpers\feastruct) 
3. Install with py setup.py install

For the usage check out feastruct/examples