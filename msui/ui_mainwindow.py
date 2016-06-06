# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MSSMainWindow(object):
    def setupUi(self, MSSMainWindow):
        MSSMainWindow.setObjectName(_fromUtf8("MSSMainWindow"))
        MSSMainWindow.resize(424, 540)
        MSSMainWindow.setWindowTitle(
            QtGui.QApplication.translate("MSSMainWindow", "DLR/IPA Mission Support User Interface", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MSSMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "Flight Tracks:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText(
            QtGui.QApplication.translate("MSSMainWindow", "Active flight track:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lblActiveFlightTrack = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblActiveFlightTrack.sizePolicy().hasHeightForWidth())
        self.lblActiveFlightTrack.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblActiveFlightTrack.setFont(font)
        self.lblActiveFlightTrack.setFrameShape(QtGui.QFrame.Box)
        self.lblActiveFlightTrack.setText(QtGui.QApplication.translate("MSSMainWindow", "(active flight track)", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.lblActiveFlightTrack.setObjectName(_fromUtf8("lblActiveFlightTrack"))
        self.horizontalLayout_2.addWidget(self.lblActiveFlightTrack)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setText(
            QtGui.QApplication.translate("MSSMainWindow", "Open flight tracks:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.listFlightTracks = QtGui.QListWidget(self.groupBox_3)
        self.listFlightTracks.setAlternatingRowColors(True)
        self.listFlightTracks.setTextElideMode(QtCore.Qt.ElideNone)
        self.listFlightTracks.setObjectName(_fromUtf8("listFlightTracks"))
        self.verticalLayout_6.addWidget(self.listFlightTracks)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btSelectFlightTrack = QtGui.QPushButton(self.groupBox_3)
        self.btSelectFlightTrack.setText(
            QtGui.QApplication.translate("MSSMainWindow", "set selected flight track active", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btSelectFlightTrack.setObjectName(_fromUtf8("btSelectFlightTrack"))
        self.horizontalLayout_3.addWidget(self.btSelectFlightTrack)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "Open Views:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listViews = QtGui.QListWidget(self.groupBox)
        self.listViews.setObjectName(_fromUtf8("listViews"))
        self.verticalLayout_4.addWidget(self.listViews)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "Open Tools:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.listTools = QtGui.QListWidget(self.groupBox_2)
        self.listTools.setObjectName(_fromUtf8("listTools"))
        self.verticalLayout_5.addWidget(self.listTools)
        self.verticalLayout.addWidget(self.groupBox_2)
        MSSMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MSSMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "&Views", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        self.menu_Tools = QtGui.QMenu(self.menubar)
        self.menu_Tools.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Tools.setObjectName(_fromUtf8("menu_Tools"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setTitle(
            QtGui.QApplication.translate("MSSMainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MSSMainWindow.setMenuBar(self.menubar)
        self.action_Quit = QtGui.QAction(MSSMainWindow)
        self.action_Quit.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(
            QtGui.QApplication.translate("MSSMainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.actionNewFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionNewFlightTrack.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&New Flight Track...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFlightTrack.setShortcut(
            QtGui.QApplication.translate("MSSMainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFlightTrack.setObjectName(_fromUtf8("actionNewFlightTrack"))
        self.actionOpenFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionOpenFlightTrack.setText(QtGui.QApplication.translate("MSSMainWindow", "&Open Flight Track...", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFlightTrack.setShortcut(
            QtGui.QApplication.translate("MSSMainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFlightTrack.setObjectName(_fromUtf8("actionOpenFlightTrack"))
        self.actionSaveActiveFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrack.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&Save Active Flight Track", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionSaveActiveFlightTrack.setShortcut(
            QtGui.QApplication.translate("MSSMainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveActiveFlightTrack.setObjectName(_fromUtf8("actionSaveActiveFlightTrack"))
        self.actionSaveActiveFlightTrackAs = QtGui.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrackAs.setText(
            QtGui.QApplication.translate("MSSMainWindow", "Save Active Flight Track &As...", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionSaveActiveFlightTrackAs.setObjectName(_fromUtf8("actionSaveActiveFlightTrackAs"))
        self.actionCloseSelectedFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionCloseSelectedFlightTrack.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&Close Selected Flight Track", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionCloseSelectedFlightTrack.setObjectName(_fromUtf8("actionCloseSelectedFlightTrack"))
        self.actionTopView = QtGui.QAction(MSSMainWindow)
        self.actionTopView.setText(QtGui.QApplication.translate("MSSMainWindow", "&Top View (Horizontal Section)", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.actionTopView.setObjectName(_fromUtf8("actionTopView"))
        self.actionSideView = QtGui.QAction(MSSMainWindow)
        self.actionSideView.setText(QtGui.QApplication.translate("MSSMainWindow", "&Side View (Vertical Section)", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.actionSideView.setObjectName(_fromUtf8("actionSideView"))
        self.actionTableView = QtGui.QAction(MSSMainWindow)
        self.actionTableView.setText(
            QtGui.QApplication.translate("MSSMainWindow", "T&able View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTableView.setObjectName(_fromUtf8("actionTableView"))
        self.actionLoopView = QtGui.QAction(MSSMainWindow)
        self.actionLoopView.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&Loop View (Images)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoopView.setObjectName(_fromUtf8("actionLoopView"))
        self.actionTimeSeriesViewTrajectories = QtGui.QAction(MSSMainWindow)
        self.actionTimeSeriesViewTrajectories.setText(
            QtGui.QApplication.translate("MSSMainWindow", "T&ime Series View (Trajectories)", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionTimeSeriesViewTrajectories.setObjectName(_fromUtf8("actionTimeSeriesViewTrajectories"))
        self.action3DView = QtGui.QAction(MSSMainWindow)
        self.action3DView.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&3D View", None, QtGui.QApplication.UnicodeUTF8))
        self.action3DView.setObjectName(_fromUtf8("action3DView"))
        self.actionTrajectoryToolLagranto = QtGui.QAction(MSSMainWindow)
        self.actionTrajectoryToolLagranto.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&Trajectory Tool (Lagranto)", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionTrajectoryToolLagranto.setObjectName(_fromUtf8("actionTrajectoryToolLagranto"))
        self.actionDiscoverEarthObservationDataGENESI = QtGui.QAction(MSSMainWindow)
        self.actionDiscoverEarthObservationDataGENESI.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&Discover Earth Observation Data (GENESI)", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionDiscoverEarthObservationDataGENESI.setObjectName(
            _fromUtf8("actionDiscoverEarthObservationDataGENESI"))
        self.actionAboutMSUI = QtGui.QAction(MSSMainWindow)
        self.actionAboutMSUI.setText(
            QtGui.QApplication.translate("MSSMainWindow", "&About MSUI", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutMSUI.setObjectName(_fromUtf8("actionAboutMSUI"))
        self.menu_File.addAction(self.actionNewFlightTrack)
        self.menu_File.addAction(self.actionOpenFlightTrack)
        self.menu_File.addAction(self.actionCloseSelectedFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionSaveActiveFlightTrack)
        self.menu_File.addAction(self.actionSaveActiveFlightTrackAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_View.addAction(self.actionTopView)
        self.menu_View.addAction(self.actionSideView)
        self.menu_View.addAction(self.actionTableView)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionLoopView)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionTimeSeriesViewTrajectories)
        self.menu_Tools.addAction(self.actionTrajectoryToolLagranto)
        self.menu_Help.addAction(self.actionAboutMSUI)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MSSMainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MSSMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MSSMainWindow)

    def retranslateUi(self, MSSMainWindow):
        pass
