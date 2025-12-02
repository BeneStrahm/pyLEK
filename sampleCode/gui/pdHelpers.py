# ------------------------------------------------------------------------------
# Description:  
# ------------------------------------------------------------------------------
# Author:       benedikt.strahm@ilek.uni-suttgart.de
# Created:      2021-07-13      (YYYY-MM-DD)
# Projekt:      Premium for Height - MA Christian Engelke
# ------------------------------------------------------------------------------
# Sources:
# https://stackoverflow.com/questions/23279125/python-pyqt4-functions-to-save-and-restore-ui-widget-values
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

import pandas as pd

# ------------------------------------------------------------------------------
# Methods
# ------------------------------------------------------------------------------


def readDataframe(filepath):
    # Read the dataframe
    df = pd.read_csv(filepath, header=0, delimiter=";", encoding="utf-8-sig")
    return df


def getAvailMaterials(df):
    # Filter column "Material" for duplicates
    materials = df.loc[:, "Material"].unique()
    return materials


def getAvailStrengthClasses(df, material):
    # Get indices of filtered selection
    idx = df['Material'] == material

    # Get cells of filtered selection
    rows = df.loc[idx]['Festigkeitsklasse']

    # Convert to list
    strengthClasses = rows.tolist()

    # strengthClasses = df[df['Material'] == material]
    return strengthClasses


def getMaterialProperties(df, strengthClass):
    # Get indices of filtered selection
    idx = df['Festigkeitsklasse'] == strengthClass

    # Get row of selected strengthClass
    row = df.loc[idx][:]

    # Convert to dict
    materialProperties = row.to_dict(orient='records')[0]

    return materialProperties