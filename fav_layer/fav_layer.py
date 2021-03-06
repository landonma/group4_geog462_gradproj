# -*- coding: utf-8 -*-
"""
/***************************************************************************
 favLayer
                                 A QGIS plugin
 saves favorite layers
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-05-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by 2
        email                : 1
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox
from qgis.core import QgsProject
from qgis.gui import QgsFileWidget
from qgis.core import (
    QgsVectorLayer
)
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .fav_layer_dialog import favLayerDialog
import os.path
testDisplayList = [r"documents\parcel.shp", r"downloads\NLCD.tif"]
testHiddenList = [r"C:\Users\Mark\Documents\parcels.shp", r"C:\Users\Mark\downloads\NLCD.tif" ]
testFilePath = [r"C:\Users\Mark\downloads\NLCD.tif"]
class favLayer:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'favLayer_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&fav layer')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('favLayer', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.actionRun = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), "icon.png")),
            "Reload chosen plugin",
            self.iface.mainWindow()
        )
        icon_path = ':/plugins/fav_layer/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'fave layer'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&fav layer'),
                action)
            self.iface.removeToolBarIcon(action)


########################################### All of out functions should be between these###################################

    # this is what a command looks like for an object
    # self.dlf.addToListButton. then add a command after this based on those avaible from the documentation
    # https: // doc.qt.io / archives / qt - 4.8 / qpushbutton.html
    # list of objects in the UI
    # addToCanvasButton (QPushButton)
    # deleteButton (QPushButton)
    # displayedList (QListWidget)
    # fileWidget (QFileWidget)

    def getFileLocation(self):  # Mark will do this function
        '''
        This function activates when the user presses the imnport button in the interface.
        It connects to the file path widget and captures the text inside as s tring that the user saves.
        The function should use a try clause in order to make sure the path is valid.
        Also check that the file selected is a data type that can be imported. (like a feature class or raster)
        Input:The text captured by the file widget.
        Output:The file location saved as a string.
        '''
        #Connect to file path widget
        filepath = self.dlg.fileWidget.filePath() # get file path from file path widget
        selected = True
        if filepath == "": # if there is nothing in file path show the message below
            QMessageBox.question(self.dlg, 'No File Selected!',
                                 "Please select a file you want to add to the list first.", QMessageBox.Ok)
            selected = False
        if selected == True: # if there is something in filepath go to the next function
            self.addLocationToHiddenList(filepath)
    def addStringToDisplayedList(self,filepath):  # Jillian will do this function
        '''
        This function runs after getfilelocation.
        This function takes the file path string and clips it down to just the final folder and file name.
        It takes this string and saves it to the end of the displayed list and repoptutes the displayed list.
        Input:String with file path.
        Output:Updated displayed list.
        '''

        filepath = str(filepath) # converts filepath to string
        filepathsplit = filepath.split("\\") # splits it py the \\
        cleanpath = filepathsplit[-2] + '\\' + filepathsplit[-1] # recombines the last two parts (folder and file name)
        displayedList.append(cleanpath)
        with open("C:\\Users\\Mark\\Documents\\fav_layerLists\\displayedlist.txt", "w+") as f: # save displayed to txt file
            for lines in displayedList:
                f.write("%s\n" % lines)
        self.dlg.dislplayedList.addItem(cleanpath) # cleanpath to list widget in the UI

    def addLocationToHiddenList(self,filepath):  # Jillian will do this function
        '''
        This function runs after the addstringtodisplayedlist.
        This function takes the file location and adds it to the hidden list.
        Read the hidden list, append the file name to the end of the hidden list.
        Input:The file location.
        Output:Updated hidden list in the UI.
        '''
        hiddenList.append(filepath) # add full file path to hidden list
        with open("C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt", "w+") as f: # write to txt
            for lines in hiddenList:
                f.write("%s\n" % lines)
        self.addStringToDisplayedList(filepath) # next function


    def addLayerToMap(self):  # Mark will do this function
        '''
        This function runs when the user presses the add to map button.
        This function captures the index in the displayed list that the user has selected,
        then uses the string attached to the hidden list with that index and loads the file for that given path.
        First, use a try clause to see if the user has selected something.
        If the user has selected something, return the index of the displayed list to an object.
        Use the index in the hidden list to capture the string for that file.
        Check the file extension.
        Use if statements to point to the correct way of loading that file type.
        Input:The index number captured from the user.
        Output:Loads the file into QGIS.
        '''
        fileIndex3 = displayedList.index(selectedLayer) # these lines make both the usable name and index
        fileIndex = selectedLayer
        fileIndexending =fileIndex.split(".")
        fileIndexname = fileIndexending[-2]
        fileIndexending = fileIndexending[-1]
        fileIndexname = fileIndexname.split("\\")
        fileIndexname = fileIndexname[-1]

        #vlayer = QgsVectorLayer(hiddenList[fileIndex3], "layer_name_you_like", "ogr")
        if fileIndexending == "shp": # add shape file to map
            vlayer = self.iface.addVectorLayer(hiddenList[fileIndex3], fileIndexname, "ogr")
        if fileIndexending == "tif":# add tif to map
            rlayer = self.iface.QgsRasterLayer(hiddenList[fileIndex3], fileIndexname, "gdal")

    def checkForLists(self):  # Christine will do this function
        '''
        This funtion should run when the plugin loads
        This function looks in the master path for lists (hidden and displayed) that were previously saved.
        If a list is missing, this function creates a new list of that type and saves it as a global variable.
        If the file is there, it saves it to a global variable.
        Then the function populates the list box with the displayed list.
        Input:Master path of lists.
        Output:Loading the displayed list into the UI.
        '''

        hiddenExists = os.path.isfile('C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt')
        displayedExists = os.path.isfile('C:\\Users\\Mark\\Documents\\fav_layerLists\\displayedlist.txt')
        print(os.getcwd())
        global hiddenList
        if hiddenExists:
            hiddenList = [line.rstrip('\n') for line in open('C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt')]

        if not hiddenExists:
            hiddenList = open("C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt", "w+")
            hiddenList = [line.rstrip('\n') for line in open('C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt')]
        global displayedList
        if displayedExists:
            displayedList = [line.rstrip('\n') for line in open("C:\\Users\\Mark\\Documents\\fav_layerLists\\displayedlist.txt")]

        if not displayedExists:
            displayedList = open("C:\\Users\\Mark\\Documents\\fav_layerLists\\displayedlist.txt", "w+")
            displayedList = [line.rstrip('\n') for line in open("C:\\Users\\Mark\\Documents\\fav_layerLists\\displayedlist.txt")]
        print("hiddenExists "+ str(hiddenExists))

        for item in displayedList:
            self.dlg.dislplayedList.addItem(item)

    def deleteFromLists(self):
        '''
        This function activates when the user presses the "X" button.
        If the user did select soemthing, the index is saved as an object.
        The object at that index is then popped off the displayed and the hidden list.
        Then the displayed list is repopulated in the UI.
        Input:The text capture from the user selection.
        Output:Displayed list with fewer items.
        '''
        try:
            for SelectedItem in self.dlg.dislplayedList.selectedItems():
                self.dlg.dislplayedList.takeItem(self.dlg.dislplayedList.row(SelectedItem))
            indexpop = displayedList.index(selectedLayer)
            hiddenList.pop(indexpop)
            displayedList.pop(indexpop)

            with open("C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt", "w+") as f:
                for lines in hiddenList:
                    f.write("%s\n" % lines)

            with open("C:\\Users\\Mark\\Documents\\fav_layerLists\\displayedlist.txt", "w+") as f:
                for lines in displayedList:
                    f.write("%s\n" % lines)
        except:
            QMessageBox.question(self.dlg, 'No Item Selected!',
                                                "Please select an item you want to remove from the list first.", QMessageBox.Ok)

    def getSelectedString(self):
        print (self.dlg.dislplayedList.currentItem().text())
        global selectedLayer
        selectedLayer = self.dlg.dislplayedList.currentItem().text()

    #########################################################################################################################


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = favLayerDialog()
            self.checkForLists()

        self.dlg.dislplayedList.itemActivated.connect(self.getSelectedString) # get text when item is selected
        self.dlg.deleteButton.clicked.connect(self.deleteFromLists) # Delete item when X is clicked
        self.dlg.addToListButton.clicked.connect(self.getFileLocation) # Get filepath when add to favorites is clicked
        self.dlg.addToCanvasButton.clicked.connect(self.addLayerToMap) # Add layer to current map when add to canvas is clicked
        self.dlg.show() # Show the tool interface to the user



        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
