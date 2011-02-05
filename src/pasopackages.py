#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Author: Read AUTHORS file.
#License: Read COPYING file.



from PyQt4 import *
from ui_pasopackagesgroup import Ui_GroupBox
from engine.pasofile.types import packageList



#t = gettext.translation(const.APP_NAME, const.APP_I18NDIR, fallback = True)
#_ = t.ugettext




class pasoPackages(QtGui.QGroupBox, Ui_GroupBox):


    def __init__(self):
        #
        QtGui.QGroupBox.__init__(self)
        self.setupUi(self)

        self.changed = False
        self.__packages = packageList()

        QtCore.QObject.connect(self.listWidget,  QtCore.SIGNAL("QListWidgetItem *"),  self.__onChange)






    def setFromList(self, lst):
        for pkg in lst:
            self.__packages.addFile(pkg)
        self.listWidget.addItems(lst)
        self.changed = False




    def getPackages(self):
        return(self.__packages)




    def getFileList(self):
        return(self.__packages.files.keys())




    def __onChange(self, string=""):
        self.changed = True





