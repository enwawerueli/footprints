from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_product_details import Ui_ProductDetails


class ProductDetails(QDialog, Ui_ProductDetails):

    def __init__(self, product, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._product = product
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.name_lb.setText(self._product.name)
        self.sku_lb.setText(self._product.sku)
        self.unit_cost_lb.setText(str(self._product.unit_cost))
        self.unit_price_lb.setText(str(self._product.unit_price))
        self.units_lb.setText(str(self._product.units))
        self.category_lb.setText(self._product.category.name)
        if self._product.description:
            self.description_te.setHtml(self._product.description)
        self.created_at_lb.setText(self._product.created_at.strftime('%a %d %b %Y, %I:%M:%S %p'))
        self.modified_at_lb.setText(self._product.updated_at.strftime('%a %d %b %Y, %I:%M:%S %p'))
