from functools import reduce
from decimal import Decimal

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from sqlalchemy.exc import DBAPIError

from .ui.ui_product_form import Ui_ProductForm
from .db import session
from .db.models import Product
from .containers import CategoriesContainer
from .money import Ksh


class ProductForm(QDialog, Ui_ProductForm):

    def __init__(self, product=None, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.product = product
        self.categories = CategoriesContainer()
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.settings = QSettings()
        self.restoreGeometry(self.settings.value('ProductForm/geometry'))
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(self.product is None)
        self.profit_bg = QButtonGroup(self)
        self.profit_bg.addButton(self.percent_rb)
        self.profit_bg.addButton(self.absolute_rb)
        self.percent_validator = QDoubleValidator(0.00, 100.00, 2, self)
        self.percent_validator.setNotation(QDoubleValidator.StandardNotation)
        self.double_validator = QDoubleValidator(self)
        self.double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.double_validator.setDecimals(2)
        self.cost_le.setValidator(self.double_validator)
        self.price_le.setValidator(self.double_validator)
        self.profit_le.setValidator(self.double_validator)
        for c in self.categories.all():
            self.category_cb.addItem(c.name, c.id)
        if self.product is not None:
            for i in range(self.category_cb.count()):
                if self.category_cb.itemData(i) == self.product.category_id:
                    self.category_cb.setCurrentIndex(i)
                    break
            self.name_le.setText(self.product.name)
            self.sku_le.setText(self.product.sku)
            self.units_sb.setValue(self.product.units)
            self.cost_le.setText(str(self.product.unit_cost.amount))
            self.price_le.setText(str(self.product.unit_price.amount))
            self.profit_le.setText(str((self.product.unit_price - self.product.unit_cost).amount))
            self.description_te.setPlainText(self.product.description)
            self.groupBox.setTitle('<b>Edit Product</b>')
        self.profit_le.textEdited.connect(self.update_price)
        self.price_le.textEdited.connect(self.update_profit)
        self.profit_bg.buttonClicked.connect(self.update_profit)
        self.cost_le.textEdited.connect(self.update_profit)
        self.name_le.textChanged.connect(self.continue_)
        self.sku_le.textChanged.connect(self.continue_)
        self.cost_le.textChanged.connect(self.continue_)
        self.price_le.textChanged.connect(self.continue_)
        self.category_cb.activated.connect(self.continue_)
        self.units_sb.valueChanged.connect(self.continue_)

    name = property(lambda self: self.name_le.text().strip())
    sku = property(lambda self: self.sku_le.text().strip())
    units = property(lambda self: self.units_sb.value())
    category_id = property(lambda self: self.category_cb.itemData(self.category_cb.currentIndex()))
    unit_cost = property(lambda self: Ksh(self.cost_le.text() or '0.00'))
    unit_price = property(lambda self: Ksh(self.price_le.text() or '0.00'))
    profit = property(lambda self: Decimal(self.profit_le.text() or '0.00'))
    description = property(lambda self: self.description_te.toPlainText().strip())

    def closeEvent(self, event):
        self.settings.setValue('ProductForm/geometry', self.saveGeometry())
        return QDialog.closeEvent(self, event)

    def accept(self):
        try:
            if self.product is not None:
                self.update()
            else:
                self.create()
        except Exception as e:
            # TODO: error logging
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occured\n' + str(e))
        return QDialog.accept(self)

    def update_price(self, *args):
        self.price_le.clear()
        if not self.unit_cost or not self.profit:
            return None
        if self.profit_bg.checkedButton() == self.percent_rb:
            price = (1 + self.profit / 100) * self.unit_cost
        else:
            price = self.unit_cost + Ksh(self.profit)
        self.price_le.setText(str(price.amount))
        return None

    def update_profit(self, *args):
        self.profit_le.clear()
        if not self.unit_cost or not self.unit_price:
            return None
        profit = (self.unit_price - self.unit_cost).amount
        validator = self.double_validator
        if self.profit_bg.checkedButton() == self.percent_rb:
            profit = (self.unit_price / self.unit_cost - 1) * 100
            validator = self.percent_validator
        self.profit_le.setText(str(profit))
        self.profit_le.setValidator(validator)
        return None

    def continue_(self, *args):
        valid = reduce(
            lambda x, y: True if x and y else False, (self.name, self.sku, self.unit_cost, self.unit_price))
        self.ok_btn.setEnabled(valid)

    def update(self):
        self.product.name = self.name
        self.product.sku = self.sku
        self.product.unit_cost = self.unit_cost
        self.product.unit_price = self.unit_price
        self.product.category_id = self.category_id
        self.product.units = self.units
        self.product.description = self.description
        try:
            session.flush()
        except DBAPIError:
            session.rollback()
            raise
        session.commit()
        self.parentWidget().products_updated[int].emit(self.product.id)

    def create(self):
        product = Product(
            name=self.name, sku=self.sku, unit_cost=self.unit_cost, unit_price=self.unit_price, units=self.units,
            description=self.description, category_id=self.category_id)
        session.add(product)
        try:
            session.flush()
        except DBAPIError:
            session.rollback()
            raise
        session.commit()
        self.parentWidget().products_updated[int].emit(product.id)
