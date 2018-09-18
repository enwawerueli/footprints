from PySide.QtGui import *

from .ui.ui_user_form import Ui_UserForm
from .db import session
from .db.models import User


class UserForm(QDialog, Ui_UserForm):

    def __init__(self, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(True)
        for le in (self.username_le, self.password_le, self.password_2_le):
            le.textEdited.connect(self.allow_to_continue)
        self.error_lb.setVisible(False)
        self.password_2_le.textEdited.connect(self.validate)

    @property
    def username(self):
        return self.username_le.text().strip()

    @property
    def password(self):
        return self.password_le.text()

    @property
    def password_2(self):
        return self.password_2_le.text()

    @property
    def privilege(self):
        return self.admin_privilege_ckb.checkState()

    def accept(self):
        try:
            self.create()
        except Exception as e:
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occurred\n' + str(e))
        else:
            QMessageBox.information(self, QApplication.applicationName(), 'User created successfully')
        return QDialog.accept(self)

    def validate(self, *args):
        self.error_lb.setVisible(self.password != self.password_2)

    def is_valid(self):
        return True if self.username and self.password and self.password == self.password_2 else False

    def allow_to_continue(self, *args):
        self.ok_btn.setEnabled(self.is_valid())

    def create(self):
        try:
            session.add(User(username=self.username, password=self.password))
            session.flush()
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        return True
