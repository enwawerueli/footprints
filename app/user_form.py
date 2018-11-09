from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_user_form import Ui_UserForm
from .db import session
from .db.models import User
# from .ui import images_rc


class UserForm(QDialog, Ui_UserForm):

    def __init__(self, parent=None, login=False, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._login = login
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_btn.setDisabled(True)
        self.error_lb.setVisible(False)
        for le in (self.password_le, self.password_2_le):
            le.textEdited.connect(self.validate)
            le.textEdited.connect(self.allow_to_continue)
        self.username_le.textEdited.connect(self.allow_to_continue)

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
    def admin(self):
        return self.admin_ckb.checkState()

    def accept(self):
        try:
            user = self.create()
        except Exception as e:
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occurred\n' + str(e))
        else:
            info = QMessageBox(QMessageBox.Information, QApplication.applicationName(),
                               'User \'%s\' created successfully' % user.username, QMessageBox.Ok, self)
            if self._login is True:
                info.button(QMessageBox.Ok).setText('Log&in')
            return QDialog.accept(self)

    def validate(self, *args):
        state = True if self.password and self.password_2 and self.password_2 != self.password else False
        self.error_lb.setVisible(state)

    def is_valid(self):
        return True if self.username and self.password and self.password == self.password_2 else False

    def allow_to_continue(self, *args):
        self.ok_btn.setEnabled(self.is_valid())

    def create(self):
        user = User(username=self.username, password=self.password)
        session.add(user)
        try:
            session.flush()
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        return user
