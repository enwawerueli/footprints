from PySide2.QtGui import *
from PySide2.QtWidgets import *

from sqlalchemy.exc import DBAPIError

from .ui.ui_category_form import Ui_CategoryForm
from .db import session
from .db.models import Category


class CategoryForm(QDialog, Ui_CategoryForm):

    def __init__(self, category=None, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.category = category
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(self.category is None)
        if self.category is not None:
            self.name_le.setText(self.category.name)
            self.description_te.setPlainText(self.category.description)
            self.groupBox.setTitle('<b>Edit Category</b>')
        self.name_le.textChanged.connect(self.continue_)

    name = property(lambda self: self.name_le.text().strip())
    description = property(lambda self: self.description_te.toPlainText().strip())

    def accept(self):
        try:
            if self.category is not None:
                self.update()
            else:
                self.create()
        except Exception as e:
            # TODO: error logging
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occured\n' + str(e))
        return QDialog.accept(self)

    def continue_(self, *args):
        self.ok_btn.setEnabled(True if self.name else False)

    def update(self):
        self.category.name = self.name
        self.category.description = self.description
        try:
            session.flush()
        except DBAPIError:
            session.rollback()
            raise
        session.commit()
        self.parentWidget().categories_updated[int].emit(self.category.id)

    def create(self):
        category = Category(name=self.name, description=self.description)
        session.add(category)
        try:
            session.flush()
        except DBAPIError:
            session.rollback()
            raise
        session.commit()
        self.category = category
        self.parentWidget().categories_updated[int].emit(self.category.id)
