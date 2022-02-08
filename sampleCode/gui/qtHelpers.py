
# ------------------------------------------------------------------------------
# Description:  Module with functions to save & restore qt widget values
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

from helpers.filemanager import openFileDialog, saveFileDialog
from PyQt5.QtWidgets import QComboBox, QCheckBox, QLineEdit,\
    QRadioButton, QSpinBox, QDoubleSpinBox, QSlider, QListWidget
from distutils.util import strtobool
from PyQt5.QtCore import QSettings

import inspect

from pyLEK.helpers.filemanager import saveFileDialog, openFileDialog

# ------------------------------------------------------------------------------
# Methods
# ------------------------------------------------------------------------------


def guiSaveState(QMainWindow):
    # Select where to save
    filepath = saveFileDialog(filetypes=[("Initialisierungsdatei", "*.ini")])

    # Getting settings of the gui via QSettings
    settings = QSettings(filepath, QSettings.IniFormat)

    # Save values for selected QtWidgets
    for name, obj in inspect.getmembers(QMainWindow):

        # if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
        if isinstance(obj, QComboBox):
            name = obj.objectName()         # get combobox name
            index = obj.currentIndex()      # get current index from combobox
            text = obj.itemText(index)      # get the text for current index
            settings.setValue(name, text)   # save combobox selection

        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = obj.text()
            settings.setValue(name, value)

        if isinstance(obj, (QCheckBox, QRadioButton)):
            name = obj.objectName()
            state = obj.isChecked()
            settings.setValue(name, state)

        if isinstance(obj, (QSpinBox, QDoubleSpinBox, QSlider)):
            name = obj.objectName()
            value = obj.value()
            settings.setValue(name, value)

        if isinstance(obj, QListWidget):
            name = obj.objectName()
            settings.beginWriteArray(name)
            for i in range(obj.count()):
                settings.setArrayIndex(i)
                settings.setValue(name, obj.item(i).text())
                settings.endArray()


def guiRestoreState(QMainWindow):
    # Select which file to open
    filepath = openFileDialog(filetypes=[("Initialisierungsdatei", "*.ini")])

    # Getting settings of the gui via QSettings
    settings = QSettings(filepath, QSettings.IniFormat)

    # Get & restore values for selected QtWidgets
    for name, obj in inspect.getmembers(QMainWindow):
        if isinstance(obj, QComboBox):
            index = obj.currentIndex()          # get current region from combobox
            # text   = obj.itemText(index)      # get the text for new selected index
            name = obj.objectName()

            value = (settings.value(name))

            if value == "":
                continue

            # get the corresponding index for specified string in combobox
            index = obj.findText(value)

            if index == -1:  # add to list if not found
                obj.insertItems(0, [value])
                index = obj.findText(value)
                obj.setCurrentIndex(index)
            else:
                # preselect a combobox value by index
                obj.setCurrentIndex(index)

        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = settings.value(name)   # get stored value
            obj.setText(value)              # restore lineEditFile

        if isinstance(obj, (QCheckBox, QRadioButton)):
            name = obj.objectName()
            value = settings.value(name)
            if value != None:
                obj.setChecked(bool(value))

        if isinstance(obj, (QSpinBox, QSlider)):
            name = obj.objectName()
            value = settings.value(name)
            if value != None:
                obj.setValue(int(value))

        if isinstance(obj, QDoubleSpinBox):
            name = obj.objectName()
            value = settings.value(name)
            if value != None:
                obj.setValue(float(value))

        if isinstance(obj, QListWidget):
            name = obj.objectName()
            size = settings.beginReadArray(name)
            for i in range(size):
                settings.setArrayIndex(i)
                value = settings.value(name)
                if value != None:
                    obj.addItem(value)
                    settings.endArray()