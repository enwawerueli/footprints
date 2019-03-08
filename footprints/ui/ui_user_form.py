# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/user_form.ui',
# licensing of 'forms/user_form.ui' applies.
#
# Created: Fri Feb 22 00:22:10 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_UserForm(object):
    def setupUi(self, UserForm):
        UserForm.setObjectName("UserForm")
        UserForm.resize(629, 361)
        self.verticalLayout = QtWidgets.QVBoxLayout(UserForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(UserForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.avatar_lb = QtWidgets.QLabel(self.groupBox)
        self.avatar_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.avatar_lb.setObjectName("avatar_lb")
        self.verticalLayout_2.addWidget(self.avatar_lb)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username_le = QtWidgets.QLineEdit(self.groupBox)
        self.username_le.setObjectName("username_le")
        self.gridLayout.addWidget(self.username_le, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password_le = QtWidgets.QLineEdit(self.groupBox)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.password_2_le = QtWidgets.QLineEdit(self.groupBox)
        self.password_2_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2_le.setObjectName("password_2_le")
        self.gridLayout.addWidget(self.password_2_le, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_user_bp = QtWidgets.QPushButton(self.groupBox)
        self.create_user_bp.setStyleSheet("back    ground-color: #00FF7F;")
        self.create_user_bp.setObjectName("create_user_bp")
        self.horizontalLayout.addWidget(self.create_user_bp)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.groupBox)
        self.label.setBuddy(self.username_le)
        self.label_2.setBuddy(self.password_le)
        self.label_3.setBuddy(self.password_2_le)

        self.retranslateUi(UserForm)
        QtCore.QObject.connect(self.create_user_bp, QtCore.SIGNAL("clicked()"), UserForm.accept)
        QtCore.QMetaObject.connectSlotsByName(UserForm)
        UserForm.setTabOrder(self.username_le, self.password_le)
        UserForm.setTabOrder(self.password_le, self.password_2_le)

    def retranslateUi(self, UserForm):
        UserForm.setWindowTitle(QtWidgets.QApplication.translate("UserForm", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("UserForm", "Create a user account", None, -1))
        self.avatar_lb.setText(QtWidgets.QApplication.translate("UserForm", "Avatar", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("UserForm", "&Username :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("UserForm", "&Password :", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("UserForm", "&Retype Password :", None, -1))
        self.create_user_bp.setText(QtWidgets.QApplication.translate("UserForm", "Create", None, -1))

