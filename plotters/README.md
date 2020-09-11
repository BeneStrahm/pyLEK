# plotters

For each plot (lineplots, histograms, bar charts...) a different function similar to plot2D shall be used.

All these use the same plot styles from ./plotStyle. As style template so called mpl-style sheets are used (https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html)

All settings for the default plot style are saved in default.mplstyle. Custom plots can be configured:

1) By modifying default.mplstyle with the style_dict passed by the plot function 

2) By creating an own mplstyle-sheet and specifying it in the plot function. Own sheets are not uploaded to github.

See also plot2D.py testPlot() for an example of the functionality