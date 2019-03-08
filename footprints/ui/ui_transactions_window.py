# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/transactions_window.ui',
# licensing of 'forms/transactions_window.ui' applies.
#
# Created: Fri Mar  8 12:03:07 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TransactionsWindow(object):
    def setupUi(self, TransactionsWindow):
        TransactionsWindow.setObjectName("TransactionsWindow")
        TransactionsWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TransactionsWindow)
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
        self.from_de.setCalendarPopup(True)
        self.from_de.setObjectName("from_de")
        self.horizontalLayout_5.addWidget(self.from_de)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.to_de = QtWidgets.QDateEdit(self.centralwidget)
        self.to_de.setCalendarPopup(True)
        self.to_de.setObjectName("to_de")
        self.horizontalLayout_5.addWidget(self.to_de)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.transactions_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.transactions_tw.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.transactions_tw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transactions_tw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.transactions_tw.setAlternatingRowColors(True)
        self.transactions_tw.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.transactions_tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.transactions_tw.setShowGrid(False)
        self.transactions_tw.setObjectName("transactions_tw")
        self.transactions_tw.setColumnCount(0)
        self.transactions_tw.setRowCount(0)
        self.transactions_tw.horizontalHeader().setHighlightSections(True)
        self.transactions_tw.verticalHeader().setVisible(False)
        self.transactions_tw.verticalHeader().setHighlightSections(True)
        self.verticalLayout_6.addWidget(self.transactions_tw)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.home_pb = QtWidgets.QPushButton(self.centralwidget)
        self.home_pb.setText("")
        self.home_pb.setIconSize(QtCore.QSize(24, 24))
        self.home_pb.setObjectName("home_pb")
        self.horizontalLayout_4.addWidget(self.home_pb)
        self.pg_up_pb = QtWidgets.QPushButton(self.centralwidget)
        self.pg_up_pb.setText("")
        self.pg_up_pb.setIconSize(QtCore.QSize(24, 24))
        self.pg_up_pb.setObjectName("pg_up_pb")
        self.horizontalLayout_4.addWidget(self.pg_up_pb)
        self.pg_down_pb = QtWidgets.QPushButton(self.centralwidget)
        self.pg_down_pb.setText("")
        self.pg_down_pb.setIconSize(QtCore.QSize(24, 24))
        self.pg_down_pb.setObjectName("pg_down_pb")
        self.horizontalLayout_4.addWidget(self.pg_down_pb)
        self.end_pb = QtWidgets.QPushButton(self.centralwidget)
        self.end_pb.setText("")
        self.end_pb.setIconSize(QtCore.QSize(24, 24))
        self.end_pb.setObjectName("end_pb")
        self.horizontalLayout_4.addWidget(self.end_pb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.print_pb = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_pb.setIcon(icon)
        self.print_pb.setObjectName("print_pb")
        self.horizontalLayout_4.addWidget(self.print_pb)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        TransactionsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TransactionsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        TransactionsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TransactionsWindow)
        self.statusbar.setObjectName("statusbar")
        TransactionsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransactionsWindow)
        QtCore.QMetaObject.connectSlotsByName(TransactionsWindow)

    def retranslateUi(self, TransactionsWindow):
        TransactionsWindow.setWindowTitle(QtWidgets.QApplication.translate("TransactionsWindow", "MainWindow", None, -1))
        self.table_caption_lb.setText(QtWidgets.QApplication.translate("TransactionsWindow", "Table caption", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("TransactionsWindow", "From :", None, -1))
        self.from_de.setDisplayFormat(QtWidgets.QApplication.translate("TransactionsWindow", "dd MMM yyyy", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("TransactionsWindow", "To :", None, -1))
        self.to_de.setDisplayFormat(QtWidgets.QApplication.translate("TransactionsWindow", "dd MMM yyyy", None, -1))
        self.print_pb.setText(QtWidgets.QApplication.translate("TransactionsWindow", "Print", None, -1))

