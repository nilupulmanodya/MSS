# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_trajectories_window.ui'
#
# Created: Thu Feb 24 15:27:55 2011
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_TrajectoriesWindow(object):
    def setupUi(self, TrajectoriesWindow):
        TrajectoriesWindow.setObjectName("TrajectoriesWindow")
        TrajectoriesWindow.resize(732, 725)
        self.centralwidget = QtGui.QWidget(TrajectoriesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabGUI = QtGui.QTabWidget(self.centralwidget)
        self.tabGUI.setEnabled(True)
        self.tabGUI.setTabPosition(QtGui.QTabWidget.North)
        self.tabGUI.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabGUI.setObjectName("tabGUI")
        self.tabData = QtGui.QWidget()
        self.tabData.setObjectName("tabData")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabData)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.tabData)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self._5 = QtGui.QVBoxLayout(self.groupBox)
        self._5.setObjectName("_5")
        self._6 = QtGui.QHBoxLayout()
        self._6.setObjectName("_6")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self._6.addWidget(self.label_4)
        self.leSelectionQuery = QtGui.QLineEdit(self.groupBox)
        self.leSelectionQuery.setObjectName("leSelectionQuery")
        self._6.addWidget(self.leSelectionQuery)
        self.cbSelectElements = QtGui.QComboBox(self.groupBox)
        self.cbSelectElements.setObjectName("cbSelectElements")
        self.cbSelectElements.addItem("")
        self.cbSelectElements.addItem("")
        self._6.addWidget(self.cbSelectElements)
        self.btSelectMapElements = QtGui.QPushButton(self.groupBox)
        self.btSelectMapElements.setObjectName("btSelectMapElements")
        self._6.addWidget(self.btSelectMapElements)
        self._5.addLayout(self._6)
        self.tvVisibleElements = QtGui.QTreeView(self.groupBox)
        self.tvVisibleElements.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tvVisibleElements.setSortingEnabled(False)
        self.tvVisibleElements.setObjectName("tvVisibleElements")
        self._5.addWidget(self.tvVisibleElements)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_7 = QtGui.QGroupBox(self.tabData)
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setObjectName("groupBox_7")
        self._7 = QtGui.QHBoxLayout(self.groupBox_7)
        self._7.setObjectName("_7")
        self._8 = QtGui.QVBoxLayout()
        self._8.setObjectName("_8")
        self._9 = QtGui.QHBoxLayout()
        self._9.setObjectName("_9")
        self.label = QtGui.QLabel(self.groupBox_7)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName("label")
        self._9.addWidget(self.label)
        self.cbColour = QtGui.QComboBox(self.groupBox_7)
        self.cbColour.setMinimumSize(QtCore.QSize(80, 0))
        self.cbColour.setObjectName("cbColour")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self.cbColour.addItem("")
        self._9.addWidget(self.cbColour)
        self.btColour = QtGui.QPushButton(self.groupBox_7)
        self.btColour.setMinimumSize(QtCore.QSize(60, 0))
        self.btColour.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btColour.setObjectName("btColour")
        self._9.addWidget(self.btColour)
        self._8.addLayout(self._9)
        self._10 = QtGui.QHBoxLayout()
        self._10.setObjectName("_10")
        self.label_2 = QtGui.QLabel(self.groupBox_7)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self._10.addWidget(self.label_2)
        self.cbLineStyle = QtGui.QComboBox(self.groupBox_7)
        self.cbLineStyle.setMinimumSize(QtCore.QSize(80, 0))
        self.cbLineStyle.setObjectName("cbLineStyle")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self._10.addWidget(self.cbLineStyle)
        self.btLineStyle = QtGui.QPushButton(self.groupBox_7)
        self.btLineStyle.setMinimumSize(QtCore.QSize(60, 0))
        self.btLineStyle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btLineStyle.setObjectName("btLineStyle")
        self._10.addWidget(self.btLineStyle)
        self._8.addLayout(self._10)
        self._11 = QtGui.QHBoxLayout()
        self._11.setObjectName("_11")
        self.label_3 = QtGui.QLabel(self.groupBox_7)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_3.setObjectName("label_3")
        self._11.addWidget(self.label_3)
        self.sbLineWidth = QtGui.QSpinBox(self.groupBox_7)
        self.sbLineWidth.setMinimumSize(QtCore.QSize(80, 0))
        self.sbLineWidth.setMinimum(1)
        self.sbLineWidth.setObjectName("sbLineWidth")
        self._11.addWidget(self.sbLineWidth)
        self.btLineWidth = QtGui.QPushButton(self.groupBox_7)
        self.btLineWidth.setMinimumSize(QtCore.QSize(60, 0))
        self.btLineWidth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btLineWidth.setObjectName("btLineWidth")
        self._11.addWidget(self.btLineWidth)
        self._8.addLayout(self._11)
        self._7.addLayout(self._8)
        self.line_3 = QtGui.QFrame(self.groupBox_7)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self._7.addWidget(self.line_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._13 = QtGui.QHBoxLayout()
        self._13.setObjectName("_13")
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setObjectName("label_5")
        self._13.addWidget(self.label_5)
        self.teTimeMarker = QtGui.QTimeEdit(self.groupBox_7)
        self.teTimeMarker.setObjectName("teTimeMarker")
        self._13.addWidget(self.teTimeMarker)
        self.btTimeMarker = QtGui.QPushButton(self.groupBox_7)
        self.btTimeMarker.setMinimumSize(QtCore.QSize(60, 0))
        self.btTimeMarker.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btTimeMarker.setObjectName("btTimeMarker")
        self._13.addWidget(self.btTimeMarker)
        self.verticalLayout_2.addLayout(self._13)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setMinimumSize(QtCore.QSize(110, 0))
        self.label_6.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.cbPlotInView = QtGui.QComboBox(self.groupBox_7)
        self.cbPlotInView.setMinimumSize(QtCore.QSize(150, 0))
        self.cbPlotInView.setObjectName("cbPlotInView")
        self.cbPlotInView.addItem("")
        self.horizontalLayout.addWidget(self.cbPlotInView)
        self.btPlotInView = QtGui.QPushButton(self.groupBox_7)
        self.btPlotInView.setMinimumSize(QtCore.QSize(60, 0))
        self.btPlotInView.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btPlotInView.setObjectName("btPlotInView")
        self.horizontalLayout.addWidget(self.btPlotInView)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtGui.QLabel(self.groupBox_7)
        self.label_7.setMinimumSize(QtCore.QSize(110, 0))
        self.label_7.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.cbRemoveFromView = QtGui.QComboBox(self.groupBox_7)
        self.cbRemoveFromView.setMinimumSize(QtCore.QSize(150, 0))
        self.cbRemoveFromView.setObjectName("cbRemoveFromView")
        self.cbRemoveFromView.addItem("")
        self.horizontalLayout_2.addWidget(self.cbRemoveFromView)
        self.btRemoveFromView = QtGui.QPushButton(self.groupBox_7)
        self.btRemoveFromView.setMinimumSize(QtCore.QSize(60, 0))
        self.btRemoveFromView.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btRemoveFromView.setObjectName("btRemoveFromView")
        self.horizontalLayout_2.addWidget(self.btRemoveFromView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self._7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.tabGUI.addTab(self.tabData, "")
        self.verticalLayout.addWidget(self.tabGUI)
        TrajectoriesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TrajectoriesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        TrajectoriesWindow.setMenuBar(self.menubar)
        self.actionOpenTrajectories = QtGui.QAction(TrajectoriesWindow)
        self.actionOpenTrajectories.setObjectName("actionOpenTrajectories")
        self.actionOpenFlightTrack = QtGui.QAction(TrajectoriesWindow)
        self.actionOpenFlightTrack.setObjectName("actionOpenFlightTrack")
        self.action_Quit = QtGui.QAction(TrajectoriesWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionCloseElement = QtGui.QAction(TrajectoriesWindow)
        self.actionCloseElement.setObjectName("actionCloseElement")
        self.menu_File.addAction(self.actionOpenTrajectories)
        self.menu_File.addAction(self.actionOpenFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(TrajectoriesWindow)
        self.tabGUI.setCurrentIndex(0)
        self.cbSelectElements.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL("triggered()"), TrajectoriesWindow.close)
        QtCore.QMetaObject.connectSlotsByName(TrajectoriesWindow)

    def retranslateUi(self, TrajectoriesWindow):
        TrajectoriesWindow.setWindowTitle(
            QtGui.QApplication.translate("TrajectoriesWindow", "Trajectories - DLR/IPA Mission Support", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("TrajectoriesWindow", "Open trajectory items:", None,
                                                            QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "Select:", None, QtGui.QApplication.UnicodeUTF8))
        self.leSelectionQuery.setToolTip(QtGui.QApplication.translate("TrajectoriesWindow",
                                                                      "Enter selection criteria here. Available "
                                                                      "variables are %lat, %lon, %pres, \n"
                                                                      "and %meta(\"NAME\"), where NAME has to be "
                                                                      "the name of a matatag that appears in "
                                                                      "the data. \n"
                                                                      "For example, type \'%lat >= 45.\' will select "
                                                                      "all elements with a start point latitude "
                                                                      "larger \n"
                                                                      "equal to 45 degrees after you click the "
                                                                      "button on the left. To select all "
                                                                      "trajectories with a \n"
                                                                      "start latitude larger than 45 degrees at "
                                                                      "flight level 320, type \'%lat > 45. and "
                                                                      "%meta(\"flightlevel\") == 320\'.",
                                                                      None, QtGui.QApplication.UnicodeUTF8))
        self.cbSelectElements.setItemText(0, QtGui.QApplication.translate("TrajectoriesWindow", "from all items", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.cbSelectElements.setItemText(1, QtGui.QApplication.translate("TrajectoriesWindow",
                                                                          "from children of current node", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.btSelectMapElements.setToolTip(QtGui.QApplication.translate("TrajectoriesWindow",
                                                                         "Select all items listed below that match "
                                                                         "the criteria given on the right.",
                                                                         None, QtGui.QApplication.UnicodeUTF8))
        self.btSelectMapElements.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "&go!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("TrajectoriesWindow", "Modify selected items:", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "Colour:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(0, QtGui.QApplication.translate("TrajectoriesWindow", "None", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(1, QtGui.QApplication.translate("TrajectoriesWindow", "blue", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(2, QtGui.QApplication.translate("TrajectoriesWindow", "green", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(3, QtGui.QApplication.translate("TrajectoriesWindow", "red", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(4, QtGui.QApplication.translate("TrajectoriesWindow", "cyan", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(5, QtGui.QApplication.translate("TrajectoriesWindow", "magenta", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(6, QtGui.QApplication.translate("TrajectoriesWindow", "yellow", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(7, QtGui.QApplication.translate("TrajectoriesWindow", "black", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.cbColour.setItemText(8, QtGui.QApplication.translate("TrajectoriesWindow", "white", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.btColour.setToolTip(
            QtGui.QApplication.translate("TrajectoriesWindow", "Set the colour of the selected items.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btColour.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "Line Style:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLineStyle.setItemText(0, QtGui.QApplication.translate("TrajectoriesWindow", "None", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.cbLineStyle.setItemText(1, QtGui.QApplication.translate("TrajectoriesWindow", "-", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.cbLineStyle.setItemText(2, QtGui.QApplication.translate("TrajectoriesWindow", "--", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.cbLineStyle.setItemText(3, QtGui.QApplication.translate("TrajectoriesWindow", "-.", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.cbLineStyle.setItemText(4, QtGui.QApplication.translate("TrajectoriesWindow", ":", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.btLineStyle.setToolTip(
            QtGui.QApplication.translate("TrajectoriesWindow", "Set the line style of the selected items.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btLineStyle.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "Line Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.btLineWidth.setToolTip(
            QtGui.QApplication.translate("TrajectoriesWindow", "Set the line width of the selected items.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btLineWidth.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("TrajectoriesWindow", "Draw time markers (hh:mm):", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.teTimeMarker.setDisplayFormat(
            QtGui.QApplication.translate("TrajectoriesWindow", "hh:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.btTimeMarker.setToolTip(QtGui.QApplication.translate("TrajectoriesWindow",
                                                                  "Draw time markers along the trajectories. These "
                                                                  "will be dots with the spacing given on the "
                                                                  "right (hh:mm).",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.btTimeMarker.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "Plot in view:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPlotInView.setItemText(0, QtGui.QApplication.translate("TrajectoriesWindow", "None", None,
                                                                      QtGui.QApplication.UnicodeUTF8))
        self.btPlotInView.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("TrajectoriesWindow", "Remove from view:", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.cbRemoveFromView.setItemText(0, QtGui.QApplication.translate("TrajectoriesWindow", "None", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.btRemoveFromView.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGUI.setTabText(self.tabGUI.indexOf(self.tabData),
                               QtGui.QApplication.translate("TrajectoriesWindow", "Data", None,
                                                            QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(
            QtGui.QApplication.translate("TrajectoriesWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenTrajectories.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "&Open Trajectories...", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionOpenTrajectories.setShortcut(
            QtGui.QApplication.translate("TrajectoriesWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFlightTrack.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "Open &Flight Track...", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFlightTrack.setShortcut(
            QtGui.QApplication.translate("TrajectoriesWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(
            QtGui.QApplication.translate("TrajectoriesWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(
            QtGui.QApplication.translate("TrajectoriesWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloseElement.setText(QtGui.QApplication.translate("TrajectoriesWindow", "&Close Element...", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
