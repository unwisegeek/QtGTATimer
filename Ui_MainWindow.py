# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 248)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 82, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushNightclub = QtWidgets.QPushButton(self.widget)
        self.pushNightclub.setObjectName("pushNightclub")
        self.verticalLayout.addWidget(self.pushNightclub)
        self.pushBunker = QtWidgets.QPushButton(self.widget)
        self.pushBunker.setObjectName("pushBunker")
        self.verticalLayout.addWidget(self.pushBunker)
        self.pushCoke = QtWidgets.QPushButton(self.widget)
        self.pushCoke.setObjectName("pushCoke")
        self.verticalLayout.addWidget(self.pushCoke)
        self.pushMeth = QtWidgets.QPushButton(self.widget)
        self.pushMeth.setObjectName("pushMeth")
        self.verticalLayout.addWidget(self.pushMeth)
        self.pushCash = QtWidgets.QPushButton(self.widget)
        self.pushCash.setObjectName("pushCash")
        self.verticalLayout.addWidget(self.pushCash)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(110, 30, 151, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressNightclub = QtWidgets.QProgressBar(self.widget1)
        self.progressNightclub.setProperty("value", 24)
        self.progressNightclub.setObjectName("progressNightclub")
        self.verticalLayout_2.addWidget(self.progressNightclub)
        self.progressBunker = QtWidgets.QProgressBar(self.widget1)
        self.progressBunker.setProperty("value", 24)
        self.progressBunker.setObjectName("progressBunker")
        self.verticalLayout_2.addWidget(self.progressBunker)
        self.progressCoke = QtWidgets.QProgressBar(self.widget1)
        self.progressCoke.setProperty("value", 24)
        self.progressCoke.setObjectName("progressCoke")
        self.verticalLayout_2.addWidget(self.progressCoke)
        self.progressMeth = QtWidgets.QProgressBar(self.widget1)
        self.progressMeth.setProperty("value", 24)
        self.progressMeth.setObjectName("progressMeth")
        self.verticalLayout_2.addWidget(self.progressMeth)
        self.progressCash = QtWidgets.QProgressBar(self.widget1)
        self.progressCash.setProperty("value", 24)
        self.progressCash.setObjectName("progressCash")
        self.verticalLayout_2.addWidget(self.progressCash)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(270, 0, 371, 181))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget2 = QtWidgets.QWidget(self.splitter)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelHeadingStart = QtWidgets.QLabel(self.widget2)
        self.labelHeadingStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeadingStart.setObjectName("labelHeadingStart")
        self.verticalLayout_3.addWidget(self.labelHeadingStart)
        self.labelNightclubStart = QtWidgets.QLabel(self.widget2)
        self.labelNightclubStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNightclubStart.setObjectName("labelNightclubStart")
        self.verticalLayout_3.addWidget(self.labelNightclubStart)
        self.labelBunkerStart = QtWidgets.QLabel(self.widget2)
        self.labelBunkerStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBunkerStart.setObjectName("labelBunkerStart")
        self.verticalLayout_3.addWidget(self.labelBunkerStart)
        self.labelCokeStart = QtWidgets.QLabel(self.widget2)
        self.labelCokeStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCokeStart.setObjectName("labelCokeStart")
        self.verticalLayout_3.addWidget(self.labelCokeStart)
        self.labelMethStart = QtWidgets.QLabel(self.widget2)
        self.labelMethStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMethStart.setObjectName("labelMethStart")
        self.verticalLayout_3.addWidget(self.labelMethStart)
        self.labelCashStart = QtWidgets.QLabel(self.widget2)
        self.labelCashStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCashStart.setObjectName("labelCashStart")
        self.verticalLayout_3.addWidget(self.labelCashStart)
        self.widget3 = QtWidgets.QWidget(self.splitter)
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelHeadingEnd = QtWidgets.QLabel(self.widget3)
        self.labelHeadingEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeadingEnd.setObjectName("labelHeadingEnd")
        self.verticalLayout_4.addWidget(self.labelHeadingEnd)
        self.labelNightclubEnd = QtWidgets.QLabel(self.widget3)
        self.labelNightclubEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNightclubEnd.setObjectName("labelNightclubEnd")
        self.verticalLayout_4.addWidget(self.labelNightclubEnd)
        self.labelBunkerEnd = QtWidgets.QLabel(self.widget3)
        self.labelBunkerEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBunkerEnd.setObjectName("labelBunkerEnd")
        self.verticalLayout_4.addWidget(self.labelBunkerEnd)
        self.labelCokeEnd = QtWidgets.QLabel(self.widget3)
        self.labelCokeEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCokeEnd.setObjectName("labelCokeEnd")
        self.verticalLayout_4.addWidget(self.labelCokeEnd)
        self.labelMethEnd = QtWidgets.QLabel(self.widget3)
        self.labelMethEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMethEnd.setObjectName("labelMethEnd")
        self.verticalLayout_4.addWidget(self.labelMethEnd)
        self.labelCashEnd = QtWidgets.QLabel(self.widget3)
        self.labelCashEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCashEnd.setObjectName("labelCashEnd")
        self.verticalLayout_4.addWidget(self.labelCashEnd)
        self.widget4 = QtWidgets.QWidget(self.splitter)
        self.widget4.setObjectName("widget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelHeadingRem = QtWidgets.QLabel(self.widget4)
        self.labelHeadingRem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeadingRem.setObjectName("labelHeadingRem")
        self.verticalLayout_5.addWidget(self.labelHeadingRem)
        self.labelNightclubRem = QtWidgets.QLabel(self.widget4)
        self.labelNightclubRem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNightclubRem.setObjectName("labelNightclubRem")
        self.verticalLayout_5.addWidget(self.labelNightclubRem)
        self.labelBunkerRem = QtWidgets.QLabel(self.widget4)
        self.labelBunkerRem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBunkerRem.setObjectName("labelBunkerRem")
        self.verticalLayout_5.addWidget(self.labelBunkerRem)
        self.labelCokeRem = QtWidgets.QLabel(self.widget4)
        self.labelCokeRem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCokeRem.setObjectName("labelCokeRem")
        self.verticalLayout_5.addWidget(self.labelCokeRem)
        self.labelMethRem = QtWidgets.QLabel(self.widget4)
        self.labelMethRem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMethRem.setObjectName("labelMethRem")
        self.verticalLayout_5.addWidget(self.labelMethRem)
        self.labelCashRem = QtWidgets.QLabel(self.widget4)
        self.labelCashRem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCashRem.setObjectName("labelCashRem")
        self.verticalLayout_5.addWidget(self.labelCashRem)
        self.widget5 = QtWidgets.QWidget(self.splitter)
        self.widget5.setObjectName("widget5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelHeadingRem_2 = QtWidgets.QLabel(self.widget5)
        self.labelHeadingRem_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeadingRem_2.setObjectName("labelHeadingRem_2")
        self.verticalLayout_6.addWidget(self.labelHeadingRem_2)
        self.labelNightclubVal = QtWidgets.QLabel(self.widget5)
        self.labelNightclubVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNightclubVal.setObjectName("labelNightclubVal")
        self.verticalLayout_6.addWidget(self.labelNightclubVal)
        self.labelBunkerVal = QtWidgets.QLabel(self.widget5)
        self.labelBunkerVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBunkerVal.setObjectName("labelBunkerVal")
        self.verticalLayout_6.addWidget(self.labelBunkerVal)
        self.labelCokeVal = QtWidgets.QLabel(self.widget5)
        self.labelCokeVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCokeVal.setObjectName("labelCokeVal")
        self.verticalLayout_6.addWidget(self.labelCokeVal)
        self.labelMethVal = QtWidgets.QLabel(self.widget5)
        self.labelMethVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMethVal.setObjectName("labelMethVal")
        self.verticalLayout_6.addWidget(self.labelMethVal)
        self.labelCashVal = QtWidgets.QLabel(self.widget5)
        self.labelCashVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCashVal.setObjectName("labelCashVal")
        self.verticalLayout_6.addWidget(self.labelCashVal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuReset = QtWidgets.QMenu(self.menubar)
        self.menuReset.setObjectName("menuReset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset_All_Timers = QtWidgets.QAction(MainWindow)
        self.actionReset_All_Timers.setObjectName("actionReset_All_Timers")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionReset_All_Timers_2 = QtWidgets.QAction(MainWindow)
        self.actionReset_All_Timers_2.setObjectName("actionReset_All_Timers_2")
        self.actionNightclub = QtWidgets.QAction(MainWindow)
        self.actionNightclub.setObjectName("actionNightclub")
        self.actionBunker = QtWidgets.QAction(MainWindow)
        self.actionBunker.setObjectName("actionBunker")
        self.actionCoke = QtWidgets.QAction(MainWindow)
        self.actionCoke.setObjectName("actionCoke")
        self.actionMeth = QtWidgets.QAction(MainWindow)
        self.actionMeth.setObjectName("actionMeth")
        self.actionCash = QtWidgets.QAction(MainWindow)
        self.actionCash.setObjectName("actionCash")
        self.menuFile.addAction(self.actionQuit)
        self.menuReset.addAction(self.actionReset_All_Timers_2)
        self.menuReset.addAction(self.actionNightclub)
        self.menuReset.addAction(self.actionBunker)
        self.menuReset.addAction(self.actionCoke)
        self.menuReset.addAction(self.actionMeth)
        self.menuReset.addAction(self.actionCash)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuReset.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtGTATimer"))
        self.pushNightclub.setText(_translate("MainWindow", "Nightclub"))
        self.pushBunker.setText(_translate("MainWindow", "Bunker"))
        self.pushCoke.setText(_translate("MainWindow", "Coke"))
        self.pushMeth.setText(_translate("MainWindow", "Meth"))
        self.pushCash.setText(_translate("MainWindow", "Cash"))
        self.labelHeadingStart.setText(_translate("MainWindow", "Start Time"))
        self.labelNightclubStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelBunkerStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelCokeStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelMethStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelCashStart.setText(_translate("MainWindow", "TextLabel"))
        self.labelHeadingEnd.setText(_translate("MainWindow", "End Time"))
        self.labelNightclubEnd.setText(_translate("MainWindow", "TextLabel"))
        self.labelBunkerEnd.setText(_translate("MainWindow", "TextLabel"))
        self.labelCokeEnd.setText(_translate("MainWindow", "TextLabel"))
        self.labelMethEnd.setText(_translate("MainWindow", "TextLabel"))
        self.labelCashEnd.setText(_translate("MainWindow", "TextLabel"))
        self.labelHeadingRem.setText(_translate("MainWindow", "ETA"))
        self.labelNightclubRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelBunkerRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelCokeRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelMethRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelCashRem.setText(_translate("MainWindow", "TextLabel"))
        self.labelHeadingRem_2.setText(_translate("MainWindow", "Value"))
        self.labelNightclubVal.setText(_translate("MainWindow", "TextLabel"))
        self.labelBunkerVal.setText(_translate("MainWindow", "TextLabel"))
        self.labelCokeVal.setText(_translate("MainWindow", "TextLabel"))
        self.labelMethVal.setText(_translate("MainWindow", "TextLabel"))
        self.labelCashVal.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuReset.setTitle(_translate("MainWindow", "Reset"))
        self.actionReset_All_Timers.setText(_translate("MainWindow", "Reset All Timers"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionReset_All_Timers_2.setText(_translate("MainWindow", "Reset All Timers"))
        self.actionNightclub.setText(_translate("MainWindow", "Reset Nightclub"))
        self.actionBunker.setText(_translate("MainWindow", "Bunker"))
        self.actionCoke.setText(_translate("MainWindow", "Coke"))
        self.actionMeth.setText(_translate("MainWindow", "Meth"))
        self.actionCash.setText(_translate("MainWindow", "Cash"))
