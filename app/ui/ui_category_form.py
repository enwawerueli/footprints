# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/category_form.ui'
#
# Created: Sun Aug 26 15:58:38 2018
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CategoryForm(object):
    def setupUi(self, CategoryForm):
        CategoryForm.setObjectName("CategoryForm")
        CategoryForm.resize(429, 203)
        CategoryForm.setAutoFillBackground(False)
        CategoryForm.setSizeGripEnabled(True)
        CategoryForm.setModal(False)
        self.verticalLayout_3 = QtGui.QVBoxLayout(CategoryForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(CategoryForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.name_le = QtGui.QLineEdit(self.groupBox)
        self.name_le.setObjectName("name_le")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.name_le)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.description_te = QtGui.QTextEdit(self.groupBox)
        self.description_te.setObjectName("description_te")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.description_te)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
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
        CategoryForm.setWindowTitle(QtGui.QApplication.translate("CategoryForm", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CategoryForm", "Add new category", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CategoryForm", "&Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CategoryForm", "&Description :", None, QtGui.QApplication.UnicodeUTF8))

