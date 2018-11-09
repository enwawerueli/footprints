# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/sales_window.ui',
# licensing of 'forms/sales_window.ui' applies.
#
# Created: Tue Nov  6 14:48:30 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SalesWindow(object):
    def setupUi(self, SalesWindow):
        SalesWindow.setObjectName("SalesWindow")
        SalesWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SalesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table_caption_lb = QtWidgets.QLabel(self.centralwidget)
        self.table_caption_lb.setObjectName("table_caption_lb")
        self.horizontalLayout_5.addWidget(self.table_caption_lb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.from_de = QtWidgets.QDateEdit(self.centralwidget)
        self.from_de.setObjectName("from_de")
        self.horizontalLayout_5.addWidget(self.from_de)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.to_de = QtWidgets.QDateEdit(self.centralwidget)
        self.to_de.setObjectName("to_de")
        self.horizontalLayout_5.addWidget(self.to_de)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.sales_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.sales_tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sales_tw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_tw.setAlternatingRowColors(True)
        self.sales_tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sales_tw.setShowGrid(False)
        self.sales_tw.setObjectName("sales_tw")
        self.sales_tw.setColumnCount(0)
        self.sales_tw.setRowCount(0)
        self.verticalLayout_6.addWidget(self.sales_tw)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.home_pb = QtWidgets.QPushButton(self.centralwidget)
        self.home_pb.setObjectName("home_pb")
        self.horizontalLayout_4.addWidget(self.home_pb)
        self.pg_up_pb = QtWidgets.QPushButton(self.centralwidget)
        self.pg_up_pb.setObjectName("pg_up_pb")
        self.horizontalLayout_4.addWidget(self.pg_up_pb)
        self.pg_down_pb = QtWidgets.QPushButton(self.centralwidget)
        self.pg_down_pb.setObjectName("pg_down_pb")
        self.horizontalLayout_4.addWidget(self.pg_down_pb)
        self.end_pb = QtWidgets.QPushButton(self.centralwidget)
        self.end_pb.setObjectName("end_pb")
        self.horizontalLayout_4.addWidget(self.end_pb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        SalesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SalesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        SalesWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SalesWindow)
        self.statusbar.setObjectName("statusbar")
        SalesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SalesWindow)
        QtCore.QMetaObject.connectSlotsByName(SalesWindow)

    def retranslateUi(self, SalesWindow):
        SalesWindow.setWindowTitle(QtWidgets.QApplication.translate("SalesWindow", "MainWindow", None, -1))
        self.table_caption_lb.setText(QtWidgets.QApplication.translate("SalesWindow", "Table caption", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SalesWindow", "From :", None, -1))
        self.from_de.setDisplayFormat(QtWidgets.QApplication.translate("SalesWindow", "MMM dd, yyyy", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("SalesWindow", "To :", None, -1))
        self.to_de.setDisplayFormat(QtWidgets.QApplication.translate("SalesWindow", "MMM dd, yyyy", None, -1))
        self.home_pb.setText(QtWidgets.QApplication.translate("SalesWindow", "<< Home", None, -1))
        self.pg_up_pb.setText(QtWidgets.QApplication.translate("SalesWindow", "< Pg Up", None, -1))
        self.pg_down_pb.setText(QtWidgets.QApplication.translate("SalesWindow", "Pg Down >", None, -1))
        self.end_pb.setText(QtWidgets.QApplication.translate("SalesWindow", "End >>", None, -1))

