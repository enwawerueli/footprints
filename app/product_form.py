from functools import reduce
from decimal import Decimal

from PySide.QtGui import *
from PySide.QtCore import *

from .ui.ui_product_form import Ui_ProductForm
from .db import session
from .db.models import Category, Product
from .containers import Categories
from .signals import AppSignals


class ProductForm(QDialog, Ui_ProductForm):

    signals = AppSignals()

    def __init__(self, parent=None, product=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._product = product
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.settings = QSettings()
        self.restoreGeometry(self.settings.value('ProductForm/geometry'))
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(product is None)
        self.profit_format_bg = QButtonGroup(self)
        for btn in (self.percent_rb, self.absolute_rb):
            self.profit_format_bg.addButton(btn)
        self.profit_format_bg.buttonClicked.connect(self.update_profit)
        self.percent_validator = QDoubleValidator(0.00, 100.00, 2, self)
        self.percent_validator.setNotation(QDoubleValidator.StandardNotation)
        self.profit_le.setValidator(self.percent_validator)
        self.double_validator = QDoubleValidator(self)
        self.double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.double_validator.setDecimals(2)
        self.cost_le.setValidator(self.double_validator)
        self.price_le.setValidator(self.double_validator)
        for le in (self.name_le, self.sku_le, self.cost_le, self.price_le):
            le.textChanged.connect(self.allow_to_continue)
        self.category_cb.activated.connect(self.allow_to_continue)
        self.units_sb.valueChanged.connect(self.allow_to_continue)
        self.price_le.textEdited.connect(self.update_profit)
        self.cost_le.textEdited.connect(self.update_profit)
        self.profit_le.textEdited.connect(self.update_price)
        for index, category in enumerate(Categories().all()):
            self.category_cb.addItem(category.name, category.uid)
            if product is None:
                continue
            if category.uid == product.category.uid:
                self.category_cb.setCurrentIndex(index)
        if product is not None:
            self.name_le.setText(product.name)
            self.sku_le.setText(product.sku)
            self.cost_le.setText(str(product.unit_cost))
            self.price_le.setText(str(product.unit_price))
            self.profit_le.setText(str(((product.unit_price / product.unit_cost - 1) * 100).quantize(Decimal('.00'))))
            self.units_sb.setValue(product.units)
            self.description_te.setPlainText(product.description)

    @property
    def name(self):
        return self.name_le.text().strip()

    @property
    def sku(self):
        return self.sku_le.text().strip()

    @property
    def units(self):
        return self.units_sb.value()

    @property
    def category(self):
        uid = self.category_cb.itemData(self.category_cb.currentIndex())
        return session.query(Category).get(uid)

    @property
    def unit_cost(self):
        return Decimal(self.cost_le.text() or '0').quantize(Decimal('.00'))

    @property
    def unit_price(self):
        return Decimal(self.price_le.text() or '0').quantize(Decimal('.00'))

    @property
    def profit(self):
        return Decimal(self.profit_le.text() or '0').quantize(Decimal('.00'))

    @property
    def description(self):
        return self.description_te.toPlainText().strip()

    def update_price(self, *args):
        self.price_le.clear()
        if not self.unit_cost or not self.profit:
            return None
        if self.profit_format_bg.checkedButton() == self.absolute_rb:
            price = self.unit_cost + self.profit
        else:
            price = (1 + self.profit / 100) * self.unit_cost
        self.price_le.setText(str(price.quantize(Decimal('.00'))))
        return None

    def update_profit(self, *args):
        self.profit_le.clear()
        if not self.unit_cost or not self.unit_price:
            return None
        btn = self.profit_format_bg.checkedButton()
        if btn == self.absolute_rb:
            profit = self.unit_price - self.unit_cost
        else:
            profit = (self.unit_price / self.unit_cost - 1) * 100
        self.profit_le.setText(str(profit.quantize(Decimal('.00'))))
        self.profit_le.setValidator(self.double_validator if btn == self.absolute_rb else self.percent_validator)
        return None

    def is_valid(self):
        return reduce(lambda x, y: True if x and y else False,
                      (self.name, self.sku, self.units, self.unit_cost, self.unit_price))

    def allow_to_continue(self, *args):
        self.ok_btn.setEnabled(self.is_valid())

    def closeEvent(self, event):
        self.settings.setValue('ProductForm/geometry', self.saveGeometry())
        return QDialog.closeEvent(self, event)

    def accept(self):
        try:
            uid = self.update() if self._product is not None else self.create()
        except Exception as e:
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occured\n' + str(e))
        else:
            self.signals.products_updated[int].emit(uid)
        return QDialog.accept(self)

    def update(self):
        self._product.name = self.name
        self._product.sku = self.sku
        self._product.unit_cost = self.unit_cost
        self._product.unit_price = self.unit_price
        self._product.category = self.category
        self._product.units = self.units
        self._product.description = self.description
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        return self._product.uid

    def create(self):
        product = Product(name=self.name, sku=self.sku, unit_cost=self.unit_cost, unit_price=self.unit_price,
                          category=self.category, units=self.units, description=self.description)
        session.add(product)
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        return product.uid
