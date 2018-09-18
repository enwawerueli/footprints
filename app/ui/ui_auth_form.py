# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/auth_form.ui'
#
# Created: Sun Aug 26 16:11:45 2018
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AuthForm(object):
    def setupUi(self, AuthForm):
        AuthForm.setObjectName("AuthForm")
        AuthForm.resize(529, 300)
        self.verticalLayout = QtGui.QVBoxLayout(AuthForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(AuthForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.icon_lb = QtGui.QLabel(self.groupBox)
        self.icon_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_lb.setObjectName("icon_lb")
        self.verticalLayout_2.addWidget(self.icon_lb)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.username_le = QtGui.QLineEdit(self.groupBox)
        self.username_le.setObjectName("username_le")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.username_le)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtGui.QLineEdit(self.groupBox)
        self.password_le.setEchoMode(QtGui.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.password_le)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_pb = QtGui.QPushButton(self.groupBox)
        self.login_pb.setObjectName("login_pb")
        self.horizontalLayout.addWidget(self.login_pb)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.label.setBuddy(self.username_le)
        self.label_2.setBuddy(self.password_le)

        self.retranslateUi(AuthForm)
        QtCore.QObject.connect(self.login_pb, QtCore.SIGNAL("clicked()"), AuthForm.accept)
        QtCore.QMetaObject.connectSlotsByName(AuthForm)

    def retranslateUi(self, AuthForm):
        AuthForm.setWindowTitle(QtGui.QApplication.translate("AuthForm", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AuthForm", "User Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.icon_lb.setText(QtGui.QApplication.translate("AuthForm", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AuthForm", "&Username :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AuthForm", "&Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.login_pb.setText(QtGui.QApplication.translate("AuthForm", "LOGIN", None, QtGui.QApplication.UnicodeUTF8))

