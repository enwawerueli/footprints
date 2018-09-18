# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/category_details.ui'
#
# Created: Sun Aug 26 15:58:37 2018
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CategoryDetails(object):
    def setupUi(self, CategoryDetails):
        CategoryDetails.setObjectName("CategoryDetails")
        CategoryDetails.resize(392, 201)
        self.verticalLayout = QtGui.QVBoxLayout(CategoryDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(CategoryDetails)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.name_lb = QtGui.QLabel(self.groupBox)
        self.name_lb.setText("")
        self.name_lb.setObjectName("name_lb")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.name_lb)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.description_lb = QtGui.QLabel(self.groupBox)
        self.description_lb.setText("")
        self.description_lb.setObjectName("description_lb")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.description_lb)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.created_at_lb = QtGui.QLabel(self.groupBox)
        self.created_at_lb.setText("")
        self.created_at_lb.setObjectName("created_at_lb")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.created_at_lb)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.modified_at_lb = QtGui.QLabel(self.groupBox)
        self.modified_at_lb.setText("")
        self.modified_at_lb.setObjectName("modified_at_lb")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.modified_at_lb)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(CategoryDetails)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CategoryDetails)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CategoryDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CategoryDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(CategoryDetails)

    def retranslateUi(self, CategoryDetails):
        CategoryDetails.setWindowTitle(QtGui.QApplication.translate("CategoryDetails", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CategoryDetails", "Category details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CategoryDetails", "Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CategoryDetails", "Description :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CategoryDetails", "Created :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CategoryDetails", "Last modified :", None, QtGui.QApplication.UnicodeUTF8))

