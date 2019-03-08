# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/auth_form.ui',
# licensing of 'forms/auth_form.ui' applies.
#
# Created: Thu Jan 31 11:55:14 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AuthForm(object):
    def setupUi(self, AuthForm):
        AuthForm.setObjectName("AuthForm")
        AuthForm.resize(529, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AuthForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(AuthForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.avatar_lb = QtWidgets.QLabel(self.groupBox)
        self.avatar_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.avatar_lb.setObjectName("avatar_lb")
        self.verticalLayout_2.addWidget(self.avatar_lb)
        self.username_lb = QtWidgets.QLabel(self.groupBox)
        self.username_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lb.setObjectName("username_lb")
        self.verticalLayout_2.addWidget(self.username_lb)
        self.password_le = QtWidgets.QLineEdit(self.groupBox)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setAlignment(QtCore.Qt.AlignCenter)
        self.password_le.setObjectName("password_le")
        self.verticalLayout_2.addWidget(self.password_le)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.login_pb = QtWidgets.QPushButton(self.groupBox)
        self.login_pb.setObjectName("login_pb")
        self.horizontalLayout.addWidget(self.login_pb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(AuthForm)
        QtCore.QObject.connect(self.login_pb, QtCore.SIGNAL("clicked()"), AuthForm.accept)
        QtCore.QMetaObject.connectSlotsByName(AuthForm)

    def retranslateUi(self, AuthForm):
        AuthForm.setWindowTitle(QtWidgets.QApplication.translate("AuthForm", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("AuthForm", "User Authentication", None, -1))
        self.avatar_lb.setText(QtWidgets.QApplication.translate("AuthForm", "Avatar", None, -1))
        self.username_lb.setText(QtWidgets.QApplication.translate("AuthForm", "Username", None, -1))
        self.login_pb.setText(QtWidgets.QApplication.translate("AuthForm", "Login", None, -1))

