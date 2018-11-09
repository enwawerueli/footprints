from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_auth_form import Ui_AuthForm
# from .ui import images_rc
from .containers import Users
from .exceptions import AuthenticationError


class AuthForm(QDialog, Ui_AuthForm):

    def __init__(self, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle(QApplication.applicationName())
        self.login_pb.setDisabled(True)
        self.avatar_lb.setPixmap(QPixmap(':/images/lock'))
        for le in (self.username_le, self.password_le):
            le.textEdited.connect(self.allow_to_continue)

    @property
    def username(self):
        return self.username_le.text().strip()

    @property
    def password(self):
        return self.password_le.text()

    def accept(self):
        try:
            self.authenticate()
        except AuthenticationError as e:
            QMessageBox.critical(self, QApplication.applicationName(), str(e))
            self.password_le.setFocus()
        else:
            return QDialog.accept(self)

    def is_valid(self):
        return True if self.username and self.password else False

    def authenticate(self):
        user = Users.get(self.username)
        if user is not None and user.check(self.password) is True:
            return True
        raise AuthenticationError('Wrong username or password.')

    def allow_to_continue(self, *args):
        self.login_pb.setEnabled(self.is_valid())
