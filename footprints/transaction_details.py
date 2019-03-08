import os
from datetime import datetime

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import QPrinter, QPrintDialog
from jinja2 import TemplateNotFound

from .ui.ui_transaction_details import Ui_TransactionDetails
from .ui import images_rc
from . import jinja_env
from .exceptions import PrinterError


class TransactionDetails(QDialog, Ui_TransactionDetails):

    def __init__(self, transaction, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._transaction = transaction
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.print_pb.setIcon(QIcon.fromTheme('document-print-symbolic', QIcon(':/icons/print')))
        try:
            trans = jinja_env.get_template('trans.jinja2.html')
        except TemplateNotFound:
            pass
        else:
            html = trans.render(transaction=self._transaction, standalone=True)
            self.statement_tb.setHtml(html)
        self.print_pb.clicked.connect(self.print_statement)

    def print_statement(self):
        printer = QPrinter()
        printer.setOutputFileName(os.path.join(
            os.environ.get('HOME'), '%s_%s.pdf' %
            (self._transaction.created_at.strftime('%Y%m%d'), self._transaction.transaction_code)))
        if QPrintDialog(printer, self.parentWidget()).exec_() != QDialog.Accepted:
            return None
        try:
            trans = jinja_env.get_template('trans.jinja2.html')
        except TemplateNotFound as e:
            raise PrinterError('Printer data source unavailable') from e
        html = trans.render(transaction=self._transaction, printed_at=datetime.now().strftime('%d/%m/%Y, %I:%M:%S %p'))
        doc = QTextDocument(self)
        doc.setHtml(html)
        doc.print_(printer)
        return None
