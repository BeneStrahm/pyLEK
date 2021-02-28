# plotters

For each plot (lineplots, histograms, bar charts...) a different function similar to plot2D shall be used.

See also plot2D.py testPlot() for an example of the functionality

To fit one or multiple figures to a specified page width see plotSize.py

## mpl-styles

All these use the same plot styles from ./plotStyle. As style template so called mpl-style sheets are used (https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html)

All settings for the default plot style are saved in default.mplstyle. Custom plots can be configured:

1) By modifying default.mplstyle with the style_dict passed by the plot function 

2) By creating an own mplstyle-sheet and specifying it in the plot function. Own sheets are not uploaded to github.

## LaTeX support

All plots support the option to export a .pdf from matplotlib and then use inkscape through the command line interface to let it create a .pdf_tex.

The .pdf_tex file can the be imported to LaTeX. 

Requirements:
- Inkscape installation (https://inkscape.org/de/)
- Configuration of the PATH variable for Inkscape (https://www.danielherber.com/guides.php?option=latex-inkscape)