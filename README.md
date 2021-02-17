# Python
In order to use Python you need at least an installation of Python and an Editor which allows you to comfortably edit your scripts.

## Installation
Go to https://www.python.org/downloads/ and download the latest release of python. Important: During the installation, check the box "Add Python to PATH", press -> Customize Installation and make sure that "pip" will be installed. Further it's recommended to use the "Install for all users" option.

## Editors 

### Visual Studio Code (VS)
Visual Studio Code is a lightweight but powerful source code editor to setup your Python Environment. It has a rich ecosystem of useful extensions. 

If you use Visual Studio code, you might also want to install the following extensions with it:

- Python -> In order to use Python in VS
- TODO.md Kanban Board -> To edit To-Do Lists in VS
- GitHub Pull Requests and Issues -> GitHub integration in VS
- CodeStream -> Collaboration, code discussion and review (Sign in with GitHub)
- GitLens — Git supercharged -> Tracking GitHub changes (Sign in with GitHub)
- Pylance -> Additional Python language support
- Visual Studio IntelliCode -> Offers autocomplete of syntax

In order to use GitHub within Visual Studio Code, you need to install "git" as well (https://git-scm.com/downloads). Here you can leave all settings in the installation as they are proposed.

Further you might want to use linting, therefore in VS, open the command bar (Ctrl+Shift+P), type "Python: Select Linter", confirm with enter and select "pylint"

Moreover, for simple PEP-Style conform code formatting, you can use a formatter. Therefore install one with "pip install autopep8". In VS, under Settings search for python.formatting.provider and select autopep8. To use the formatter on your code, open the command bar (Ctrl+Shift+P), type "Format:" and select the desired option.

See also https://www.youtube.com/watch?v=TILIcrrVABg for a VS complete guide

## Example
See "./sampleCode" for an exemplary code structure as we recommend it.

# pyLEK Repo
## Template
When adding new functions always respect the following template and the style guideline. Otherwise you're file will be removed. Keep the functions simple, short and comment when necessary.

    # -*- coding: utf-8 -*-
    # ------------------------------------------------------------------------------
    # Description:  ** Add here short description **
    # Author:       ** Add here author's e-mail adress **
    # Created:      ** Add here the date of creation **
    # Execution:    Import functions / collections (from pyLek.helpers import util)
    # ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------
    # Sources
    # ------------------------------------------------------------------------------ 
    # https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
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

    def sample():                                       # Sample of the function
        pass

    if __name__ == "__main__":
        sample()

## Style guideline:
https://www.python.org/dev/peps/pep-0008/

## Import modules / usage
1. Add the path of this folder (e.g. if the pyLEK folder is located under C:\Users\ac123456\GitHub\pyLEK use the path C:\Users\ac123456\GitHub) to PYTHONPATH  (Umgebungsvariable -> Nutzervariablen). 
Now you don't have to add the full path for import statements.
https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages

2. import modules, z.B: from pyLEK.helpers import pyExtras

## .gitignore / Custom scripts
Ignored files are usually build artifacts and machine generated files that can be derived from your repository source or should otherwise not be committed. Some common examples are:

- dependency caches, such as the contents of /node_modules or /packages
- compiled code, such as .o, .pyc, and .class files
- build output directories, such as /bin, /out, or /target
- files generated at runtime, such as .log, .lock, or .tmp
- hidden system files, such as .DS_Store or Thumbs.db
- personal IDE config files, such as .idea/workspace.xml

Ignored files are tracked in a special file named .gitignore that is checked in at the root of your repository. There is no explicit git ignore command: instead the .gitignore file must be edited and committed by hand when you have new files that you wish to ignore. .gitignore files contain patterns that are matched against file names in your repository to determine whether or not they should be ignored.

.gitignore also offers support for custom files. All files named with the prefix *custom*, eg "custom_plot2D.py" will be ignored for upload but will remain on your local machine. Saying you want to create your own plot2D.py, just copy the file and rename it as "custom_plot2D.py", and it will not be uploaded to the repository.

## Linked Repositories (Submodules)
The repository is using linked repositories created by third-party authors. In order to setup new submodules check out https://git-scm.com/book/en/v2/Git-Tools-Submodules

Too pull submodules, from the root of the repo just run: git submodule update --init

### robbievanleeuwen/feastruct
Structural finite element analysis, the pythonic way, see https://github.com/robbievanleeuwen/feastruct/

In order to use the module:

1. Open "cmd" as Administrator
2. With "cd" navigate to your local GitHub-Folder (e.g. C:\Users\Username\GitHub\pyLEK\feastruct) 
3. Install with py setup.py install

For the usage check out feastruct/examples

## TODO.md
The TODO.md format is based on GFM - GitHub Flavored Markdown - Task Lists. TODO.md is a file that contains tasks organized in multiple sections. Keeping a TODO.md file makes it easier for anyone wants to know about the project's plans and work needs to be done.

Tasks in TODO.md can be visualized using Kanban Board where sections become columns on the board.

### TODO.md format
- TODO.md can have multiple columns.
- Each column has tasks that start with a checkbox sign `- [ ]` or just a hyphen `- `
- Completed column name must contain `✓` or `[x]`.
- There are "2 spaces" at the end of every task title to serve as line breaks on Github pages.
- Tags, mentions, estimate, date time, ticket id, etc. can be entered at the end of the task title.
- A task with 2 space indentation in the title is a sub-task or description. 

```
# Project Name
Project Description

### Column Name
- [ ] Task title ~3d #type @name yyyy-mm-dd  
- [ ] Sub-task or description  

### Completed Column ✓
- [x] Completed task title  
```

- Checkboxes are used as described in [GFM - GitHub Flavored Markdown - Task Lists](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown) but they are optional.
- A task list without checkboxes look like this:

```
### Column Name
- Task title ~3d #type @name yyyy-mm-dd  
- Sub-task or description  

### Completed Column ✓
- Completed task title  
```

### See also
- [An example of TODO.md](TODO.md)
- [Vscode Kanban Extension](https://bit.ly/2JcrUWJ)

## Delete Repo from local machine

In order to delete the repository from your local machine, simply delete the folder. Make sure you uploaded all your changes before deleting. 

You can delete the folder in the windows explorer, or better, using git-bash (https://gitforwindows.org/), navigate to your folder, and use the command rm-rf Name_of_your_repo
