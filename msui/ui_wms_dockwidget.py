# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_wms_dockwidget.ui'
#
# Created: Mon Jan 31 10:41:45 2011
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_WMSDockWidget(object):
    def setupUi(self, WMSDockWidget):
        WMSDockWidget.setObjectName("WMSDockWidget")
        WMSDockWidget.resize(1001, 155)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WMSDockWidget.sizePolicy().hasHeightForWidth())
        WMSDockWidget.setSizePolicy(sizePolicy)
        WMSDockWidget.setMinimumSize(QtCore.QSize(1001, 0))
        WMSDockWidget.setMaximumSize(QtCore.QSize(16777215, 155))
        self.verticalLayout_4 = QtGui.QVBoxLayout(WMSDockWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtGui.QLabel(WMSDockWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.cbWMS_URL = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbWMS_URL.sizePolicy().hasHeightForWidth())
        self.cbWMS_URL.setSizePolicy(sizePolicy)
        self.cbWMS_URL.setEditable(True)
        self.cbWMS_URL.setObjectName("cbWMS_URL")
        self.cbWMS_URL.addItem("")
        self.cbWMS_URL.addItem("")
        self.horizontalLayout_9.addWidget(self.cbWMS_URL)
        self.btGetCapabilities = QtGui.QPushButton(WMSDockWidget)
        self.btGetCapabilities.setObjectName("btGetCapabilities")
        self.horizontalLayout_9.addWidget(self.btGetCapabilities)
        self.tbViewCapabilities = QtGui.QToolButton(WMSDockWidget)
        self.tbViewCapabilities.setObjectName("tbViewCapabilities")
        self.horizontalLayout_9.addWidget(self.tbViewCapabilities)
        self.line_4 = QtGui.QFrame(WMSDockWidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_9.addWidget(self.line_4)
        self.cbAutoUpdate = QtGui.QCheckBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAutoUpdate.sizePolicy().hasHeightForWidth())
        self.cbAutoUpdate.setSizePolicy(sizePolicy)
        self.cbAutoUpdate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cbAutoUpdate.setObjectName("cbAutoUpdate")
        self.horizontalLayout_9.addWidget(self.cbAutoUpdate)
        self.btGetMap = QtGui.QPushButton(WMSDockWidget)
        self.btGetMap.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btGetMap.setFont(font)
        self.btGetMap.setObjectName("btGetMap")
        self.horizontalLayout_9.addWidget(self.btGetMap)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtGui.QLabel(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.cbLayer = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLayer.sizePolicy().hasHeightForWidth())
        self.cbLayer.setSizePolicy(sizePolicy)
        self.cbLayer.setMinimumSize(QtCore.QSize(200, 0))
        self.cbLayer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbLayer.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cbLayer.setMinimumContentsLength(0)
        self.cbLayer.setObjectName("cbLayer")
        self.cbLayer.addItem("")
        self.cbLayer.addItem("")
        self.cbLayer.addItem("")
        self.horizontalLayout.addWidget(self.cbLayer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtGui.QLabel(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(40, 0))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.cbStyle = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbStyle.sizePolicy().hasHeightForWidth())
        self.cbStyle.setSizePolicy(sizePolicy)
        self.cbStyle.setMinimumSize(QtCore.QSize(200, 0))
        self.cbStyle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbStyle.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cbStyle.setFrame(True)
        self.cbStyle.setObjectName("cbStyle")
        self.cbStyle.addItem("")
        self.horizontalLayout_2.addWidget(self.cbStyle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teLayerAbstract = QtGui.QTextEdit(WMSDockWidget)
        self.teLayerAbstract.setMinimumSize(QtCore.QSize(242, 0))
        self.teLayerAbstract.setReadOnly(True)
        self.teLayerAbstract.setObjectName("teLayerAbstract")
        self.verticalLayout.addWidget(self.teLayerAbstract)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(WMSDockWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbLevelOn = QtGui.QCheckBox(WMSDockWidget)
        self.cbLevelOn.setEnabled(False)
        self.cbLevelOn.setMinimumSize(QtCore.QSize(95, 0))
        self.cbLevelOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbLevelOn.setPalette(palette)
        self.cbLevelOn.setCheckable(True)
        self.cbLevelOn.setObjectName("cbLevelOn")
        self.horizontalLayout_4.addWidget(self.cbLevelOn)
        self.cbLevel = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLevel.sizePolicy().hasHeightForWidth())
        self.cbLevel.setSizePolicy(sizePolicy)
        self.cbLevel.setMinimumSize(QtCore.QSize(180, 0))
        self.cbLevel.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbLevel.setObjectName("cbLevel")
        self.horizontalLayout_4.addWidget(self.cbLevel)
        self.tbLevel_back = QtGui.QToolButton(WMSDockWidget)
        self.tbLevel_back.setObjectName("tbLevel_back")
        self.horizontalLayout_4.addWidget(self.tbLevel_back)
        self.tbLevel_fwd = QtGui.QToolButton(WMSDockWidget)
        self.tbLevel_fwd.setObjectName("tbLevel_fwd")
        self.horizontalLayout_4.addWidget(self.tbLevel_fwd)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.line_5 = QtGui.QFrame(WMSDockWidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.cbTransparent = QtGui.QCheckBox(WMSDockWidget)
        self.cbTransparent.setChecked(True)
        self.cbTransparent.setObjectName("cbTransparent")
        self.horizontalLayout_4.addWidget(self.cbTransparent)
        self.line_3 = QtGui.QFrame(WMSDockWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.label = QtGui.QLabel(WMSDockWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.cbCacheEnabled = QtGui.QCheckBox(WMSDockWidget)
        self.cbCacheEnabled.setChecked(True)
        self.cbCacheEnabled.setTristate(False)
        self.cbCacheEnabled.setObjectName("cbCacheEnabled")
        self.horizontalLayout_4.addWidget(self.cbCacheEnabled)
        self.btClearCache = QtGui.QPushButton(WMSDockWidget)
        self.btClearCache.setObjectName("btClearCache")
        self.horizontalLayout_4.addWidget(self.btClearCache)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbInitialisationOn = QtGui.QCheckBox(WMSDockWidget)
        self.cbInitialisationOn.setEnabled(False)
        self.cbInitialisationOn.setMinimumSize(QtCore.QSize(95, 0))
        self.cbInitialisationOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbInitialisationOn.setPalette(palette)
        self.cbInitialisationOn.setObjectName("cbInitialisationOn")
        self.horizontalLayout_3.addWidget(self.cbInitialisationOn)
        self.cbInitTime = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbInitTime.sizePolicy().hasHeightForWidth())
        self.cbInitTime.setSizePolicy(sizePolicy)
        self.cbInitTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbInitTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbInitTime.setObjectName("cbInitTime")
        self.cbInitTime.addItem("")
        self.horizontalLayout_3.addWidget(self.cbInitTime)
        self.tbInitTime_cbback = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_cbback.setObjectName("tbInitTime_cbback")
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbback)
        self.tbInitTime_cbfwd = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_cbfwd.setObjectName("tbInitTime_cbfwd")
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbfwd)
        self.dteInitTime = QtGui.QDateTimeEdit(WMSDockWidget)
        self.dteInitTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteInitTime.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setBold(False)
        self.dteInitTime.setFont(font)
        self.dteInitTime.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.dteInitTime.setCalendarPopup(False)
        self.dteInitTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteInitTime.setObjectName("dteInitTime")
        self.horizontalLayout_3.addWidget(self.dteInitTime)
        self.tbInitTime_back = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_back.setObjectName("tbInitTime_back")
        self.horizontalLayout_3.addWidget(self.tbInitTime_back)
        self.cbInitTime_step = QtGui.QComboBox(WMSDockWidget)
        self.cbInitTime_step.setObjectName("cbInitTime_step")
        self.horizontalLayout_3.addWidget(self.cbInitTime_step)
        self.tbInitTime_fwd = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_fwd.setObjectName("tbInitTime_fwd")
        self.horizontalLayout_3.addWidget(self.tbInitTime_fwd)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbValidOn = QtGui.QCheckBox(WMSDockWidget)
        self.cbValidOn.setEnabled(False)
        self.cbValidOn.setMinimumSize(QtCore.QSize(95, 0))
        self.cbValidOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbValidOn.setPalette(palette)
        self.cbValidOn.setObjectName("cbValidOn")
        self.horizontalLayout_8.addWidget(self.cbValidOn)
        self.cbValidTime = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbValidTime.sizePolicy().hasHeightForWidth())
        self.cbValidTime.setSizePolicy(sizePolicy)
        self.cbValidTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbValidTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbValidTime.setObjectName("cbValidTime")
        self.horizontalLayout_8.addWidget(self.cbValidTime)
        self.tbValidTime_cbback = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_cbback.setObjectName("tbValidTime_cbback")
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbback)
        self.tbValidTime_cbfwd = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_cbfwd.setObjectName("tbValidTime_cbfwd")
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbfwd)
        self.dteValidTime = QtGui.QDateTimeEdit(WMSDockWidget)
        self.dteValidTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteValidTime.setMaximumSize(QtCore.QSize(160, 16777215))
        self.dteValidTime.setDate(QtCore.QDate(2010, 1, 22))
        self.dteValidTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.dteValidTime.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dteValidTime.setMinimumTime(QtCore.QTime(12, 0, 0))
        self.dteValidTime.setCalendarPopup(False)
        self.dteValidTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteValidTime.setObjectName("dteValidTime")
        self.horizontalLayout_8.addWidget(self.dteValidTime)
        self.tbValidTime_back = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_back.setObjectName("tbValidTime_back")
        self.horizontalLayout_8.addWidget(self.tbValidTime_back)
        self.cbValidTime_step = QtGui.QComboBox(WMSDockWidget)
        self.cbValidTime_step.setObjectName("cbValidTime_step")
        self.horizontalLayout_8.addWidget(self.cbValidTime_step)
        self.tbValidTime_fwd = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_fwd.setObjectName("tbValidTime_fwd")
        self.horizontalLayout_8.addWidget(self.tbValidTime_fwd)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(WMSDockWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)

        self.retranslateUi(WMSDockWidget)
        QtCore.QMetaObject.connectSlotsByName(WMSDockWidget)

    def retranslateUi(self, WMSDockWidget):
        WMSDockWidget.setWindowTitle(
            QtGui.QApplication.translate("WMSDockWidget", "WMS Dock Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(
            QtGui.QApplication.translate("WMSDockWidget", "WMS URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbWMS_URL.setToolTip(QtGui.QApplication.translate("WMSDockWidget", "Enter a valid WMS URL here.", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.cbWMS_URL.setItemText(0,
                                   QtGui.QApplication.translate("WMSDockWidget", "http://localhost:8002/fc_wms", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.cbWMS_URL.setItemText(1, QtGui.QApplication.translate("WMSDockWidget",
                                                                   "http://osm.omniscale.net/proxy/service", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.btGetCapabilities.setToolTip(
            QtGui.QApplication.translate("WMSDockWidget", "Request the capabilities from the WMS server.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btGetCapabilities.setText(
            QtGui.QApplication.translate("WMSDockWidget", "get capabilities", None, QtGui.QApplication.UnicodeUTF8))
        self.tbViewCapabilities.setText(
            QtGui.QApplication.translate("WMSDockWidget", "view", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoUpdate.setToolTip(QtGui.QApplication.translate("WMSDockWidget",
                                                                  "Automatically request an updated map when the "
                                                                  "layer parameters have changed.",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoUpdate.setText(
            QtGui.QApplication.translate("WMSDockWidget", "update on changes", None, QtGui.QApplication.UnicodeUTF8))
        self.btGetMap.setToolTip(
            QtGui.QApplication.translate("WMSDockWidget", "Request a map with the specifed parameters.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btGetMap.setText(
            QtGui.QApplication.translate("WMSDockWidget", "get map", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(
            QtGui.QApplication.translate("WMSDockWidget", "Layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLayer.setItemText(0, QtGui.QApplication.translate("WMSDockWidget", "BASEMAP", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.cbLayer.setItemText(1, QtGui.QApplication.translate("WMSDockWidget", "MSLP", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.cbLayer.setItemText(2, QtGui.QApplication.translate("WMSDockWidget", "TCC", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(
            QtGui.QApplication.translate("WMSDockWidget", "Style:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbStyle.setItemText(0, QtGui.QApplication.translate("WMSDockWidget", "...", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.teLayerAbstract.setHtml(QtGui.QApplication.translate("WMSDockWidget",
                                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                                  "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                                  "/><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" "
                                                                  "font-family:\'Sans Serif\'; font-size:10pt; "
                                                                  "font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px;"
                                                                  " margin-bottom:0px; margin-left:0px; "
                                                                  "margin-right:0px; -qt-block-indent:0; "
                                                                  "text-indent:0px;\"></p></body></html>",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.cbLevelOn.setText(
            QtGui.QApplication.translate("WMSDockWidget", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLevel.setToolTip(
            QtGui.QApplication.translate("WMSDockWidget", "Elevation values provided by the WMS server.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tbLevel_back.setText(
            QtGui.QApplication.translate("WMSDockWidget", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tbLevel_fwd.setText(
            QtGui.QApplication.translate("WMSDockWidget", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTransparent.setText(
            QtGui.QApplication.translate("WMSDockWidget", "transparent", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("WMSDockWidget", "Cache:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCacheEnabled.setToolTip(QtGui.QApplication.translate("WMSDockWidget",
                                                                    "Enable the image cache (retrieved images will "
                                                                    "be stored locally to speed up repeated "
                                                                    "retrievals).",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.cbCacheEnabled.setText(
            QtGui.QApplication.translate("WMSDockWidget", "on", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearCache.setToolTip(QtGui.QApplication.translate("WMSDockWidget", "Clear all cache contents.", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.btClearCache.setText(
            QtGui.QApplication.translate("WMSDockWidget", "clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cbInitialisationOn.setText(
            QtGui.QApplication.translate("WMSDockWidget", "Initialisation:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbInitTime.setToolTip(QtGui.QApplication.translate("WMSDockWidget",
                                                                "Forecast initialisation time (base time) values "
                                                                "provided by the WMS server.",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.cbInitTime.setItemText(0, QtGui.QApplication.translate("WMSDockWidget", "2010-12-12T00:00:00Z", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.tbInitTime_cbback.setText(
            QtGui.QApplication.translate("WMSDockWidget", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tbInitTime_cbfwd.setText(
            QtGui.QApplication.translate("WMSDockWidget", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.dteInitTime.setToolTip(
            QtGui.QApplication.translate("WMSDockWidget", "You can also specify an initialisation date here.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.dteInitTime.setDisplayFormat(
            QtGui.QApplication.translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC", None, QtGui.QApplication.UnicodeUTF8))
        self.tbInitTime_back.setText(
            QtGui.QApplication.translate("WMSDockWidget", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tbInitTime_fwd.setText(
            QtGui.QApplication.translate("WMSDockWidget", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cbValidOn.setText(
            QtGui.QApplication.translate("WMSDockWidget", "Valid:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbValidTime.setToolTip(
            QtGui.QApplication.translate("WMSDockWidget", "Valid time values provided by the WMS server.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tbValidTime_cbback.setText(
            QtGui.QApplication.translate("WMSDockWidget", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tbValidTime_cbfwd.setText(
            QtGui.QApplication.translate("WMSDockWidget", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.dteValidTime.setToolTip(QtGui.QApplication.translate("WMSDockWidget",
                                                                  "Specify the time value here, especially if the "
                                                                  "server does not provide predefined values. "
                                                                  "Keep in mind that the specified value may not be "
                                                                  "available from the server, though.",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.dteValidTime.setDisplayFormat(
            QtGui.QApplication.translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC", None, QtGui.QApplication.UnicodeUTF8))
        self.tbValidTime_back.setText(
            QtGui.QApplication.translate("WMSDockWidget", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tbValidTime_fwd.setText(
            QtGui.QApplication.translate("WMSDockWidget", ">", None, QtGui.QApplication.UnicodeUTF8))
