# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/category_details.ui',
# licensing of 'forms/category_details.ui' applies.
#
# Created: Mon Oct 29 23:51:50 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CategoryDetails(object):
    def setupUi(self, CategoryDetails):
        CategoryDetails.setObjectName("CategoryDetails")
        CategoryDetails.resize(392, 201)
        self.verticalLayout = QtWidgets.QVBoxLayout(CategoryDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(CategoryDetails)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_lb = QtWidgets.QLabel(self.groupBox)
        self.name_lb.setText("")
        self.name_lb.setObjectName("name_lb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lb)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.description_lb = QtWidgets.QLabel(self.groupBox)
        self.description_lb.setText("")
        self.description_lb.setObjectName("description_lb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.description_lb)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.created_at_lb = QtWidgets.QLabel(self.groupBox)
        self.created_at_lb.setText("")
        self.created_at_lb.setObjectName("created_at_lb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.created_at_lb)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.modified_at_lb = QtWidgets.QLabel(self.groupBox)
        self.modified_at_lb.setText("")
        self.modified_at_lb.setObjectName("modified_at_lb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.modified_at_lb)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(CategoryDetails)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CategoryDetails)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CategoryDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CategoryDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(CategoryDetails)

    def retranslateUi(self, CategoryDetails):
        CategoryDetails.setWindowTitle(QtWidgets.QApplication.translate("CategoryDetails", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("CategoryDetails", "Category details", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CategoryDetails", "Name :", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("CategoryDetails", "Description :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("CategoryDetails", "Created :", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("CategoryDetails", "Last modified :", None, -1))

