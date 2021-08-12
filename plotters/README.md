# plotters

For each plot (lineplots, histograms, bar charts...) a different function shall be used.

Currently implemented are:

    [X] 2D Plots - plot2D.py

        [X] w/ lines and/or markers

    [X] Bar Chart - plotBarChart.py

        [X] stacked: horizontal & vertical
    
        [X] grouped: horizontal & vertical 

    [X] Pie Chart - plotPieChart.py

        [X] w/ inner and outer pies

In each corresponding .py script at the very end there are examples (def sample():) of the functionality which can be displayed when executing the respective .py script.

All plotters can be customized if desired. In this case, copy the script, e.g. plot2D.py and give it your own name. Your custom script will not be uploaded to github since they are excluded via the plotters/.gitignore

## mpl-styles

All the plots use the same plot styles from ./plotStyle. As style template so called mpl-style sheets are used (https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html)

All settings for the default plots style are saved in the *.mplstyle-files. 

Custom plots can be configured:

1) Using style_dict (Prefered)
By modifying default.mplstyle with the style_dict passed by the plot function. See plot2D.py - sample_1(), where the style-dict is used to change the linewidth.

2) Using .mplstyle in pyLEK
By creating an own mplstyle-sheet and specifying it in the plot function. In this case, copy or create a style sheet, e.g. _myStyle.mpystyle and give it your own name. Your own sheets are not uploaded to github since they are excluded via the plotters/.gitignore. In the params of the plot function, change *mpl=...* to *mpl=_myStyle*, then your style template will be used.

3) Using .mplstyle in project folder (Prefered)
Same as 2), but this time save the .mplstyle-file in an arbitrary folder, e.g. "plotStyle". The folder needs to be placed in the same folder, where your __main__.py is located. Also here, in the params of the plot function, change *mpl=...* to *mpl=_myStyle*, then your style template will be used. 

The advantage of this approach is that your style will be included within your project, so everybody working with your project will be able to use it. An example can be found in sampleCode/plotStyle and foo/bar/somePlot.py.

## LaTeX support

All plots support the option to export a .pdf from matplotlib and then use Inkscape through the command line interface to let Inkscape create a .pdf_tex.

The .pdf_tex file can then be imported to LaTeX. 

The advantage here is that your LaTeX-Document will take care about the styling of the figure. E.g. the font in the figure will be the same as you set in your LaTeX-Document. Also you can save LaTeX-Code with matplotlib in your figure which LaTeX will then compile, which can be helpful e.g when using mathematical expressions.

Requirements:
- Inkscape installation (https://inkscape.org/de/)
- Configuration of the PATH variable for Inkscape (https://www.danielherber.com/guides.php?option=latex-inkscape)

## Fonts

In order to use the official Univers for UniS font, download the font (https://ilias3.uni-stuttgart.de/goto_Uni_Stuttgart_crs_970352.html) and install it.

Windows: Choose the option "Install for all users" to install the font in "C:\Windows\Fonts", otherwise matplotlib might have troubles finding it.

## Figure Size

To fit one or multiple figures to a specified page width see plotSize.py

## Pickle

In order to combine multiple plots after plotting, you can use pickle. This can be particularly useful when having set up an automatized routine that generates multiple plots which you want to combine later on. 

mergePicklePlots.py is an example on how to use pickle to load existing plots and replot them.

The work flow looks as the following:

1) Create plots with the plotters using the option savePkl = True
2) Copy all plots you want to combine into a folder
3) Copy mergePicklePlots.py into the folder and customize it to your needs
4) Use again the plotters to plot the figures loaded with mergePicklePlots.py
