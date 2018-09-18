# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/user_form.ui'
#
# Created: Sun Aug 26 15:58:37 2018
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UserForm(object):
    def setupUi(self, UserForm):
        UserForm.setObjectName("UserForm")
        UserForm.resize(415, 273)
        self.verticalLayout = QtGui.QVBoxLayout(UserForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(UserForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.password_2_le = QtGui.QLineEdit(self.groupBox)
        self.password_2_le.setEchoMode(QtGui.QLineEdit.Password)
        self.password_2_le.setObjectName("password_2_le")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.password_2_le)
        self.error_lb = QtGui.QLabel(self.groupBox)
        self.error_lb.setStyleSheet("color: #B22222;")
        self.error_lb.setObjectName("error_lb")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.error_lb)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.admin_privilege_ckb = QtGui.QCheckBox(self.groupBox)
        self.admin_privilege_ckb.setObjectName("admin_privilege_ckb")
        self.verticalLayout_2.addWidget(self.admin_privilege_ckb)
        spacerItem = QtGui.QSpacerItem(20, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(UserForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.username_le)
        self.label_2.setBuddy(self.password_le)
        self.label_3.setBuddy(self.password_2_le)

        self.retranslateUi(UserForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), UserForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), UserForm.reject)
        QtCore.QMetaObject.connectSlotsByName(UserForm)
        UserForm.setTabOrder(self.username_le, self.password_le)
        UserForm.setTabOrder(self.password_le, self.password_2_le)
        UserForm.setTabOrder(self.password_2_le, self.admin_privilege_ckb)
        UserForm.setTabOrder(self.admin_privilege_ckb, self.buttonBox)

    def retranslateUi(self, UserForm):
        UserForm.setWindowTitle(QtGui.QApplication.translate("UserForm", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("UserForm", "Add new user", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("UserForm", "&Username :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("UserForm", "&Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("UserForm", "&Retype Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.error_lb.setText(QtGui.QApplication.translate("UserForm", "Password do not match", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_privilege_ckb.setText(QtGui.QApplication.translate("UserForm", "A&dministrative privilege", None, QtGui.QApplication.UnicodeUTF8))

