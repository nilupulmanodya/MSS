# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mslib/msui/ui/ui_wms_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WMSDockWidget(object):
    def setupUi(self, WMSDockWidget):
        WMSDockWidget.setObjectName("WMSDockWidget")
        WMSDockWidget.resize(1001, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WMSDockWidget.sizePolicy().hasHeightForWidth())
        WMSDockWidget.setSizePolicy(sizePolicy)
        WMSDockWidget.setMinimumSize(QtCore.QSize(1001, 0))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(WMSDockWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbLevel = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLevel.sizePolicy().hasHeightForWidth())
        self.cbLevel.setSizePolicy(sizePolicy)
        self.cbLevel.setMinimumSize(QtCore.QSize(180, 0))
        self.cbLevel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cbLevel.setObjectName("cbLevel")
        self.horizontalLayout_4.addWidget(self.cbLevel)
        self.tbLevel_back = QtWidgets.QToolButton(WMSDockWidget)
        self.tbLevel_back.setObjectName("tbLevel_back")
        self.horizontalLayout_4.addWidget(self.tbLevel_back)
        self.tbLevel_fwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbLevel_fwd.setObjectName("tbLevel_fwd")
        self.horizontalLayout_4.addWidget(self.tbLevel_fwd)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cbAutoUpdate = QtWidgets.QCheckBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAutoUpdate.sizePolicy().hasHeightForWidth())
        self.cbAutoUpdate.setSizePolicy(sizePolicy)
        self.cbAutoUpdate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cbAutoUpdate.setChecked(True)
        self.cbAutoUpdate.setObjectName("cbAutoUpdate")
        self.horizontalLayout_4.addWidget(self.cbAutoUpdate)
        self.cbTransparent = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbTransparent.setChecked(True)
        self.cbTransparent.setObjectName("cbTransparent")
        self.horizontalLayout_4.addWidget(self.cbTransparent)
        self.cbCacheEnabled = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbCacheEnabled.setChecked(True)
        self.cbCacheEnabled.setTristate(False)
        self.cbCacheEnabled.setObjectName("cbCacheEnabled")
        self.horizontalLayout_4.addWidget(self.cbCacheEnabled)
        self.btClearCache = QtWidgets.QPushButton(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btClearCache.sizePolicy().hasHeightForWidth())
        self.btClearCache.setSizePolicy(sizePolicy)
        self.btClearCache.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btClearCache.setObjectName("btClearCache")
        self.horizontalLayout_4.addWidget(self.btClearCache)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.pbLayerSelect = QtWidgets.QPushButton(WMSDockWidget)
        self.pbLayerSelect.setObjectName("pbLayerSelect")
        self.gridLayout.addWidget(self.pbLayerSelect, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbInitTime = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbInitTime.sizePolicy().hasHeightForWidth())
        self.cbInitTime.setSizePolicy(sizePolicy)
        self.cbInitTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbInitTime.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cbInitTime.setObjectName("cbInitTime")
        self.cbInitTime.addItem("")
        self.horizontalLayout_3.addWidget(self.cbInitTime)
        self.tbInitTime_cbback = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_cbback.setObjectName("tbInitTime_cbback")
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbback)
        self.tbInitTime_cbfwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_cbfwd.setObjectName("tbInitTime_cbfwd")
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbfwd)
        self.dteInitTime = QtWidgets.QDateTimeEdit(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dteInitTime.sizePolicy().hasHeightForWidth())
        self.dteInitTime.setSizePolicy(sizePolicy)
        self.dteInitTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteInitTime.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.dteInitTime.setFont(font)
        self.dteInitTime.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dteInitTime.setCalendarPopup(False)
        self.dteInitTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteInitTime.setObjectName("dteInitTime")
        self.horizontalLayout_3.addWidget(self.dteInitTime)
        self.tbInitTime_back = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_back.setObjectName("tbInitTime_back")
        self.horizontalLayout_3.addWidget(self.tbInitTime_back)
        self.cbInitTime_step = QtWidgets.QComboBox(WMSDockWidget)
        self.cbInitTime_step.setObjectName("cbInitTime_step")
        self.horizontalLayout_3.addWidget(self.cbInitTime_step)
        self.tbInitTime_fwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_fwd.setObjectName("tbInitTime_fwd")
        self.horizontalLayout_3.addWidget(self.tbInitTime_fwd)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbValidTime = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbValidTime.sizePolicy().hasHeightForWidth())
        self.cbValidTime.setSizePolicy(sizePolicy)
        self.cbValidTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbValidTime.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cbValidTime.setObjectName("cbValidTime")
        self.horizontalLayout_8.addWidget(self.cbValidTime)
        self.tbValidTime_cbback = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_cbback.setArrowType(QtCore.Qt.NoArrow)
        self.tbValidTime_cbback.setObjectName("tbValidTime_cbback")
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbback)
        self.tbValidTime_cbfwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_cbfwd.setObjectName("tbValidTime_cbfwd")
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbfwd)
        self.dteValidTime = QtWidgets.QDateTimeEdit(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dteValidTime.sizePolicy().hasHeightForWidth())
        self.dteValidTime.setSizePolicy(sizePolicy)
        self.dteValidTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteValidTime.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dteValidTime.setDate(QtCore.QDate(2009, 12, 29))
        self.dteValidTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1999, 12, 31), QtCore.QTime(12, 0, 0)))
        self.dteValidTime.setMinimumDate(QtCore.QDate(1999, 12, 31))
        self.dteValidTime.setMinimumTime(QtCore.QTime(12, 0, 0))
        self.dteValidTime.setCalendarPopup(False)
        self.dteValidTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteValidTime.setObjectName("dteValidTime")
        self.horizontalLayout_8.addWidget(self.dteValidTime)
        self.tbValidTime_back = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_back.setObjectName("tbValidTime_back")
        self.horizontalLayout_8.addWidget(self.tbValidTime_back)
        self.cbValidTime_step = QtWidgets.QComboBox(WMSDockWidget)
        self.cbValidTime_step.setObjectName("cbValidTime_step")
        self.horizontalLayout_8.addWidget(self.cbValidTime_step)
        self.tbValidTime_fwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_fwd.setObjectName("tbValidTime_fwd")
        self.horizontalLayout_8.addWidget(self.tbValidTime_fwd)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lLayerName = QtWidgets.QLabel(WMSDockWidget)
        self.lLayerName.setWordWrap(False)
        self.lLayerName.setObjectName("lLayerName")
        self.horizontalLayout.addWidget(self.lLayerName)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(WMSDockWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.btClearMap = QtWidgets.QPushButton(WMSDockWidget)
        self.btClearMap.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btClearMap.setObjectName("btClearMap")
        self.horizontalLayout.addWidget(self.btClearMap)
        self.btGetMap = QtWidgets.QPushButton(WMSDockWidget)
        self.btGetMap.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btGetMap.setFont(font)
        self.btGetMap.setObjectName("btGetMap")
        self.horizontalLayout.addWidget(self.btGetMap)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)

        self.retranslateUi(WMSDockWidget)
        QtCore.QMetaObject.connectSlotsByName(WMSDockWidget)

    def retranslateUi(self, WMSDockWidget):
        _translate = QtCore.QCoreApplication.translate
        WMSDockWidget.setWindowTitle(_translate("WMSDockWidget", "WMS Dock Widget"))
        self.cbLevel.setToolTip(_translate("WMSDockWidget", "Elevation values provided by the WMS server."))
        self.tbLevel_back.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: down"))
        self.tbLevel_back.setText(_translate("WMSDockWidget", "<"))
        self.tbLevel_back.setShortcut(_translate("WMSDockWidget", "Down"))
        self.tbLevel_fwd.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: up"))
        self.tbLevel_fwd.setText(_translate("WMSDockWidget", ">"))
        self.tbLevel_fwd.setShortcut(_translate("WMSDockWidget", "Up"))
        self.cbAutoUpdate.setToolTip(_translate("WMSDockWidget", "Automatically request an updated map when the layer parameters have changed."))
        self.cbAutoUpdate.setText(_translate("WMSDockWidget", "Auto-Update"))
        self.cbTransparent.setText(_translate("WMSDockWidget", "Transparent"))
        self.cbCacheEnabled.setToolTip(_translate("WMSDockWidget", "Enable the image cache (retrieved images will be stored locally to speed up repeated retrievals)."))
        self.cbCacheEnabled.setText(_translate("WMSDockWidget", "Use Cache"))
        self.btClearCache.setToolTip(_translate("WMSDockWidget", "Clear all cache contents."))
        self.btClearCache.setText(_translate("WMSDockWidget", "Clear Cache"))
        self.pbLayerSelect.setText(_translate("WMSDockWidget", "Server/Layer"))
        self.label_3.setText(_translate("WMSDockWidget", "Valid:"))
        self.label.setText(_translate("WMSDockWidget", "Level:"))
        self.label_2.setText(_translate("WMSDockWidget", "Initialisation:"))
        self.cbInitTime.setToolTip(_translate("WMSDockWidget", "Forecast initialisation time (base time) values provided by the WMS server."))
        self.cbInitTime.setItemText(0, _translate("WMSDockWidget", "2010-12-12T00:00:00Z"))
        self.tbInitTime_cbback.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: alt-left"))
        self.tbInitTime_cbback.setText(_translate("WMSDockWidget", "<"))
        self.tbInitTime_cbback.setShortcut(_translate("WMSDockWidget", "Alt+Left"))
        self.tbInitTime_cbfwd.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: alt-right"))
        self.tbInitTime_cbfwd.setText(_translate("WMSDockWidget", ">"))
        self.tbInitTime_cbfwd.setShortcut(_translate("WMSDockWidget", "Alt+Right"))
        self.dteInitTime.setToolTip(_translate("WMSDockWidget", "You can also specify an initialisation date here."))
        self.dteInitTime.setDisplayFormat(_translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC"))
        self.tbInitTime_back.setText(_translate("WMSDockWidget", "<"))
        self.tbInitTime_fwd.setText(_translate("WMSDockWidget", ">"))
        self.cbValidTime.setToolTip(_translate("WMSDockWidget", "Valid time values provided by the WMS server."))
        self.tbValidTime_cbback.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: left"))
        self.tbValidTime_cbback.setText(_translate("WMSDockWidget", "<"))
        self.tbValidTime_cbback.setShortcut(_translate("WMSDockWidget", "Left"))
        self.tbValidTime_cbfwd.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: right"))
        self.tbValidTime_cbfwd.setText(_translate("WMSDockWidget", ">"))
        self.tbValidTime_cbfwd.setShortcut(_translate("WMSDockWidget", "Right"))
        self.dteValidTime.setToolTip(_translate("WMSDockWidget", "Specify the time value here, especially if the server does not provide predefined values. Keep in mind that the specified value may not be available from the server, though."))
        self.dteValidTime.setDisplayFormat(_translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC"))
        self.tbValidTime_back.setText(_translate("WMSDockWidget", "<"))
        self.tbValidTime_fwd.setText(_translate("WMSDockWidget", ">"))
        self.lLayerName.setText(_translate("WMSDockWidget", "No Layer selected"))
        self.btClearMap.setText(_translate("WMSDockWidget", "remove"))
        self.btGetMap.setToolTip(_translate("WMSDockWidget", "<html><head/><body><p>Request the layer(s) with the specifed parameters.</p><p>Keyboard shortcut: Enter</p></body></html>"))
        self.btGetMap.setText(_translate("WMSDockWidget", "retrieve"))
        self.btGetMap.setShortcut(_translate("WMSDockWidget", "Return"))

