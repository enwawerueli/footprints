from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_user_form import Ui_UserForm
from .ui import images_rc
from .db import session
from .db.models import User


class UserForm(QDialog, Ui_UserForm):

    def __init__(self, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.setWindowFlags(Qt.Window)
        pixmap = QPixmap(':/icons/user')
        self.avatar_lb.setPixmap(pixmap.scaled(self.avatar_lb.size(), Qt.KeepAspectRatio))
        self.create_user_bp.setDisabled(True)
        self.password_le.textEdited.connect(self.continue_)
        self.password_2_le.textEdited.connect(self.continue_)
        self.username_le.textEdited.connect(self.continue_)

    username = property(lambda self: self.username_le.text().strip())
    password = property(lambda self: self.password_le.text().strip())
    password_2 = property(lambda self: self.password_2_le.text().strip())

    def accept(self):
        try:
            self.create_user()
        except Exception as e:
            # TODO: error logging
            QMessageBox.critical(self, QApplication.applicationName(), 'An error occurred\n' + str(e))
        else:
            return QDialog.accept(self)

    def continue_(self, *args):
        is_match = self.password == self.password_2
        style = ''
        if self.password and self.password_2 and not is_match:
            style = '''
            background-color: #ffe4e1;
            border: 1px solid #b22222;
            border-radius: 3px;
            padding: 2px;
            '''
        self.password_2_le.setStyleSheet(style)
        self.create_user_bp.setEnabled(
            True if self.username and self.password and is_match else False)

    def create_user(self):
        user = User(name=self.username, password=self.password)
        session.add(user)
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        return user
