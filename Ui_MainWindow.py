# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushNightclub = QtWidgets.QPushButton(self.centralwidget)
        self.pushNightclub.setGeometry(QtCore.QRect(20, 30, 86, 26))
        self.pushNightclub.setObjectName("pushNightclub")
        self.progressNightclub = QtWidgets.QProgressBar(self.centralwidget)
        self.progressNightclub.setGeometry(QtCore.QRect(120, 30, 118, 23))
        self.progressNightclub.setProperty("value", 24)
        self.progressNightclub.setObjectName("progressNightclub")
        self.labelNightclubStart = QtWidgets.QLabel(self.centralwidget)
        self.labelNightclubStart.setGeometry(QtCore.QRect(260, 30, 101, 21))
        self.labelNightclubStart.setObjectName("labelNightclubStart")
        self.labelNightclubEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelNightclubEnd.setGeometry(QtCore.QRect(370, 30, 101, 21))
        self.labelNightclubEnd.setObjectName("labelNightclubEnd")
        self.labelNightclubRem = QtWidgets.QLabel(self.centralwidget)
        self.labelNightclubRem.setGeometry(QtCore.QRect(500, 30, 101, 21))
        self.labelNightclubRem.setObjectName("labelNightclubRem")
        self.labelHeadingStart = QtWidgets.QLabel(self.centralwidget)
        self.labelHeadingStart.setGeometry(QtCore.QRect(260, 0, 101, 21))
        self.labelHeadingStart.setObjectName("labelHeadingStart")
        self.labelHeadingRem = QtWidgets.QLabel(self.centralwidget)
        self.labelHeadingRem.setGeometry(QtCore.QRect(500, 0, 101, 21))
        self.labelHeadingRem.setObjectName("labelHeadingRem")
        self.labelHeadingEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelHeadingEnd.setGeometry(QtCore.QRect(370, 0, 101, 21))
        self.labelHeadingEnd.setObjectName("labelHeadingEnd")
        self.pushBunker = QtWidgets.QPushButton(self.centralwidget)
        self.pushBunker.setGeometry(QtCore.QRect(20, 70, 86, 26))
        self.pushBunker.setObjectName("pushBunker")
        self.labelBunkerStart = QtWidgets.QLabel(self.centralwidget)
        self.labelBunkerStart.setGeometry(QtCore.QRect(260, 70, 101, 21))
        self.labelBunkerStart.setObjectName("labelBunkerStart")
        self.labelBunkerRem = QtWidgets.QLabel(self.centralwidget)
        self.labelBunkerRem.setGeometry(QtCore.QRect(500, 70, 101, 21))
        self.labelBunkerRem.setObjectName("labelBunkerRem")
        self.progressBunker = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBunker.setGeometry(QtCore.QRect(120, 70, 118, 23))
        self.progressBunker.setProperty("value", 24)
        self.progressBunker.setObjectName("progressBunker")
        self.labelBunkerEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelBunkerEnd.setGeometry(QtCore.QRect(370, 70, 101, 21))
        self.labelBunkerEnd.setObjectName("labelBunkerEnd")
        self.pushCoke = QtWidgets.QPushButton(self.centralwidget)
        self.pushCoke.setGeometry(QtCore.QRect(20, 110, 86, 26))
        self.pushCoke.setObjectName("pushCoke")
        self.labelCokeStart = QtWidgets.QLabel(self.centralwidget)
        self.labelCokeStart.setGeometry(QtCore.QRect(260, 110, 101, 21))
        self.labelCokeStart.setObjectName("labelCokeStart")
        self.labelCokeRem = QtWidgets.QLabel(self.centralwidget)
        self.labelCokeRem.setGeometry(QtCore.QRect(500, 110, 101, 21))
        self.labelCokeRem.setObjectName("labelCokeRem")
        self.progressCoke = QtWidgets.QProgressBar(self.centralwidget)
        self.progressCoke.setGeometry(QtCore.QRect(120, 110, 118, 23))
        self.progressCoke.setProperty("value", 24)
        self.progressCoke.setObjectName("progressCoke")
        self.labelCokeEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelCokeEnd.setGeometry(QtCore.QRect(370, 110, 101, 21))
        self.labelCokeEnd.setObjectName("labelCokeEnd")
        self.pushMeth = QtWidgets.QPushButton(self.centralwidget)
        self.pushMeth.setGeometry(QtCore.QRect(20, 150, 86, 26))
        self.pushMeth.setObjectName("pushMeth")
        self.labelMethStart = QtWidgets.QLabel(self.centralwidget)
        self.labelMethStart.setGeometry(QtCore.QRect(260, 150, 101, 21))
        self.labelMethStart.setObjectName("labelMethStart")
        self.labelMethRem = QtWidgets.QLabel(self.centralwidget)
        self.labelMethRem.setGeometry(QtCore.QRect(500, 150, 101, 21))
        self.labelMethRem.setObjectName("labelMethRem")
        self.progressMeth = QtWidgets.QProgressBar(self.centralwidget)
        self.progressMeth.setGeometry(QtCore.QRect(120, 150, 118, 23))
        self.progressMeth.setProperty("value", 24)
        self.progressMeth.setObjectName("progressMeth")
        self.labelMethEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelMethEnd.setGeometry(QtCore.QRect(370, 150, 101, 21))
        self.labelMethEnd.setObjectName("labelMethEnd")
        self.pushCash = QtWidgets.QPushButton(self.centralwidget)
        self.pushCash.setGeometry(QtCore.QRect(20, 190, 86, 26))
        self.pushCash.setObjectName("pushCash")
        self.labelCashStart = QtWidgets.QLabel(self.centralwidget)
        self.labelCashStart.setGeometry(QtCore.QRect(260, 190, 101, 21))
        self.labelCashStart.setObjectName("labelCashStart")
        self.labelCashRem = QtWidgets.QLabel(self.centralwidget)
        self.labelCashRem.setGeometry(QtCore.QRect(500, 190, 101, 21))
        self.labelCashRem.setObjectName("labelCashRem")
        self.progressCash = QtWidgets.QProgressBar(self.centralwidget)
        self.progressCash.setGeometry(QtCore.QRect(120, 190, 118, 23))
        self.progressCash.setProperty("value", 24)
        self.progressCash.setObjectName("progressCash")
        self.labelCashEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelCashEnd.setGeometry(QtCore.QRect(370, 190, 101, 21))
        self.labelCashEnd.setObjectName("labelCashEnd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset_All_Timers = QtWidgets.QAction(MainWindow)
        self.actionReset_All_Timers.setObjectName("actionReset_All_Timers")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionReset_All_Timers)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushNightclub.setText(_translate("MainWindow", "Nightclub"))
        self.labelNightclubStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelNightclubEnd.setText(_translate("MainWindow", "TextLabel"))
        self.labelNightclubRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelHeadingStart.setText(_translate("MainWindow", "Start Time"))
        self.labelHeadingRem.setText(_translate("MainWindow", "Time Remaining"))
        self.labelHeadingEnd.setText(_translate("MainWindow", "End Time"))
        self.pushBunker.setText(_translate("MainWindow", "Bunker"))
        self.labelBunkerStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelBunkerRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelBunkerEnd.setText(_translate("MainWindow", "TextLabel"))
        self.pushCoke.setText(_translate("MainWindow", "Coke"))
        self.labelCokeStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelCokeRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelCokeEnd.setText(_translate("MainWindow", "TextLabel"))
        self.pushMeth.setText(_translate("MainWindow", "Meth"))
        self.labelMethStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelMethRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelMethEnd.setText(_translate("MainWindow", "TextLabel"))
        self.pushCash.setText(_translate("MainWindow", "Cash"))
        self.labelCashStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelCashRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelCashEnd.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionReset_All_Timers.setText(_translate("MainWindow", "Reset All Timers"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

