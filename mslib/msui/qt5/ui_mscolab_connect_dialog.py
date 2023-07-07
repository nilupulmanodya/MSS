# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mslib/msui/ui/ui_mscolab_connect_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MSColabConnectDialog(object):
    def setupUi(self, MSColabConnectDialog):
        MSColabConnectDialog.setObjectName("MSColabConnectDialog")
        MSColabConnectDialog.resize(478, 268)
        self.verticalLayout = QtWidgets.QVBoxLayout(MSColabConnectDialog)
        self.verticalLayout.setContentsMargins(12, 10, 10, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.urlLabel = QtWidgets.QLabel(MSColabConnectDialog)
        self.urlLabel.setObjectName("urlLabel")
        self.horizontalLayout_2.addWidget(self.urlLabel)
        self.urlCb = QtWidgets.QComboBox(MSColabConnectDialog)
        self.urlCb.setEditable(True)
        self.urlCb.setObjectName("urlCb")
        self.horizontalLayout_2.addWidget(self.urlCb)
        self.connectBtn = QtWidgets.QPushButton(MSColabConnectDialog)
        self.connectBtn.setAutoDefault(False)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_2.addWidget(self.connectBtn)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(MSColabConnectDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(MSColabConnectDialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.loginPage)
        self.gridLayout_3.setContentsMargins(100, 0, 100, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.loginBtn = QtWidgets.QPushButton(self.loginPage)
        self.loginBtn.setAutoDefault(False)
        self.loginBtn.setObjectName("loginBtn")
        self.gridLayout_3.addWidget(self.loginBtn, 3, 0, 1, 2)
        self.addUserBtn = QtWidgets.QPushButton(self.loginPage)
        self.addUserBtn.setAutoDefault(False)
        self.addUserBtn.setObjectName("addUserBtn")
        self.gridLayout_3.addWidget(self.addUserBtn, 4, 1, 1, 1)
        self.loginTopicLabel = QtWidgets.QLabel(self.loginPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginTopicLabel.setFont(font)
        self.loginTopicLabel.setObjectName("loginTopicLabel")
        self.gridLayout_3.addWidget(self.loginTopicLabel, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.clickNewUserLabel = QtWidgets.QLabel(self.loginPage)
        self.clickNewUserLabel.setObjectName("clickNewUserLabel")
        self.gridLayout_3.addWidget(self.clickNewUserLabel, 4, 0, 1, 1)
        self.loginWithIDPBtn = QtWidgets.QPushButton(self.loginPage)
        self.loginWithIDPBtn.setObjectName("loginWithIDPBtn")
        self.gridLayout_3.addWidget(self.loginWithIDPBtn, 5, 0, 1, 2)
        self.loginEmailLe = QtWidgets.QLineEdit(self.loginPage)
        self.loginEmailLe.setObjectName("loginEmailLe")
        self.gridLayout_3.addWidget(self.loginEmailLe, 1, 0, 1, 2)
        self.loginPasswordLe = QtWidgets.QLineEdit(self.loginPage)
        self.loginPasswordLe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPasswordLe.setObjectName("loginPasswordLe")
        self.gridLayout_3.addWidget(self.loginPasswordLe, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.loginPage)
        self.newuserPage = QtWidgets.QWidget()
        self.newuserPage.setObjectName("newuserPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.newuserPage)
        self.gridLayout_2.setContentsMargins(50, 0, 50, 0)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.newUsernameLe = QtWidgets.QLineEdit(self.newuserPage)
        self.newUsernameLe.setObjectName("newUsernameLe")
        self.gridLayout_2.addWidget(self.newUsernameLe, 1, 1, 1, 1)
        self.newPasswordLabel = QtWidgets.QLabel(self.newuserPage)
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.gridLayout_2.addWidget(self.newPasswordLabel, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.newConfirmPasswordLabel = QtWidgets.QLabel(self.newuserPage)
        self.newConfirmPasswordLabel.setObjectName("newConfirmPasswordLabel")
        self.gridLayout_2.addWidget(self.newConfirmPasswordLabel, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.newUserTopicLabel = QtWidgets.QLabel(self.newuserPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newUserTopicLabel.setFont(font)
        self.newUserTopicLabel.setObjectName("newUserTopicLabel")
        self.gridLayout_2.addWidget(self.newUserTopicLabel, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.newEmailLe = QtWidgets.QLineEdit(self.newuserPage)
        self.newEmailLe.setObjectName("newEmailLe")
        self.gridLayout_2.addWidget(self.newEmailLe, 2, 1, 1, 1)
        self.newEmailLabel = QtWidgets.QLabel(self.newuserPage)
        self.newEmailLabel.setObjectName("newEmailLabel")
        self.gridLayout_2.addWidget(self.newEmailLabel, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.newUserBb = QtWidgets.QDialogButtonBox(self.newuserPage)
        self.newUserBb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newUserBb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.newUserBb.setObjectName("newUserBb")
        self.gridLayout_2.addWidget(self.newUserBb, 5, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.newPasswordLe = QtWidgets.QLineEdit(self.newuserPage)
        self.newPasswordLe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordLe.setObjectName("newPasswordLe")
        self.gridLayout_2.addWidget(self.newPasswordLe, 3, 1, 1, 1)
        self.newUsernameLabel = QtWidgets.QLabel(self.newuserPage)
        self.newUsernameLabel.setObjectName("newUsernameLabel")
        self.gridLayout_2.addWidget(self.newUsernameLabel, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.newConfirmPasswordLe = QtWidgets.QLineEdit(self.newuserPage)
        self.newConfirmPasswordLe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newConfirmPasswordLe.setObjectName("newConfirmPasswordLe")
        self.gridLayout_2.addWidget(self.newConfirmPasswordLe, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.newuserPage)
        self.httpAuthPage = QtWidgets.QWidget()
        self.httpAuthPage.setObjectName("httpAuthPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.httpAuthPage)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.httpTopicLabel = QtWidgets.QLabel(self.httpAuthPage)
        self.httpTopicLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.httpTopicLabel.sizePolicy().hasHeightForWidth())
        self.httpTopicLabel.setSizePolicy(sizePolicy)
        self.httpTopicLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.httpTopicLabel.setObjectName("httpTopicLabel")
        self.verticalLayout_4.addWidget(self.httpTopicLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.httpPasswordLe = QtWidgets.QLineEdit(self.httpAuthPage)
        self.httpPasswordLe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.httpPasswordLe.setObjectName("httpPasswordLe")
        self.gridLayout.addWidget(self.httpPasswordLe, 0, 1, 1, 1)
        self.httpPasswordLabel = QtWidgets.QLabel(self.httpAuthPage)
        self.httpPasswordLabel.setObjectName("httpPasswordLabel")
        self.gridLayout.addWidget(self.httpPasswordLabel, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.stackedWidget.addWidget(self.httpAuthPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.line_2 = QtWidgets.QFrame(MSColabConnectDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.statusHL = QtWidgets.QHBoxLayout()
        self.statusHL.setContentsMargins(-1, 0, -1, -1)
        self.statusHL.setObjectName("statusHL")
        self.statusLabel = QtWidgets.QLabel(MSColabConnectDialog)
        self.statusLabel.setStyleSheet("")
        self.statusLabel.setObjectName("statusLabel")
        self.statusHL.addWidget(self.statusLabel)
        self.statusHL.setStretch(0, 1)
        self.verticalLayout.addLayout(self.statusHL)

        self.retranslateUi(MSColabConnectDialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MSColabConnectDialog)
        MSColabConnectDialog.setTabOrder(self.urlCb, self.connectBtn)
        MSColabConnectDialog.setTabOrder(self.connectBtn, self.loginEmailLe)
        MSColabConnectDialog.setTabOrder(self.loginEmailLe, self.loginPasswordLe)
        MSColabConnectDialog.setTabOrder(self.loginPasswordLe, self.loginBtn)
        MSColabConnectDialog.setTabOrder(self.loginBtn, self.addUserBtn)
        MSColabConnectDialog.setTabOrder(self.addUserBtn, self.newUsernameLe)
        MSColabConnectDialog.setTabOrder(self.newUsernameLe, self.newEmailLe)
        MSColabConnectDialog.setTabOrder(self.newEmailLe, self.newPasswordLe)
        MSColabConnectDialog.setTabOrder(self.newPasswordLe, self.newConfirmPasswordLe)
        MSColabConnectDialog.setTabOrder(self.newConfirmPasswordLe, self.httpPasswordLe)

    def retranslateUi(self, MSColabConnectDialog):
        _translate = QtCore.QCoreApplication.translate
        MSColabConnectDialog.setWindowTitle(_translate("MSColabConnectDialog", "Connect to MSColab"))
        self.urlLabel.setText(_translate("MSColabConnectDialog", "MSColab URL:"))
        self.urlCb.setToolTip(_translate("MSColabConnectDialog", "Enter Mscolab Server URL"))
        self.connectBtn.setToolTip(_translate("MSColabConnectDialog", "Connect to entered URL"))
        self.connectBtn.setText(_translate("MSColabConnectDialog", "Connect"))
        self.loginBtn.setToolTip(_translate("MSColabConnectDialog", "Login using entered credentials"))
        self.loginBtn.setText(_translate("MSColabConnectDialog", "Login"))
        self.addUserBtn.setToolTip(_translate("MSColabConnectDialog", "Add new user to the server"))
        self.addUserBtn.setText(_translate("MSColabConnectDialog", "Add user"))
        self.loginTopicLabel.setText(_translate("MSColabConnectDialog", "Login Details:"))
        self.clickNewUserLabel.setText(_translate("MSColabConnectDialog", "Click here if new user"))
        self.loginWithIDPBtn.setText(_translate("MSColabConnectDialog", "Login by Identity Provider"))
        self.loginEmailLe.setPlaceholderText(_translate("MSColabConnectDialog", "Email ID"))
        self.loginPasswordLe.setPlaceholderText(_translate("MSColabConnectDialog", "Password"))
        self.newUsernameLe.setPlaceholderText(_translate("MSColabConnectDialog", "John Doe"))
        self.newPasswordLabel.setText(_translate("MSColabConnectDialog", "Password:"))
        self.newConfirmPasswordLabel.setText(_translate("MSColabConnectDialog", "Confirm Password:"))
        self.newUserTopicLabel.setText(_translate("MSColabConnectDialog", "New User Details"))
        self.newEmailLe.setPlaceholderText(_translate("MSColabConnectDialog", "johndoe@gmail.com"))
        self.newEmailLabel.setText(_translate("MSColabConnectDialog", "Email:"))
        self.newPasswordLe.setPlaceholderText(_translate("MSColabConnectDialog", "New Password"))
        self.newUsernameLabel.setText(_translate("MSColabConnectDialog", "Username:"))
        self.newConfirmPasswordLe.setPlaceholderText(_translate("MSColabConnectDialog", "Confirm New Password"))
        self.httpTopicLabel.setText(_translate("MSColabConnectDialog", "HTTP Server Authentication"))
        self.httpPasswordLe.setPlaceholderText(_translate("MSColabConnectDialog", "Server Auth Password"))
        self.httpPasswordLabel.setText(_translate("MSColabConnectDialog", "Password:"))
        self.statusLabel.setText(_translate("MSColabConnectDialog", "Status:"))
