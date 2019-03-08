import os
from datetime import date, datetime
from functools import partial

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import QPrintDialog, QPrinter
from jinja2 import TemplateNotFound

from .ui.ui_transactions_window import Ui_TransactionsWindow
from .ui import images_rc
from .transaction_details import TransactionDetails
from .containers import TransactionsContainer
from .utils import subwindow, close_subwindow, create_action
from . import jinja_env
from .exceptions import PrinterError


@subwindow
class TransactionsWindow(QMainWindow, Ui_TransactionsWindow):

    def __init__(self, parent, *args, **kwargs):
        QMainWindow.__init__(self, parent, *args, **kwargs)
        self._transactions = TransactionsContainer()
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.settings = QSettings(self)
        today = date.today()
        self.from_de.setDate(today)
        self.to_de.setDate(today)
        self.home_pb.setIcon(QIcon.fromTheme('go-first-symbolic', QIcon(':/icons/first')))
        self.pg_up_pb.setIcon(QIcon.fromTheme('go-next-symbolic-rtl', QIcon(':/icons/back')))
        self.pg_down_pb.setIcon(QIcon.fromTheme('go-previous-symbolic-rtl', QIcon(':/icons/foward')))
        self.end_pb.setIcon(QIcon.fromTheme('go-last-symbolic', QIcon(':/icons/end')))
        self.print_pb.setIcon(QIcon.fromTheme('document-print-symbolic', QIcon(':/icons/print')))
        self.print_pb.setEnabled(bool(self._transactions))
        self.home_pb.clicked.connect(self.transactions_tw.scrollToTop)
        self.end_pb.clicked.connect(self.transactions_tw.scrollToBottom)
        self.pg_up_pb.clicked.connect(self.scroll_page_up)
        self.pg_down_pb.clicked.connect(self.scroll_page_down)
        self.from_de.dateChanged.connect(lambda d: self._transactions.add_filter(from_=d.toPython()))
        self.from_de.dateChanged.connect(lambda: self.parentWidget().transactions_updated.emit())
        self.to_de.dateChanged.connect(lambda d: self._transactions.add_filter(to=d.toPython()))
        self.to_de.dateChanged.connect(lambda: self.parentWidget().transactions_updated.emit())
        self.transactions_tw.customContextMenuRequested.connect(self.open_transaction_menu)
        self.parentWidget().transactions_updated.connect(partial(self.populate_transactions, None))
        self.parentWidget().transactions_updated.connect(lambda: self.print_pb.setEnabled(bool(self._transactions)))
        self.print_pb.clicked.connect(self.print_statement)
        self.populate_transactions()

    def showEvent(self, event):
        self.restoreGeometry(self.settings.value('SalesWindow/geometry'))
        self.restoreState(self.settings.value('SalesWindow/state'))
        return QMainWindow.showEvent(self, event)

    @close_subwindow
    def closeEvent(self, event):
        self.settings.setValue('SalesWindow/state', self.saveState())
        self.settings.setValue('SalesWindow/geometry', self.saveGeometry())
        return QMainWindow.closeEvent(self, event)

    def scroll_page_down(self):
        rect = self.transactions_tw.rect()
        item = self.transactions_tw.itemAt(
            rect.left(), rect.bottom() - self.transactions_tw.horizontalHeader().height())
        self.transactions_tw.scrollToItem(item, QAbstractItemView.PositionAtTop)

    def scroll_page_up(self):
        rect = self.transactions_tw.rect()
        item = self.transactions_tw.itemAt(rect.left(), rect.top() - self.transactions_tw.horizontalHeader().height())
        self.transactions_tw.scrollToItem(item, QAbstractItemView.PositionAtBottom)

    def populate_transactions(self, selected=None):
        self.transactions_tw.clear()
        self.transactions_tw.clearSpans()
        transactions = self._transactions.all()
        n_rows = len(transactions) + 1
        n_columns = len(self._transactions.HEADER_LABELS)
        self.transactions_tw.setColumnCount(n_columns)
        self.transactions_tw.setHorizontalHeaderLabels(self._transactions.HEADER_LABELS)
        self.transactions_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.transactions_tw.setRowCount(n_rows)
        frm = self._transactions.from_date.date()
        to = self._transactions.to_date.date()
        is_specific_day = frm == to
        is_today = is_specific_day and frm == date.today()
        if is_today:
            caption = "Today's transaction report, %s." % date.today().strftime('%d/%m/%Y')
        elif is_specific_day:
            caption = 'Transaction report for %s.' % frm.strftime('%d/%m/%Y')
        else:
            caption = 'Transaction report from %s to %s.' % (frm.strftime('%d/%m/%Y'), to.strftime('%d/%m/%Y'))
        self.table_caption_lb.setText(caption)
        for row in range(n_rows):
            twi = QTableWidgetItem()
            twi.setData(Qt.UserRole, None)
            self.transactions_tw.setVerticalHeaderItem(row, twi)
        if not transactions:
            if is_today:
                text = 'No transaction record yet.'
            elif is_specific_day:
                text = 'No transaction records found for the specified date.'
            else:
                text = 'No transaction records found for the specified period.'
            self.transactions_tw.setItem(0, 0, QTableWidgetItem(text))
            self.transactions_tw.setSpan(0, 0, 1, n_columns)
            return None
        gen_rindex = (i for i in range(n_rows))
        for transaction in transactions:
            row = next(gen_rindex)
            twi = self.transactions_tw.verticalHeaderItem(row)
            twi.setData(Qt.UserRole, transaction.id)
            self.transactions_tw.setItem(
                row, self._transactions.TIMESTAMP,
                QTableWidgetItem(transaction.created_at.strftime('%d/%m/%Y, %I:%M:%S %p')))
            self.transactions_tw.setItem(row, self._transactions.CODE, QTableWidgetItem(transaction.code))
            twi = QTableWidgetItem(str(transaction.gross_amount))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.transactions_tw.setItem(row, self._transactions.GROSS_AMOUNT, twi)
            twi = QTableWidgetItem(str(transaction.discount))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.transactions_tw.setItem(row, self._transactions.DISCOUNT, twi)
            twi = QTableWidgetItem(str(transaction.net_amount))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.transactions_tw.setItem(row, self._transactions.NET_AMOUNT, twi)
        row = next(gen_rindex)
        self.transactions_tw.setSpan(row, 0, 1, n_columns - 1)
        label_twi = QTableWidgetItem('Total Amount :')
        total_twi = QTableWidgetItem(str(self._transactions.total()))
        total_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for twi in (label_twi, total_twi):
            font = twi.font()
            font.setBold(True)
            twi.setFont(font)
        self.transactions_tw.setItem(row, self._transactions.TIMESTAMP, label_twi)
        self.transactions_tw.setItem(row, self._transactions.NET_AMOUNT, total_twi)
        return None

    def open_transaction_menu(self, pos):
        twi = self.transactions_tw.itemAt(pos)
        if twi is None:
            return None
        id = self.transactions_tw.verticalHeaderItem(twi.row()).data(Qt.UserRole)
        if id is None:
            return None
        transaction = self._transactions.get(id)
        menu = QMenu(self)
        act_details = create_action(
            self, 'Details', icon=QIcon.fromTheme('view-more-symbolic', QIcon(':/icons/more')),
            slot=lambda: TransactionDetails(transaction, self).exec_(), statustip='Show transaction details')
        menu.addAction(act_details)
        pos += QPoint(
            self.transactions_tw.verticalHeader().width(), self.transactions_tw.horizontalHeader().height())
        menu.exec_(self.transactions_tw.mapToGlobal(pos))
        return None

    def print_statement(self):
        printer = QPrinter()
        printer.setOutputFileName(os.path.join(
            os.environ.get('HOME'), '%s_%s.pdf'
            % (self._transactions.from_date.strftime('%Y%m%d'), self._transactions.to_date.strftime('%Y%m%d'))))
        if QPrintDialog(printer, self).exec_() != QDialog.Accepted:
            return None
        try:
            stmt = jinja_env.get_template('stmt.jinja2.html')
        except TemplateNotFound as e:
            raise printerError('Printer data source unavailable') from e
        html = stmt.render(
            transactions=self._transactions,
            frm=self._transactions.from_date.strftime('%d/%m/%Y'),
            to=self._transactions.to_date.strftime('%d/%m/%Y'),
            printed_at=datetime.now().strftime('%d/%m/%Y, %I:%M:%S %p'))
        doc = QTextDocument(self)
        doc.setHtml(html)
        doc.print_(printer)
        return None
