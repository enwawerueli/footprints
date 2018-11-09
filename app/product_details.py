from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_product_details import Ui_ProductDetails


class ProductDetails(QDialog, Ui_ProductDetails):

    def __init__(self, parent, product, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.name_lb.setText(product.name)
        self.sku_lb.setText(product.sku)
        self.unit_cost_lb.setText('{:,}'.format(product.unit_cost))
        self.unit_price_lb.setText('{:,}'.format(product.unit_price))
        self.units_lb.setText(str(product.units))
        self.category_lb.setText(product.category.name)
        self.description_lb.setText(product.description)
        self.created_at_lb.setText(product.created_at.strftime('%a %d %b %Y, %H:%M:%S'))
        self.modified_at_lb.setText(product.updated_at.strftime('%a %d %b %Y, %H:%M:%S'))
