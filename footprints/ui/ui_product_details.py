# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/product_details.ui',
# licensing of 'forms/product_details.ui' applies.
#
# Created: Fri Feb  8 19:39:07 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ProductDetails(object):
    def setupUi(self, ProductDetails):
        ProductDetails.setObjectName("ProductDetails")
        ProductDetails.resize(467, 356)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProductDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(ProductDetails)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.details_tbw = QtWidgets.QTabWidget(ProductDetails)
        self.details_tbw.setObjectName("details_tbw")
        self.basic_info_tab = QtWidgets.QWidget()
        self.basic_info_tab.setObjectName("basic_info_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.basic_info_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.category_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.category_lb.setObjectName("category_lb")
        self.gridLayout.addWidget(self.category_lb, 5, 1, 1, 1)
        self.name_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.unit_price_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.unit_price_lb.setObjectName("unit_price_lb")
        self.gridLayout.addWidget(self.unit_price_lb, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.basic_info_tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.created_at_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.created_at_lb.setObjectName("created_at_lb")
        self.gridLayout.addWidget(self.created_at_lb, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.sku_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.sku_lb.setObjectName("sku_lb")
        self.gridLayout.addWidget(self.sku_lb, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.units_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.units_lb.setObjectName("units_lb")
        self.gridLayout.addWidget(self.units_lb, 4, 1, 1, 1)
        self.modified_at_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.modified_at_lb.setObjectName("modified_at_lb")
        self.gridLayout.addWidget(self.modified_at_lb, 7, 1, 1, 1)
        self.unit_cost_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.unit_cost_lb.setObjectName("unit_cost_lb")
        self.gridLayout.addWidget(self.unit_cost_lb, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 2)
        self.details_tbw.addTab(self.basic_info_tab, "")
        self.description_tab = QtWidgets.QWidget()
        self.description_tab.setObjectName("description_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.description_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.description_te = QtWidgets.QTextEdit(self.description_tab)
        self.description_te.setReadOnly(True)
        self.description_te.setObjectName("description_te")
        self.verticalLayout_2.addWidget(self.description_te)
        self.details_tbw.addTab(self.description_tab, "")
        self.verticalLayout.addWidget(self.details_tbw)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProductDetails)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProductDetails)
        self.details_tbw.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProductDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProductDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(ProductDetails)

    def retranslateUi(self, ProductDetails):
        ProductDetails.setWindowTitle(QtWidgets.QApplication.translate("ProductDetails", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ProductDetails", "<h4>Product Details</h4>", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("ProductDetails", "Last modified :", None, -1))
        self.category_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "category", None, -1))
        self.name_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "name", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("ProductDetails", "Unit Price :", None, -1))
        self.unit_price_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "unit price", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("ProductDetails", "Unit Cost :", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ProductDetails", "Name :", None, -1))
        self.created_at_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "creation date", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("ProductDetails", "Units :", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("ProductDetails", "Created :", None, -1))
        self.sku_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "sku", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ProductDetails", "SKU :", None, -1))
        self.units_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "units", None, -1))
        self.modified_at_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "modification date", None, -1))
        self.unit_cost_lb.setText(QtWidgets.QApplication.translate("ProductDetails", "unit cost", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("ProductDetails", "Category :", None, -1))
        self.details_tbw.setTabText(self.details_tbw.indexOf(self.basic_info_tab), QtWidgets.QApplication.translate("ProductDetails", "Basic", None, -1))
        self.description_te.setHtml(QtWidgets.QApplication.translate("ProductDetails", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No description.</p></body></html>", None, -1))
        self.details_tbw.setTabText(self.details_tbw.indexOf(self.description_tab), QtWidgets.QApplication.translate("ProductDetails", "Description", None, -1))

