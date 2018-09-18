from PySide.QtGui import *
from PySide.QtCore import *

from .ui.ui_category_details import Ui_CategoryDetails


class CategoryDetails(QDialog, Ui_CategoryDetails):

    def __init__(self, parent, category, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.name_lb.setText(category.name)
        self.description_lb.setText(category.description)
        self.created_at_lb.setText(category.created_at.strftime('%a %d %b %Y, %H:%M:%S'))
        self.modified_at_lb.setText(category.updated_at.strftime('%a %d %b %Y, %H:%M:%S'))
