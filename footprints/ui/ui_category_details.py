# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/category_details.ui',
# licensing of 'forms/category_details.ui' applies.
#
# Created: Fri Feb  8 19:39:07 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CategoryDetails(object):
    def setupUi(self, CategoryDetails):
        CategoryDetails.setObjectName("CategoryDetails")
        CategoryDetails.resize(387, 288)
        self.verticalLayout = QtWidgets.QVBoxLayout(CategoryDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(CategoryDetails)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.details_tbw = QtWidgets.QTabWidget(CategoryDetails)
        self.details_tbw.setObjectName("details_tbw")
        self.basic_info_tab = QtWidgets.QWidget()
        self.basic_info_tab.setObjectName("basic_info_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.basic_info_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.basic_info_tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.modified_at_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.modified_at_lb.setObjectName("modified_at_lb")
        self.gridLayout.addWidget(self.modified_at_lb, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.basic_info_tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.name_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)
        self.created_at_lb = QtWidgets.QLabel(self.basic_info_tab)
        self.created_at_lb.setObjectName("created_at_lb")
        self.gridLayout.addWidget(self.created_at_lb, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(CategoryDetails)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CategoryDetails)
        self.details_tbw.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CategoryDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CategoryDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(CategoryDetails)

    def retranslateUi(self, CategoryDetails):
        CategoryDetails.setWindowTitle(QtWidgets.QApplication.translate("CategoryDetails", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CategoryDetails", "<h4>Category Details</h4>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CategoryDetails", "Name :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("CategoryDetails", "Created :", None, -1))
        self.modified_at_lb.setText(QtWidgets.QApplication.translate("CategoryDetails", "modification date", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("CategoryDetails", "Last modified :", None, -1))
        self.name_lb.setText(QtWidgets.QApplication.translate("CategoryDetails", "name", None, -1))
        self.created_at_lb.setText(QtWidgets.QApplication.translate("CategoryDetails", "creation date", None, -1))
        self.details_tbw.setTabText(self.details_tbw.indexOf(self.basic_info_tab), QtWidgets.QApplication.translate("CategoryDetails", "Basic", None, -1))
        self.description_te.setHtml(QtWidgets.QApplication.translate("CategoryDetails", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No description.</p></body></html>", None, -1))
        self.details_tbw.setTabText(self.details_tbw.indexOf(self.description_tab), QtWidgets.QApplication.translate("CategoryDetails", "Description", None, -1))

