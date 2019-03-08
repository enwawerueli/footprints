# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/about_app.ui',
# licensing of 'forms/about_app.ui' applies.
#
# Created: Sat Feb  9 15:10:58 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AboutApplication(object):
    def setupUi(self, AboutApplication):
        AboutApplication.setObjectName("AboutApplication")
        AboutApplication.resize(470, 377)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(AboutApplication)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(AboutApplication)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.appicon_lb = QtWidgets.QLabel(self.frame)
        self.appicon_lb.setStyleSheet("margin: 10px;")
        self.appicon_lb.setObjectName("appicon_lb")
        self.horizontalLayout_2.addWidget(self.appicon_lb)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.appname_lb = QtWidgets.QLabel(self.frame)
        self.appname_lb.setObjectName("appname_lb")
        self.verticalLayout.addWidget(self.appname_lb)
        self.appversion_lb = QtWidgets.QLabel(self.frame)
        self.appversion_lb.setObjectName("appversion_lb")
        self.verticalLayout.addWidget(self.appversion_lb)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.frame)
        self.info_tbw = QtWidgets.QTabWidget(AboutApplication)
        self.info_tbw.setObjectName("info_tbw")
        self.about_tab = QtWidgets.QWidget()
        self.about_tab.setObjectName("about_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.about_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.about_te = QtWidgets.QTextBrowser(self.about_tab)
        self.about_te.setObjectName("about_te")
        self.verticalLayout_3.addWidget(self.about_te)
        self.info_tbw.addTab(self.about_tab, "")
        self.license_tab = QtWidgets.QWidget()
        self.license_tab.setObjectName("license_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.license_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.license_te = QtWidgets.QTextEdit(self.license_tab)
        self.license_te.setReadOnly(True)
        self.license_te.setObjectName("license_te")
        self.verticalLayout_6.addWidget(self.license_te)
        self.info_tbw.addTab(self.license_tab, "")
        self.verticalLayout_4.addWidget(self.info_tbw)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutApplication)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(AboutApplication)
        self.info_tbw.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AboutApplication.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AboutApplication.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutApplication)

    def retranslateUi(self, AboutApplication):
        AboutApplication.setWindowTitle(QtWidgets.QApplication.translate("AboutApplication", "Dialog", None, -1))
        self.appicon_lb.setText(QtWidgets.QApplication.translate("AboutApplication", "app icon", None, -1))
        self.appname_lb.setText(QtWidgets.QApplication.translate("AboutApplication", "app name", None, -1))
        self.appversion_lb.setText(QtWidgets.QApplication.translate("AboutApplication", "app version", None, -1))
        self.about_te.setHtml(QtWidgets.QApplication.translate("AboutApplication", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No information provided.</p></body></html>", None, -1))
        self.info_tbw.setTabText(self.info_tbw.indexOf(self.about_tab), QtWidgets.QApplication.translate("AboutApplication", "About", None, -1))
        self.license_te.setHtml(QtWidgets.QApplication.translate("AboutApplication", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No license information.</p></body></html>", None, -1))
        self.info_tbw.setTabText(self.info_tbw.indexOf(self.license_tab), QtWidgets.QApplication.translate("AboutApplication", "License", None, -1))

