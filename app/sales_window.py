from datetime import date

from PySide2.QtCore import *
from PySide2.QtWidgets import *

from .ui.ui_sales_window import Ui_SalesWindow
from .containers import SalesContainer
from .signals import AppSignals
from .utils.func import subwindow, close_subwindow


@subwindow
class SalesWindow(QMainWindow, Ui_SalesWindow):

    signals = AppSignals()

    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.settings = QSettings()
        self.sales = SalesContainer()
        self.from_de.setDate(date.today())
        self.to_de.setDate(date.today())
        self.from_de.dateChanged.connect(self.filter)
        self.to_de.dateChanged.connect(self.filter)
        self.signals.sales_updated.connect(lambda: self.populate_sales(None))
        self.home_pb.clicked.connect(self.sales_tw.scrollToTop)
        self.end_pb.clicked.connect(self.sales_tw.scrollToBottom)
        self.pg_up_pb.clicked.connect(self.scroll_page_up)
        self.pg_down_pb.clicked.connect(self.scroll_page_down)
        self.populate_sales()

    def scroll_page_down(self):
        rect = self.sales_tw.rect()
        item = self.sales_tw.itemAt(rect.left(), rect.bottom() - self.sales_tw.horizontalHeader().height())
        self.sales_tw.scrollToItem(item, QAbstractItemView.PositionAtTop)

    def scroll_page_up(self):
        rect = self.sales_tw.rect()
        item = self.sales_tw.itemAt(rect.left(), rect.top() - self.sales_tw.horizontalHeader().height())
        self.sales_tw.scrollToItem(item, QAbstractItemView.PositionAtBottom)

    def showEvent(self, event):
        self.restoreGeometry(self.settings.value('SalesWindow/geometry'))
        self.restoreState(self.settings.value('SalesWindow/state'))
        return QMainWindow.showEvent(self, event)

    @close_subwindow
    def closeEvent(self, event):
        self.settings.setValue('SalesWindow/state', self.saveState())
        self.settings.setValue('SalesWindow/geometry', self.saveGeometry())
        return QMainWindow.closeEvent(self, event)

    def populate_sales(self, selected=None):
        self.sales_tw.clear()
        self.sales_tw.clearSpans()
        self.sales_tw.setColumnCount(len(self.sales.HEADERS))
        self.sales_tw.setHorizontalHeaderLabels(self.sales.HEADERS)
        self.sales_tw.horizontalHeader().setSectionResizeMode(self.sales.NAME, QHeaderView.Stretch)
        sales = self.sales.all()
        self.sales_tw.setRowCount(len(sales) or 1)
        frm = self.sales.from_date.date()
        to = self.sales.to_date.date()
        is_specific_day = frm == to
        is_today = is_specific_day and frm == date.today()
        if is_today:
            caption = 'Today\'s sales report, %s ' % date.today().strftime('%b %d, %Y')
        elif is_specific_day:
            caption = 'Sales report for %s ' % frm.strftime('%b %d, %Y')
        else:
            caption = 'Sales report from %s to %s ' % tuple([d.strftime('%b %d, %Y') for d in (frm, to)])
        self.table_caption_lb.setText(caption)
        if not sales:
            self.sales_tw.setVerticalHeaderItem(0, QTableWidgetItem('#'))
            if is_today:
                text = 'No sale record today'
            elif is_specific_day:
                text = 'No sale records found for this day'
            else:
                text = 'No sale records found for the specified period'
            self.sales_tw.setItem(0, 0, QTableWidgetItem(text))
            self.sales_tw.setSpan(0, 0, 1, self.sales_tw.columnCount())
            return None
        for row, sale in enumerate(sales):
            vhi = QTableWidgetItem(str(row + 1))
            vhi.setData(Qt.UserRole, sale.uid)
            self.sales_tw.setVerticalHeaderItem(row, vhi)
            self.sales_tw.setItem(row, self.sales.TIMESTAMP,
                                  QTableWidgetItem(sale.created_at.strftime('%b %d %Y, %H:%M:%S')))
            self.sales_tw.setItem(row, self.sales.NAME, QTableWidgetItem(sale.product.name))
            qty_twi = QTableWidgetItem(str(sale.qty))
            qty_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.sales_tw.setItem(row, self.sales.QTY, qty_twi)
            amount_twi = QTableWidgetItem('{:,}'.format(sale.amount))
            amount_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.sales_tw.setItem(row, self.sales.AMOUNT, amount_twi)
        end = self.sales_tw.rowCount()
        self.sales_tw.insertRow(end)
        self.sales_tw.setVerticalHeaderItem(end, QTableWidgetItem('#'))
        self.sales_tw.setSpan(end, self.sales.TIMESTAMP, 1, self.sales.AMOUNT)
        label_twi = QTableWidgetItem('Total Amount :')
        total_twi = QTableWidgetItem('{:,}'.format(self.sales.total()))
        total_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for twi in (label_twi, total_twi):
            font = twi.font()
            font.setBold(True)
            twi.setFont(font)
        self.sales_tw.setItem(end, self.sales.TIMESTAMP, label_twi)
        self.sales_tw.setItem(end, self.sales.AMOUNT, total_twi)
        return None

    def filter(self, date):
        py_date = date.toPython()  # Qt date to python date
        editor = self.sender()
        if editor == self.from_de:
            self.sales.from_date = py_date
        elif editor == self.to_de:
            self.sales.to_date = py_date
        self.signals.sales_updated.emit()
