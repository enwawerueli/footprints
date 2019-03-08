# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/transaction_details.ui',
# licensing of 'forms/transaction_details.ui' applies.
#
# Created: Tue Feb 26 23:57:13 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TransactionDetails(object):
    def setupUi(self, TransactionDetails):
        TransactionDetails.setObjectName("TransactionDetails")
        TransactionDetails.resize(584, 348)
        self.verticalLayout = QtWidgets.QVBoxLayout(TransactionDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(TransactionDetails)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.statement_tb = QtWidgets.QTextBrowser(TransactionDetails)
        self.statement_tb.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.statement_tb.setObjectName("statement_tb")
        self.verticalLayout.addWidget(self.statement_tb)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.print_pb = QtWidgets.QPushButton(TransactionDetails)
        self.print_pb.setObjectName("print_pb")
        self.horizontalLayout.addWidget(self.print_pb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(TransactionDetails)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TransactionDetails)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TransactionDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TransactionDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(TransactionDetails)

    def retranslateUi(self, TransactionDetails):
        TransactionDetails.setWindowTitle(QtWidgets.QApplication.translate("TransactionDetails", "Dialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("TransactionDetails", "<html><head/><body><p><span style=\" font-weight:600;\">Transaction Details</span></p></body></html>", None, -1))
        self.print_pb.setText(QtWidgets.QApplication.translate("TransactionDetails", "Print", None, -1))

