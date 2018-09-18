from PySide.QtGui import *

from .ui.ui_category_form import Ui_CategoryForm
from .db import session
from .db.models import Category
from .signals import AppSignals


class CategoryForm(QDialog, Ui_CategoryForm):

    signals = AppSignals()

    def __init__(self, parent=None, category=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._category = category
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(category is None)
        self.name_le.textChanged.connect(self.allow_to_continue)
        if self._category is not None:
            self.name_le.setText(category.name)
            self.description_te.setPlainText(category.description)

    @property
    def name(self):
        return self.name_le.text().strip()

    @property
    def description(self):
        return self.description_te.toPlainText().strip()

    def is_valid(self):
        return True if self.name else False

    def clear(self):
        self.name_le.clear()
        self.description_te.clear()

    def allow_to_continue(self, *args):
        self.ok_btn.setEnabled(self.is_valid())

    def accept(self):
        try:
            uid = self.update() if self._category is not None else self.create()
        except Exception as e:
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occured\n' + str(e))
        else:
            self.signals.categories_updated[int].emit(uid)
        return QDialog.accept(self)

    def update(self):
        self._category.name = self.name
        self._category.description = self.description
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        return self._category.uid

    def create(self):
        category = Category(name=self.name, description=self.description)
        session.add(category)
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        return category.uid
