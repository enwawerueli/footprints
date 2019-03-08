from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_category_details import Ui_CategoryDetails


class CategoryDetails(QDialog, Ui_CategoryDetails):

    def __init__(self, category, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._category = category
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.name_lb.setText(category.name)
        if self._category.description:
            self.description_te.setText(self._category.description)
        self.created_at_lb.setText(self._category.created_at.strftime('%a %d %b %Y, %I:%M:%S %p'))
        self.modified_at_lb.setText(self._category.updated_at.strftime('%a %d %b %Y, %I:%M:%S %p'))
