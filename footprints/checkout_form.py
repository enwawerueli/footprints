from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Signal

from sqlalchemy.exc import DBAPIError

from .ui.ui_checkout_form import Ui_CheckoutForm
from .db import session
from .db.models import Sale, Transaction
from .money import Ksh


class CheckoutForm(QDialog, Ui_CheckoutForm):

    transaction_completed = Signal()

    def __init__(self, cartitems, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._cartitems = cartitems
        self._total = cartitems.total()
        self._amount_due = cartitems.total()
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.total_lb.setText(str(self._total))
        self.amount_due_lb.setText(str(self._amount_due))
        self.change_lb.setText(str(Ksh('0.00')))
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(True)
        self.discount_validator = QDoubleValidator(0.00, self._total.amount, 2, self)
        self.discount_validator.setNotation(QDoubleValidator.StandardNotation)
        self.double_validator = QDoubleValidator(self)
        self.double_validator.setDecimals(2)
        self.double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.cash_le.setValidator(self.double_validator)
        self.discount_le.textEdited.connect(self.update_amount_due)
        self.discount_le.textEdited.connect(self.update_change)
        self.cash_le.textEdited.connect(self.update_change)
        self.discount_le.textEdited.connect(self.continue_)
        self.cash_le.textEdited.connect(self.continue_)
        self.transaction_completed.connect(self._cartitems.clear)
        self.transaction_completed.connect(self.parentWidget().cartitems_updated.emit)
        self.transaction_completed.connect(self.parentWidget().products_updated.emit)
        self.transaction_completed.connect(self.parentWidget().transactions_updated.emit)

    discount = property(lambda self: Ksh(self.discount_le.text() or '0.00'))
    cash = property(lambda self: Ksh(self.cash_le.text() or '0.00'))

    def accept(self):
        try:
            self.complete_transaction()
        except Exception as e:
            QMessageBox.critical(self, QApplication.applicationName(), str(e))
        return QDialog.accept(self)

    def update_amount_due(self, *args):
        self._amount_due = self._total - self.discount
        self.amount_due_lb.setText(str(self._amount_due))

    def update_change(self, *args):
        change = self.cash - self._amount_due if self.cash > self._amount_due else Ksh('0.00')
        self.change_lb.setText(str(change))

    def continue_(self, *args):
        self.ok_btn.setEnabled(self.cash >= self._amount_due)

    def complete_transaction(self):
        with session.no_autoflush:  # temporarily disable autoflush
            code = Transaction.generate_transaction_code()
            transaction = Transaction(code=code, total=self._total, discount=self.discount)
            session.add(transaction)
            for item in self._cartitems.all():
                sale = Sale(product_id=item.product.id, qty=item.qty)
                session.add(sale)
                transaction.sales.append(sale)
                item.product.units -= item.qty
            try:
                session.flush()
            except DBAPIError:
                session.rollback()
                raise
            session.commit()
        self.transaction_completed.emit()

    def print_receipt(self):
        pass
