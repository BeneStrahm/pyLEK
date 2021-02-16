# gui
## PyQt5
See https://www.learnpyqt.com/tutorials/first-steps-qt-creator/ or https://likegeeks.com/pyqt5-tutorial to start with the gui

For the design of the gui the PyQt5 designer is recommended.

1) Install PyQt5
pip install PyQt5

2) Install PyQt5 designer
pip install PyQt5-tools

3) Where is PyQt5 designer?
To start search for the path "..\Python\Python39\Scripts\qt5-tools.exe" and start in a terminal with  "..\Python\Python39\Scripts\qt5-tools.exe designer"

The *.ui files created with the PyQt5 designer should be converted using "pyuic5 infile.ui -o outfile.py"

## Matplotlib
Implemented according to https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5

In order to use a widget created in the PyQt5 designer in matplotlib one needs to "Promote" the blank QtWidget to a MplWidget using the header mplwidget. This works as the following:

1) Add a "widget" in the PyQt5 designer
2) Right click on the widget in the PyQt5 designer - select "Promote to" / "Als Platzhalter für benutzerdefinierte Klasse festlegen"
3) Under "Promoted Class Name" / "Klassenname" select the class name , hereinafter "MplWidget"
4) Under "Include" select the path and name to the include, hereinafter "sampleCode.gui.mplwidget"
5) Press "Promote" / "Anwenden"
6) Rename the widget-object, hereinafter "MplWidget"

You can easily create multiple widgets showing matplotlib-plots. They all (can) use the same class, since they are simply different objects of the same class. Just make sure that they have a unique object-name (E.g. here "MplWiget_left" and ".._right"), which you then use in your code (see also app_framework.py)

## Layouts
The PyQt5 designer works with layouts. This will ensure that all your widgets will be displayed and resized properly when the form is previewed or used in an application.

For more information see: https://www.learnpyqt.com/tutorials/qt-designer-gui-layout/