# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/auth_form.ui',
# licensing of 'forms/auth_form.ui' applies.
#
# Created: Mon Oct 29 23:51:52 2018
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
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username_le = QtWidgets.QLineEdit(self.groupBox)
        self.username_le.setObjectName("username_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_le)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.groupBox)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_pb = QtWidgets.QPushButton(self.groupBox)
        self.login_pb.setObjectName("login_pb")
        self.horizontalLayout.addWidget(self.login_pb)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.label.setBuddy(self.username_le)
        self.label_2.setBuddy(self.password_le)

        self.retranslateUi(AuthForm)
        QtCore.QObject.connect(self.login_pb, QtCore.SIGNAL("clicked()"), AuthForm.accept)
        QtCore.QMetaObject.connectSlotsByName(AuthForm)

    def retranslateUi(self, AuthForm):
        AuthForm.setWindowTitle(QtWidgets.QApplication.translate("AuthForm", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("AuthForm", "User Authentication", None, -1))
        self.avatar_lb.setText(QtWidgets.QApplication.translate("AuthForm", "Avatar", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("AuthForm", "&Username :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("AuthForm", "&Password :", None, -1))
        self.login_pb.setText(QtWidgets.QApplication.translate("AuthForm", "LOG&IN", None, -1))

