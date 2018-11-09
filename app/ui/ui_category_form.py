# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/category_form.ui',
# licensing of 'forms/category_form.ui' applies.
#
# Created: Mon Oct 29 23:51:51 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CategoryForm(object):
    def setupUi(self, CategoryForm):
        CategoryForm.setObjectName("CategoryForm")
        CategoryForm.resize(429, 203)
        CategoryForm.setAutoFillBackground(False)
        CategoryForm.setSizeGripEnabled(True)
        CategoryForm.setModal(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(CategoryForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(CategoryForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_le = QtWidgets.QLineEdit(self.groupBox)
        self.name_le.setObjectName("name_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_le)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.description_te = QtWidgets.QTextEdit(self.groupBox)
        self.description_te.setObjectName("description_te")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.description_te)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.label.setBuddy(self.name_le)
        self.label_2.setBuddy(self.description_te)

        self.retranslateUi(CategoryForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CategoryForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CategoryForm.reject)
        QtCore.QMetaObject.connectSlotsByName(CategoryForm)
        CategoryForm.setTabOrder(self.name_le, self.description_te)
        CategoryForm.setTabOrder(self.description_te, self.buttonBox)

    def retranslateUi(self, CategoryForm):
        CategoryForm.setWindowTitle(QtWidgets.QApplication.translate("CategoryForm", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("CategoryForm", "Add new category", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CategoryForm", "&Name :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CategoryForm", "&Description :", None, -1))

