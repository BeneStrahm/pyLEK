# plotters

For each plot (lineplots, histograms, bar charts...) a different function shall be used.

Currently implemented are:

[X] 2D Plots - plot2D.py
    [X] Line Plots
    [X] Marker Plots

[X] Bar Chart - plotBarChart.py
    [X] Stacked: Horizontal & Vertical
    [X] Grouped: Horizontal & Vertical 

In each corresponding .py script at the very end there are examples (sample()) of the functionality which can be displayed when executing the respective .py script.

All plotters can be customized if desired. In this case, copy the script, e.g. plot2D.py and give it your own name. Your custom script will not be uploaded to github since they are excluded via the plotters\.gitignore

## mpl-styles

All the plots use the same plot styles from ./plotStyle. As style template so called mpl-style sheets are used (https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html)

All settings for the default plot style are saved in default.mplstyle. Custom plots can be configured:

1) By modifying default.mplstyle with the style_dict passed by the plot function 

2) By creating an own mplstyle-sheet and specifying it in the plot function. In this case, copy or create a style sheet, e.g. default.mpystyle and give it your own name. Your own sheets are not uploaded to github since they are excluded via the plotters\.gitignore

## LaTeX support

All plots support the option to export a .pdf from matplotlib and then use inkscape through the command line interface to let it create a .pdf_tex.

The .pdf_tex file can the be imported to LaTeX. 

Requirements:
- Inkscape installation (https://inkscape.org/de/)
- Configuration of the PATH variable for Inkscape (https://www.danielherber.com/guides.php?option=latex-inkscape)

## Fonts

In order to use the official Univers for UniS font, download the font (https://ilias3.uni-stuttgart.de/goto_Uni_Stuttgart_crs_970352.html) and install it.

Windows: Choose the option "Install for all users" to install the font in "C:\Windows\Fonts", otherwise matplotlib might have troubles finding it.

## Figure Size

To fit one or multiple figures to a specified page width see plotSize.py