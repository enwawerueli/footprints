# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/product_details.ui'
#
# Created: Sun Aug 26 15:58:38 2018
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProductDetails(object):
    def setupUi(self, ProductDetails):
        ProductDetails.setObjectName("ProductDetails")
        ProductDetails.resize(426, 288)
        self.verticalLayout = QtGui.QVBoxLayout(ProductDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ProductDetails)
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
        self.sku_lb = QtGui.QLabel(self.groupBox)
        self.sku_lb.setText("")
        self.sku_lb.setObjectName("sku_lb")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sku_lb)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.unit_cost_lb = QtGui.QLabel(self.groupBox)
        self.unit_cost_lb.setText("")
        self.unit_cost_lb.setObjectName("unit_cost_lb")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.unit_cost_lb)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.unit_price_lb = QtGui.QLabel(self.groupBox)
        self.unit_price_lb.setText("")
        self.unit_price_lb.setObjectName("unit_price_lb")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.unit_price_lb)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.description_lb = QtGui.QLabel(self.groupBox)
        self.description_lb.setText("")
        self.description_lb.setObjectName("description_lb")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.description_lb)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_11)
        self.created_at_lb = QtGui.QLabel(self.groupBox)
        self.created_at_lb.setText("")
        self.created_at_lb.setObjectName("created_at_lb")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.created_at_lb)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_13)
        self.modified_at_lb = QtGui.QLabel(self.groupBox)
        self.modified_at_lb.setText("")
        self.modified_at_lb.setObjectName("modified_at_lb")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.modified_at_lb)
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self.units_lb = QtGui.QLabel(self.groupBox)
        self.units_lb.setText("")
        self.units_lb.setObjectName("units_lb")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.units_lb)
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_17)
        self.category_lb = QtGui.QLabel(self.groupBox)
        self.category_lb.setText("")
        self.category_lb.setObjectName("category_lb")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.category_lb)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ProductDetails)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProductDetails)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProductDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProductDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(ProductDetails)

    def retranslateUi(self, ProductDetails):
        ProductDetails.setWindowTitle(QtGui.QApplication.translate("ProductDetails", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProductDetails", "Product Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductDetails", "Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProductDetails", "SKU :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProductDetails", "Unit Cost :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ProductDetails", "Unit Price :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ProductDetails", "Description :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ProductDetails", "Created :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ProductDetails", "Last modified :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ProductDetails", "Units :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ProductDetails", "Category :", None, QtGui.QApplication.UnicodeUTF8))
