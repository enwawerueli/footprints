from decimal import Decimal

from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_checkout_form import Ui_CheckoutForm
from .signals import AppSignals
from .db import session
from .db.models import Sale


class CheckoutForm(QDialog, Ui_CheckoutForm):

    signals = AppSignals()

    def __init__(self, parent, cartitems, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._cartitems = cartitems
        self._total = cartitems.total()
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(True)
        self.total_lb.setText(str(self._total))
        self.amount_due_lb.setText(str(self._total))
        self.percent_validator = QDoubleValidator(0.00, 100.00, 2, self)
        self.percent_validator.setNotation(QDoubleValidator.StandardNotation)
        self.discount_le.setValidator(self.percent_validator)
        self.absolute_validator = QDoubleValidator(0.00, self._total, 2, self)
        self.absolute_validator.setNotation(QDoubleValidator.StandardNotation)
        self.discount_format_bg = QButtonGroup(self)
        for btn in (self.percent_rb, self.absolute_rb):
            self.discount_format_bg.addButton(btn)
        self.discount_format_bg.buttonClicked.connect(self.update_discount)
        self.double_validator = QDoubleValidator(self)
        self.double_validator.setDecimals(2)
        self.double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.cash_le.setValidator(self.double_validator)
        self.discount_le.textEdited.connect(self.update_amount_due)
        self.discount_le.textEdited.connect(self.update_change)
        self.cash_le.textEdited.connect(self.update_change)
        self.cash_le.textChanged.connect(self.allow_to_continue)
        self.signals.sales_updated.connect(self.signals.products_updated)
        self.signals.sales_updated.connect(self.signals.cartitems_updated)

    @property
    def discount(self):
        return Decimal(self.discount_le.text() or '0').quantize(Decimal('.00'))

    @property
    def amount_due(self):
        return Decimal(self.amount_due_lb.text() or '0').quantize(Decimal('.00'))

    @property
    def cash(self):
        return Decimal(self.cash_le.text() or '0').quantize(Decimal('.00'))

    def update_discount(self, btn):
        if not self.discount:
            return None
        self.discount_le.clear()
        if btn == self.absolute_rb:
            discount = self._total - self.amount_due
        else:
            discount = (1 - self.amount_due / self._total) * 100
        self.discount_le.setText(str(discount.quantize(Decimal('.00'))))
        self.discount_le.setValidator(self.absolute_validator if btn == self.absolute_rb else self.percent_validator)
        return None

    def update_amount_due(self, *args):
        if self.discount_format_bg.checkedButton() == self.absolute_rb:
            amount_due = self._total - self.discount
        else:
            amount_due = (1 - self.discount / 100) * self._total
        self.amount_due_lb.setText(str(amount_due.quantize(Decimal('.00'))))

    def update_change(self, *args):
        if self.cash < self.amount_due:
            return None
        self.change_lb.clear()
        change = self.cash - self.amount_due
        self.change_lb.setText(str(change.quantize(Decimal('.00'))))
        return None

    def allow_to_continue(self, *args):
        self.ok_btn.setEnabled(self.cash >= self.amount_due)

    def accept(self):
        try:
            self.make_sale()
        except Exception as e:
            QMessageBox.critical(self, QApplication.applicationName(), str(e))
        else:
            self._cartitems.clear()
            self.signals.sales_updated.emit()
        return QDialog.accept(self)

    def make_sale(self):
        for item in self._cartitems.all():
            sale = Sale(product=item.product, qty=item.qty)
            session.add(sale)
            item.product.units -= item.qty
        try:
            session.flush()
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
